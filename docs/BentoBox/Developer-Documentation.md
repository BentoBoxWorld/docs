# Welcome to the BentoBox developer documentation!

BentoBox is a platform plugin that supports a suite of API's for Addons that run on it. The architecture is virtually identical to the Bukkit plugin system. You can create GameModeAddons like BSkyBlock that provide players with your own game mode experience, or you can develop utility Addons, like Warps that enable players to use warp signs in those game modes.

## Pladdons

Due to changes in the way servers operate (remapping of code when beingg loaded), it is now recommended that all Addons now run inside a Bukkit Plugin wrapper, which is provided by BentoBox and called a Pladdon - 
Pladdons = Plugin + Addon. by being a Plugin, they will be correctly remapped when loaded, which is important for servers such a Paper. 

The Pladdon wrapper's job is to generate the Addon instance and supply it any time it is requested via the `getAddon` method.

As a result of Addons being Plugins, they will be listed as such by the server, however they should still be placed in the `Bentobox/Addons` folder. 

# JavaDocs
Javadocs are here: [https://javadocs.bentobox.world](https://ci.codemc.io/job/BentoBoxWorld/job/BentoBox/javadoc/)

The core API package is `world.bentobox.bentobox.api.*`. Methods in those packages are kept as stable as possible over the long term. Methods and classes outside of the api package may change a lot or more frequently.

# Example Addon

@BONNe maintains an example addon here: [https://github.com/BONNePlayground/ExampleAddon](https://github.com/BONNePlayground/ExampleAddon)

# Cancellable player reset events

*Added in BentoBox 3.17.0.*

When a player leaves a team or their island is reset, BentoBox can clear their inventory, ender chest, money, health, hunger and XP, and untame their animals — depending on each game mode's `island.reset.on-leave` settings. Each of these reset actions now fires a **cancellable** event **before** it runs, so an addon can veto an individual reset instead of all-or-nothing. If a listener cancels the event, BentoBox skips that action.

These events live in `world.bentobox.bentobox.api.events.player`:

| Event | Fired before |
| --- | --- |
| `PlayerTamedRemovalEvent` | untaming the player's animals |
| `PlayerResetEnderChestEvent` | clearing the ender chest |
| `PlayerResetInventoryEvent` | clearing the inventory |
| `PlayerResetMoneyEvent` | withdrawing the player's balance |
| `PlayerResetHealthEvent` | resetting health |
| `PlayerResetHungerEvent` | resetting hunger |
| `PlayerResetExpEvent` | resetting XP |

All events extend `PlayerBaseEvent` (which implements `Cancellable`) and carry the player UUID, the island, and the world. Listening is standard Bukkit:

```java
@EventHandler
public void onInventoryReset(PlayerResetInventoryEvent e) {
    if (shouldKeepInventory(e.getPlayerUUID())) {
        e.setCancelled(true); // inventory will not be cleared
    }
}
```

Events are constructed and dispatched through a small builder API:

```java
PlayerEvent.builder()
    .reason(PlayerEvent.Reason.INVENTORY_RESET)
    .involvedPlayer(uuid)
    .island(island)
    .world(world)
    .build();
```

This is purely additive — all classes are new and no existing API changed, so 3.17.0 is binary-compatible with existing addons. The [Inventory Switcher addon](../addons/InvSwitcher/index.md) uses these events to protect per-world inventories and balances during resets. See [Release 3.17.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.17.0).

# Modal dialogs

*Added in BentoBox 3.21.0.*

`world.bentobox.bentobox.api.dialogs` wraps Paper's modal dialog system, which requires **Minecraft 26 or later**. Dialogs sit alongside the Panels API: a panel is an inventory the player can click away, a dialog is a modal the player has to answer. Core uses them for command confirmations, the `/island go` destination picker, team invites, and the first-join game-mode chooser.

| Class | Purpose |
| --- | --- |
| `Dialogs` | `Dialogs.isSupported()` — whether this server can show dialogs |
| `DialogBuilder` | Fluent builder: `title`, `body`, `escapable`, `pause`, `confirmation`, `button`, `build` |
| `DialogButton` | A label, an optional tooltip, and a `Consumer<User>` click handler |
| `BBDialog` | The built dialog — `show(User)` to display it |

`title(...)`, `body(...)` and `DialogButton.of(...)` each take either an Adventure `Component` or a `User` plus a locale reference (with optional variables), so dialog text is translated the same way as the rest of your addon. Everything is `Component`-based end to end, so click actions survive.

```java
if (!Dialogs.isSupported()) {
    // Pre-26 server: fall back to your chat or panel flow
    askInChat(user);
    return;
}
new DialogBuilder()
    .title(user, "myaddon.confirm.title")
    .body(user, "myaddon.confirm.body", "[name]", island.getName())
    .confirmation(
        DialogButton.of(user, "myaddon.confirm.yes", u -> doTheThing(u)),
        DialogButton.of(user, "myaddon.confirm.no", u -> u.sendMessage("myaddon.confirm.cancelled")))
    .build()
    .show(user);
```

!!! warning "Always provide a fallback"
    Check `Dialogs.isSupported()` and keep your previous chat or panel behaviour for older servers, exactly as core does. Button click handlers run on the main thread, so they can touch the Bukkit API directly.

See [Release 3.21.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.21.0).

## Dialog forms

*Added in BentoBox 3.24.0.*

A dialog can have input fields. Add them with `DialogBuilder.input(DialogField)` and read what the player entered from the `DialogResponse` passed to a submit button.

| Class | Purpose |
| --- | --- |
| `DialogField` | A field: `DialogField.text(...)`, `number(...)`, `toggle(...)` or `choice(...)`. Each has a key, which may contain only letters, digits and underscores and must be unique in the dialog |
| `DialogButton.submit(...)` | A button whose handler is a `BiConsumer<User, DialogResponse>` |
| `DialogResponse` | The values, by field key: `getText`, `getNumber`, `getInt`, `getBoolean`, `getChoice`. Each returns an `Optional`, empty if there is no such field or the value is of another type |

```java
new DialogBuilder()
    .title(user, "myaddon.edit.title")
    .input(DialogField.text(user, "name", "myaddon.edit.name", current.getName()).maxLength(32))
    .input(DialogField.number(user, "chance", "myaddon.edit.chance", 0, 100, current.getChance()).step(0.5f))
    .input(DialogField.toggle(user, "enabled", "myaddon.edit.enabled", current.isEnabled()))
    .button(DialogButton.submit(user, "general.buttons.save", (u, response) -> {
        current.setName(response.getText("name").orElse(""));
        current.setChance(response.getNumber("chance").orElse(0f));
        current.setEnabled(response.getBoolean("enabled").orElse(false));
    }))
    .build()
    .show(user);
```

`DialogBuilder` also gained `body(ItemStack, Component)` to show an item in the body, `notice(DialogButton)` for a message with a single button, and `afterAction(AfterAction)` to choose what the client does after a click. The existing dialog API is unchanged.

# Paged panels and value pickers

*Added in BentoBox 3.24.0.*

Two additions to the Panels API (`world.bentobox.bentobox.api.panels`) for lists that don't fit in one inventory.

**`PagedPanelBuilder`** builds a `PagedPanel`: a list of any length, shown a page at a time. The bottom row is the control row. Its first and last slots hold the previous and next buttons when there is a page to go to, and the seven slots between take your own fixed controls, such as Back or Add. Turning the page refreshes the open inventory in place.

```java
PagedPanelBuilder b = new PagedPanelBuilder().user(user).name(user.getTranslation("myaddon.list.title"));
things.forEach(t -> b.item(toPanelItem(t)));
b.control(4, backButton).build();
```

**`PickerPanel<T>`** is a paged panel for choosing one value. `PickerPanel.materials(user)`, `entities(user)` and `biomes(user)` are ready-made; `PickerPanel.of(...)` takes any collection. A picker can have a Search button, which asks for text in a dialog and is hidden on servers without dialogs, and can let the player click an item in their own inventory to choose it. Its text is in BentoBox's locale files under `panels.picker`.

```java
PickerPanel.materials(user)
    .title(user.getTranslation("myaddon.pick-block"))
    .filter(Material::isBlock)
    .onPick(m -> { recipe.setIcon(m); openEditor(user); })
    .onCancel(() -> openEditor(user))
    .open();
```

Templated panels also understand two button types without any code, `COMMAND` and `CLOSE`; see [Command and Close buttons](../Tutorials/generic/Customizable-GUI.md#command-and-close-buttons). A panel that registers its own type of the same name keeps its own behaviour.

See [Release 3.24.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.24.0).

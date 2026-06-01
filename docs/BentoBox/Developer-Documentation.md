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

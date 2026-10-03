# Island Protection, Flags & Ranks

[TOC]

## Introduction
Player (and even Environment, such as entities, pistons...) interactions with islands are ruled by a set of **Flags** that **determine *who* or *what* can do what on an island**. These Flags are mostly handled and provided by BentoBox, yet addons (e.g. [Greenhouses](https://github.com/BentoBoxWorld/Greenhouses)) can add their own.

See a list of flags [here](/en/latest/BentoBox/Flags).

## Settings Panel

The **Settings Panel** is the GUI in which the island owner is able to edit how the Flags are configured for his island. Other players, including island members, are only able to view them.

This GUI can be opened using the following command: `/[player_command] settings` (which requires the following permission: `[gamemode].island.settings`).

![Default view of the Settings Panel](https://user-images.githubusercontent.com/20014332/80591492-1689c100-8a1e-11ea-9a59-c55f35ab6ad9.png)

*Default view of the Settings Panel.*

Admins can change the settings of a player's island by using the admin settings command: `/[admin_command] settings <player_name>`

### Protection Tab

The **Protection Tab** is the tab displayed upon opening the Setting Panel. It includes the **Protection Flags**.

**Protection Flags** are Flags that can be set by [rank](#ranks). By **left-** or **right-clicking** on the icon of a Flag, the island owner will cycle through the various ranks so that the interaction the Flag is ruling will be allowed or disallowed depending on the rank of a player.

![Example of a Protection Flag](https://user-images.githubusercontent.com/20014332/62974085-b31c1c80-be17-11e9-8b27-2fd4bf54ae87.png)

*Example of a Protection Flag.*

By default, most of the Protection Flags are set to allow only island members (or above rank) to do the interaction. However, some are initially allowed for visitors too. See [the gamemode's config.yml].

![Example of a Protection Flag which is, by default, allowing visitors to do the interaction.](https://user-images.githubusercontent.com/20014332/62974359-553c0480-be18-11e9-8679-0033fd8bf8bd.png)

*Example of a Protection Flag which is, by default, allowing visitors to do the interaction.*

Admins can set how protections will work outside of island boundaries by using the admin settings command: `/[admin_command] settings`

### Settings Tab

### Display mode

As of [BentoBox 1.6.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/1.6.0), various amounts of Flags can be displayed in the Settings Panel, depending on the **display mode**.
It is either `BASIC`, `ADVANCED` or `EXPERT`.
The display mode can be changed by clicking on the ingot in the top-right corner of the Settings Panel.

![Changing the display mode](https://user-images.githubusercontent.com/20014332/80592558-f0652080-8a1f-11ea-9b7a-eaf3d585b753.png).

`BASIC` is the default display mode and features the Flags we deem essential to manage the island.

![Basic Protection Flags](https://user-images.githubusercontent.com/20014332/80592424-b98f0a80-8a1f-11ea-94f5-3b2246b6ae61.png)

`ADVANCED` features more Flags to allow further customization of the island.

![Advanced Protection Flags](https://user-images.githubusercontent.com/20014332/80592698-24d8dc80-8a20-11ea-93d5-3b1b8dbcd18d.png)

`EXPERT` features all the available Flags. There are so many that it requires additional pages.

![Expert Protection Flags](https://user-images.githubusercontent.com/20014332/80592793-4df96d00-8a20-11ea-891e-8833578642e4.png)

!!! new "Changed in BentoBox 3.23.3"
    The Settings Panel remembers the display mode each player last chose and opens in it the next time. One mode is shared by the Protection and Settings tabs. If a tab has no flags to show in the chosen mode, it shows the next mode up without changing the player's choice. The admin settings panel always opens in `EXPERT`.

### Hide Flags

As of [BentoBox 1.4.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/1.4.0), admins can hide Flags in the GUI by opening the Settings Panel and ++shift+left-button++ on the icon of the Flag they want to hide.
This will apply a "Curse of Vanishing" enchantment to the icon and will result in the corresponding Flag being hidden to the players.
Admins can later unhide the Flag by reiterating the same procedure.

![Default flags](https://user-images.githubusercontent.com/20014332/80591609-45a03280-8a1e-11ea-9e37-4725d62cdb3c.png)

*Player's view of all the basic Flags being allowed to be displayed.*

![Curse of Vanishing](https://user-images.githubusercontent.com/20014332/80591692-6799b500-8a1e-11ea-9ab8-e076f47d2220.png)

*The "Curse of Vanishing" being applied to one of the Flag.*

![A bunch of hidden flags](https://user-images.githubusercontent.com/20014332/80591757-839d5680-8a1e-11ea-8864-83b09252a7b9.png)

*Player's view of the basic Flags, with the "trapdoor" Flag being hidden.*

### Customizing the Settings Panel

!!! new "Added in BentoBox 3.23.0"
    The Settings Panel is laid out by a template file, like the other [customizable GUIs](/en/latest/Tutorials/generic/Customizable-GUI/).

The layout of the Settings Panel comes from `plugins/BentoBox/panels/settings_panel.yml`, which BentoBox writes on first start. A game mode addon can ship its own copy in its `panels` folder (for example `plugins/BentoBox/addons/BSkyBlock/panels/settings_panel.yml`), and that one is used for that game mode instead. The default file reproduces the panel exactly as it looked before, so nothing changes until you edit it. If the file cannot be read, BentoBox logs an error and shows the built-in panel.

Every button is placed with a `data.type`:

| Type | What it shows |
| --- | --- |
| `TAB` | A tab button. `data.tab` is `PROTECTION`, `SETTING`, or `WORLD_PROTECTION` (the read-only view a player gets when not standing on an island). A tab that does not apply is not shown and the button's `fallback` is used instead. |
| `FLAG` | One slot of the paged flag list. Put as many of these as you want flags per page. With `data.flag: <FLAG_ID>` the slot always shows that flag instead, and the flag leaves the paged list; this is how the lock and change-settings icons are placed. |
| `MODE` | The display mode switch. Icons can be set per mode with `basic-icon`, `advanced-icon` and `expert-icon` in `data`. |
| `RESET` | Reset every flag to its default. Only the island owner sees it. |
| `NEXT`, `PREVIOUS` | Paging. Only shown when there is a page to go to. |

**Title and tab names are separate.** The panel title is the template's `title`, by default the locale entry `panels.settings.title`, which is translated with `[tab]` (the name of the tab being shown) and `[world_name]`. The default is just `[tab]`. Each tab button has its own `title` and `description`, by default the `protection.panel.PROTECTION.title` and similar entries. So you can style the title one way and the tab buttons another, in either the template or the locale.

**Lore layout.** A flag's lore is built from `protection.panel.flag-item.description-layout` (protection flags), `setting-layout` (settings) or `menu-layout` (flags that open a sub-panel) in the locale. As of 3.23.0 these layouts may contain `[ranks]`, where the rank list of a protection flag is inserted, and `[tooltips]`, where the tooltips of the flag button's `actions` in the template are inserted. Without `[ranks]` the rank list is appended after the layout, as before; without `[tooltips]` any tooltips are appended after an empty line. To move the click hints under the rank list, remove them from the layout, put `[ranks]` and `[tooltips]` where you want them, and declare the hints as tooltips on the `flag_button` in the template. A flag button's own `title` and `description` in the template may name a different locale entry to use as the name and lore layout for that panel only.

### Command Ranks

The **Command Ranks** icon on the Settings tab opens a panel where the island owner chooses the lowest [rank](#ranks) that may use each team command, for example who may invite, kick, or set the island's name. **Left-** and **right-clicking** a command cycles through the ranks, as for a Protection Flag. Operators can hide a command from players with ++shift+left-button++, the same way as [hiding a Flag](#hide-flags).

As of BentoBox 3.23.3 a player only sees the commands they have permission to use. If you deny a command's permission on your server, for example `[gamemode].island.border`, it no longer appears in this panel either. Previously only the top-level command was checked, so sub-commands the player could not run were still listed.

#### Customizing the Command Ranks panel

!!! new "Added in BentoBox 3.23.3"
    The Command Ranks panel is laid out by a template file, like the [Settings Panel](#customizing-the-settings-panel).

The layout comes from `plugins/BentoBox/panels/command_ranks_panel.yml`, which BentoBox writes on first start. A game mode addon can ship its own copy in its `panels` folder, and that one is used for that game mode instead. The default file keeps the panel looking as it did before: a map for each command, no filler, and only as many rows as the commands need. If the file cannot be read, BentoBox shows the built-in panel.

Every button is placed with a `data.type`:

| Type | What it shows |
| --- | --- |
| `COMMAND` | One slot of the paged command list. Put as many of these as you want commands per page; the default has 45. |
| `NEXT`, `PREVIOUS` | Paging. Only shown when there is a page to go to. |

The built-in panel stopped at 49 commands, so any beyond that were never shown. The template pages instead.

How a command is drawn can be changed on the `command_button` in the template's `reusable` section:

- `icon` replaces the default `MAP`.
- `title` is a locale entry (or text) used as the name layout instead of `protection.panel.flag-item.name-layout`. `[name]` is the command, e.g. `/island sethome`.
- `description` is a locale entry (or text) used as the lore layout instead of `protection.panel.flag-item.description-layout`. `[description]` is the command's text from `protection.panel.flag-item.command-instructions`. The rank list is added after it.
- `actions` only add tooltips, which are added after the rank list. The clicks themselves always work as described above. The default layout already includes the click hints.

For example, to show each command as paper and fill the empty slots:

```yaml
command_ranks_panel:
  title: protection.flags.COMMAND_RANKS.name
  type: INVENTORY
  background:
    icon: LIGHT_BLUE_STAINED_GLASS_PANE
    title: "&b&r"
  force-shown: 6
  content:
    # ... rows of command_button, and the paging buttons, as in the default file
  reusable:
    command_button:
      icon: PAPER
      data:
        type: COMMAND
```

## Ranks

TODO.

* BANNED: -1 (partially unused)
* VISITOR: 0
* COOP: 200
* TRUSTED: 400
* MEMBER: 500
* SUB-OWNER: 900
* OWNER: 1000
* MOD: 5000 (unused)
* ADMIN: 10000 (unused)

## Bypass the protection

Protection flags are only enforced inside BentoBox game worlds, and only against players who have no legitimate way through them. There are several ways the protection can be bypassed — some are intended (island ranks), some are for staff (operator status and moderator permissions), and some are structural (the world or the flag type).

!!! tip
    `[gamemode]` in the permissions below is the lowercased name of the game mode. For BSkyBlock the nodes start `bskyblock.mod…`, for AcidIsland `acidisland.mod…`, and so on.

### Island ranks — the intended way

The normal, designed way to "bypass" a protection flag is to have a high enough **rank** on the island. Every protection flag has a required rank, and any member whose rank is greater than or equal to it is allowed the action. This is why an owner can build while a visitor cannot — it is not really a bypass, just the flag working as configured. See the [Ranks](#ranks) list above.

### Operators

A server operator (`/op`) is the broadest bypass. Ops pass **every protection flag** in every BentoBox world, can enter locked and banned islands, and are immune to being banned or expelled.

Two important caveats:

- **Ops do not bypass island setting flags.** `SETTING`-type flags (island toggles such as *Allow PVP*, *Mob spawning*, …) are evaluated before the operator check, so an op is subject to them exactly like any other player. Operator status only overrides *protection* flags.
- **The admin switch cannot fully "un-op" a player on their own island.** Even with the switch turned on (see below), an op is still allowed on an island because the rank check treats operator status as always-allowed. To test protection as a true non-op, remove operator status.

### Moderator bypass permissions

For staff who should *not* be full operators, protection can be bypassed with permissions instead. These are gated by the admin switch (see below), so a moderator can toggle their own bypass off to experience the world as a normal player would.

- `[gamemode].mod.bypassprotect` — bypass **all** protection flags, everywhere in the world.
- `[gamemode].mod.bypass.<FLAG_ID>.everywhere` — bypass **one** named flag (e.g. `BREAK_BLOCKS`) everywhere in the world.
- `[gamemode].mod.bypass.<FLAG_ID>.island` — bypass **one** named flag, but only where the player would otherwise be blocked on an island.

### The admin "switch" — testing as a normal player

The command `/[admin_command] switch` (permission `[gamemode].mod.switch`) toggles a moderator's bypass permissions on and off. By default the bypass permissions are **active** (the moderator is bypassing protection); running the command once switches the bypass **off** so they are subject to protection like an ordinary player, and running it again switches it back on. This affects the `mod.bypassprotect` and `mod.bypass.*` permissions above — it does **not** disable raw operator status.

### Locks, bans and expels

Island locks, bans and expulsions have their own bypass permissions, separate from the flag system:

- `[gamemode].mod.bypasslock` — enter a locked island.
- `[gamemode].mod.bypassban` — enter an island you are banned from.
- `[gamemode].mod.bypassexpel` and `[gamemode].admin.noexpel` — cannot be expelled.
- `[gamemode].admin.noban` — cannot be banned.

Any entity carrying the Bukkit `NPC` metadata (for example Citizens NPCs) is also allowed through lock, ban, PVP and invincible-visitor checks, so plugin NPCs are not trapped or harmed by island protection.

### Cooldowns and delays

Command cooldowns and teleport warm-up delays can be skipped with:

- `[gamemode].mod.bypasscooldowns` — ignore command cooldowns.
- `[gamemode].mod.bypassdelays` — skip the movement warm-up delay on delayed-teleport commands.

### What is never protected

- **Non-BentoBox worlds.** Protection only exists in game-mode worlds (and their linked standard Nether/End). The server's default worlds and other plugins' worlds are never checked.
- **The "wild".** When a player is inside a game-mode world but not standing on any island, the world's default flag settings apply rather than an island's — these are configured in the **Admin Settings Panel** below (or the game mode's `config.yml`).
- **Deleted islands are the exception:** on an island that is pending deletion, nothing is allowed by default — apart from operators and holders of a `mod.bypassprotect` / `mod.bypass.<FLAG_ID>.everywhere` permission, whose bypass is checked first.

## Admin Settings Panel

The **Admin Settings Panel** is accessible via `/[admin_command] settings` (with no arguments). It contains three tabs:

!!! new "Added in BentoBox 3.23.0"
    The Admin Settings Panel is laid out by `plugins/BentoBox/panels/admin_settings_panel.yml`, in the same way as the [player's Settings Panel](#customizing-the-settings-panel). Its tab types are `WORLD_SETTING`, `WORLD_DEFAULTS` and `ISLAND_DEFAULTS`; the last two need the `[gamemode].admin.set-world-defaults` permission and are hidden without it. The same file lays out `/[admin_command] settings <player_name>`: each world tab names an island tab (`PROTECTION`, `SETTING`) as its `fallback`, which is what is shown when there is an island.

### World Settings

Toggles world-level setting flags that apply across the entire game world.

### World Default Protection

Controls which protection flags are active outside of any island boundaries (i.e. for visitors in the wilderness).

### Island Defaults

!!! new "Added in BentoBox 3.14.0"
    The **Island Defaults** tab is a new tab in the Admin Settings Panel that allows admins to set the default flag values applied to **newly created islands**.

Previously, these defaults could only be changed in the gamemode's `config.yml`. Now they can be changed directly in-game by opening `/[admin_command] settings` and navigating to the **Island Defaults** tab (tab 3).

Each protection flag is listed with its current default rank — clicking cycles it through the rank ladder. Each island settings flag shows its current default `true`/`false` state — clicking toggles it. Changes are saved immediately to the world settings and take effect for all **new** islands created after the change. Existing islands are not affected.
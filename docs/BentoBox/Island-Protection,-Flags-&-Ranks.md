# Island Protection, Flags & Ranks

[TOC]

## Introduction

Everything a player (or the environment: pistons, mobs, fire, explosions…) can do in a BentoBox game world is controlled by **Flags**. Each flag covers one kind of action, such as breaking blocks, opening chests or hurting animals. Most flags come with BentoBox. Addons such as [Greenhouses](https://github.com/BentoBoxWorld/Greenhouses) can add more.

See the [list of flags](Flags.md) for every flag, its icon and its default.

There are three types of flag:

| Type | What it controls | Who changes it |
| --- | --- | --- |
| **Protection** | Which [rank](#ranks) may do an action, e.g. *Break blocks*. On an island it is a rank. Off an island it is on or off for everyone. | The island owner on their island. Admins for the world and for new islands. |
| **Setting** | An island-wide on/off switch, e.g. *PVP* or *Animal spawning*. | The island owner. |
| **World setting** | A switch for the whole game world, e.g. *Creeper damage*. | Admins only. |

### On an island, off an island, and new islands

The most common confusion is that one protection flag can have **three different values**, depending on where the player is standing and which island is meant:

| Question | Where it is set | Panel tab |
| --- | --- | --- |
| What rank may do this on **this island**? | That island's settings | `/[player_command] settings` → **Protection** |
| What may anyone do **outside any island** in this world? | The world's protection flags (`world.flags` in the game mode's `config.yml`) | `/[admin_command] settings` → **World Protections** |
| What rank will a **new island** start with? | `world.default-island-flags` in the game mode's `config.yml` | `/[admin_command] settings` → **Island Defaults** |

Changing one never changes the others. In particular, **Island Defaults has no effect outside islands**, and **World Protections has no effect on islands**.

### Where an island ends

An island's protection does not cover its whole grid square. Islands are placed `distance-between-islands` apart, but each one is only protected within its **protection range**, a square of `protection-range` blocks out from the island's centre in each direction. The range can be raised per island with `/[admin_command] range` or the `[gamemode].island.range.<number>` permission.

Anywhere outside a protection range counts as **off-island**, even if it is inside an island's grid square. That includes the void between islands, the area around the world spawn if it is not an island, and the wilderness in game modes such as Boxed. Off-island, the [World Protections](#world-protections) apply.

## Ranks

Every player has a rank on each island: owner, member, visitor and so on. A protection flag sets the **lowest rank allowed** to do the action. Anyone at that rank or higher is allowed. Ranks are numbers, so higher means more trusted:

| Rank | Value | Who has it |
| --- | --- | --- |
| Banned | -1 | Players banned from the island. They cannot enter it. |
| Visitor | 0 | Anyone who is not part of the island. |
| Coop | 200 | Players added with `/[player_command] team coop`. Removed when every team member has logged off. |
| Trusted | 400 | Players added with `/[player_command] team trust`. Kept across logins. |
| Member | 500 | Team members. |
| Sub-owner | 900 | Team members promoted with `/[player_command] team promote`. |
| Owner | 1000 | The island owner. |
| Mod | 5000 | Not given to players. Reserved. |
| Admin | 10000 | Not given to players. Reserved. |

So a flag set to *Member* lets members, sub-owners and the owner do the action, but not trusted players, coops or visitors. A flag set to *Visitor* lets everyone do it.

Addons can register more ranks between these.

Admins can see or change a player's rank with `/[admin_command] getrank <player>` and `/[admin_command] setrank <player> <rank>`.

## Island Settings Panel

The **Settings Panel** is where an island owner configures their island. Open it with `/[player_command] settings` (permission `[gamemode].island.settings`). Everyone on the island can view it. Only the owner can change it, along with any rank the owner allows with the **Change settings** flag (the crafting table, top row).

![Default view of the Settings Panel](https://user-images.githubusercontent.com/20014332/80591492-1689c100-8a1e-11ea-9a59-c55f35ab6ad9.png)

*Default view of the Settings Panel.*

The panel shows the island whose area the player is standing in, or their own island if they are elsewhere. Admins can open any player's island with `/[admin_command] settings <player_name>`.

### Protection Tab

The **Protection** tab is shown first and lists the island's **protection flags**.

**Left-click** a flag to raise the rank it needs and **right-click** to lower it. The lore lists the ranks and highlights the current one. Going past *Owner* wraps around to *Visitor*, and the other way round.

![Example of a Protection Flag](https://user-images.githubusercontent.com/20014332/62974085-b31c1c80-be17-11e9-8b27-2fd4bf54ae87.png)

*Example of a Protection Flag.*

A new island starts with the ranks set on the [Island Defaults](#island-defaults) tab. Most flags start at *Member*, so visitors can look but not touch. A few start lower so visitors can use them. For example, *Lock* starts at *Visitor*, which means the island is open to visitors.

![Example of a Protection Flag which is, by default, allowing visitors to do the interaction.](https://user-images.githubusercontent.com/20014332/62974359-553c0480-be18-11e9-8679-0033fd8bf8bd.png)

*Example of a Protection Flag which is, by default, allowing visitors to do the interaction.*

### Settings Tab

The **Settings** tab lists the island's **setting flags**: on/off switches for the island as a whole, such as PVP, fire spread, leaf decay and mob spawning. Click a setting to toggle it.

Each setting also needs the permission `[gamemode].settings.<FLAG_ID>` (or `[gamemode].settings.*`). This lets a server take a setting away from players completely, for example to stop them turning PVP off. Some settings, such as PVP, have a cooldown between changes.

Since BentoBox 3.24.0 there is also a **Creeper block damage** setting (`CREEPER_BLOCK_DAMAGE`), which lets an owner stop creepers breaking blocks on their island. The explosion still happens and still hurts players and mobs. It is [hidden](#hide-flags) by default, so players don't see it until an operator shows it. If the world setting *Creeper explosions* (`CREEPER_DAMAGE`) is off, creepers break no blocks anywhere, whatever this setting says.

This tab also has the [Command Ranks](#command-ranks) icon.

### World Protection view

!!! new "Added in BentoBox 3.22.0"

A player who has no island in the world, and is not standing in another island's area, sees a read-only **World Protections** tab instead. It shows what anyone may do off-island, as set by the admin on the [World Protections](#world-protections) tab. It is for information only and cannot be changed from here.

### Display mode

Depending on the **display mode**, the Settings Panel shows more or fewer flags. The mode is `BASIC`, `ADVANCED` or `EXPERT`. Change it by clicking the ingot in the top-right corner of the panel.

![Changing the display mode](https://user-images.githubusercontent.com/20014332/80592558-f0652080-8a1f-11ea-9b7a-eaf3d585b753.png)

`BASIC` is the default and shows the flags most players need.

![Basic Protection Flags](https://user-images.githubusercontent.com/20014332/80592424-b98f0a80-8a1f-11ea-94f5-3b2246b6ae61.png)

`ADVANCED` shows more flags for finer control.

![Advanced Protection Flags](https://user-images.githubusercontent.com/20014332/80592698-24d8dc80-8a20-11ea-93d5-3b1b8dbcd18d.png)

`EXPERT` shows every flag and needs extra pages.

![Expert Protection Flags](https://user-images.githubusercontent.com/20014332/80592793-4df96d00-8a20-11ea-891e-8833578642e4.png)

!!! new "Changed in BentoBox 3.23.3"
    The Settings Panel remembers the display mode each player last chose and opens in it the next time. One mode is shared by the Protection and Settings tabs. If a tab has no flags to show in the chosen mode, it shows the next mode up without changing the player's choice. The admin settings panel always opens in `EXPERT`.

### Hide Flags

Operators can hide a flag from players: open the Settings Panel and ++shift+left-button++ the flag's icon. The icon gets a "Curse of Vanishing" glint, and players no longer see the flag. Do the same again to show it. Hidden flags are stored in `world.hidden-flags` in the game mode's `config.yml`.

Hiding a flag only removes it from the panel. The flag keeps its current value and is still enforced. To make sure players cannot change a flag, set its value first, then hide it.

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

## Admin Settings Panel

Run `/[admin_command] settings` with **no arguments** while in the game world to open the **Admin Settings Panel** (permission `[gamemode].admin.settings`). It has three tabs. They control the world and new islands, not any existing island.

!!! tip
    Each game mode has its own admin command and its own settings. Run the command for the game mode you want to change, e.g. `/bsbadmin settings` for BSkyBlock or `/acid settings` for AcidIsland.

!!! new "Added in BentoBox 3.23.0"
    The Admin Settings Panel is laid out by `plugins/BentoBox/panels/admin_settings_panel.yml`, in the same way as the [player's Settings Panel](#customizing-the-settings-panel). Its tab types are `WORLD_SETTING`, `WORLD_DEFAULTS` and `ISLAND_DEFAULTS`; the last two need the `[gamemode].admin.set-world-defaults` permission and are hidden without it. The same file lays out `/[admin_command] settings <player_name>`: each world tab names an island tab (`PROTECTION`, `SETTING`) as its `fallback`, which is what is shown when there is an island.

Changes made in these tabs are saved to the game mode's `config.yml` straight away.

### World Settings

The first tab lists the **world setting** flags: switches that apply to the whole game world, on and off islands, such as *Creeper damage*, *Offline redstone* or *Visitor keep inventory*. Click a flag to turn it on or off. Each needs the permission `[gamemode].admin.world.settings.<FLAG_ID>`, which operators have.

World settings can also be set from the console or chat:

```
/[admin_command] settings <FLAG_ID> <Active|Disabled>
```

!!! new "Added in BentoBox 3.23.6"
    The **Always-allowed entity types** item (iron ingot) opens a list of every living entity type. Green types spawn even when animal or monster spawning is off, on any island or in the world; Iron Golem is green by default so village iron farms keep working. The **Global mob spawning** block list still takes priority. The list is stored by BentoBox, not in the game mode's `config.yml`; see [Mob spawning precedence](#mob-spawning-precedence). Requires `[gamemode].admin.settings.ALLOW_MOBS`.

#### What each world setting does

These are the world settings most servers will want to review. Defaults are for BSkyBlock; other game modes may differ. Every flag is listed in [Flags](Flags.md).

| Setting | What it does | Default |
|---|---|---|
| **Always-allowed entity types** | Entities that spawn no matter what the animal and monster spawning flags say, on islands and in the world. Use it to let village iron farms work on a server, or an island, that has animal spawning turned off. Iron Golem is allowed by default. The block list (*Global mob spawning*) still wins. See [Mob spawning precedence](#mob-spawning-precedence). | Iron Golem |
| **Chest explosion damage** | Protects chests from being destroyed by explosions (Creepers, TNT, Withers, Ghasts). Prevents grief but means chests can be used to make explosion-proof rooms. | On |
| **Clean Super Flat** | If the world generator stops working, new chunks generate as flat grass. This setting detects and repairs those chunks. Leave it off unless you have this problem — it is resource-intensive. | Off |
| **Coarse Dirt Tilling** | Prevents players from converting coarse dirt into regular dirt using a hoe. Dirt is scarce and valuable in most game modes; coarse dirt tilling can be exploited to generate it cheaply if gravel is easy to obtain. | Off (prevention on) |
| **Creeper explosions** | Prevent Creeper explosion damage to island blocks. Creepers are the most common cause of island destruction. Preventing this makes the game easier, but reduces admin support load. | On |
| **Creeper visitor ignition** | Prevent visitors from using flint & steel to prime Creepers on someone else's island — a common griefing method. | On |
| **Ender Chests** | Block access to and crafting of Ender Chests, which can smuggle items between game mode worlds. Disable if you use a per-world Ender Chest plugin. | On (blocked) |
| **Enderman block theft** | Prevent Endermen from picking up blocks from islands. Without this, players lose blocks they did not remove themselves. | On |
| **Geo-limiting mobs** | Prevent certain mobs (e.g. the Wither, flying mobs) from leaving the island they were spawned on. If they cross the boundary they are removed. | On |
| **Visitor protection** | Protect visitors from most types of damage while on another player's island. Also teleports visitors to safety if they fall into the void. | On |
| **Item frame protection** | Prevent item frames from being broken or having their items knocked out by non-members. | On |
| **Global mob spawning** | Set which mob types can spawn anywhere in the world, overriding all other spawning settings. For example, disable Phantoms server-wide. | Varies |
| **Liquid flow outside islands** | Stop lava and water from flowing beyond island protection boundaries, preventing cobblestone formation between islands or floods. | On |
| **Mob spawning outside islands** | Prevent mobs from spawning in the areas between islands, concentrating spawning inside island zones. Not recommended for AcidIsland as it looks unnatural. | Off |
| **Obsidian scooping** | Allow players to right-click an isolated single obsidian block with an empty bucket to recover lava. Helps new players who accidentally make obsidian during cobblestone generator setup. | On |
| **Offline plant growth** | Stop crops and plants from growing on an island when no team members are online, even if a visitor is loading the chunks. | Off |
| **Offline Redstone** | Disable Redstone circuits on an island when no team members are online. | Off |
| **Piston outside boundary** | Stop pistons from pushing blocks beyond the island's protection boundary — a common exploit for griefing adjacent islands. | On |
| **PVP outside islands** | Allow PVP in the parts of the world that have no island. On an island, the island's own PVP setting always decides. Needs BentoBox 3.24.0 or later; before that, PVP was always off where there was no island. | Off |
| **Remove mobs on teleport** | Clear hostile mobs from the area when a player teleports to their island home, preventing surprise deaths on arrival. | On |
| **Spawner type protection** | Prevent players from changing the mob type of spawner blocks using spawn eggs. Useful when spawners are given as rewards. | On |
| **Tree growth boundary** | Prevent trees from growing beyond the island protection boundary. Without this, trees can intrude on other islands or create unreachable blocks. | On |
| **Wither damage** | Limit the destruction the Wither can cause on and between islands. | On |

#### Mob spawning precedence

Natural and spawner mob spawning is decided in this order. The first rule that matches wins.

1. **Global mob spawning** block list (`protection.block-mobs` in the game mode config). A blocked type never spawns.
2. **Always-allowed entity types** allow list. An allowed type spawns regardless of the flags below.
3. The island's **Animal natural spawn**, **Monster natural spawn**, **Animal spawners spawn** and **Monster spawners spawn** settings, or the world's defaults for those flags when there is no island.

Spawns caused directly by a player, such as breeding, spawn eggs or building a golem, are never gated by any of these.

!!! note "Where the allow list is stored"
    Unlike the other world settings, the allow list is not in the game mode's `config.yml`. BentoBox stores it itself, one record per game mode, in its database: with the default flat-file database it is `plugins/BentoBox/database/CoreWorldSettings/<GameMode>.json`. It is seeded with `IRON_GOLEM` the first time the game mode is seen; after that only the admin's edits in the panel apply. Clearing the record restores the seed.

### World Protections

The second tab, **World Protections**, decides what players may do **outside any island's protection range**. That includes the void between islands, the spawn area if it is not an island, and the wilderness. See [Where an island ends](#where-an-island-ends).

Off an island there is no team and no ranks, so each protection flag here is just **on or off for everyone**. Click a flag to switch it:

- **Allowed**: anyone may do the action off-island.
- **Not allowed**: nobody may, apart from operators and players with a [bypass permission](#bypass-the-protection).

Most protection flags are **not allowed** off-island by default, so players cannot build, break blocks or use items outside their island. This tab needs `[gamemode].admin.set-world-defaults`, and each flag also needs `[gamemode].admin.world.settings.<FLAG_ID>`. Operators have both. The values are stored under `world.flags` in the game mode's `config.yml`.

!!! example "Letting players build bridges between islands"
    Players can only build on their own island, so they cannot bridge to a neighbour. To let them build off-island:

    1. Stand in the game world and run `/[admin_command] settings` with no player name.
    2. Open the **World Protections** tab. It is neither the first tab nor **Island Defaults**.
    3. Switch on **Place blocks** and **Break blocks**, plus anything else players need out there, such as buckets, doors or pressure plates.

    The islands themselves stay protected by their own settings. To let visitors take things from other islands as well, set the [Island Defaults](#island-defaults) for new islands, or change existing islands with `/[admin_command] settings <player>`.

Players without an island can see these values (read-only) in `/[player_command] settings`. See [World Protection view](#world-protection-view).

### Island Defaults

!!! new "Added in BentoBox 3.14.0"
    The **Island Defaults** tab sets the flags that **newly created islands** start with. Before, this could only be done in the game mode's `config.yml`.

The third tab sets the starting value of every flag for **new islands**:

- Each **protection flag** shows its default rank. Left-click or right-click to cycle through the ranks.
- Each **setting flag** shows its default on/off state. Click to toggle it.

These values are stored in `world.default-island-flags` and `world.default-island-settings` in the game mode's `config.yml`. A flag that is not listed there uses the flag's built-in default.

Changes only apply to islands created **after** the change. To push the defaults onto **existing** islands, run `/[admin_command] resetflags` to reset every flag on every island, or `/[admin_command] resetflags <FLAG_ID>` to reset one flag. This overwrites whatever the island owners have set, so you are asked to confirm.

This tab does **not** control what players may do outside islands. For that, use [World Protections](#world-protections).

### Changing a player's island

`/[admin_command] settings <player_name>` opens the Protection and Settings tabs for that player's island, as the owner would see them, so an admin can change any flag. `/[admin_command] settings spawn-island` does the same for the spawn island.

The same can be done from the command line:

```
/[admin_command] settings <player_name> <FLAG_ID> <rank>              # protection flag, e.g. Visitor
/[admin_command] settings <player_name> <FLAG_ID> <Active|Disabled>   # setting flag
```

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

A player who rides a boat, a minecart or a mount into an island they are locked out of or banned from is turned back **with the vehicle**, rather than being thrown out of it. If any rider is not allowed in, the vehicle does not enter. A player turned away from a locked island also sees the island's border for a few seconds, so they can tell where it starts. Only that player sees it. Both need BentoBox 3.24.0 or later. The border is set in BentoBox's `config.yml`:

```yaml
island:
  locked-border:
    show: true    # false turns the border off
    color: RED    # RED, GREEN or BLUE
```

Any entity carrying the Bukkit `NPC` metadata (for example Citizens NPCs) is also allowed through lock, ban, PVP and invincible-visitor checks, so plugin NPCs are not trapped or harmed by island protection.

### Cooldowns and delays

Command cooldowns and teleport warm-up delays can be skipped with:

- `[gamemode].mod.bypasscooldowns` — ignore command cooldowns.
- `[gamemode].mod.bypassdelays` — skip the movement warm-up delay on delayed-teleport commands.

### What is never protected

- **Non-BentoBox worlds.** Protection only exists in game-mode worlds (and their linked standard Nether/End). The server's default worlds and other plugins' worlds are never checked.
- **Off-island areas follow different rules.** When a player is in a game-mode world but outside every island's protection range, the [World Protections](#world-protections) apply instead of any island's flags.
- **Deleted islands are the exception:** on an island that is pending deletion, nothing is allowed by default — apart from operators and holders of a `mod.bypassprotect` / `mod.bypass.<FLAG_ID>.everywhere` permission, whose bypass is checked first.

## Troubleshooting

**Players can't build or break blocks between islands.**
That area is off-island, so the [World Protections](#world-protections) tab applies. Turn on the flags you need there. Changing Island Defaults will not help.

**I changed Island Defaults but existing islands didn't change.**
Island Defaults only apply to islands created afterwards. Use `/[admin_command] resetflags` to apply them to existing islands, or change single islands with `/[admin_command] settings <player>`.

**A player can't change a setting even though they own the island.**
The setting probably needs the `[gamemode].settings.<FLAG_ID>` permission, or the setting is on cooldown.

**I'm an operator and can't test whether protection works.**
Operators bypass every protection flag. Test with a non-op account. `/[admin_command] switch` only turns off the moderator bypass permissions, not operator status.

**I don't know which flag is blocking an action.**
Run `/[admin_command] why <player>` to log every protection check for that player to the console, then do the action. The log names the flag, the location and the result. Run the command again to stop.

**`why` says the action is allowed, but the player is still blocked.**
Something other than BentoBox is blocking it: another plugin, or the server itself (for example spawn protection in `server.properties`).

**Should I use WorldGuard in BentoBox worlds?**
You don't need it: BentoBox protects islands and the space between them. If you do use WorldGuard there, its regions and BentoBox's flags both apply, which can block things unexpectedly. Keep WorldGuard regions out of game mode worlds, or check them first when something is blocked.

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

### World Settings

Toggles world-level setting flags that apply across the entire game world.

### World Default Protection

Controls which protection flags are active outside of any island boundaries (i.e. for visitors in the wilderness).

### Island Defaults

!!! new "Added in BentoBox 3.14.0"
    The **Island Defaults** tab is a new tab in the Admin Settings Panel that allows admins to set the default flag values applied to **newly created islands**.

Previously, these defaults could only be changed in the gamemode's `config.yml`. Now they can be changed directly in-game by opening `/[admin_command] settings` and navigating to the **Island Defaults** tab (tab 3).

Each protection flag is listed with its current default rank — clicking cycles it through the rank ladder. Each island settings flag shows its current default `true`/`false` state — clicking toggles it. Changes are saved immediately to the world settings and take effect for all **new** islands created after the change. Existing islands are not affected.
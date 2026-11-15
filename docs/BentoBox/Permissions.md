# Permissions

Every BentoBox permission, generated from the BentoBox source. For how to use them (VIP ranks, staff roles, common mistakes), see [Permissions & VIP Perks](Permissions-Guide.md).

Game mode permissions start with the game mode's prefix, written `[gamemode].` here: `bskyblock.`, `aoneblock.`, `acidisland.`, `caveblock.` and so on. Addon permissions are listed on each [addon's page](../addons/Bank/index.md).

!!! tip "See the defaults on your server"
    Defaults (everyone, operators only, or nobody) are set by each game mode and differ between them. Run `/bentobox perms` in the console to print every command permission with its default on your server.

## BentoBox

| Permission | Default | Allows |
|---|---|---|
| `bentobox.about` | Everyone | `/bentobox about` |
| `bentobox.version` | Operators | `/bentobox version` |
| `bentobox.admin` | Operators | `/bentobox` and its admin subcommands |
| `bentobox.admin.reload` | Operators | `/bentobox reload` and `reload locales` |
| `bentobox.admin.manage` | Operators | `/bentobox manage` |
| `bentobox.admin.catalog` | Operators | `/bentobox catalog` |
| `bentobox.admin.locale` | Operators | `/bentobox locale` |
| `bentobox.admin.migrate` | Operators | `/bentobox migrate` |
| `bentobox.admin.perms` | Operators | `/bentobox perms` |
| `bentobox.admin.rank` | Operators | `/bentobox rank` |
| `bentobox.admin.placeholders` | Operators | `/bentobox placeholders` |
| `bentobox.admin.dump-placeholders` | Operators | `/bentobox dump-placeholders` |

## Game mode: player commands

Most of these are given to everyone by the game mode. Check with `/bentobox perms`: in game mode releases from before November 2026, `island.homes`, `island.deletehome` and `island.renamehome` are operator-only in most game modes, and SkyGrid is also missing most `island.team` permissions.

| Permission | Allows |
|---|---|
| `[gamemode].island` | The player command itself and `help` |
| `[gamemode].island.ban` | `ban`, `banlist`, `unban` |
| `[gamemode].island.create` | `create` |
| `[gamemode].island.deletehome` | `deletehome` |
| `[gamemode].island.expel` | `expel` |
| `[gamemode].island.home` | `go` |
| `[gamemode].island.homes` | `homes` |
| `[gamemode].island.info` | `info` |
| `[gamemode].island.language` | `language` |
| `[gamemode].island.lock` | `lock` |
| `[gamemode].island.name` | `resetname`, `setname` |
| `[gamemode].island.near` | `near` |
| `[gamemode].island.renamehome` | `renamehome` |
| `[gamemode].island.reset` | `reset` |
| `[gamemode].island.sethome` | `sethome` |
| `[gamemode].island.settings` | `settings` |
| `[gamemode].island.spawn` | `spawn` |
| `[gamemode].island.team` | `team` |
| `[gamemode].island.team.accept` | `team accept` |
| `[gamemode].island.team.coop` | `team coop`, `team uncoop` |
| `[gamemode].island.team.invite` | `team invite` |
| `[gamemode].island.team.kick` | `team kick` |
| `[gamemode].island.team.leave` | `team leave` |
| `[gamemode].island.team.promote` | `team demote`, `team promote` |
| `[gamemode].island.team.reject` | `team reject` |
| `[gamemode].island.team.setowner` | `team setowner` |
| `[gamemode].island.team.trust` | `team trust`, `team untrust` |

## Game mode: admin and moderator commands

Operators only by default.

| Permission | Allows `/[admin_command]` |
|---|---|
| `[gamemode].admin` | The admin command itself and `help` |
| `[gamemode].admin.blueprint` | `blueprint` |
| `[gamemode].admin.blueprint.copy` | `blueprint copy` |
| `[gamemode].admin.blueprint.delete` | `blueprint delete` |
| `[gamemode].admin.blueprint.list` | `blueprint list` |
| `[gamemode].admin.blueprint.load` | `blueprint load` |
| `[gamemode].admin.blueprint.origin` | `blueprint origin` |
| `[gamemode].admin.blueprint.paste` | `blueprint paste` |
| `[gamemode].admin.blueprint.pos1` | `blueprint pos1` |
| `[gamemode].admin.blueprint.pos2` | `blueprint pos2` |
| `[gamemode].admin.blueprint.rename` | `blueprint rename` |
| `[gamemode].admin.blueprint.save` | `blueprint save` |
| `[gamemode].admin.blueprint.sink` | `blueprint sink` |
| `[gamemode].admin.deaths` | `deaths` |
| `[gamemode].admin.deaths.add` | `deaths add` |
| `[gamemode].admin.deaths.remove` | `deaths remove` |
| `[gamemode].admin.deaths.reset` | `deaths reset` |
| `[gamemode].admin.deaths.set` | `deaths set` |
| `[gamemode].admin.delete` | `delete` |
| `[gamemode].admin.getrank` | `getrank` |
| `[gamemode].admin.purge` | `purge` |
| `[gamemode].admin.purge.age-regions` | `purge age-regions` |
| `[gamemode].admin.purge.deleted` | `purge deleted` |
| `[gamemode].admin.purge.protect` | `purge protect` |
| `[gamemode].admin.purge.unowned` | `purge unowned` |
| `[gamemode].admin.range` | `range` |
| `[gamemode].admin.range.add` | `range add` |
| `[gamemode].admin.range.display` | `range display` |
| `[gamemode].admin.range.purgebonus` | `range purgebonus` |
| `[gamemode].admin.range.remove` | `range remove` |
| `[gamemode].admin.range.removebonus` | `range removebonus` |
| `[gamemode].admin.range.reset` | `range reset` |
| `[gamemode].admin.range.set` | `range set` |
| `[gamemode].admin.register` | `register` |
| `[gamemode].admin.reload` | `reload` |
| `[gamemode].admin.resetflags` | `resetflags` |
| `[gamemode].admin.resets` | `resets` |
| `[gamemode].admin.resets.add` | `resets add` |
| `[gamemode].admin.resets.remove` | `resets remove`, `resets reset` |
| `[gamemode].admin.resets.set` | `resets set` |
| `[gamemode].admin.setprotectionlocation` | `setprotectionlocation` |
| `[gamemode].admin.setrank` | `setrank` |
| `[gamemode].admin.setspawn` | `setspawn` |
| `[gamemode].admin.setspawnpoint` | `setspawnpoint` |
| `[gamemode].admin.settings` | `settings` |
| `[gamemode].admin.tp` | `tp`, `tpend`, `tpnether` |
| `[gamemode].admin.tpuser` | `tpuser`, `tpuserend`, `tpusernether` |
| `[gamemode].admin.undelete` | `undelete` |
| `[gamemode].admin.unregister` | `unregister` |
| `[gamemode].admin.version` | `version` |
| `[gamemode].admin.why` | `why` |
| `[gamemode].mod.deletehomes` | `deletehomes` |
| `[gamemode].mod.info` | `info` |
| `[gamemode].mod.maxhomes` | `maxhomes` |
| `[gamemode].mod.resethome` | `resethome` |
| `[gamemode].mod.resetname` | `resetname` |
| `[gamemode].mod.switch` | `switch` |
| `[gamemode].mod.team` | `team` |
| `[gamemode].mod.team.add` | `team add` |
| `[gamemode].mod.team.disband` | `team disband` |
| `[gamemode].mod.team.disbandall` | `team disbandall` |
| `[gamemode].mod.team.kick` | `team kick` |
| `[gamemode].mod.team.maxsize` | `team maxsize` |
| `[gamemode].mod.team.setowner` | `team setowner` |

## Game mode: limits and perks

These end in a number, which replaces the config value for that player. The highest number a player has wins. See [Permissions & VIP Perks](Permissions-Guide.md#perks-with-a-number) for the rules.

| Permission | Sets | Config value it replaces |
|---|---|---|
| `[gamemode].team.maxsize.<n>` | Team size, including the owner (island owner's permission) | `island.max-team-size` |
| `[gamemode].coop.maxsize.<n>` | Coop players (island owner's permission) | `island.max-coop-size` |
| `[gamemode].trust.maxsize.<n>` | Trusted players (island owner's permission) | `island.max-trusted-size` |
| `[gamemode].island.range.<n>` | Island protection range (island owner's permission) | `world.protection-range` |
| `[gamemode].island.maxhomes.<n>` | Number of homes (island owner's permission) | `island.max-homes` |
| `[gamemode].island.number.<n>` | Number of islands a player can own | `world.concurrent-islands` |
| `[gamemode].ban.maxlimit.<n>` | Players they can ban at once | `world.ban-limit` |

| Permission | Allows |
|---|---|
| `[gamemode].island.create.<bundle>` | Choosing a starter island (blueprint bundle) that requires a permission |
| `[gamemode].island.name.format` | Colour codes in island names |

## Game mode: island settings

| Permission | Allows |
|---|---|
| `[gamemode].settings.<FLAG_ID>` | Changing that setting in `/[player_command] settings` |
| `[gamemode].settings.*` | Changing every setting |
| `[gamemode].admin.settings.<FLAG_ID>` | Changing that flag in `/[admin_command] settings` |
| `[gamemode].admin.world.settings.<FLAG_ID>` | Changing that world setting or world protection |
| `[gamemode].admin.set-world-defaults` | The World Protections tab of the admin settings |

See [Protection, Flags & Ranks](Island-Protection,-Flags-&-Ranks.md) for the flag IDs.

## Game mode: moderator bypasses

| Permission | Effect |
|---|---|
| `[gamemode].mod.bypassprotect` | Ignore all protection flags everywhere |
| `[gamemode].mod.bypass.<FLAG_ID>.everywhere` | Ignore one protection flag everywhere |
| `[gamemode].mod.bypass.<FLAG_ID>.island` | Ignore one protection flag on islands |
| `[gamemode].mod.bypasslock` | Enter locked islands |
| `[gamemode].mod.bypassban` | Enter islands they are banned from |
| `[gamemode].mod.bypassexpel` | Can't be expelled |
| `[gamemode].mod.bypasscooldowns` | Skip command cooldowns |
| `[gamemode].mod.bypassdelays` | Skip teleport delays |
| `[gamemode].admin.noban` | Can't be banned from islands |
| `[gamemode].admin.noexpel` | Can't be expelled from islands |

`/[admin_command] switch` turns a moderator's bypass permissions off and on. See [Bypass the protection](Island-Protection,-Flags-&-Ranks.md#bypass-the-protection).

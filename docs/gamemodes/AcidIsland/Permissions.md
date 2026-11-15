# AcidIsland Permissions

AcidIsland permissions start with `acidisland.`. Every permission is listed in the [Permissions reference](../../BentoBox/Permissions.md) with `[gamemode]` in place of `acidisland`. For VIP perks such as bigger teams, islands and more homes, see [Permissions & VIP Perks](../../BentoBox/Permissions-Guide.md).

## Player commands: who has them by default

These defaults come from AcidIsland's `addon.yml`. **Everyone** means all players have the permission unless you take it away; **Operators** means you need to give it to players with your permissions plugin. Run `/bentobox perms` in the console to see the defaults on your server.

| Permission | Commands | Default |
|---|---|---|
| `acidisland.island` | The player command itself | Everyone |
| `acidisland.island.create` | `create` | Everyone |
| `acidisland.island.home` | `go` | Everyone |
| `acidisland.island.homes` | `homes` | Everyone |
| `acidisland.island.sethome` | `sethome` | Everyone |
| `acidisland.island.deletehome` | `deletehome` | Everyone |
| `acidisland.island.renamehome` | `renamehome` | Everyone |
| `acidisland.island.spawn` | `spawn` | Everyone |
| `acidisland.island.info` | `info` | Everyone |
| `acidisland.island.near` | `near` | Everyone |
| `acidisland.island.reset` | `reset` | Everyone |
| `acidisland.island.name` | `setname`, `resetname` | Everyone |
| `acidisland.island.language` | `language` | Everyone |
| `acidisland.island.settings` | `settings` | Everyone |
| `acidisland.island.lock` | `lock` | Everyone |
| `acidisland.island.ban` | `ban`, `unban`, `banlist` | Everyone |
| `acidisland.island.expel` | `expel` | Everyone |
| `acidisland.island.team` | `team` | Everyone |
| `acidisland.island.team.invite` | `team invite` | Everyone |
| `acidisland.island.team.accept` | `team accept` | Everyone |
| `acidisland.island.team.reject` | `team reject` | Everyone |
| `acidisland.island.team.leave` | `team leave` | Everyone |
| `acidisland.island.team.kick` | `team kick` | Everyone |
| `acidisland.island.team.promote` | `team promote`, `team demote` | Everyone |
| `acidisland.island.team.setowner` | `team setowner` | Everyone |
| `acidisland.island.team.trust` | `team trust`, `team untrust` | Everyone |
| `acidisland.island.team.coop` | `team coop`, `team uncoop` | Everyone |

Admin and moderator permissions (`acidisland.admin.*`, `acidisland.mod.*`) are for operators by default. See [Staff permissions](../../BentoBox/Permissions-Guide.md#staff-permissions).

# StrangerRealms Permissions

StrangerRealms permissions start with `strangerrealms.`. Every permission is listed in the [Permissions reference](../../BentoBox/Permissions.md) with `[gamemode]` in place of `strangerrealms`. For VIP perks such as bigger teams, islands and more homes, see [Permissions & VIP Perks](../../BentoBox/Permissions-Guide.md).

## Player commands: who has them by default

These defaults come from StrangerRealms's `addon.yml`. **Everyone** means all players have the permission unless you take it away; **Operators** means you need to give it to players with your permissions plugin. Run `/bentobox perms` in the console to see the defaults on your server.

| Permission | Commands | Default |
|---|---|---|
| `strangerrealms.island` | The player command itself | Everyone |
| `strangerrealms.island.create` | `create` | Operators (not declared) |
| `strangerrealms.island.home` | `go` | Everyone |
| `strangerrealms.island.homes` | `homes` | Everyone |
| `strangerrealms.island.sethome` | `sethome` | Everyone |
| `strangerrealms.island.deletehome` | `deletehome` | Everyone |
| `strangerrealms.island.renamehome` | `renamehome` | Everyone |
| `strangerrealms.island.info` | `info` | Everyone |
| `strangerrealms.island.near` | `near` | Everyone |
| `strangerrealms.island.reset` | `reset` | Nobody |
| `strangerrealms.island.name` | `setname`, `resetname` | Everyone |
| `strangerrealms.island.language` | `language` | Everyone |
| `strangerrealms.island.settings` | `settings` | Everyone |
| `strangerrealms.island.lock` | `lock` | Everyone |
| `strangerrealms.island.ban` | `ban`, `unban`, `banlist` | Everyone |
| `strangerrealms.island.expel` | `expel` | Everyone |
| `strangerrealms.island.team` | `team` | Everyone |
| `strangerrealms.island.team.invite` | `team invite` | Everyone |
| `strangerrealms.island.team.accept` | `team accept` | Everyone |
| `strangerrealms.island.team.reject` | `team reject` | Everyone |
| `strangerrealms.island.team.leave` | `team leave` | Everyone |
| `strangerrealms.island.team.kick` | `team kick` | Everyone |
| `strangerrealms.island.team.promote` | `team promote`, `team demote` | Everyone |
| `strangerrealms.island.team.setowner` | `team setowner` | Everyone |
| `strangerrealms.island.team.trust` | `team trust`, `team untrust` | Everyone |
| `strangerrealms.island.team.coop` | `team coop`, `team uncoop` | Everyone |

## Permissions only in StrangerRealms

| Permission | Allows | Default |
|---|---|---|
| `strangerrealms.claim` | `/st claim` | Everyone |
| `strangerrealms.unclaim` | `/st unclaim` | Everyone |
| `strangerrealms.spawn` | `/st spawn` | Everyone |
| `strangerrealms.admin.worldborder` | `/stranger worldborder` | Operators (not declared) |

Admin and moderator permissions (`strangerrealms.admin.*`, `strangerrealms.mod.*`) are for operators by default. See [Staff permissions](../../BentoBox/Permissions-Guide.md#staff-permissions).

# SkyGrid Permissions

SkyGrid permissions start with `skygrid.`. Every permission is listed in the [Permissions reference](../../BentoBox/Permissions.md) with `[gamemode]` in place of `skygrid`. For VIP perks such as bigger teams, islands and more homes, see [Permissions & VIP Perks](../../BentoBox/Permissions-Guide.md).

## Player commands: who has them by default

These defaults come from SkyGrid's `addon.yml`. **Everyone** means all players have the permission unless you take it away; **Operators** means you need to give it to players with your permissions plugin. Run `/bentobox perms` in the console to see the defaults on your server.

| Permission | Commands | Default |
|---|---|---|
| `skygrid.island` | The player command itself | Everyone |
| `skygrid.island.create` | `create` | Everyone |
| `skygrid.island.home` | `go` | Everyone |
| `skygrid.island.homes` | `homes` | Everyone |
| `skygrid.island.sethome` | `sethome` | Everyone |
| `skygrid.island.deletehome` | `deletehome` | Everyone |
| `skygrid.island.renamehome` | `renamehome` | Everyone |
| `skygrid.island.spawn` | `spawn` | Everyone |
| `skygrid.island.info` | `info` | Everyone |
| `skygrid.island.near` | `near` | Everyone |
| `skygrid.island.reset` | `reset` | Everyone |
| `skygrid.island.name` | `setname`, `resetname` | Everyone |
| `skygrid.island.language` | `language` | Everyone |
| `skygrid.island.settings` | `settings` | Everyone |
| `skygrid.island.lock` | `lock` | Nobody |
| `skygrid.island.ban` | `ban`, `unban`, `banlist` | Everyone |
| `skygrid.island.expel` | `expel` | Everyone |
| `skygrid.island.team` | `team` | Everyone |
| `skygrid.island.team.invite` | `team invite` | Everyone |
| `skygrid.island.team.accept` | `team accept` | Everyone |
| `skygrid.island.team.reject` | `team reject` | Everyone |
| `skygrid.island.team.leave` | `team leave` | Everyone |
| `skygrid.island.team.kick` | `team kick` | Everyone |
| `skygrid.island.team.promote` | `team promote`, `team demote` | Everyone |
| `skygrid.island.team.setowner` | `team setowner` | Everyone |
| `skygrid.island.team.trust` | `team trust`, `team untrust` | Everyone |
| `skygrid.island.team.coop` | `team coop`, `team uncoop` | Everyone |

Admin and moderator permissions (`skygrid.admin.*`, `skygrid.mod.*`) are for operators by default. See [Staff permissions](../../BentoBox/Permissions-Guide.md#staff-permissions).

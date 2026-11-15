# Boxed Permissions

Boxed permissions start with `boxed.`. Every permission is listed in the [Permissions reference](../../BentoBox/Permissions.md) with `[gamemode]` in place of `boxed`. For VIP perks such as bigger teams, islands and more homes, see [Permissions & VIP Perks](../../BentoBox/Permissions-Guide.md).

## Player commands: who has them by default

These defaults come from Boxed's `addon.yml`. **Everyone** means all players have the permission unless you take it away; **Operators** means you need to give it to players with your permissions plugin. Run `/bentobox perms` in the console to see the defaults on your server.

| Permission | Commands | Default |
|---|---|---|
| `boxed.island` | The player command itself | Everyone |
| `boxed.island.create` | `create` | Everyone |
| `boxed.island.home` | `go` | Everyone |
| `boxed.island.homes` | `homes` | Everyone |
| `boxed.island.sethome` | `sethome` | Everyone |
| `boxed.island.deletehome` | `deletehome` | Everyone |
| `boxed.island.renamehome` | `renamehome` | Everyone |
| `boxed.island.spawn` | `spawn` | Everyone |
| `boxed.island.info` | `info` | Everyone |
| `boxed.island.near` | `near` | Everyone |
| `boxed.island.reset` | `reset` | Everyone |
| `boxed.island.name` | `setname`, `resetname` | Everyone |
| `boxed.island.language` | `language` | Everyone |
| `boxed.island.settings` | `settings` | Everyone |
| `boxed.island.lock` | `lock` | Everyone |
| `boxed.island.ban` | `ban`, `unban`, `banlist` | Everyone |
| `boxed.island.expel` | `expel` | Everyone |
| `boxed.island.team` | `team` | Everyone |
| `boxed.island.team.invite` | `team invite` | Everyone |
| `boxed.island.team.accept` | `team accept` | Everyone |
| `boxed.island.team.reject` | `team reject` | Everyone |
| `boxed.island.team.leave` | `team leave` | Everyone |
| `boxed.island.team.kick` | `team kick` | Everyone |
| `boxed.island.team.promote` | `team promote`, `team demote` | Everyone |
| `boxed.island.team.setowner` | `team setowner` | Everyone |
| `boxed.island.team.trust` | `team trust`, `team untrust` | Everyone |
| `boxed.island.team.coop` | `team coop`, `team uncoop` | Everyone |

## Permissions only in Boxed

| Permission | Allows | Default |
|---|---|---|
| `boxed.boxed.commands.boxadmin.place` | `/boxadmin place` | Operators (not declared) |

Admin and moderator permissions (`boxed.admin.*`, `boxed.mod.*`) are for operators by default. See [Staff permissions](../../BentoBox/Permissions-Guide.md#staff-permissions).

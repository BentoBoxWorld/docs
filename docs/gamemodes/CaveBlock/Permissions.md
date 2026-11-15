# CaveBlock Permissions

CaveBlock permissions start with `caveblock.`. Every permission is listed in the [Permissions reference](../../BentoBox/Permissions.md) with `[gamemode]` in place of `caveblock`. For VIP perks such as bigger teams, islands and more homes, see [Permissions & VIP Perks](../../BentoBox/Permissions-Guide.md).

## Player commands: who has them by default

These defaults come from CaveBlock's `addon.yml`. **Everyone** means all players have the permission unless you take it away; **Operators** means you need to give it to players with your permissions plugin. Run `/bentobox perms` in the console to see the defaults on your server.

| Permission | Commands | Default |
|---|---|---|
| `caveblock.island` | The player command itself | Everyone |
| `caveblock.island.create` | `create` | Everyone |
| `caveblock.island.home` | `go` | Everyone |
| `caveblock.island.homes` | `homes` | Everyone |
| `caveblock.island.sethome` | `sethome` | Everyone |
| `caveblock.island.deletehome` | `deletehome` | Everyone |
| `caveblock.island.renamehome` | `renamehome` | Everyone |
| `caveblock.island.spawn` | `spawn` | Everyone |
| `caveblock.island.info` | `info` | Everyone |
| `caveblock.island.near` | `near` | Everyone |
| `caveblock.island.reset` | `reset` | Everyone |
| `caveblock.island.name` | `setname`, `resetname` | Everyone |
| `caveblock.island.language` | `language` | Everyone |
| `caveblock.island.settings` | `settings` | Everyone |
| `caveblock.island.lock` | `lock` | Everyone |
| `caveblock.island.ban` | `ban`, `unban`, `banlist` | Everyone |
| `caveblock.island.expel` | `expel` | Everyone |
| `caveblock.island.team` | `team` | Everyone |
| `caveblock.island.team.invite` | `team invite` | Everyone |
| `caveblock.island.team.accept` | `team accept` | Everyone |
| `caveblock.island.team.reject` | `team reject` | Everyone |
| `caveblock.island.team.leave` | `team leave` | Everyone |
| `caveblock.island.team.kick` | `team kick` | Everyone |
| `caveblock.island.team.promote` | `team promote`, `team demote` | Everyone |
| `caveblock.island.team.setowner` | `team setowner` | Everyone |
| `caveblock.island.team.trust` | `team trust`, `team untrust` | Everyone |
| `caveblock.island.team.coop` | `team coop`, `team uncoop` | Everyone |

Admin and moderator permissions (`caveblock.admin.*`, `caveblock.mod.*`) are for operators by default. See [Staff permissions](../../BentoBox/Permissions-Guide.md#staff-permissions).

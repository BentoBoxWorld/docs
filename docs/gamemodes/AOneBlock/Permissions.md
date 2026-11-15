# AOneBlock Permissions

AOneBlock permissions start with `aoneblock.`. Every permission is listed in the [Permissions reference](../../BentoBox/Permissions.md) with `[gamemode]` in place of `aoneblock`. For VIP perks such as bigger teams, islands and more homes, see [Permissions & VIP Perks](../../BentoBox/Permissions-Guide.md).

## Player commands: who has them by default

These defaults come from AOneBlock's `addon.yml`. **Everyone** means all players have the permission unless you take it away; **Operators** means you need to give it to players with your permissions plugin. Run `/bentobox perms` in the console to see the defaults on your server.

| Permission | Commands | Default |
|---|---|---|
| `aoneblock.island` | The player command itself | Everyone |
| `aoneblock.island.create` | `create` | Everyone |
| `aoneblock.island.home` | `go` | Everyone |
| `aoneblock.island.homes` | `homes` | Everyone |
| `aoneblock.island.sethome` | `sethome` | Everyone |
| `aoneblock.island.deletehome` | `deletehome` | Everyone |
| `aoneblock.island.renamehome` | `renamehome` | Everyone |
| `aoneblock.island.spawn` | `spawn` | Everyone |
| `aoneblock.island.info` | `info` | Everyone |
| `aoneblock.island.near` | `near` | Everyone |
| `aoneblock.island.reset` | `reset` | Everyone |
| `aoneblock.island.name` | `setname`, `resetname` | Everyone |
| `aoneblock.island.language` | `language` | Everyone |
| `aoneblock.island.settings` | `settings` | Everyone |
| `aoneblock.island.lock` | `lock` | Everyone |
| `aoneblock.island.ban` | `ban`, `unban`, `banlist` | Everyone |
| `aoneblock.island.expel` | `expel` | Everyone |
| `aoneblock.island.team` | `team` | Everyone |
| `aoneblock.island.team.invite` | `team invite` | Everyone |
| `aoneblock.island.team.accept` | `team accept` | Everyone |
| `aoneblock.island.team.reject` | `team reject` | Everyone |
| `aoneblock.island.team.leave` | `team leave` | Everyone |
| `aoneblock.island.team.kick` | `team kick` | Everyone |
| `aoneblock.island.team.promote` | `team promote`, `team demote` | Everyone |
| `aoneblock.island.team.setowner` | `team setowner` | Everyone |
| `aoneblock.island.team.trust` | `team trust`, `team untrust` | Everyone |
| `aoneblock.island.team.coop` | `team coop`, `team uncoop` | Everyone |

## Permissions only in AOneBlock

| Permission | Allows | Default |
|---|---|---|
| `aoneblock.count` | `/ob count` | Everyone |
| `aoneblock.phases` | `/ob phases` | Nobody |
| `aoneblock.island.setcount` | `/ob setCount` | Operators |
| `aoneblock.respawn-block` | `/ob respawnBlock` | Everyone |
| `aoneblock.island.bossbar` | `/ob bossbar` | Everyone |
| `aoneblock.island.actionbar` | `/ob actionbar` | Everyone |
| `aoneblock.admin.setcount` | `/obadmin setcount` | Operators |
| `aoneblock.admin.setchest` | `/obadmin setchest` | Operators |
| `aoneblock.admin.sanity` | `/obadmin sanity` | Operators |
| `aoneblock.admin.phases` | `/obadmin phases` | Operators |

Admin and moderator permissions (`aoneblock.admin.*`, `aoneblock.mod.*`) are for operators by default. See [Staff permissions](../../BentoBox/Permissions-Guide.md#staff-permissions).

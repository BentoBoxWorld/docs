# BSkyBlock Permissions

BSkyBlock permissions start with `bskyblock.`. Every permission is listed in the [Permissions reference](../../BentoBox/Permissions.md) with `[gamemode]` in place of `bskyblock`. For VIP perks such as bigger teams, islands and more homes, see [Permissions & VIP Perks](../../BentoBox/Permissions-Guide.md).

## Player commands: who has them by default

These defaults come from BSkyBlock's `addon.yml`. **Everyone** means all players have the permission unless you take it away; **Operators** means you need to give it to players with your permissions plugin. Run `/bentobox perms` in the console to see the defaults on your server.

| Permission | Commands | Default |
|---|---|---|
| `bskyblock.island` | The player command itself | Everyone |
| `bskyblock.island.create` | `create` | Everyone |
| `bskyblock.island.home` | `go` | Everyone |
| `bskyblock.island.homes` | `homes` | Everyone |
| `bskyblock.island.sethome` | `sethome` | Everyone |
| `bskyblock.island.deletehome` | `deletehome` | Everyone |
| `bskyblock.island.renamehome` | `renamehome` | Everyone |
| `bskyblock.island.spawn` | `spawn` | Everyone |
| `bskyblock.island.info` | `info` | Everyone |
| `bskyblock.island.near` | `near` | Everyone |
| `bskyblock.island.reset` | `reset` | Everyone |
| `bskyblock.island.name` | `setname`, `resetname` | Everyone |
| `bskyblock.island.language` | `language` | Everyone |
| `bskyblock.island.settings` | `settings` | Everyone |
| `bskyblock.island.lock` | `lock` | Everyone |
| `bskyblock.island.ban` | `ban`, `unban`, `banlist` | Everyone |
| `bskyblock.island.expel` | `expel` | Everyone |
| `bskyblock.island.team` | `team` | Everyone |
| `bskyblock.island.team.invite` | `team invite` | Everyone |
| `bskyblock.island.team.accept` | `team accept` | Everyone |
| `bskyblock.island.team.reject` | `team reject` | Everyone |
| `bskyblock.island.team.leave` | `team leave` | Everyone |
| `bskyblock.island.team.kick` | `team kick` | Everyone |
| `bskyblock.island.team.promote` | `team promote`, `team demote` | Everyone |
| `bskyblock.island.team.setowner` | `team setowner` | Everyone |
| `bskyblock.island.team.trust` | `team trust`, `team untrust` | Everyone |
| `bskyblock.island.team.coop` | `team coop`, `team uncoop` | Everyone |

Admin and moderator permissions (`bskyblock.admin.*`, `bskyblock.mod.*`) are for operators by default. See [Staff permissions](../../BentoBox/Permissions-Guide.md#staff-permissions).

# Poseidon Permissions

Poseidon permissions start with `poseidon.`. Every permission is listed in the [Permissions reference](../../BentoBox/Permissions.md) with `[gamemode]` in place of `poseidon`. For VIP perks such as bigger teams, islands and more homes, see [Permissions & VIP Perks](../../BentoBox/Permissions-Guide.md).

## Player commands: who has them by default

These defaults come from Poseidon's `addon.yml`. **Everyone** means all players have the permission unless you take it away; **Operators** means you need to give it to players with your permissions plugin. Run `/bentobox perms` in the console to see the defaults on your server.

| Permission | Commands | Default |
|---|---|---|
| `poseidon.island` | The player command itself | Everyone |
| `poseidon.island.create` | `create` | Everyone |
| `poseidon.island.home` | `go` | Everyone |
| `poseidon.island.homes` | `homes` | Everyone |
| `poseidon.island.sethome` | `sethome` | Everyone |
| `poseidon.island.deletehome` | `deletehome` | Everyone |
| `poseidon.island.renamehome` | `renamehome` | Everyone |
| `poseidon.island.spawn` | `spawn` | Everyone |
| `poseidon.island.info` | `info` | Everyone |
| `poseidon.island.near` | `near` | Everyone |
| `poseidon.island.reset` | `reset` | Everyone |
| `poseidon.island.name` | `setname`, `resetname` | Everyone |
| `poseidon.island.language` | `language` | Everyone |
| `poseidon.island.settings` | `settings` | Everyone |
| `poseidon.island.lock` | `lock` | Everyone |
| `poseidon.island.ban` | `ban`, `unban`, `banlist` | Everyone |
| `poseidon.island.expel` | `expel` | Everyone |
| `poseidon.island.team` | `team` | Everyone |
| `poseidon.island.team.invite` | `team invite` | Everyone |
| `poseidon.island.team.accept` | `team accept` | Everyone |
| `poseidon.island.team.reject` | `team reject` | Everyone |
| `poseidon.island.team.leave` | `team leave` | Everyone |
| `poseidon.island.team.kick` | `team kick` | Everyone |
| `poseidon.island.team.promote` | `team promote`, `team demote` | Everyone |
| `poseidon.island.team.setowner` | `team setowner` | Everyone |
| `poseidon.island.team.trust` | `team trust`, `team untrust` | Everyone |
| `poseidon.island.team.coop` | `team coop`, `team uncoop` | Everyone |

Admin and moderator permissions (`poseidon.admin.*`, `poseidon.mod.*`) are for operators by default. See [Staff permissions](../../BentoBox/Permissions-Guide.md#staff-permissions).

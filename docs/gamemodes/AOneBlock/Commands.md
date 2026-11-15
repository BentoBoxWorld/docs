# AOneBlock Commands

| | Command | Permission prefix |
|---|---|---|
| Players | `/ob` (also `/oneblock`) | `aoneblock.` |
| Admins | `/obadmin` (also `/oneblockadmin`, `/oba`) | `aoneblock.` |

You can rename both commands in the game mode's `config.yml`.

## Standard commands

AOneBlock uses BentoBox's standard player and admin commands. They're all listed, with their permissions, in the [Commands reference](../../BentoBox/Commands.md): replace `/[player_command]` with `/ob`, `/[admin_command]` with `/obadmin` and `[gamemode]` with `aoneblock`. For example:

```
/ob              go to your island, or create one
/ob team invite <player>
/ob settings
/obadmin info <player>
/obadmin why <player>
```

For what they do, see the [Player Guide](../../BentoBox/Player-Guide.md) and the Admin Guides, such as [Teams & Ranks](../../BentoBox/About/Teams.md) and [Islands](../../BentoBox/About/IslandManagement.md).

## Commands only in AOneBlock

| Command | What it does | Permission | Default |
|---|---|---|---|
| `/ob count` | Show your block count and phase | `aoneblock.count` | Everyone |
| `/ob phases` | Show a list of all the phases | `aoneblock.phases` | Nobody |
| `/ob setCount <count>` | Set your block count back to a value you have already reached | `aoneblock.island.setcount` | Operators |
| `/ob respawnBlock` | Respawn the magic block if it has disappeared (alias: check) | `aoneblock.respawn-block` | Everyone |
| `/ob bossbar` | Turn the phase boss bar on or off | `aoneblock.island.bossbar` | Everyone |
| `/ob actionbar` | Turn the phase action bar on or off | `aoneblock.island.actionbar` | Everyone |
| `/obadmin setcount <name> <count> [lifetime]` | Set a player's block count | `aoneblock.admin.setcount` | Operators |
| `/obadmin setchest <phase> <rarity>` | Add the chest you are looking at to a phase, with that rarity | `aoneblock.admin.setchest` | Operators |
| `/obadmin sanity <phase>` | Print a check of the phase's block probabilities to the console | `aoneblock.admin.sanity` | Operators |
| `/obadmin phases` | Open the phase order editor | `aoneblock.admin.phases` | Operators |

The AOneBlock player command labels (`count`, `phases`, `setCount`, `respawnBlock`, `bossbar`, `actionbar`) can be renamed in `config.yml` under `aoneblock.command`. The boss bar and action bar commands only exist when those features are turned on.

## Addon commands

Addons add subcommands to `/ob` and `/obadmin`, for example `/ob level` from [Level](../../addons/Level/index.md) or `/ob challenges` from [Challenges](../../addons/Challenges/index.md). See each addon's page.

# CaveBlock Commands

| | Command | Permission prefix |
|---|---|---|
| Players | `/cave` (also `/cb`) | `caveblock.` |
| Admins | `/cbadmin` (also `/cba`) | `caveblock.` |

You can rename both commands in the game mode's `config.yml`.

## Standard commands

CaveBlock uses BentoBox's standard player and admin commands. They're all listed, with their permissions, in the [Commands reference](../../BentoBox/Commands.md): replace `/[player_command]` with `/cave`, `/[admin_command]` with `/cbadmin` and `[gamemode]` with `caveblock`. For example:

```
/cave              go to your cave, or create one
/cave team invite <player>
/cave settings
/cbadmin info <player>
/cbadmin why <player>
```

For what they do, see the [Player Guide](../../BentoBox/Player-Guide.md) and the Admin Guides, such as [Teams & Ranks](../../BentoBox/About/Teams.md) and [Islands](../../BentoBox/About/IslandManagement.md).

## Commands only in CaveBlock

| Command | What it does | Permission | Default |
|---|---|---|---|
| `/cave about` | Show copyright and license information | `caveblock.island` | Everyone |

## Addon commands

Addons add subcommands to `/cave` and `/cbadmin`, for example `/cave level` from [Level](../../addons/Level/index.md) or `/cave challenges` from [Challenges](../../addons/Challenges/index.md). See each addon's page.

# BSkyBlock Commands

| | Command | Permission prefix |
|---|---|---|
| Players | `/island` (also `/is`, `/skyblock`, `/sb`) | `bskyblock.` |
| Admins | `/bsbadmin` (also `/bsb`, `/skyblockadmin`, `/sbadmin`, `/sba`) | `bskyblock.` |

You can rename both commands in the game mode's `config.yml`.

## Standard commands

BSkyBlock uses BentoBox's standard player and admin commands. They're all listed, with their permissions, in the [Commands reference](../../BentoBox/Commands.md): replace `/[player_command]` with `/island`, `/[admin_command]` with `/bsbadmin` and `[gamemode]` with `bskyblock`. For example:

```
/island              go to your island, or create one
/island team invite <player>
/island settings
/bsbadmin info <player>
/bsbadmin why <player>
```

For what they do, see the [Player Guide](../../BentoBox/Player-Guide.md) and the Admin Guides, such as [Teams & Ranks](../../BentoBox/About/Teams.md) and [Islands](../../BentoBox/About/IslandManagement.md).

## Commands only in BSkyBlock

| Command | What it does | Permission | Default |
|---|---|---|---|
| `/island about` | Show copyright and license information | `bskyblock.island` | Everyone |

## Addon commands

Addons add subcommands to `/island` and `/bsbadmin`, for example `/island level` from [Level](../../addons/Level/index.md) or `/island challenges` from [Challenges](../../addons/Challenges/index.md). See each addon's page.

# AcidIsland Commands

| | Command | Permission prefix |
|---|---|---|
| Players | `/ai` | `acidisland.` |
| Admins | `/acid` | `acidisland.` |

You can rename both commands in the game mode's `config.yml`.

## Standard commands

AcidIsland uses BentoBox's standard player and admin commands. They're all listed, with their permissions, in the [Commands reference](../../BentoBox/Commands.md): replace `/[player_command]` with `/ai`, `/[admin_command]` with `/acid` and `[gamemode]` with `acidisland`. For example:

```
/ai              go to your island, or create one
/ai team invite <player>
/ai settings
/acid info <player>
/acid why <player>
```

For what they do, see the [Player Guide](../../BentoBox/Player-Guide.md) and the Admin Guides, such as [Teams & Ranks](../../BentoBox/About/Teams.md) and [Islands](../../BentoBox/About/IslandManagement.md).

## Commands only in AcidIsland

| Command | What it does | Permission | Default |
|---|---|---|---|
| `/ai about` | Show copyright and license information | `acidisland.island` | Everyone |

## Addon commands

Addons add subcommands to `/ai` and `/acid`, for example `/ai level` from [Level](../../addons/Level/index.md) or `/ai challenges` from [Challenges](../../addons/Challenges/index.md). See each addon's page.

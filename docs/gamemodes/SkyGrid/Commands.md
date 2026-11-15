# SkyGrid Commands

| | Command | Permission prefix |
|---|---|---|
| Players | `/skygrid` (also `/sg`) | `skygrid.` |
| Admins | `/sgadmin` (also `/sga`) | `skygrid.` |

You can rename both commands in the game mode's `config.yml`.

## Standard commands

SkyGrid uses BentoBox's standard player and admin commands. They're all listed, with their permissions, in the [Commands reference](../../BentoBox/Commands.md): replace `/[player_command]` with `/skygrid`, `/[admin_command]` with `/sgadmin` and `[gamemode]` with `skygrid`. For example:

```
/skygrid              go to your area, or create one
/skygrid team invite <player>
/skygrid settings
/sgadmin info <player>
/sgadmin why <player>
```

For what they do, see the [Player Guide](../../BentoBox/Player-Guide.md) and the Admin Guides, such as [Teams & Ranks](../../BentoBox/About/Teams.md) and [Islands](../../BentoBox/About/IslandManagement.md).

SkyGrid doesn't add any commands of its own.

## Addon commands

Addons add subcommands to `/skygrid` and `/sgadmin`, for example `/skygrid level` from [Level](../../addons/Level/index.md) or `/skygrid challenges` from [Challenges](../../addons/Challenges/index.md). See each addon's page.

# Boxed Commands

| | Command | Permission prefix |
|---|---|---|
| Players | `/boxed` (also `/bx`, `/box`) | `boxed.` |
| Admins | `/boxadmin` | `boxed.` |

You can rename both commands in the game mode's `config.yml`.

## Standard commands

Boxed uses BentoBox's standard player and admin commands. They're all listed, with their permissions, in the [Commands reference](../../BentoBox/Commands.md): replace `/[player_command]` with `/boxed`, `/[admin_command]` with `/boxadmin` and `[gamemode]` with `boxed`. For example:

```
/boxed              go to your box, or create one
/boxed team invite <player>
/boxed settings
/boxadmin info <player>
/boxadmin why <player>
```

For what they do, see the [Player Guide](../../BentoBox/Player-Guide.md) and the Admin Guides, such as [Teams & Ranks](../../BentoBox/About/Teams.md) and [Islands](../../BentoBox/About/IslandManagement.md).

## Commands only in Boxed

| Command | What it does | Permission | Default |
|---|---|---|---|
| `/boxadmin place <x> <y> <z> <rotation> <mirror> <no mobs>` | Place a structure at a location | `boxed.boxed.commands.boxadmin.place` | Operators (not declared) |

## Addon commands

Addons add subcommands to `/boxed` and `/boxadmin`, for example `/boxed level` from [Level](../../addons/Level/index.md) or `/boxed challenges` from [Challenges](../../addons/Challenges/index.md). See each addon's page.

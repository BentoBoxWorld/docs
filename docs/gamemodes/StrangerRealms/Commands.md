# StrangerRealms Commands

| | Command | Permission prefix |
|---|---|---|
| Players | `/st` (also `/strange`) | `strangerrealms.` |
| Admins | `/stranger` | `strangerrealms.` |

You can rename both commands in the game mode's `config.yml`.

## Standard commands

StrangerRealms uses BentoBox's standard player and admin commands. They're all listed, with their permissions, in the [Commands reference](../../BentoBox/Commands.md): replace `/[player_command]` with `/st`, `/[admin_command]` with `/stranger` and `[gamemode]` with `strangerrealms`. For example:

```
/st              go to your claim, or create one
/st team invite <player>
/st settings
/stranger info <player>
/stranger why <player>
```

For what they do, see the [Player Guide](../../BentoBox/Player-Guide.md) and the Admin Guides, such as [Teams & Ranks](../../BentoBox/About/Teams.md) and [Islands](../../BentoBox/About/IslandManagement.md).

## Commands only in StrangerRealms

| Command | What it does | Permission | Default |
|---|---|---|---|
| `/st claim` | Claim the land you are standing on | `strangerrealms.claim` | Everyone |
| `/st unclaim` | Remove your claim | `strangerrealms.unclaim` | Everyone |
| `/st spawn` | Teleport to the spawn (replaces the standard spawn command) | `strangerrealms.spawn` | Everyone |
| `/stranger worldborder [on\|off\|set\|auto\|info]` | Change the world border settings | `strangerrealms.admin.worldborder` | Operators (not declared) |

Stranger Realms players claim land with `/st claim` instead of creating an island, so `/st create` is not given to players (`strangerrealms.island.create` is not declared, which makes it operator-only), and `/st` with no subcommand sends new players to spawn.

## Addon commands

Addons add subcommands to `/st` and `/stranger`, for example `/st level` from [Level](../../addons/Level/index.md) or `/st challenges` from [Challenges](../../addons/Challenges/index.md). See each addon's page.

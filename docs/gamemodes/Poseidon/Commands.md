# Poseidon Commands

| | Command | Permission prefix |
|---|---|---|
| Players | `/po` | `poseidon.` |
| Admins | `/padmin` | `poseidon.` |

You can rename both commands in the game mode's `config.yml`.

## Standard commands

Poseidon uses BentoBox's standard player and admin commands. They're all listed, with their permissions, in the [Commands reference](../../BentoBox/Commands.md): replace `/[player_command]` with `/po`, `/[admin_command]` with `/padmin` and `[gamemode]` with `poseidon`. For example:

```
/po              go to your island, or create one
/po team invite <player>
/po settings
/padmin info <player>
/padmin why <player>
```

For what they do, see the [Player Guide](../../BentoBox/Player-Guide.md) and the Admin Guides, such as [Teams & Ranks](../../BentoBox/About/Teams.md) and [Islands](../../BentoBox/About/IslandManagement.md).

## Commands only in Poseidon

| Command | What it does | Permission | Default |
|---|---|---|---|
| `/po about` | Show copyright and license information | `poseidon.island` | Everyone |

## Addon commands

Addons add subcommands to `/po` and `/padmin`, for example `/po level` from [Level](../../addons/Level/index.md) or `/po challenges` from [Challenges](../../addons/Challenges/index.md). See each addon's page.

# Islands

Every BentoBox game mode is built on **islands**: a protected area of the world that belongs to one player or a team. (In game modes like CaveBlock or Boxed the "island" is a cave or a box, but it works the same way.) This page covers how islands are created, sized, reset and deleted, how homes work, and how to clean up old islands.

!!! info "Commands on this page"
    Commands are shown for BSkyBlock (`/island`, `/bsbadmin`). Other game modes use their own command names, for example `/ob` in AOneBlock. Permissions start with the game mode's prefix, for example `bskyblock.` or `aoneblock.`. For what players see, send them the [Player Guide](../Player-Guide.md).

## Before you open: plan the world

Two settings in the game mode's `config.yml` **cannot be changed after islands exist**. Changing them later means wiping the world and database, so decide before players join:

```yaml
world:
  # Radius of each island's space, in blocks.
  # Island centres are twice this apart, so 400 puts centres 800 blocks apart.
  distance-between-islands: 400
  # How much of that space the owner protects to start with (a radius).
  # Can be raised later per island, up to distance-between-islands.
  protection-range: 50
```

- `distance-between-islands` is the **most** an island can ever grow to. Set it to the largest size you might want to give VIPs or sell as upgrades.
- `protection-range` is where islands **start**. It's the area players can build in and protect.

Other settings you may want to look at: `island-height` (Y level of the starting island), `max-islands` (cap the number of islands in the world, `0` = no limit) and `start-x`/`start-z` (which also can't change later).

## Creating islands

New players type `/island`. BentoBox:

1. Shows the **Create Island** menu if there's more than one starter island to choose from (otherwise it skips this).
2. Finds the next free spot, pastes the starter island, and teleports the player there.

You can change what happens:

| Setting (game mode `config.yml`) | Default | What it does |
|---|---|---|
| `new-player-action` | `create` | What `/island` does for players without an island |
| `default-action` | `go` | What `/island` does for players with an island |
| `create-island-on-first-login.enable` | `false` | Create an island automatically when a new player joins |
| `teleport-player-to-island-when-created` | `true` | Teleport the player when their island is ready |

**Choice of starter islands.** Each choice in the Create Island menu is a blueprint bundle. To make one available only to some players (for example a VIP island), set it to require a permission in `/bsbadmin blueprint`, then give `bskyblock.island.create.<bundle-name>`. See [Starter Islands (Blueprints)](BlueprintsSummary.md) and [Making Blueprints](../Blueprints.md).

## Island size (protection range)

The protection range is the radius around the island centre that the owner controls. Players see it with `/island info`; admins can show it in game with `/bsbadmin range display`.

To give some players bigger islands:

| How | Command or permission |
|---|---|
| By rank or VIP, automatically | Give the owner `bskyblock.island.range.<number>`. Checked when the island is created and when the owner logs in |
| One island, by hand | `/bsbadmin range set <player> <range>`, or `range add` / `range remove` to change it by an amount |
| Back to the default | `/bsbadmin range reset <player>` |

The range can't go above `distance-between-islands`. Addons like [Upgrades](../../addons/Upgrades/index.md) can also add range as a bonus; remove addon bonuses with `/bsbadmin range removebonus <player>`.

## Homes

Players teleport to their island with `/island` or `/island go`, and move their home with `/island sethome`.

By default each island has one home. To allow more named homes:

```yaml
island:
  max-homes: 1    # game mode config.yml
```

or give the owner `bskyblock.island.maxhomes.<number>`. Players then use `/island sethome <name>`, `/island go <name>` and `/island homes`. Admins can change one island with `/bsbadmin maxhomes <player> <number>`.

`/island go <name>` finds the home even if the player gets the capital letters wrong or only types the start of the name. On Minecraft 26 and later, a player with several homes who types `/island go` gets a pop-up to pick one (`island.dialogs.go-picker` in BentoBox's `config.yml`).

**Homes in the Nether and End** (when the game mode has island Nether and End worlds) are controlled by `island.sethome.nether.allow` and `island.sethome.the-end.allow`.

| Admin task | Command |
|---|---|
| Put a player's home back to the default spot | `/bsbadmin resethome <player>` |
| Delete all of a player's named homes | `/bsbadmin deletehomes <player>` |
| Go to a player's island | `/bsbadmin tp <player>` |

## Island names

Players name their island with `/island setname <name>` and remove it with `/island resetname`. Names show in leaderboards, warps and placeholders.

Set the rules in **BentoBox's** `config.yml`:

```yaml
island:
  name:
    min-length: 4
    max-length: 20
    uniqueness: false   # true = no two islands in a game mode can share a name
```

Players need `bskyblock.island.name.format` to use colours in names. Admins can clear an offensive name by standing on the island and running `/bsbadmin resetname`.

## Resetting islands

`/island reset` gives a player a fresh island. **The old island is deleted.** Only the owner can reset; any team members are removed from the island.

Control it in the game mode's `config.yml`:

```yaml
island:
  reset:
    reset-limit: -1   # -1 = unlimited, 0 = no resets, 2 = two resets (three islands in total)
```

and in BentoBox's `config.yml`:

```yaml
island:
  cooldown:
    time:
      reset: 300        # seconds a player must wait between resets
  confirmation:
    commands:
      reset: true       # players must confirm before resetting
```

What gets cleared from the player (inventory, ender chest, money, XP) on a new island is set by the `on-join` options described in [Teams & Ranks](Teams.md#what-happens-to-items-and-money-when-players-join-or-leave).

To give a player more resets, change their reset count:

| Command | Effect |
|---|---|
| `/bsbadmin resets reset <player>` | Back to 0 resets used |
| `/bsbadmin resets set <player> <number>` | Set how many resets they've used |
| `/bsbadmin resets add <player> <number>` | Count more resets as used |
| `/bsbadmin resets remove <player> <number>` | Give resets back |

There's no permission for extra resets; use these commands, for example from a rank-up or store plugin.

## Deleting islands

| I want to… | Command |
|---|---|
| Delete a player's island | `/bsbadmin delete <player>` |
| Delete the island I'm standing on | `/bsbadmin delete` (refused while it still has a team) |
| Undo a delete before cleanup runs | Stand on it and run `/bsbadmin undelete` |
| Give a deleted or unowned island to a player | Stand on it and run `/bsbadmin register <player>` |
| Remove an owner but keep the blocks | `/bsbadmin unregister <owner>` |

Deleting an island removes the owner straight away, so the player can create a new one. The **blocks** are removed later, when the region files are cleaned up (see below). Until then, `undelete` or `register` can bring the island back.

## Cleaning up old islands

Deleted and reset islands, and islands from players who never came back, take up disk space. BentoBox removes them by deleting the world's **region files** (each covers a 512×512 block area) once no active island is in them.

**Automatic cleanup** is set in BentoBox's `config.yml`:

```yaml
island:
  deletion:
    housekeeping:
      deleted-sweep:
        enabled: true         # clean up deleted and reset islands
        interval-hours: 24
      age-sweep:
        enabled: false        # also clean up islands nobody has visited
        interval-days: 30
        min-age-days: 60
  purge-level: 10             # never purge islands above this level (needs Level)
```

The deleted-island sweep is safe and on by default. The age sweep is off by default because it removes abandoned islands that were never deleted.

**Manual cleanup:**

| Command | What it does |
|---|---|
| `/bsbadmin purge <days>` | Deletes islands in region files nobody has touched for that many days |
| `/bsbadmin purge deleted` | Cleans up deleted islands now instead of waiting for the sweep |
| `/bsbadmin purge unowned` | Marks islands with no owner as deletable |
| `/bsbadmin purge protect` | Stand on an island and run this to protect it from all purges |

Purges skip islands with online players, spawn islands, protected islands, and islands above `purge-level`.

!!! warning "Back up first"
    Purging deletes region files from disk and can't be undone. Back up the world folder before your first purge. Islands that share a region file with an active island stay until that region is clear.

## Multiple islands per player

Players can own more than one island in a game mode if you allow it:

```yaml
island:
  concurrent-islands: 1          # BentoBox config.yml: default for all game modes

world:
  concurrent-islands: 1          # game mode config.yml: 0 = use BentoBox's value
  disallow-team-member-islands: true
```

Or give players `bskyblock.island.number.<number>`. See [Multiple Islands](../ConcurrentIslands.md) for how players create and switch between islands.

## Finding out about an island

| Command | Shows |
|---|---|
| `/island info` | Owner, team, size and location of the island you're on |
| `/bsbadmin info [player]` | Full details: owner, members, range, homes, resets, deaths, and more. With no name, the island you're on |
| `/bsbadmin why <player>` | Logs why a player can or can't do something. See [Admin Tools](AdminTools.md) |

## Troubleshooting

**The server won't start after I changed `distance-between-islands`.**
It can't change once islands exist. Put the old value back.

**A VIP permission for a bigger island or more homes didn't apply.**
Permissions are checked for the island **owner**, when they log in (and at island creation for range). Have the owner log out and in.

**A player has no resets left.**
`/bsbadmin resets reset <player>`.

**A deleted island is still there.**
Its blocks go when the region file is cleaned up, at the next deleted-island sweep (24 hours by default), or run `/bsbadmin purge deleted`. If another active island shares the region file, the blocks stay.

**Disk usage keeps growing.**
Make sure `deleted-sweep` is enabled, and consider `/bsbadmin purge <days>` or the age sweep for abandoned islands.

## See also

- [Player Guide](../Player-Guide.md): the commands your players use
- [Teams & Ranks](Teams.md)
- [Protection, Flags & Ranks](../Island-Protection,-Flags-&-Ranks.md)
- [Starter Islands (Blueprints)](BlueprintsSummary.md)
- [Multiple Islands](../ConcurrentIslands.md)
- [Admin Tools](AdminTools.md)

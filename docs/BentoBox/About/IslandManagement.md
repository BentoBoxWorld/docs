# Island Management

At the heart of every BentoBox game mode is the **island** — a protected area of the world that belongs to a player or a team. BentoBox handles the full lifecycle of islands so you don't have to manage any of it manually.

## Creating an Island

When a player joins a game mode for the first time and runs the main command (e.g. `/island` for BSkyBlock, `/oneblock` for AOneBlock), BentoBox automatically:

1. Finds a free spot in the world for them.
2. Pastes their **starter island** from a Blueprint (a saved island template).
3. Teleports them to their new island's spawn point.
4. Registers the island as theirs in the database.

Players get exactly one island per game mode. If your server runs multiple game modes (e.g. both BSkyBlock and AcidIsland), each player gets a separate island in each world.

## Island Names

Players can give their island a custom name using `/island setname <name>`. Names show up in various places — leaderboards, the Warps addon, and placeholders displayed by other plugins. Admins can restrict what names are allowed via the game mode's `config.yml`.

## Home Locations

Players can set multiple home locations on their island with `/island sethome`. When they use `/island go` or `/island home`, they teleport to their home point. Multiple named homes can be unlocked via permissions:

```
[gamemode].island.home.maxhomes.<number>
```

## Resetting an Island

Players can start fresh by resetting their island with `/island reset`. This **deletes the current island** and creates a brand new one. Admins can:

- Limit how many times a player can reset (set in `config.yml`).
- Grant extra resets via the permission `[gamemode].island.reset.maxresets.<number>`.
- Set resets to unlimited with the value `-1`.

!!! warning
    Island resets are permanent. The old island and everything built on it is deleted. Advise players to back up anything important before resetting.

## Island Deletion (Admin)

Admins can delete a player's island with:
```
/[admin_command] delete <player>
```

This removes the island from the database and queues the area for cleanup. The player will be able to create a new island afterwards.

## Inactive Island Cleanup

If players abandon the server, their islands stay in the world. BentoBox does not automatically delete inactive islands, but the **deletion flag** and external tools can be used to manage this. Many server admins handle this by setting a reset limit and reviewing inactive players periodically.

## What Happens When a Player Leaves a Team

If a player is a member (not owner) and leaves a team or is kicked, they lose access to that island. They can then create their own island, subject to any reset limits. If the player *was* the owner, they must transfer ownership before leaving — they cannot simply walk away from an owned island.

## Multiple Islands (Concurrent Islands)

By default, each player has one island per game mode. BentoBox optionally supports **concurrent islands** — allowing a single player to own more than one island at a time. This is an advanced feature configured in the game mode's `config.yml` and controlled by permissions.

### Config Examples

There are two places where concurrent islands can be configured:

**1. BentoBox `config.yml`** — sets the global default for all game modes:

```yaml
island:
  # The default number of concurrent islands a player may have.
  # This may be overridden by individual game mode config settings.
  concurrent-islands: 1
```

**2. Game mode `config.yml`** (e.g. BSkyBlock) — overrides the global default for that game mode:

```yaml
world:
  # The number of concurrent islands a player can have in the world.
  # A value of 0 will use the BentoBox config.yml default.
  concurrent-islands: 1
  # Disallow players to have other islands if they are in a team.
  disallow-team-member-islands: true
```

For example, to let every player own up to **3** islands in BSkyBlock, set `concurrent-islands: 3` in the BSkyBlock `config.yml`. If you also want team members to be able to create their own islands, set `disallow-team-member-islands: false`.

### Permission

The per-player maximum can be overridden with a permission node:

```
[gamemode].island.number.<number>
```

Replace `[gamemode]` with the game mode prefix and `<number>` with the maximum number of islands allowed. For example:

| Permission | Effect |
|---|---|
| `bskyblock.island.number.5` | Allows the player up to 5 islands in BSkyBlock |
| `acidisland.island.number.3` | Allows the player up to 3 islands in AcidIsland |
| `caveblock.island.number.2` | Allows the player up to 2 islands in CaveBlock |

The permission value overrides the `concurrent-islands` config value for that player. If a player does not have the permission, the config value is used as the default.

!!! tip
    For a full guide — including how players create, navigate, and manage multiple islands — see the [Concurrent Islands](../../BentoBox/ConcurrentIslands.md) page.

## Island Range and Spacing

Islands are placed in a grid. The spacing between island centres is set once in `config.yml` (`distance-between-islands`) and **cannot be changed once the world has been created**. Choose this value before players start joining. A larger value gives more build space between islands; a smaller value makes the world more compact.

The player's **protection range** — the area they actually own and can protect — is always smaller than or equal to half the island distance. It can be expanded by admins or by player permissions up to that maximum.

## Seeing Island Info

Players can check their own island info with `/island info`. Admins can check any island with:
```
/[admin_command] info <player>
```
This shows the island's location, owner, team members, and current protection range.

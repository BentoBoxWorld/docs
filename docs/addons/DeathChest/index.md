# DeathChest

**DeathChest** puts a player's items into a chest when they die instead of dropping them on the ground — and, unlike a general-purpose death chest plugin, it knows where islands are.

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("DeathChest") }}

## Why an island-specific death chest addon

A conventional death chest plugin assumes two things: that the player died somewhere a chest can be placed, and that they can get back to it afterwards. On an island server neither assumption holds.

- **The void.** A player who falls off their island dies in empty space, often below the world floor. There is no block to build a grave on, so a conventional plugin either drops the chest into the void, gives up, or places it at bedrock level where nobody can reach it.
- **Oceans.** On AcidIsland the space around an island is sea. Ground exists, but it is a hundred blocks down and under water — technically a valid spot, practically a lost chest.
- **Other players' islands.** A visitor who dies cannot build there, usually cannot break the chest, and often cannot open it either.
- **The wild.** The space between islands is neither protected nor reachable without flying.

Which is why the usual advice ends up being "just turn on `keepInventory`" — and with that, dying stops mattering at all.

DeathChest solves the placement problem instead, so death can still cost something without costing everything.

## How the chest location is chosen

The addon works through three stages and stops at the first that succeeds.

1. **Where the player died** — but only if they died inside the *protected* part of an island they are a member of, **and** there is reachable ground: a free block with something solid under it, within `chest.search-depth` blocks below them, and not submerged. This is the normal case. You died on your island, your things are where you died.

2. **On their own island** — next to their island home. Void deaths, deaths at sea, deaths in lava, deaths while visiting someone else and deaths in the wild all land here, which is also where the player respawns.

3. **Held by the addon** — if the player has no island at all, the items go into the addon's database and are recovered with `/[player command] deathchest claim 1`.

!!! info "Why 'reachable ground' is the important part"
    Requiring solid ground within reach, rather than any solid ground, is what stops a chest ending up somewhere useless. A player who falls into the void is still inside their island's column, so an unbounded downward search would happily find bedrock and leave the chest there. On an ocean game mode it would find the sea bed. Failing this check is not an error — it is the signal that sends the chest to stage 2, where the player can actually walk to it.

## Installation

1. Put the addon jar into the `plugins/BentoBox/addons` folder
2. Restart the server (to enable the addon and have the `config.yml` file generated)
3. Customize settings in `config.yml` (optional)
4. Run `/bentobox reload` or restart the server to apply new settings

!!! warning "DeathChest does nothing while `keepInventory` is on"
    If the `keepInventory` gamerule keeps a player's inventory, there are no drops to store and the addon steps aside. Turn `keepInventory` off in your game mode worlds if you want death chests to be what saves players' items.

## Commands

!!! tip
    `[player command]` and `[admin command]` differ depending on the game mode you are running.
    The game mode's `config.yml` contains settings that let you change them.
    As an example, on BSkyBlock the default `[player command]` is `island` and the default `[admin command]` is `bsbadmin`.

### deathchest
**Command**: `/[player command] deathchest`
**Aliases**: `deaths`, `grave`
**Description**: Lists your death chests, newest first, with where each one is and how long it has left.
**Permission**: `[gamemode].deathchest`. Default: `true`.

Chests held by the addon rather than placed in the world are shown as held instead of with coordinates.

### deathchest claim {number}
**Command**: `/[player command] deathchest claim {number}`
**Description**: Hands over the items the addon is holding for that chest, plus any stored experience. Items that do not fit in the player's inventory are dropped at their feet.
**Permission**: `[gamemode].deathchest`. Default: `true`.
**Example**: `/[player command] deathchest claim 1`

This is how a player recovers a chest that could not be placed in the world. It also collects any overflow — see [How items are stored](#how-items-are-stored).

### deathchest tp {number}
**Command**: `/[player command] deathchest tp {number}`
**Description**: Teleports the player to that death chest.
**Permission**: `[gamemode].deathchest.teleport`. Default: `true`.
**Example**: `/[player command] deathchest tp 1`

Requires `commands.allow-teleport` to be `true` in `config.yml`. A chest with no block in the world cannot be visited — claim it instead.

### admin deathchest
**Command**: `/[admin command] deathchest`
**Description**: Reports how many death chests are stored on the server.
**Permission**: `[gamemode].admin.deathchest`. Default: `op`.

### admin deathchest {player}
**Command**: `/[admin command] deathchest {player}`
**Aliases**: `deathchests`
**Description**: Lists a player's death chests, showing both where the chest is and where they died. Those two differ whenever the chest was relocated to the island, which makes it easy to see a void or sea death at a glance.
**Permission**: `[gamemode].admin.deathchest`. Default: `op`.
**Example**: `/[admin command] deathchest tastybento`

### admin deathchest purge
**Command**: `/[admin command] deathchest purge`
**Description**: Expires every chest that is already past due, immediately, rather than waiting for the next check.
**Permission**: `[gamemode].admin.deathchest`. Default: `op`.

!!! tip
    `[gamemode]` is a prefix that differs depending on the game mode you are running.
    The prefix is the lowercased name of the game mode, i.e. if you are using BSkyBlock, the prefix is `bskyblock`.
    Similarly, if you are using AcidIsland, the prefix is `acidisland`.

## Permissions

| Permission | Default | Description |
|---|---|---|
| `[gamemode].deathchest` | `true` | Use `/[player command] deathchest` to list chests and claim held items |
| `[gamemode].deathchest.teleport` | `true` | Use `/[player command] deathchest tp {number}` |
| `[gamemode].admin.deathchest` | `op` | Use the admin command |

## How items are stored

The chest block holds the items. A player's inventory is 41 slots including armour and offhand, and a chest is 27, so **overflow is normal rather than rare**.

Anything that does not fit is kept by the addon and moved into the chest automatically each time the player closes it. So a player empties the chest, closes it, and the next items appear — until nothing is left. Once the chest and the addon's store are both empty, the chest block disappears along with its record.

If the chest block goes away for a reason the addon did not cause — a world edit, a rollback, a manual `/setblock` — the record survives and turns into a held chest that can be recovered with `deathchest claim`.

## Protection

Only the owner can open or break their own death chest. Anyone else is refused and told whose chest it is.

- `chest.team-access` extends that to island team members, but only when the chest sits on an island that both the owner and the other player belong to.
- `chest.protect-from-explosions` keeps death chests out of creeper, TNT and bed explosion block lists.
- Records are deleted when an island is reset or deleted, because the blocks are about to be wiped along with it.

!!! warning "Hoppers are not blocked"
    A hopper underneath a death chest will drain it. The chest is on the owner's own island, so this is self-inflicted rather than griefing, but it is worth knowing if your players build sorting systems near their island home. Tracked as [issue #5](https://github.com/BentoBoxWorld/DeathChest/issues/5).

## Configuration

The `config.yml` file contains the settings below. Values shown are the defaults.

### Disable game modes
DeathChest operates in all game mode worlds on the BentoBox server by default.
You can disable a game mode by writing its name on a new line that starts with `-`.

Example to disable BSkyBlock:

```yml
disabled-gamemodes:
  - BSkyBlock
```

Default value:

```yml
disabled-gamemodes: []
```

### Chest material
The block used for the death chest.

`CHEST` is the classic look. `BARREL` is a good choice for cramped islands because it can be opened even with a block directly above it.

The material must be a container. If it is not — or if the name is not a real material — the addon logs an error and falls back to holding the items for the player.

```yml
chest:
  material: CHEST
```

### Place at death location
Place the chest where the player died, if that is a spot they can reach and build in.

Set to `false` to always send chests to the island home instead.

Deaths in the void, outside a build-allowed area, or in an unreachable spot fall back to the island home regardless of this setting.

```yml
chest:
  place-at-death-location: true
```

### Search radius
How far to look **sideways**, in blocks, for a free spot to put the chest. Range 1 to 32.

```yml
chest:
  search-radius: 8
```

### Search depth
How far to look **downwards**, in blocks, for ground to stand the chest on. Range 1 to 64.

This is what stops a chest ending up far below the player — on the sea bed of an ocean world, or buried in terrain. If no ground is found within this distance the chest goes to the player's island instead, which is usually what you want.

Raising it lets chests follow a long fall down to the ground; lowering it sends more deaths to the island.

```yml
chest:
  search-depth: 16
```

### Expiry minutes
How many minutes a death chest lasts before it expires. `0` means never.

```yml
chest:
  expiry-minutes: 60
```

### Expiry action
What happens when a death chest expires.

- `DROP` — break the chest and let the items drop on the ground. They will despawn like any other dropped item.
- `DELETE` — remove the chest and its contents.

```yml
chest:
  expiry-action: DROP
```

### Expiry check seconds
How often, in seconds, to check for expired chests. Minimum 5.

```yml
chest:
  expiry-check-seconds: 60
```

### Max per player
Maximum number of death chests a player may have at once. When exceeded, the player's oldest chest is expired early, following the `expiry-action` above. `0` means unlimited.

This stops a player who keeps dying from littering their island with chests.

```yml
chest:
  max-per-player: 3
```

### Team access
Let island team members open each other's death chests.

Set to `false` if only the owner should ever open their own chest.

```yml
chest:
  team-access: true
```

### Protect from explosions
Stop death chests being blown up by creepers, TNT and so on.

```yml
chest:
  protect-from-explosions: true
```

### Store experience
Store the player's dropped experience with the chest and give it back when it is opened.

```yml
experience:
  store: true
```

### Experience percent
Percentage of the player's dropped experience to store, 0 to 100. The remainder is lost, which keeps some cost in dying.

Only applies when `experience.store` is `true`.

```yml
experience:
  percent: 100
```

### Notify on death
Tell the player where their death chest is when they die, and how long it will last.

The message names the world using the game mode's friendly name, adding `Nether` or `The End` when the death was not in the overworld.

```yml
notify:
  on-death: true
```

### Allow teleport
Allow `/[player command] deathchest tp {number}` to teleport the player to their chest.

Players still need the `[gamemode].deathchest.teleport` permission.

```yml
commands:
  allow-teleport: true
```

## Translations

{{ translations("DeathChest") }}

## Source
Want to contribute? See this documentation's source code at [GitHub](https://github.com/BentoBoxWorld/docs/blob/master/docs/addons/DeathChest/).

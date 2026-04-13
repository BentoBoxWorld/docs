# InvSwitcher

**InvSwitcher** separates player inventories and other aspects between the various worlds.

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("InvSwitcher") }}

The following are switched per-world:

* Inventory & armor
* Advancements
* Food level
* Experience
* Health
* Game mode (creative, survival, etc.)

## How to use

1. Place the addon jar in the addons folder of the BentoBox plugin
2. Restart the server
3. Done!

## Config.yml

InvSwitcher has a `config.yml` with two main sections.

### Worlds

Lists the gamemode worlds that InvSwitcher operates in. Nether and End worlds are included automatically.

```yml
worlds:
- bskyblock_world
- acidisland_world
- oneblock_world
# ... etc.
```

### Options

Controls which player aspects are switched per-world and, optionally, per-island.

```yml
options:
  inventory: true
  health: true
  food: true
  advancements: true
  gamemode: true       # game mode (Survival/Creative/etc.)
  experience: true
  ender-chest: true
  statistics: true
  # Per-island inventory switching (added in 1.17.0)
  # The world-level option must also be true for the island option to take effect.
  islands:
    active: true       # Enable per-island switching overall
    inventory: true    # Give players a different inventory on each island they own
    health: false
    food: false
    advancements: false
    gamemode: false
    experience: false
    ender-chest: true
    statistics: false
```

Set `islands.active: true` to allow players who own more than one island to maintain separate inventories (and other aspects) per island, not just per gamemode world.

## Commands

There are no commands.

## What it does
This addon will give players a separate inventory, health, food level, advancements and experience for each gamemode installed and their corresponding worlds. It enables players to play each gamemode independently of each other.

## An example
**BSkyBlock**'s Inventory, Health, Food level, Advancements and Experience are shared only between its corresponding worlds:
- BSkyBlock_world
- BSkyBlock_world_nether
- BSkyBlock_world_the_end

**Please note:**
- It is not limited to just BentoBox worlds. It applies to all worlds on the server (right now).

## Changelog

??? note "What's new in v1.17.0"
    **Released:** 2026-03-31

    - **Per-island inventory switching.** Players who own more than one island can now maintain separate inventories (and optionally health, food, experience, ender-chest, statistics) per island within the same gamemode. Enable with `options.islands.active: true` and configure each sub-option. The world-level option must also be `true` for its island counterpart to take effect.
    - ⚙️ New `options.islands` section in `config.yml`.
    - Bug fix: inventory was lost when returning to the original island.

    [Release v1.17.0](https://github.com/BentoBoxWorld/InvSwitcher/releases/tag/1.17.0)

## Translations

{{ translations("InvSwitcher") }}

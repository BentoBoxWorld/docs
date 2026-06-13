# Limits

**Limits** allows you to limit island blocks and entities in GameModes like BSkyBlock and AcidIsland.

This addon was made to help limit lag-inducing entities or blocks, e.g., hoppers. It can be used to limit regular blocks and entities but not all can be limited.

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("Limits") }}

## Installation

1. Place the Limits addon jar in the addons folder of the BentoBox plugin
2. Restart the server
3. The addon will create a data folder and inside the folder will be a config.yml
4. Edit the config.yml how you want.
5. Restart the server if you make a change

## Commands
There is a user command and an admin command called "limits". Admins can check the limits of a specific island owner. Both show a GUI panel with the limits and the current count.

## Setup - Config.yml

The config.yml has the following sections:

* blocklimits
* blocklimits-nether
* blocklimits-end
* worlds
* entitylimits
* entitylimits-nether
* entitylimits-end

!!! info "Per-dimension limits (1.28.2+)"
    As of **1.28.2**, block counts, entity counts, limits, and offsets are tracked **independently for the overworld, nether, and end**. A single limit defined in `blocklimits` or `entitylimits` applies separately to each dimension — e.g. `HOPPER: 10` allows 10 hoppers in the overworld, 10 in the nether, and 10 in the end (30 total across the island). Use the optional `-nether` / `-end` sections to override a single dimension.

    On first load after upgrading, your existing single-dimension data is migrated automatically into the **overworld** slot. The on-disk format changes, so take a backup before upgrading and note that downgrading afterwards is not supported.

### blocklimits

This section lists the maximum number of blocks allowed for each block material. Do not use non-block materials because they will not work. The limits apply independently in every dimension (overworld, nether, end).

### blocklimits-nether / blocklimits-end

Optional sections that override the `blocklimits` defaults for the nether or the end respectively. They are commented out in the default config; uncomment and add entries to set dimension-specific block limits.

### worlds

This section lists block limits for specific worlds. You must name the world specifically, e.g. AcidIsland_world and then list the materials and the limit. World-named limits override the dimension-default limit above for that specific world.

### entitylimits

This section lists the default entity limits within a player's island space (protected area and to island limit). A limit of 5 will allow up to 5 entities. Affects all types of creature spawning. Also includes entities like MINECARTS. As of **1.28.2**, entity limits apply independently per dimension, so the nether and end are now counted and limited correctly (this fixes the long-standing bug where nether/end counts reset to zero on chunk unload).

### entitylimits-nether / entitylimits-end

Optional sections that override the `entitylimits` defaults for the nether or the end respectively. They are commented out in the default config; uncomment and add entries to set dimension-specific entity limits.

Note: Only the first 49 limited blocks and entities are shown in the limits GUI.

### entitygrouplimits

!!! note "Experimental feature"
    The following feature is only available in development builds, which you may find on ci.codemc.io.

```yaml
entitygrouplimits:
  friendly:
    limit: 2
    entities:
      - COW
      - SHEEP
  monsters:
    limit: 4
    entities:
      - ZOMBIE
      - CREEPER
```

## Permissions

Island owners can have exclusive permissions that override the default or world settings. Two formats are supported:

1. `GAME-MODE-NAME.island.limit.MATERIAL.LIMIT` — applied to every dimension.

    example: `bskyblock.island.limit.hopper.10`

2. `GAME-MODE-NAME.island.limit.ENV.MATERIAL.LIMIT` — applied to one dimension only, where `ENV` is one of `overworld`, `nether`, or `end` (1.28.2+).

    example: `bskyblock.island.limit.nether.hopper.5`

Permissions activate when the player logs in.

Usage permissions are (put the gamemode name, e.g. acidisland at the front):

```
  GAMEMODE_NAME.limits.player.limits:
    description: Player can use limits command
    default: true
  GAMEMODE_NAME.mod.bypass:
    description: Player can bypass limits
    default: op
  GAMEMODE_NAME.limits.admin.limits:
    description: Player can use admin limits command
    default: op
```

Full permissions are listed [here](Permissions).

## Placeholders

{{ placeholders_source(source="Limits") }}


## Translations

{{ translations("Limits") }}

## Items that cannot be limited
Some items cannot be limited (right now). The reasons are usually because there are too many ways to remove the item without it being tracked. If you are a programmer and can work out how to fix these, then please submit a PR!

* Primed TNT
* Evoker Fangs
* Llama Spit
* Dragon Fireball
* Area Effect Cloud
* Ender signal
* Small fireball
* Fireball
* Thrown Exp Bottle
* Shulker Bullet
* Wither Skull
* Tridents
* Arrows
* Spectral Arrows
* Snowballs
* Eggs
* Leashes
* Ender crystals
* Ender pearls
* Ender dragon
* Item frames
* Paintings


## Changelog

??? warning "What's new in v1.28.0 — Java 21 required"
    **Released:** 2026-04-01

    - **Shulker duplication farms properly limited on Paper.** Uses Paper's `ShulkerDuplicateEvent` to enforce limits before duplication occurs, fixing a bypass where shulkers teleported outside the island before the limit check.
    - **Copper chest limits can no longer be bypassed.** All copper chest variants (oxidized, waxed, scraped, golem-created) are now normalized to a single tracked material. Block state transitions are properly counted.
    - **Invalid config entries handled gracefully.** Malformed namespaced keys, non-block materials, and uncountable materials (lava, water, air) in `blocklimits` config now produce clear warning messages instead of NPEs.
    - 🔺 **Java 21 is now required** (previously Java 17). Ensure your server runs Java 21 before upgrading.
    - Bumped Spigot target to 1.21.11.

    [Release v1.28.0](https://github.com/BentoBoxWorld/Limits/releases/tag/1.28.0)

??? note "What's new in v1.28.1"
    **Released:** 2026-04-07

    Hotfix for two regressions in 1.28.0:

    - **Existing databases load again.** In 1.28.0 the `IslandBlockCount` map fields changed from `Map<Material, Integer>` to `Map<NamespacedKey, Integer>`, breaking reads of pre-1.28.0 JSON files. A backwards-compatible Gson `TypeAdapter` now reads legacy enum names, namespaced strings, and the complex array form. **No manual migration required** — old files load as-is.
    - **Block names in the limits GUI are readable again.** Items were showing as `Minecraft:hopper` due to incorrect key formatting.

    [Release v1.28.1](https://github.com/BentoBoxWorld/Limits/releases/tag/1.28.1)

??? warning "What's new in v1.28.2 — Per-dimension limits (data migration)"
    **Released:** 2026-06-13

    - 🔺⚙️ **Per-dimension limits.** Block counts, entity counts, limits, and offsets are now tracked independently for the overworld, nether, and end, fixing the long-standing bug where nether/end counts reset to zero on chunk unload ([#43](https://github.com/BentoBoxWorld/Limits/issues/43)). A single `blocklimits`/`entitylimits` value now applies to each dimension separately, with new optional `blocklimits-nether`, `blocklimits-end`, `entitylimits-nether`, and `entitylimits-end` override sections.
    - 🔺 **Data migration.** Existing single-dimension data is migrated into the **overworld** slot on first load. The on-disk format changes, so take a backup before upgrading; downgrading afterwards is not supported.
    - 🔺 **Per-dimension permissions.** A new 6-segment format, `<gamemode>.island.limit.<overworld|nether|end>.<KEY>.<NUMBER>`, scopes a limit to a single dimension. The existing 5-segment format still applies to all dimensions.
    - 🐛 Accurate counting fixes: double-counted beds/doors ([#86](https://github.com/BentoBoxWorld/Limits/issues/86)), golem/snowman block removal anchored on the pumpkin ([#127](https://github.com/BentoBoxWorld/Limits/issues/127)), three entity-counting bugs, spawn eggs no longer consumed at the limit ([#134](https://github.com/BentoBoxWorld/Limits/issues/134)), and count leaks during recount.
    - 🩹 Resolves a `NoSuchFieldError` crash on Minecraft 1.21.8 and earlier caused by referencing 1.21.9 copper blocks; these are now resolved by name.
    - 🔡 All bundled locale files converted from legacy `&` colour codes to MiniMessage, and missing keys synced across all 21 languages. Review any customised locale strings against the new files.

    Compatibility: BentoBox API 2.7.1 · Minecraft 1.21.5 – 26.1.2 · Java 21.

    [Release v1.28.2](https://github.com/BentoBoxWorld/Limits/releases/tag/1.28.2)

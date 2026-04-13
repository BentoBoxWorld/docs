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
* worlds
* entitylimits

### blocklimits

This section lists the maximum number of blocks allowed for each block material. Do not use non-block materials because they will not work. The limits apply to all game worlds.

### worlds

This section lists block limits for specific worlds. You must name the world specifically, e.g. AcidIsland_world and then list the materials and the limit.

### entitylimits

This section lists the default entity limits within a player's island space (protected area and to island limit). A limit of 5 will allow up to 5 entities in over world. Affects all types of creature spawning. Also includes entities like MINECARTS. Note that entity limits are no longer supported in the Nether and End because limits require chunks to be loaded to count entities and it causes too much lag.

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

Island owners can have exclusive permissions that override the default or world settings. The format is:

Format is `GAME-MODE-NAME.island.limit.MATERIAL.LIMIT`

example: `bskyblock.island.limit.hopper.10`

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

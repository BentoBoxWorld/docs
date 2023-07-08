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
    The following feature is only available in development builds, which you may find on ci.codemc.org.

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

{{ translations(2974, ["cs", "de", "hu", "ja", "lv", "pl", "tr", "zh-CN", "fr", "id", "ro", "es", "vi"]) }}

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

# Boxed

Players survive in a box that can only be expanded by accomplishing advancements!

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("Boxed") }}

## BentoBox Requirements

* Always used the latest BentoBox version (Snapshots can be downloaded here: [https://ci.bentobox.world](https://ci.bentobox.world))
* InvSwitcher - keeps advancements, inventory, etc. separate between worlds on a server.
* Border - shows the box

## How to install

### Quick Start

1. Place Boxed addon into the BentoBox addons folder along with InvSwitcher and Border (use the latest versions!).
2. Restart the server - new worlds will be created. *This will take a long time first time through*
3. Login
4. Type `/boxed` to start.
5. (Optional) Turn off advancement announcements `/gamerule announceAdvancements false` otherwise there is a lot of spam from the server when players get advancements.

* You will start by a tree. The is a chest with some handy items in it. (This is the island blueprint)
* The only area you can operate on is your box that shows as a border.
* To make your box bigger, complete advancements.
* Check your progress with the Advancements screen, (L-key).
* Monsters do not spawn by default outside your box, but your box becomes bigger, and it only takes one block to spawn a mob!
* The box owner can move the box using enderpearls thrown from within the box. Beware! It's a one-way trip. (Optional setting in config.yml)
* The box settings have an option to allow box moving by other ranks (look for the Composter box icon)

## Custom Advancements

[Download the official Boxed DataPack](https://github.com/BentoBoxWorld/BoxedDataPack) for custom advancements.
Or you can do it yourself. See the [tutorial video for more information](https://youtu.be/zNzQvIbweQs)

## Using Regionerator

*Note: This plugin is designed to delete unused regions of you world! Make sure you take backups if you use it! Use at your own risk!*

[Regionerator](https://github.com/Jikoo/Regionerator) is a plugin that gradually deletes unused chunks to keep world sizes low. It is not written by the BentoBox team, but it supports BentoBox and respects box boundaries. It can be used to delete box chunks so that they can be regenerated. As Boxed uses seed worlds to copy from, these can appear to be unused by Regionerator and deleted, which means that startup becomes very slow. To avoid this, set the seed worlds as exempt from its deletions by having these in the world section of the Regionarator config file:

```
# Worlds the plugin is able to delete regions in
worlds:
  # "default" applies to all worlds not specified.
  boxed_world/seed_base:
    days-till-flag-expires: -1
  boxed_world/seed:
    days-till-flag-expires: -1
  default:
    # Flags older than x days can be ignored and the region deleted.
    # Set to -1 to disable Regionerator in a world.
    # To disable flagging, set this to 0.
    # days-till-flag-expires must be greater than 0 to be used with delete-new-unvisited-chunks
    days-till-flag-expires: 0
```

To get the most out of Regionarator, change the BentoBox config.yml file to *not* delete chunks when an island is removed. This will then leave the deletion up to it and it should clean up the chunks if the unused area is big enough. The config is to set `keep-previous-island-on-reset: true`:

```
deletion:
    # Toggles whether islands, when players are resetting them, should be kept in the world or deleted.
    # * If set to 'true', whenever a player resets his island, his previous island will become unowned and won't be deleted from the world.
    #   You can, however, still delete those unowned islands through purging.
    #   On bigger servers, this can lead to an increasing world size.
    #   Yet, this allows admins to retrieve a player's old island in case of an improper use of the reset command.
    #   Admins can indeed re-add the player to his old island by registering him to it.
    # * If set to 'false', whenever a player resets his island, his previous island will be deleted from the world.
    #   This is the default behaviour.
    # Added since 1.13.0.
    keep-previous-island-on-reset: true
```


## Advanced Config

### config.yml
The config is very similar to BSkyBlock, AcidIsland, etc.

Each player will have a land of their own to explore up to the limit of the island distance value. The default is 400, so the land will be 800 x 800 blocks. The land is semi-random, but each player will get roughly the same layout (see the biomes config). Structures such as villages, broken nether gates, shipwrecks, etc. are random and so some players may get them, others not. In a future version, switching off structures will be a config option. Strongholds are switched off and do not exist. Each player's land is surrounded by seas of different temperatures. If the border is not solid, then players can theoretically explore other lands.

*World Seed*
The world seed is what it is used to generate the lands. I recommend keeping this value. If you change it the land may be very different.

### Blueprint

There is one blueprint "island" that is used to generate the tree, chest and blocks below down to y = 5. The default height of the surface is about y = 65, so the blueprint has to be about 60 blocks tall. If you make any good blueprints, please share them!

### advancements.yml
This file contains all the advancements and how much your box should grow if you get one. The file can contain custom advancements if you have them.

There are two settings at the top - the first `default-root-increase` you probably don't need to change. This sets the score of any root advancement to 0. In other words, players will not get box expansion just for seeing the new advancement tab.

The second setting `unknown-advancement-increase` gives any unknown advancements, i.e., ones not listed in this file, a default value. This is the default value used should you add custom advancements via a data pack and it frees you up from having to list every new advancement in this file.

Example:

```
# Lists how many blocks the box will increase when advancement occurs
settings:
  default-root-increase: 0
  unknown-advancement-increase: 1
advancements:
  'minecraft:adventure/adventuring_time': 1
  'minecraft:adventure/arbalistic': 1
  'minecraft:adventure/bullseye': 1
...
```
  
### biomes.yml
The player's land has biomes and they are defined here. It's not possible to define where the biomes are right now, only what affect they have on the terrain.

* height: the default height is 8. Lower numbers will produce lower land, higher higher land.
* scale: this is how smooth the land will be. Smaller numbers are more jagged, larger numbers are flatter.

Setting ocean biomes to higher height numbers will result in the ocean floor being above the sea level and creating land.

A lot of these numbers are rough guesses right now and if you come up with better values, please share them!


## Permissions

Permissions can be found [here](Permissions).

## Commands

Commands can be found [here](Commands).

## Placeholders

Placeholders can be found [here](Placeholders).

## Translations

{{ translations(2953, ["cs", "es", "fr", "id", "it", "ja", "ko", "lv", "pl", "pt", "zh-CN", "zh-TW", "hr", "de", "hu", "ro", "ru", "tr", "vi"]) }}

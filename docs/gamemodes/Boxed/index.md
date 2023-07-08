# Boxed

Players survive in a box that can only be expanded by accomplishing advancements!

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("Boxed") }}

## BentoBox Requirements

* Requires BentoBox 1.16.0 or later (Snapshots can be downloaded here: [https://ci.bentobox.world](https://ci.bentobox.world))
* InvSwitcher - keeps advancements, inventory, etc. separate between worlds on a server.
* Border - shows the box

## Required Plugins

* Requires WorldGeneratorAPI plugin. [Download the correct one for your server here.](https://github.com/rutgerkok/WorldGeneratorApi/releases)
* Border requires WorldBorderAPI by default. [Download it here.](https://github.com/yannicklamprecht/WorldBorderAPI/releases)

## How to install

### Quick Start

1. Place Boxed addon into the BentoBox addons folder along with InvSwitcher and Border (use the latest versions!).
2. Place the WorldGeneratorAPI and WorldBorderAPI plugins into your plugins folder.
3. Make sure you are using BentoBox 1.16.0-SNAPSHOT or later.
4. Restart the server - new worlds will be created. There may be a delay.
5. Login
6. Type `/boxed` to start.
7. Turn off advancement announcements `/gamerule announceAdvancements false` otherwise there is a lot of spam from the server when players get advancements.

* You will start by a tree. The is a chest with some handy items in it. (This is the island blueprint)
* The only area you can operate on is your box that shows as a border.
* To make your box bigger, complete advancements.
* Check your progress with the Advancements screen, (L-key).
* Monsters do not spawn by default outside your box, but your box becomes bigger, and it only takes one block to spawn a mob!
* The box owner can move the box using enderpearls thrown from within the box. Beware! It's a one-way trip.
* The island settings have an option to allow box moving by other ranks (look for the Composter box icon)

## Custom Advancements

You can add custom advancements via data packs. See the [tutorial video for more information](https://youtu.be/zNzQvIbweQs)


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

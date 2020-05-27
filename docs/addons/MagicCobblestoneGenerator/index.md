# MagicCobblestoneGenerator

This is a high-level set of instructions on how to use the addon.

# Installation
Copy the JAR file into the addons folder of BentoBox and restart the server. You will find a new folder created and a config file.

## Config.yml walkthrough
The latest config file is [here](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/blob/master/src/main/resources/config.yml)

Sections:

### Disabled Game Mode Addons
By default, the addon will work in all game modes, e.g., BSkyBlock, AcidIsland, SkyGrid, etc. If you do not want it to work in a game mode then list the name of the game mode in this section.

### Offline ore gen
Sometimes players set up machines to make ore when they are offline. To dissuade players from doing this you can turn off magic ore generation if all the players of an island are offline with this setting.

### Tiers
Magic Ore Gen uses island levels (from the Level addon) plugin to determine what ore will be generated. If there is no Level addon installed then only the default setting will be used.
Tiers are not cumulative so you must fully define all the blocks you want generated for each tier level.

Each tier must contain:
* min-level: island level (integer > -1).  -1 will mean that this level will be the only level that will be applied. First level will be always selected.
* name: String that will be displayed in commands
* blocks: List of Minecraft Materials and chance of getting it.

Note: You can not use decimals for chances and the total chances for your tier do not have to add to 100. Therefore, you can do the same thing as decimals but with larger numbers.

# FAQ
1. Can you add feature X?

Please add it to the list [here](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/issues).

2. I can code Java and I would like to be a maintainer of this addon!

Great! Start by forking the repo and then submit some PR's. If your PR's start to get accepted and your code is good we might ask you to become the maintainer. We are a meritocracy!

3. Can tiers be determined by permission?

No, not yet.

## Translations

{{ translations(2972, ["fr", "lv", "es"]) }}

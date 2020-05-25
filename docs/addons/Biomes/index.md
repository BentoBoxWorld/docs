# Biomes

Biomes addon for SkyBlock, SkyGrid, CaveBlock and AcidIsland. It allows to change biome on Island.

## Where to find

Currently Biomes Addon is in **Beta stage**, so it may or may not contain bugs... a lot of bugs. Also it means, that some features are not working or implemented. 
Latest official **Beta Release is 1.6.0.1**, and you can download it from [Release tab](https://github.com/BentoBoxWorld/Biomes/releases)

Or you can try **nightly builds** where you can check and test new features that will be implemented in next release from [Jenkins Server](https://ci.codemc.org/job/BentoBoxWorld/job/Biomes/lastStableBuild/).

If you like this addon but something is missing or is not working as you want, you can always submit an [Issue request](https://github.com/BentoBoxWorld/Biomes/issues) or get a support in Discord [BentoBox ![icon](https://avatars2.githubusercontent.com/u/41555324?s=15&v=4)](https://discord.gg/JgWKvR)

## Translations

As most of BentoBox projects, Biomes Addon is translatable in any language. Everyone can contribute, and translate some parts of the addon in their language via [GitLocalize](https://gitlocalize.com/repo/2894).
If your language is not in the list, please contact to developers via Discord and it will be added there.

Translation status is [here](Translate-Biomes).

## How to use

1. Place the addon jar in the addons folder of the BentoBox plugin
2. Restart the server
3. The addon will create a data folder and inside the folder will be a *config.yml* and an example *biomes.yml*
4. Edit the config.yml and *biomes.yml* files how you want. The *biomes.yml* is for importing only.
5. Restart the server

## Config.yml

After addon is successful installed, it will create config.yml file. Every option in this file comes with comments about them. Please check file for more information.
Most of options are also editable admin via commands.

## Biomes.yml

This file contains all necessary information about default biomes. 
If you change values in biomes.yml, then to apply them, you must run **/bsb biomes import** or **/acid biomes import**.

If you want to force an overwrite of biomes via an import, add the **overwrite** option to the end of the import command.
Note that you must import biomes into both BSkyBlock and AcidIsland separately.

## Commands

!!! tip
    `[user_command]` and `[admin_command]` are prefixes that differs depending on the gamemode you are running. Gamemodes config section contains option to modify these values.
    F.e. in BSkyBlock default `[user_command]` is `island` and default `[admin_command]` is `bsbadmin`. 

### User commands

* `/[user_command] biomes`: This method opens GUI that allows to change biome on User island.
* `/[user_command] biomes help`: Show help for all the commands
* `/[user_command] biomes info <biome>`: This command returns information about given biome, like cost and necessary level.
* `/[user_command] biomes set <biome> [<type>] [<size>]`: This command allows to change biome on island without opening GUI. If prarameters < type> and < size> are not provided, command uses default values from addon config.

!!! info
    - `<biome>` may not be equal Minecraft biome name. It is defined by admin.
    - `<type>` is one of 3 biome chaning types. It offers to change biome on whole island (`ISLAND`), in current chunk(-s) (`CHUNK`) or by distance around player (`RANGE`).
    - Currently biome is changed in whole height.

### Admin commands

* `/[admin_command] biomes`: To open Admin GUI. 
* `/[admin_command] biomes help` : Show help for all the commands
* `/[admin_command] biomes import [overwrite]`: import biomes from biomes.yml
* `/[admin_command] biomes add <biome>`: add a new biome what can be edited via GUI or `biomes edit` command. Biome will not be deployed. To do it, you should enable it in GUI or via `biomes edit <biome> deployed true` command.
* `/[admin_command] biomes set <player> <biome> [<type>] [<size>]`: This command works the same as user biome set command, but it is necessary to provide also player, which island biome will be updated.
* `/[admin_command] biomes edit <biome> <property> <new_value>`: This command allows to edit provided biome property to new value. 
* `/[admin_command] biomes settings <property> <new_value>`: This command allows to edit current addon settings via command. 

## Permissions

!!! tip
    `[gamemode]` is a prefix that differs depending on the gamemode you are running.
    The prefix is the lowercased name of the gamemode, i.e. if you are using BSkyBlock, the prefix is `bskyblock`.
    Similarly, if you are using AcidIsland, the prefix is `acidisland`.

??? question "Something is missing?"
    You can find the comprehensive list of permissions in the [addon.yml](https://github.com/BentoBoxWorld/Biomes/blob/develop/src/main/resources/addon.yml) file of this addon.

### User permissions
- `[gamemode].biomes` (default: `true`): player can use biomes command that opens GUI.
- `[gamemode].biomes.info` (default: `true`): player can use biomes info command.
- `[gamemode].biomes.set` (default: `true`): player can use biomes set command.

### Admin permissions
- `[gamemode].admin.biomes` (default: `op`): player can use admin biomes command that opens GUI.
- `[gamemode].admin.biomes.add` (default: `op`): player can use admin biomes add command that adds new biome.
- `[gamemode].admin.biomes.edit` (default: `op`): player can use admin biomes edit command that edits existing biomes parameters.
- `[gamemode].admin.biomes.set` (default: `op`): player can use admin biomes set command that allows to change other player biomes.
- `[gamemode].admin.biomes.import` (default: `op`): player can use admin biomes import command allows to import biomes in world.
- `[gamemode].admin.biomes.settings` (default: `op`): player can use admin biomes settings command that allows to change addon settings.

## API Addon Request Handlers

The addon request handlers are [here](Addon-Request-Handlers).

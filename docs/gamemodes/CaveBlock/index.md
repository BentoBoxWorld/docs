# CaveBlock

**CaveBlock** lets ~~dwarves~~ players survive underground. Mine, craft, and dig a hole (*diggy diggy hole*)!

Created and maintained by [BONNe](https://github.com/BONNe).

{{ addon_description("CaveBlock") }}

## Installation

0. Install BentoBox and run it on the server at least once to create its data folders.
1. Place this jar in the addons folder of the BentoBox plugin.
2. Restart the server.
3. The addon will create worlds and a data folder and inside the folder will be a config.yml.
4. Stop the server .
5. Edit the config.yml how you want.
6. Delete any worlds that were created by default if you made changes that would affect them.
7. Restart the server.

## Configuration

The main `config.yml` file contains basic information about game-mode addon setup.

### config.yml

After addon is successfully installed, it will create config.yml file. Every option in this file comes with comments about them. Please check file for more information.

You can find the latest config file: [config.yml](https://github.com/BentoBoxWorld/CaveBlock/blob/develop/src/main/resources/config.yml)

=== "world.world-depth"
    !!! summary "Description"
        The depth of world indicates till which height blocks will be generated in world. Setting it to -64 will create just a basic void world.

        Allows to create some fresh air above your cave.

=== "world.generation-tries"
    !!! summary "Description"
        This allows to specify how many tries will it take to change a main dimension block with an ore block.

=== "world.use-new-material-generator"
    !!! summary "Description"
        Improve material generator generates vanillish ore bolbs, granite, diorite and tuff patches, as well as uses some deepslate.

        However, it will disable any customization you are adding via dimension block configs.

=== "world.normal.roof"
    !!! summary "Description"
        Allows toggling if overworld top block should be bedrock block. Otherwise, it will be made of stone.

=== "world.normal.natural-surface"
    !!! summary "Description"
        Option allows toggling if world generator should generate natural(-ish) looking surface with dirt and grass blocks. 
        Currently, natural(-ish) is just dirt and grass block layers.

        This option disables `world.normal.roof` option.

=== "world.normal.natural-caves"
    !!! summary "Description"
        Option allows toggling if world generator should generate natural caves like in vanilla world.
        Caves will be generated with all blocks and biomes.

=== "world.normal.floor"
    !!! summary "Description"
        Allows toggling if overworld bottom block should be bedrock block. Otherwise, it will be made of stone.

=== "world.normal.natural-bedrock"
    !!! summary "Description"
        Allows toggling if overworld bedrock should be generated like in vanilla world with 4 block height.

=== "world.normal.main-block"
    !!! summary "Description"
        Allows setting main block that will be used for overworld generation. Setting it to AIR will create void world.

=== "world.normal.blocks"
    !!! summary "Description"
        Blocks that will occasionally replace main block by random chance.
        Blocks will replace only main-block and will try to create packs that
        are set in their strings. Chance of spawning also is required.
        
        For materials first string must be MATERIAL, for entity: ENTITY.
        
        Entities spawned via generator are not protected from despawing.
        Working only with 2 high mobs currently.

    !!! example "Example"
        ```yaml
            blocks:
                - MATERIAL:DIAMOND_ORE:100:5 
        ```        
        Means there is 100% chace of spawing diamonds where max amount in pack are 5 per each subchunk!

=== "world.nether.roof"
    !!! summary "Description"
        Allows toggling if the nether top block should be bedrock block. Otherwise, it will be made of netherrack.

=== "world.nether.floor"
    !!! summary "Description"
        Allows toggling if nether bottom block should be bedrock block. Otherwise, it will be made of netherrack.

=== "world.nether.main-block"
    !!! summary "Description"
        Allows setting main block that will be used for the nether world generation. Setting it to AIR will create void world.

=== "world.nether.blocks"
    !!! summary "Description"
        Blocks that will occasionally replace main block by random chance.
        Blocks will replace only main-block and will try to create packs that
        are set in their strings. Chance of spawning also is required.
        
        For materials first string must be MATERIAL, for entity: ENTITY.
        
        Entities spawned via generator are not protected from despawing.
        Working only with 2 high mobs currently.

    !!! example "Example"
        ```yaml
            blocks:
                - MATERIAL:DIAMOND_ORE:100:5 
        ```        
        Means there is 100% chace of spawing diamonds where max amount in pack are 5 per each subchunk!

=== "world.end.roof"
    !!! summary "Description"
        Allows toggling if the end top block should be bedrock block. Otherwise, it will be made of endstone.

=== "world.end.floor"
    !!! summary "Description"
        Allows toggling if the end bottom block should be bedrock block. Otherwise, it will be made of endstone.

=== "world.end.main-block"
    !!! summary "Description"
        Allows setting main block that will be used for the end world generation. Setting it to AIR will create void world.

=== "world.end.blocks"
    !!! summary "Description"
        Blocks that will occasionally replace main block by random chance.
        Blocks will replace only main-block and will try to create packs that
        are set in their strings. Chance of spawning also is required.
        
        For materials first string must be MATERIAL, for entity: ENTITY.
        
        Entities spawned via generator are not protected from despawing.
        Working only with 2 high mobs currently.

    !!! example "Example"
        ```yaml
            blocks:
                - MATERIAL:DIAMOND_ORE:100:5 
        ```        
        Means there is 100% chace of spawing diamonds where max amount in pack are 5 per each subchunk!

## Commands

!!! tip
    `[player_command]` and `[admin_command]` are commands that differ depending on the gamemode you are running.
    
    The Gamemodes' `config.yml` file contains options that allows you to modify these values.
    
    As an example, on CaveBlock, the default `[player_command]` is `cave`, and the default `[admin_command]` is `cba`.
    
    Be aware, that this addon allows changing player commands aliases in addon `config.yml` file.


By default, BentoBox GameMode addons comes with the default sub-command set, however, each addon may introduce even more sub commands.

[Complete CaveBlock Command List](Commands)

## Permissions

!!! tip
    `[gamemode]` prefix in every place for CaveBlock addon must be replaced with `caveblock`.

By default, BentoBox GameMode addons comes with the default sub-permission set, however, each addon may introduce even more sub-permissions.

[Complete CaveBlock Permission List](Permissions)


## Placeholders

By default, BentoBox GameMode addons comes with [default placeholders set](../../BentoBox/Placeholders), however, each addon may introduce even more placeholders.

[Complete CaveBlock Placeholder List](Placeholders)


## Flags

Addon introduces 1 BentoBox Settings flag:

- ![feather](https://static.wikia.nocookie.net/minecraft_gamepedia/images/e/e2/Feather_JE3_BE2.png){: loading=lazy width=16px } SKY_WALKER_FLAG: flag in world settings that allows enabling/disabling player walking on cave roof.


## FAQ

??? question "Can you add a feature X?"
    Please add it to the list [here](https://github.com/BentoBoxWorld/CaveBlock/issues).

??? question "I have a bug, where should I report it?"
    Please add it to the list [here](https://github.com/BentoBoxWorld/CaveBlock/issues).


## Translations

{{ translations(2968, ["cs", "id", "ja", "lv", "ro", "zh-CN", "de", "pl", "ru", "es", "tr", "vi"]) }}

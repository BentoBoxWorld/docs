# AOneBlock

**AOneBlock** is our take on **IJAminecraft**'s popular survival map: OneBlock.
Players have to survive on a single block, which appears to be magic...

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("AOneBlock") }}

OneBlock puts you on a block in space. There is only one block. What do you do next?

## Installation

0. Install BentoBox and run it on the server at least once to create its data folders.
1. Place this jar in the addons folder of the BentoBox plugin.
2. Restart the server.
3. The addon will create worlds and a data folder and inside the folder will be a config.yml and config files in phases folder.
4. Stop the server.
5. Edit config.yml and the .yml config files how you want.
6. Delete any worlds that were created by default if you made changes that would affect them.
7. Restart the server.

## Configuration

The main `config.yml` file contains basic information about game-mode addon setup. 

`phases` contains all information about phases that will be present in your AOneBlock world.

`panels` allows to customize some user accessible panels.

### config.yml

After addon is successfully installed, it will create config.yml file. Every option in this file comes with comments about them. Please check file for more information.
You can find the latest config file: [config.yml](https://github.com/BentoBoxWorld/AOneBlock/blob/develop/src/main/resources/config.yml)

### Phase Config Files

The config files to make the phases are in the `phases` folder.

There are two files per phase - a file that contains the blocks and mobs, and a file that contains the chests.

The first number of any file is how many blocks need to be mined to reach that phase. This is the phase's key number.

=== "name"
    !!! summary "Description"
        The display name for phases. This name will be displayed in all spots where player try to view a phase. 

=== "icon"
    !!! summary "Description"
        The icon of the phase is used only in the `phases` panel. 

        The icon is created using [BentoBox ItemParser](https://docs.bentobox.world/en/latest/BentoBox/ItemParser/)

=== "fixedBlocks"
    !!! summary "Description"
        The fixedBlocks section allows forcing certain blocks when player breaks it. The first is a number of block in phase, and then it follows with Bukkit Material. The first block in phase has the index 0, while adding number that is larger than phase running time, will mean that it will not be reached.
        
        Available values you can find here: [Materials](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)    
    
        We recomend to use blocks that does not require a support block (like torch, rails, plants).

    !!! example "Example"
        ```yaml
            0: GRASS_BLOCK
            1: GRASS_BLOCK
            2: GRASS_BLOCK
            50: SPONGE
        ```

=== "holograms"
    !!! summary "Description"
        AOneBlock uses [Holographic Displays](https://dev.bukkit.org/projects/holographic-displays) plugin for showing these lines. The first line that is showed before any phase has started is located in aoneblock locales file.
        
        Similar to the `fixedBlocks`, `holograms` also starts with a number when it should be displayed that follows with a displayed text.

    !!! example "Example"
        ```yaml
            0: "&aFirst block is grass!"
            1: "&aSecond block is grass!"
            2: "&cWhat if there will be no next block?"
            3: "&aGood Luck!"
        ```

=== "biome"
    !!! summary "Description"
        `biome` is an experimental option. However, it changes biome only for the "magic" block location. 
        So we would suggest to use Biomes addon that has an option to change biome on whole island. 
        You can do it with phase start commands which would trigger biome change.

=== "start-commands"
    !!! summary "Description"
        `start-commands` section allows defining commands that will be triggered when player starts this phase.
    
        Commands are run as the Console unless the command is prefixed with `[SUDO]`, then the command is run as the player triggering the commands.
    
        These placeholders in the command string will be replaced with the appropriate value:
    
        - `[island]` - Island name
        - `[owner]` - Island owner's name
        - `[player]` - The name of the player who broke the block triggering the commands
        - `[phase]` - the name of this phase
        - `[blocks]` - the number of blocks broken
        - `[level]` - your island level (Requires Levels Addon)
        - `[bank-balance]` - your island bank balance (Requires Bank Addon)
        - `[eco-balance]` - player's economy balance (Requires Vault and an economy plugin)

    !!! example "Example"
        ```yaml
            start-commands:
            - 'give [player] WOODEN_AXE 1'
            - 'broadcast [player] just started OneBlock!'
            - 'obadmin biomes set [player] aoneblock_fields ISLAND!'
        ```

=== "end-commands"
    !!! summary "Description"
        `end-commands` section allows defining commands that will be triggered when player finishes this phase.
    
        Commands are run as the Console unless the command is prefixed with `[SUDO]`, then the command is run as the player triggering the commands.
    
        These placeholders in the command string will be replaced with the appropriate value:
    
        - `[island]` - Island name
        - `[owner]` - Island owner's name
        - `[player]` - The name of the player who broke the block triggering the commands
        - `[phase]` - the name of this phase
        - `[blocks]` - the number of blocks broken
        - `[level]` - your island level (Requires Levels Addon)
        - `[bank-balance]` - your island bank balance (Requires Bank Addon)
        - `[eco-balance]` - player's economy balance (Requires Vault and an economy plugin)

    !!! example "Example"
        ```yaml
            end-commands:
            - '[SUDO]say Just finished [phase]'
        ```

=== "requirements"
    !!! summary "Description"
        `requirements` section allows limiting access to the next phase until specified requirements are met.
        Currently, there are 4 requirement fields:
    
        - `economy-balance` - the minimum player's economy balance (Requires Vault and an economy plugin)
        - `bank-balance` - the minimum island bank balance (requires Bank Addon)
        - `level` - the island level (Requires Levels Addon)
        - `permission` - a permission string

    !!! example "Example"
        ```yaml
            requirements:
              bank-balance: 10000
              level: 10
              permission: ready.for.battle
        ```

=== "blocks"
    !!! summary "Description"
        The blocks section list Bukkit Materials followed by a relative probability. 
    
        Available values you can find here: [Materials](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)
    
        All the probability values are added up for the whole phase and the chance of the block being placed is the relative probability divided by the total of all the probabilities.

    !!! example "Example"
        ```yaml
            blocks:
              GRASS_BLOCK: 2
              STONE: 3
        ```
        
        This example shows that there is 40% chance to spawn a grass block while 60% to spawn stone. (2 / (2+3)) and (3 / (2+3))

=== "mobs"
    !!! summary "Description"
        The mob section list mobs that can spawn and their relative probability along with blocks.
        You can only list entities that are alive and can spawn in this list. [EntityTypes](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/EntityType.html)

    !!! example "Example"
        ```yaml
            mobs:
              COW: 150
              SPIDER: 75
        ```

=== "Custom Blocks"
    !!! summary "Description"
        Since version 1.11 you can now specify custom blocks (thanks to [@HSGamer](https://github.com/HSGamer)).
        You can do it in both places: blocks and fixed-blocks. 
        
        To define custom blocks in `blocks` section, you need to add `-` before each element.
        Also, blocks must be defined with type, data and probability values.

    !!! example "Example"
        ```yaml
            fixedBlocks:
              0:
                type: data
                data: minecraft:chest[waterlogged=true]
              1: GRASS_BLOCK
              2: GRASS_BLOCK
            blocks:
              - type: data
                data: minecraft:chest[waterlogged=true]
                probability: 10
              - type: data
                data: minecraft:chest
                probability: 10
              - DIRT: 10     # old syntax still works.
        ```


In the chests file, it just has the phase number and a chests section.

=== "chests"
    !!! summary "Description"
        If CHEST is listed in the blocks section, then it will be randomly filled according to this section. 
        You can define as many chests as you like. The first number is a unique chest number.
        Then follows the chest contents that includes the slot number and the item stack contents. 
        Finally, there is the chest's rarity, which can be COMMON, UNCOMMON, RARE or EPIC. The chances for them are hard-codded with values: 62%, 25%, 9%, and 4%.
        
        The best way to set chests is to do it in game.
        Fill a chest with the contents you want and then while looking at it enter the command `/[admin_cmd] setchest <phase> <rarity>` where <phase> is the name of the phase and rarity is the rarity. Use Tab Complete to see the options. The chest will be automatically added to the oneblocks.yml file and be ready to use. Deleting chests must be done by editing the oneblocks.yml file for now and reloading the addon.
    
        Be very careful when editing the chest items and check that the material is a true Bukkit material and spelled correctly.


### Customizable GUI's

BentoBox 1.17 API introduced a function that allows to implement customizable GUI's. This addon is one of the first one which uses this functionality. We tried to be as simple as possible for customization, however, some features requires explanation.
You can find more information how BentoBox custom GUI's works here: [Custom GUI's](/en/latest/Tutorials/generic/Customizable-GUI/)

??? question "How can I customize GUI's"
    To customize Addon GUI's you need to have version 1.10. This is a first version that has implemented them. Addon will create a new directory under `/plugins/BentoBox/addons/AOneBlock` with a name `panels`

??? question "What does `PREVIOUS`|`NEXT` button type?"
    The PREVIOUS and NEXT button types allows creating automatic paging, when you have more islands than spaces in GUI.
    These types have extra parameters under data:
 
    - `indexing` - indicates if button will show page number.

    Example: 
    ```yaml
        icon: TIPPED_ARROW:INSTANT_HEAL::::1
        title: aoneblock.gui.buttons.previous.name
        description: aoneblock.gui.buttons.previous.description
        data:
          type: PREVIOUS
          indexing: true
        actions:
          previous:
            click-type: LEFT
            tooltip: aoneblock.gui.tips.click-to-previous
    ```

??? question "What is `PHASE` button type?"
    This button allows players to view phase name and requirements. If users has access to phase changing, and they already have reached a phase, they can select it again and replay it.

    icon, title and description is generated dynamically based on phase properties. However, you can change it manually.

    Example: 
    ```yaml
      # icon: PLAYER_HEAD
      # title: aoneblock.gui.buttons.phase.name
      # description: aoneblock.gui.buttons.phase.description
      data:
        type: PHASE
      actions:
        select:
          click-type: LEFT
          tooltip: aoneblock.gui.tips.click-to-change
    ```


## Commands

!!! tip
    `[player_command]` and `[admin_command]` are commands that differ depending on the gamemode you are running.
    
    The Gamemodes' `config.yml` file contains options that allows you to modify these values.
    
    As an example, on AOneBlock, the default `[player_command]` is `ob`, and the default `[admin_command]` is `oba`.
    
    Be aware, that this addon allows changing player commands aliases in addon `config.yml` file.

=== "AOneBlock unique player commands"
    - `/[player_command] count`: sends a message in chant about current phase progress.
    - `/[player_command] phases`: opens GUI that allows to view and choose phases.
    - `/[player_command] setcount <number>`: allows changing current phase where <number> is phase start number.
    - `/[player_command] check`: spawns particles around magic block or respawns it, if for some reason it was mising.

=== "Admin commands"
    - `/[admin_command] sanity [<phase>]`: sends a message if phases (or <phase>) chests are correct.
    - `/[admin_command] setcount <player> <number>`: allows changing current phase to a <player> where <number> is phase start number.
    - `/[admin_command] setchest <phase> <rarity>`: saves a chest that player is looking at into <phase> chests section with <rarity>.


By default, BentoBox GameMode addons comes with [default sub-command set](#), however, each addon may introduce even more sub commands.

[Complete AOneBlock Command List](Commands)


## Permissions

!!! tip
    `[gamemode]` prefix in every place for AOneBlock addon must be replaced with `aoneblock`.

=== "Player permissions"
    - `aoneblock.count` - Let the player use the '/[player_command] count' command. Enabled by default.
    - `aoneblock.phases` - Let the player use the '/[player_command] phases' command. Disabled by default.
    - `aoneblock.island.setcount` - Let the player use the '/[player_command] setcount' command. Disabled by default.
    - `aoneblock.respawn-block` - Let the player use the '/[player_command] check' command. Enabled by default.

=== "Admin permissions"
    - `aoneblock.admin.sanity` - Let the player use the '/[admin_command] sanity' command. Default OP.
    - `aoneblock.admin.setchest` - Let the player use the '/[admin_command] setchest' command. Default OP.
    - `aoneblock.admin.setcount` - Let the player use the '/[admin_command] setcount' command. Default OP.

By default, BentoBox GameMode addons comes with [default sub-permission set](#), however, each addon may introduce even more sub-permissions.

[Complete AOneBlock Permission List](Permissions)


## Placeholders

AOneBlock addon has its own unique placeholders. These placeholders relates to the data AOneBlock is storing.

|Placeholder|Description|AOneBlock Version|
|--- |--- |--- |
|%aoneblock_my_island_phase%|the phase of your island|1.1.2|
|%aoneblock_my_island_count%|the block count of your island|1.1.2|
|%aoneblock_visited_island_phase%|the phase of the island you are standing on|1.1.2|
|%aoneblock_visited_island_count%|the block count of the island you are standing on|1.1.2|
|%aoneblock_my_island_next_phase%|the next phase for your island|1.1.2|
|%aoneblock_visited_island_next_phase%|the next phase for the island you are standing on|1.1.2|
|%aoneblock_my_island_blocks_to_next_phase%|blocks to go until the next phase, or "infinite" if there is no next phase|1.5.2|
|%aoneblock_visited_island_blocks_to_next_phase%|blocks until the next phase for the island you are standing on|1.5.2|
|%aoneblock_my_island_percent_done%|phase completion percentage|1.5.2|
|%aoneblock_visited_island_percent_done%|phase completion percentage of the island you are standing on|1.5.2|
|%aoneblock_my_island_done_scale%|phase completion scale of your island|1.5.2|
|%aoneblock_visited_island_done_scale%|phase completion scale of the island you are standing on|1.5.2|
|%aoneblock_my_island_lifetime_count%|the block count of lifetime for your island|1.10.0|
|%aoneblock_visited_island_lifetime_count%|the block count of lifetime for the island you are standing on|1.10.0|

By default, BentoBox GameMode addons comes with [default placeholders set](../../BentoBox/Placeholders), however, each addon may introduce even more placeholders.

[Complete AOneBlock Placeholder List](Placeholders)

## FAQ

??? question "Can you add a feature X?"
    Please add it to the list [here](https://github.com/BentoBoxWorld/AOneBlock/issues).

??? question "I have a bug, where should I report it?"
    Please add it to the list [here](https://github.com/BentoBoxWorld/AOneBlock/issues).

??? question "What phases are there?"
    There are 11 phases: Plains, Underground, Winter, Ocean, Jungle, Swamp, Dungeon, Desert, The Nether, Plenty, Desolation, and The End. 

    Each phase features a set of blocks, items, and mobs appropriate for the setting.

??? question "How many blocks are there in the 11 phases?"
    There are currently 11 thousand blocks!

??? question "What happens after the last phase?"
    The phases repeat.

??? question "Why do I keep falling and dying!"
    There are tricks to surviving, but it might be difficult! You need to build defenses.

??? question "Why do certain blocks spawn more frequently than others?"
    They just do! You can set the relative probability in the config files in the phases folder.

??? question "How do I know which is the magic block?"
    Hit it and it will give out green particles.

??? question "My magic block is no longer there! How do I get another one?"
    You will have to place a block there. Worse case, kill yourself and one will be generated.

??? question "My magic block is liquid! How can I mine it?"
    Use a bucket.

??? question "Which mobs can spawn?"
    Each phase has a different set of mobs that can spawn. Be careful because they may push you off! If you listen carefully, you may hear hostile mobs coming.

??? question "I have no chance to react to hostile mobs spawning!"
    Be prepared. Listen carefully when you mine a block and you will hear hostile mobs coming before they spawn. If you are in a hostile phase, then expect mobs and build defenses to protect yourself. You can mine a block from quite far away.

??? question "When mobs spawn, my defenses are destroyed! Why?"
    Mobs make space to spawn. If there's anything in the way, it'll be broken and dropped. You'll have to build accordingly.

??? question "Do chests spawn?"
    Yes. Chests spawn with random items in them from the current phase. There are common, uncommon, rare and epic chests. Chests with sparkles are good.

??? question "Is it possible to reach the Nether or End in this map?"
    The vanilla Nether exists by default but there is no End world.

    However, BentoBox is customizable, and you can enable nether islands and end world in AOneBlock config file.

    Be aware, magic block is located only in overworld.

??? question "What is the end goal?"
    It's whatever you want it to be! 

??? question "How to use holograms?"
    AOneBlock uses [Holographic Displays](https://dev.bukkit.org/projects/holographic-displays) for holograms if you use 1.12.3 and below.
    You need to install this plugin to use holograms sections!
    
    However, since 1.13 version and Minecraft 1.19.4, you do not need any extra plugins for holograms. They will be displayed using Minecraft Text Entity.

??? question "Should I use the Levels addon?"
    It's up to you, but if you do be aware that levels could get high because players have an infinite block. 
    I prefer not to use it and instead use the Likes addon.


## Translations

{{ translations(4481, ["cs", "lv", "de", "es", "fr", "hr", "hu", "id", "it", "ja", "tr", "vi", "zh-CN", "zh-TW"]) }}

## Api

Since BentoBox 1.17 API implemented a feature that solved an issue with classloaders. Plugins that wants to use access to the code directly, now can do it.

You just need to add AOneBlock to your project as dependency. You can use Maven for that:

```xml
<dependency>
    <groupId>world.bentobox</groupId>
    <artifactId>aoneblock</artifactId>
    <version>1.10.0</version>
    <scope>provided</scope>
</dependency>
```

AOneBlock addon stores data in a separate database table.

=== "OneBlockIslands"
    !!! summary "Description"
        OneBlockIslands stores all information about island progress through phases.

        Link to the source code: [OneBlockIslands](https://github.com/BentoBoxWorld/AOneBlock/blob/develop/src/main/java/world/bentobox/aoneblock/dataobjects/OneBlockIslands.java)

    !!! question "Variables"
        - "uniqueId": the island unique ID. It is equal to the Island uniqueId.
        - "blockNumber": the current broken block number.
        - "lifetime": the overall number of broken blocks.
        - "phaseName": the current phase name.
        - "hologram": the hologram text that is shown.

    !!! example "Code example"
        To access this data, you need to access to AOneBlock addon. It can be several ways, but example bellow shows
        a generic way that is accessible from everywhere.
        
        ```java
        public void accessToAOneBlockData(@NonNull Island island) {
           BentoBox.getInstance().getAddonsManager().<AOneBlock>getAddonByName("AOneBlock").ifPresent(aOneBlock -> {
                OneBlockIslands oneBlockData = aOneBlock.getOneBlocksIsland(island);           
                        
                String islandUniqueId = oneBlockData.getUniqueId();
                int brokenBlocks = oneBlockData.getBlockNumber();
                long lifetimeBlocks = oneBlockData.getLifetime();
                String phase = oneBlockData.getPhaseName();
                String hologram = oneBlockData.getHologram();
           });
        }
        ```

### Events

AOneBlock has some custom events that are called only in AOneBlock. But BentoBox GameMode events are still triggered in AOneBlock.

=== "BlockClearEvent"
    !!! summary "Description"
        This event is triggered before entity is spawned. It contains a list of blocks that will be cleared or replaced with water.

        Can be cancelled.

        Link to the class: [BlockClearEvent](https://github.com/BentoBoxWorld/AOneBlock/blob/develop/src/main/java/world/bentobox/aoneblock/events/BlockClearEvent.java)

    !!! question "Variables"
        - `Entity entity` - entity that is spawned.
        - `List<Block> airBlocks` - the list of blocks that will be replaced with air.
        - `List<Block> waterBlocks` - the list of blocks that will be replaced with water.
        - `boolean cancelled` - the boolean that indicates if event is cancelled.
 
    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onBlockClear(BlockClearEvent event) {
            Entity entity = event.getEntity();
            List<Block> airBlocks = event.getAirBlocks();
            List<Block> waterBlocks = event.getWaterBlocks();

            boolean cancelled = event.isCancelled();
        }
        ```

=== "MagicBlockEntityEvent"
    !!! summary "Description"
        This event is triggered after entity is spawned. It just contains basic information about spawned entity.

        Link to the class: [MagicBlockEntityEvent](https://github.com/BentoBoxWorld/AOneBlock/blob/develop/src/main/java/world/bentobox/aoneblock/events/MagicBlockEntityEvent.java)

    !!! question "Variables"
        - `EntityType entityType` - entityType that is spawned.
        - `@NonNull Island island` - the island where entity is summoned
        - `@Nullable UUID playerUUID` - the user id who triggered entity spawning. Can be Null.
        - `@NonNull Block block` - the magic block location.
 
    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onMagicBlockEntity(MagicBlockEntityEvent event) {
            EntityType entityType = event.getEntityType();

            Island island = event.getIsland();
            UUID playerUUID = event.getPlayerUUID();
            Block block = event.getBlock();
        }
        ```

=== "MagicBlockEvent"
    !!! summary "Description"
        This event is triggered after magic block is broken.

        Link to the class: [MagicBlockEvent](https://github.com/BentoBoxWorld/AOneBlock/blob/develop/src/main/java/world/bentobox/aoneblock/events/MagicBlockEvent.java)

    !!! question "Variables"
        - `@Nullable ItemStack tool` - the tool that broke magic block.
        - `@NotNull Material nextBlockMaterial` - the next magic block material.
        - `@NonNull Island island` - the island where block is summoned.
        - `@Nullable UUID playerUUID` - the user id who broke magic block. Can be Null.
        - `@NonNull Block block` - the magic block location.
 
    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onMagicBlock(MagicBlockEvent event) {
            ItemStack tool = event.getTool();
            Material nextBlockMaterial = event.getNextBlockMaterial();

            Island island = event.getIsland();
            UUID playerUUID = event.getPlayerUUID();
            Block block = event.getBlock();
        }
        ```

=== "MagicBlockPhaseEvent"
    !!! summary "Description"
        This event is triggered after a new phase has started.

        Link to the class: [MagicBlockPhaseEvent](https://github.com/BentoBoxWorld/AOneBlock/blob/develop/src/main/java/world/bentobox/aoneblock/events/MagicBlockPhaseEvent.java)

    !!! question "Variables"
        - `String phase` - the name of the new phase.
        - `String oldPhase` - the name of previous phase.
        - `int blockNumber` - the block number when new phase starts.
        - `@NonNull Island island` - the island where block is summoned.
        - `@Nullable UUID playerUUID` - the user id who broke magic block. Can be Null.
        - `@NonNull Block block` - the magic block location.
 
    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onMagicBlockPhase(MagicBlockPhaseEvent event) {
            String phase = event.getPhase();
            String oldPhase = event.getOldPhase();
            int blockNumber = event.getBlockNumber();

            Island island = event.getIsland();
            UUID playerUUID = event.getPlayerUUID();
            Block block = event.getBlock();
        }
        ```

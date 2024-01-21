# Level

**Level** lets your players compete to have the top island! Place blocks and increase the island level!

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("Level") }}

## Installation

1. Place the level addon jar in the addons folder of the BentoBox plugin
2. Restart the server
3. The addon will create a data folder and inside the folder will be a config.yml
4. Edit the config.yml how you want. The config specifies how much blocks are worth (see below)
5. Restart the server if you make a change

## Configuration

Level addon has 3 general configuration things:

- config.yml file contains default addon configuration files.
- blockconfig.yml file contains value for each block.
- /panels/ contains files that manages player GUI's

### config.yml

Config file contains main functions for the addon. 

The latest config.yml can be found [here](https://github.com/BentoBoxWorld/Level/blob/develop/src/main/resources/config.yml).

This section defines a number of overall settings for the add-on.

??? note "disabled-game-modes"
    Allows to specify in which GameModeAddons Level addon should not operate.
    
    Level will NOT hook into these game mode addons.

    Default: `[]`

??? note "log-report-to-console"
    Allows to see a level report if command is executed from console.

    Default: `true`

??? note "concurrent-island-calcs"
    Allows to specify how many island level calculations can be happening at once.

    If your CPU can handle it, you can run parallel island calcs if there are more than one in the queue.

    Default: `1`

??? note "calculation-timeout"
    Allows to specify the amount of minutes when level calculation should be stopped.

    Generally, calculation should only take a few seconds, so if this ever triggers then something is not right.

    Default: `5`

??? note "zero-new-island-levels"
    Allows to specify if starting blocks should be included in island level.

    If true, Level will calculate the starter island's level and remove it from any future level calculations.
    Player level may go into negative values if all starting blocks are removed.
    
    If this is false, the player's starter island blocks will count towards their level.

    Default: `true`

??? note "login"
    Allows to set that island level is calculated on player login.

    This silently calculates the player's island level when they login.

    Default: `false`

??? note "nether"
    Allows to include nether island in level calculation.

    Warning: Enabling this mid-game will give players with an island a jump island level. New islands will be correctly zeroed.

    Default: `false`

??? note "end"
    Allows to include the end island in level calculation.

    Warning: Enabling this mid-game will give players with an island a jump island level. New islands will be correctly zeroed.

    Default: `false`

??? note "include-chests"
    Allows to include chest content in level calculation.

    Warning: level calculation will be longer and server performance may be affected.

    Default: `false`

??? note "underwater"
    Allows to specify underwater block multiplier.

    If blocks are below sea-level, they can have a higher value. e.g. 2x. 
    Promotes under-water development if there is a sea. Value can be fractional.

    Default: `1.0`

??? note "levelcost"
    Allows to specify value of one island level.

    Default: `100`

    Minimum: `1`

??? note "level-calc"
    Allows to specify the formula for level calculation.

    * blocks - the sum total of all block values, less any death penalty
    * level_cost - in a linear equation, the value of one level

    This formula can include +,=,*,/,sqrt,^,sin,cos,tan,log (natural log). 
    Result will always be rounded to a long integer.

    For example, an alternative non-linear option could be: `3 * sqrt(blocks / level_cost)`

    Default: `blocks / level_cost`

??? note "levelwait"
    Allows to specify cool down between level requests in seconds.

    Default: `60`

??? note "deathpenalty"
    Allows to specify the death penalty.

    How many block values a player will lose per death. 
    Default value of 100 means that for every death, the player will lose 1 level (if levelcost is 100).
    
    Set to zero to not use this feature.

    Default: `100`

??? note "sumteamdeaths"
    Allows to sum all team members for the death penalty.

    If false, only the leader's deaths counts.

    Default: `false`

??? note "shorthand"
    Allows to show shorter island level numbers.

    Shows large level values rounded down, e.g., 10,345 -> 10k

    Default: `false`

### blockconfig.yml

Block config file contains values for blocks.

The latest blockconfig.yml can be found [here](https://github.com/BentoBoxWorld/Level/blob/develop/src/main/resources/blockconfig.yml).

This section defines values for blocks and limits for them. 

!!! tip
    Values in this file supports only integers -> full numbers.

!!! tip
    The correct material names can be found in Spigot material page. 

    Note: this is latest spigot material list: [MATERIALS](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)

??? note "limits"
    This section lists the limits for any particular block. 
    Blocks over this amount are not counted. 
    This limit applies to all game modes and is not world-specific.

    Format: `MATERIAL: NUMBER`

??? note "blocks"
    This section lists the value of a block in all game modes (worlds). 
    To specific world-specific values, use the next section. 
    Any blocks not listed will have a value of 0. AIR is always zero.

    Format: `MATERIAL: NUMBER`

??? note "worlds"
    List any blocks that have a different value in a specific world. 
    If a block is not listed, the default value will be used from the blocks section.
    Prefix with world name. The values will apply to the associated nether and the end if they exist. 

    Example:

    ```
        worlds:
          AcidIsland_world:
            SAND: 0
            SANDSTONE: 0
            ICE: 0
    ```

    In this example, AcidIsland will use the same values as BSkyBlock for all blocks except for sand, sandstone and ice.

### Customizable GUI's

BentoBox 1.17 API introduced a function that allows to implement customizable GUI's. We tried to be as simple as possible for customization, however, some features requires explanation.
You can find more information how BentoBox custom GUI's works here: [Custom GUI's](/en/latest/Tutorials/generic/Customizable-GUI/)

??? question "How can I customize GUI's"
    To customize Level Addon GUI's you need to have version 2.10.0. This is a first version that has implemented them. Addon will create a new directory under `/plugins/bentobox/addons/level` with a name `panels`

    Currently you can customize 3 GUI's:

    - Top panel: `top_panel` - allows to see top 10 islands.
    - The detail block panel: `detail_panel` - allows to view detailed list block values in game.
    - The block value panel: `value_panel` - allows to view each block value in game.

    Each GUI contains functions that is supported only by itself.

??? question "What does `PREVIOUS`|`NEXT` button type?"
    This button is available in detail_panel and value_panel.
    The PREVIOUS and NEXT button types allows creating automatic paging, when you have more blocks than spaces in GUI.
    These types have extra parameters under data:

    - `indexing` - indicates if button will show page number.

      Example: 
      ```yaml
          icon: tipped_arrow{CustomPotionColor:11546150}
          title: level.gui.buttons.previous.name
          description: level.gui.buttons.previous.description
          data:
            type: PREVIOUS
            indexing: true
          action:
            left:
              tooltip: level.gui.tips.click-to-previous
      ```

??? question "What does `TOP` button type?"
    This button is available in top_panel. It shows island at the top X by island level.
    
    The `icon` by default will be `PLAYER_HEAD` with a proper player skin. Enabling it will replace it with specified material.

    `index` in the data field allows to specify which place of Top 10 should be showed in current spot.

    Top panel has 2 implemented actions which funstion requires extra addon:
    
    - `warp` - requires Warps addon. Will be shown only if warp sign exists on players island.
    - `visit` - requires Visit addon. Will be shown only if visiting is allowed on players island.

    Fallback allows to change background icon, when there are no player in top spot.

    Example:
    ```yaml
        #icon: PLAYER_HEAD
        title: level.gui.buttons.island.name
        description: level.gui.buttons.island.description
        data:
          type: TOP
          index: 1
        actions:
          warp:
            click-type: LEFT
            tooltip: level.gui.tips.click-to-warp
          visit:
            click-type: RIGHT
            tooltip: level.gui.tips.right-click-to-visit
        fallback:
          icon: LIME_STAINED_GLASS_PANE
          title: level.gui.buttons.island.empty
    ```

??? question "What does `VIEW` button type?"
    This button is available in top_panel. It shows viewer island level.

    The `icon` by default will be `PLAYER_HEAD` with a proper player skin. Enabling it will replace it with specified material.
    
    The action `view` allows to see detailed menu of players island.

    Example:
    ```yaml
        #icon: PLAYER_HEAD
        title: level.gui.buttons.island.name
        description: level.gui.buttons.island.description
        data:
          type: VIEW
        actions:
          view:
            click-type: unknown
            tooltip: level.gui.tips.click-to-view
    ```

??? question "What does `BLOCK` button type?"
    This button is available in detail_panel and value_panel. This button shows given material as icon. 

    Example:
    ```yaml
      #icon: STONE
      title: level.gui.buttons.value.name
      description: level.gui.buttons.value.description
      data:
        type: BLOCK
    ```

## Commands

!!! tip
    `[player_command]` and `[admin_command]` are commands that differ depending on the gamemode you are running.
    The Gamemodes' `config.yml` file contains options that allows you to modify these values.
    As an example, on BSkyBlock, the default `[player_command]` is `island`, and the default `[admin_command]` is `bsbadmin`.

=== "Player commands"
    - `/[player_command] top`: access to the top panel. Requires `[gamemode].island.top` permission.
    - `/[player_command] level`: triggers level calculation for player. Requires `[gamemode].island.level` permission.
    - `/[player_command] value [material]`: allows to check block value. Requires `[gamemode].island.value` permission.


=== "Admin commands"
    - `/[admin_command] level <player>`: triggers level calculation for player. Requires `[gamemode].admin.level` permission.
    - `/[admin_command] levelstatus`: shows how many islands are in the queue. Requires `[gamemode].admin.levelstatus` permission.
    - `/[admin_command] sethandicap <player> <number>`: allows to set initial number of island level. Requires `[gamemode].admin.level.sethandicap` permission.
    - `/[admin_command] top`: shows the top 10 islands in chat. Requires `[gamemode].admin.top` permission.
    - `/[admin_command] top remove <player>`: allows to remove player from the top. Requires `[gamemode].admin.top.remove` permission.


## Permissions

!!! tip
    `[gamemode]` is a prefix that differs depending on the gamemode you are running.
    The prefix is the lowercased name of the gamemode, i.e. if you are using BSkyBlock, the prefix is `bskyblock`.
    Similarly, if you are using AcidIsland, the prefix is `acidisland`.

=== "Player permissions"
    - `[gamemode].intopten` - (default: `true`) - Lets the player be in top 10 panel.
    - `[gamemode].island.level` - (default: `true`) - Allows player to use the `/[player_command] level` command.
    - `[gamemode].island.top` - (default: `true`) - Allows player to use the `/[player_command] top` command.
    - `[gamemode].island.value` - (default: `true`) - Allows player to use the `/[player_command] value` command.
    - `[gamemode].island.level.details.blocks` - (default: `true`) - Allows player to see detailed list of blocks for island.
    - `[gamemode].island.level.details.spawners` - (default: `false`) - Allows player to see detailed list of spawners for island.
    - `[gamemode].island.level.details.underwater` - (default: `false`) - Allows player to see detailed list of underwater blocks for island.
    - `[gamemode].island.level.details.above-sea-level` - (default: `false`) - Allows player to see detailed list of above the sea level blocks for island.

=== "Admin permissions"
    - `[gamemode].admin.level` - (default: `op`) - Let the player use the `/[admin_command] level <player>` command.
    - `[gamemode].admin.levelstatus` - (default: `op`) - Let the player use the `/[admin_command] levelstatus` command.
    - `[gamemode].admin.level.sethandicap` - (default: `op`) - Let the player use the `/[admin_command] sethandicap <player> <number>` command.
    - `[gamemode].admin.top` - (default: `op`) - Allows the access to `/[admin_command] top` command.
    - `[gamemode].admin.top.remove` - (default: `op`) - Allows the access to `/[admin_command] top remove <player>` command.

??? question "Something is missing?"
    You can find the comprehensive list of permissions in the [addon.yml](https://github.com/BentoBoxWorld/Level/blob/develop/src/main/resources/addon.yml) file of this addon.  
    If something is indeed missing from the list below, please let us know!


## Placeholders

{{ placeholders_source(source="Level") }}

## FAQ

??? question "Can you add a feature X?"
    Please add it to the list [here](https://github.com/BentoBoxWorld/Level/issues).

??? question "How to make that `level-cost` increases after each level?"
    You cannot do it directly because BentoBox level calculation happens at once, and not iterative for each level.

    However, this can be done using the `level-calc` formula, if you know what formula you need. If we use your example of making each level 50% harder to reach than the previous level, then the approximate formula for that is:
    
    `level-calc: 2.4661 * log(blocks) - (2.4661 * log(level_cost) - 1)`
    
    where `level_cost` is the cost in blocks to get to level 1. e.g., if level 1 costs 100 blocks, the level 2 costs 150 blocks, level 3 costs 225, etc.
    
    Here's the graph:

    ![template](https://user-images.githubusercontent.com/4407265/212771452-edc943fe-c861-4ba1-b581-8ec987e52f94.png){: loading=lazy }
 
    Note that that particular formula does start to asymptote around level 25, i.e., it becomes really hard to get to level 26 or 27 because so many blocks are required, so having that particular rule might not be that good an approach because eventually almost everyone will end up with the same level.
     
    Anyway, although I understand what you're asking, the `level-calc` formula should actually be able to provide what you want so long as it supports the right formula. Having the `next-levelcost` is problematic from a programming standpoint because the level calculations would have to be done iteratively instead of by just applying a single formula to the blocks counted. I can't quite work out how to do that right now but I do know that the current method of having a formula for how you want levels increased does work for sure.
    
    How can I work out a formula for levels?

    The best way is to start with a formula and plot it to see if it makes sense, e.g., by using something like Excel. If you want to work out what formula you need from say a table of values, then Excel (or maybe some other spreadsheet) can do that too: make a graph of levels and how many blocks for each level and then plot a graph of the table (X Y Plot). Right click the graph to add a trend line, select the approximation, e.g., linear, log, exponential, etc. that best fits, and then select "Display equation on chart" to display the formula and substitute `blocks` for `x`. Here's some screenshots of what I did you find out the equation for increasing by 50% each time with a starting cost of 100 blocks.
    
    ![template](https://user-images.githubusercontent.com/4407265/212773894-6f635ed4-f337-4936-b50f-3b616b6bf041.png){: loading=lazy }
    ![template](https://user-images.githubusercontent.com/4407265/212773929-b51ae6b3-5df3-43ae-b35f-bc6fcb42d78f.png){: loading=lazy }
 
    So, for that, it would be:
    
    `level-calc: 2.4661 * log(blocks) - 10.357`
    
    I hope that helps.



## Translations

{{ translations(3013, ["cs", "de", "es", "fr", "hu", "id", "lv", "pl", "ro", "tr", "zh-CN", "ko", "pt", "vi", "ru"]) }}



## API

Since Level 2.7.2 and BentoBox 1.17 other plugins can access to the Level addon data directly. However, addon requests are still a good solution for a plugins that do not want to use too many dependencies.

### Maven Dependency
Level provides an API for other plugins. This covers Level 2.8.1 and onwards.

!!! note
    Add the Level dependency to your Maven POM.xml:

    ```xml
        <repositories>
            <repository>
                <id>codemc-repo</id>
                <url>https://repo.codemc.io/repository/maven-public/</url>
            </repository>
        </repositories>
        
        <dependencies>
            <dependency>
                <groupId>world.bentobox</groupId>
                <artifactId>level</artifactId>
                <version>2.8.1</version>
                <scope>provided</scope>
            </dependency>
        </dependencies>
    ```
Use the latest Level version.

Then you can obtain the level for a player by asking Level once you have the world that the island is in and confirming that the player is the owner of an island in that world.

The JavaDocs for Level can be found [here](https://ci.codemc.io/job/BentoBoxWorld/job/Level/ws/target/apidocs/index.html).

### Events

=== "IslandLevelCalculatedEvent"
    !!! summary "Description"
        Event that is triggered when player level is calculated.

        Link to the class: [IslandLevelCalculatedEvent](https://github.com/BentoBoxWorld/Level/blob/develop/src/main/java/world/bentobox/level/events/IslandLevelCalculatedEvent.java)

    !!! question "Variables"
        - `Island island` - the island object.
        - `UUID targetPlayer` - id of the player who calculated level.
        - `Results results` - the calculated island results.
        
    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onLevelCalculated(IslandLevelCalculatedEvent event) {
            UUID user = event.getTargetPlayer();
            Island island = event.getIsland();
            Results results = event.getResults();
            
            // death handicap from results.
            int deathHandicap = event.getDeathHandicap();

            // the island initial level from results.
            long initialLevel = event.getInitialLevel();
            
            // the island level from results.
            long level = event.getLevel();

            // this will overwrite island level to 100.
            event.setLevel(100);
            
            // number of points required to next level
            long pointsToNextLevel = event.getPointsToNextLevel();

            // the report text from results.
            List<String> report = event.getReport();
        }
        ``` 

=== "IslandPreLevelEvent "
    !!! summary "Description"
        Event that is triggered before player level is calculated.

        Link to the class: [IslandPreLevelEvent](https://github.com/BentoBoxWorld/Level/blob/develop/src/main/java/world/bentobox/level/events/IslandPreLevelEvent.java)

    !!! question "Variables"
        - `Island island` - the island object.
        - `UUID targetPlayer` - id of the player who calculated level.
        
    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.LOW)
        public void beforeLevelCalculated(IslandPreLevelEvent event) {
            UUID user = event.getTargetPlayer();
            Island island = event.getIsland();
        }
        ```

### Addon Request Handlers

Till BentoBox 1.17 we had an issue with accessing data outside BentoBox environment doe to the class loader we used to load addons.
This meant that data was accessible only from other addons. But BentoBox implemented PlAddon functionality, which means that request
handlers are not necessary anymore.

More information about addon request handlers can be found [here](/en/latest/BentoBox/Request-Handler-API---How-plugins-can-get-data-from-addons/)

=== "island-level"
    !!! summary "Description"
        Returns the level of this player's island in the given world.

    !!! question "Input"
        - `world-name`: String - the name of the world.
        - `player`: UUID - the UUID of the player.

    !!! success "Output"
        The player's island level or `0L` if the input was invalid or if this player does not have an island in this world.

    !!! failure
        This handler will return `0L` if the `world-name` has not been provided or if the `world-name` does not exist or is not a gamemode world.

    !!! example "Code example"
        ```java
            /**
             * Returns the level of this player's island in the given world.
             * @param playerUUID UUID of the player, not null.
             * @param worldName Name of the world (Overworld) the island is in, not null.
             * @return the player's island level or {@code 0L} if the input was invalid or
             *         if this player does not have an island in this world.
             */
            public long getIslandLevel(UUID playerUUID, String worldName) {
                return (Long) new AddonRequestBuilder()
                    .addon("Level")
                    .label("island-level")
                    .addMetaData("world-name", worldName)
                    .addMetaData("player", playerUUID)
                    .request();
            }
        ```

=== "top-ten-level"
    !!! summary "Description"
        Returns the players whose island they own is in the Top 10 mapped to the level of their island.

    !!! question "Input"
        - `world-name`: String - the name of the world.

    !!! success "Output"
        `Map<UUID, Long>` containing the UUIDs of the island owners whose island is in the Top 10, mapped to the level of their island.

    !!! failure
        This handler will return empty map if the `world-name` has not been provided or if the `world-name` does not exist or is not a gamemode world.

    !!! example "Code example"
        ```java
            /**
             * Returns the players whose island they own is in the Top 10 mapped to the level of their island.
             * @param worldName Name of the world (Overworld) the island is in, not null.
             * @return a Map containing the UUIDs of the island owners whose island is in the Top 10, mapped to the level of their island,
             *         or an empty map if the specified world doesn't exist or doesn't contain islands.
             */
            public Map<UUID, Long> getTopTen(String worldName) {
                return (Map<UUID, Long>) new AddonRequestBuilder()
                    .addon("Level")
                    .label("top-ten-level")
                    .addMetaData("world-name", worldName)
                    .request();
            }
        ```
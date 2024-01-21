# Challenges

**Challenges** lets your players **complete various customizable challenges and receive rewards**!

Created and maintained by [BONNe](https://github.com/BONNe).

{{ addon_description("Challenges") }}

## Installation

1. Place the addon jar in the addons folder of the BentoBox plugin
2. Restart the server
3. Run the admin challenges command, e.g., `/bsbadmin challenges` to configure the addon

## Configuration

By default, the challenges addon comes without any challenge or levels. On first runtime only the Admin GUI will be accessible.
Admins can create their own challenges or load a set of default challenges. Default challenges contains 5 levels and 57 challenges.
There also exist a Web Library, where admins can download public challenges. It is accessible via the Admin GUI by clicking on the Web icon.

### config.yml

Config file contains main functions for the addon.

The latest config.yml can be found [here](https://github.com/BentoBoxWorld/Challenges/blob/develop/src/main/resources/config.yml).

### Template

Challenges addon contains a template file which can be used to import challenges into database. This file is useful for bulk challenge adding for people that do not like to use ingame-gui. However, be aware, that not all functions are available for the template file, and some items/options can be added only via GUI.
You can have as many template files as you want. Admin GUI will allow choosing which one you want to import.
The example template file: [template.yml](https://github.com/BentoBoxWorld/Challenges/blob/develop/src/main/resources/template.yml)

!!! tip
    The template file must contain both: challenges and levels. Without them, it will not work.

??? question "What is challenge type?"
    Challenges addon has 4 different types of challenges. Each type offers different things to be tested for challenge to be marked as completed. These types are:
    
    - Inventory Challenge (`INVENTORY_TYPE`) - challenge that requires items in player inventory to be completed.
    - Island Challenge (`ISLAND_TYPE`) - challenge that requires blocks or entities on the player island to be completed.
    - Other Challenge (`OTHER_TYPE`) - challenge that requires player XP, money or island level to be completed.
    - Statistic Challenge (`STATISTIC_TYPE`) - challenge that requires certain value from player statistic to be completed.

??? question "Can I specify an enchantment on required/reward items?"
    Unfortunately Spigot does not have a general item parsing mechanics. So plugin authors need to create their own. Challenges addon uses BentoBox [Item Parser](/en/latest/BentoBox/ItemParser/). If function is not supported by it, then you cannot. However, you can always use in-game admin GUI to set any items you want. There is not any limitation.

??? question "How I can know what values I can put in statistic challenge type?"
    The statistic type you can find here: [Statistic](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Statistic.html).
    
    Some information can be found in fandom site: [minecraft.fandom](https://minecraft.fandom.com/wiki/Statistics)
    
    However, there is not a place where you could find out what things you can specify. I would recommend to use ingame admin GUI for creating statistic challenges, as it has more options to detect which fields can fill.

### Customizable GUI's

BentoBox 1.17 API introduced a function that allows to implement customizable GUI's. Challenges addon is one of the first one which uses this functionality. We tried to be as simple as possible for customization, however, some features requires explanation.
You can find more information how BentoBox custom GUI's works here: [Custom GUI's](/en/latest/Tutorials/generic/Customizable-GUI/)

??? question "How can I customize GUI's"
    To customize Challenges Addon GUI's you need to have version 1.0. This is a first version that has implemented them. Addon will create a new directory under `/plugins/bentobox/addons/challenges` with a name `panels`
    
    Currently you can customize 3 GUI's:

    - Main Challenges Panel: `main_panel` - panel that is opened when player can see list of challenges.
    - Multiple Completion Panel: `multiple_panel` - panel that is opened when player wants to specify number of times challenge must be completed.
    - Gamemode Selection Panel: `gamemode_panel` - panel that is opened when `commands.global-command` is enabled in settings and there are multiple gamemodes installed.

    Each GUI contains functions that is supported only by itself.

??? question "What does `PREVIOUS`|`NEXT` button type?"
    This button is available in main_panel and gamemode_panel.
    The PREVIOUS and NEXT button types allows creating automatic paging, when you have more challenges than spaces in GUI.
    These types have extra parameters under data:
    - `target` - indicates if button will switch `LEVEL` or `CHALLENGE` in main_panel and `GAMEMODE` in gamemode_panel.
    - `indexing` - indicates if button will show page number.

    Example: 
    ```yaml
        icon: tipped_arrow{CustomPotionColor:11546150}
        title: challenges.gui.buttons.previous.name
        description: challenges.gui.buttons.previous.description
        data:
          type: PREVIOUS
          target: CHALLENGE
          indexing: true
        action:
          left:
            tooltip: challenges.gui.tips.click-to-previous
    ```

??? question "What does `CHALLENGE` button type?"
    This button is available in main_panel.
    The CHALLENGE button creates a dynamic entry for a challenge. Button will be filled only if there exist a challenge. F.e. if you have only 3 challenge, but defined 7 spots for challenges in the GUI, then only 3 spots will be filled. Other spots will be left empty.

    By default challenges will be ordered by their order numbers, however, you can specify a specific level to be in a specific slot with `id` parameter under data.
    
    ```yaml
      data:
        type: CHALLENGE
        id: example_challenge
    ```

    Specifying title, description and icon will overwrite dynammic generation based on database data. By default these values will be generated from database entries.
    This button supports 3 different action types:

    - COMPLETE - just completes a challenge once.
    - COMPLETE_MAX - completes a challenge as much as possible.
    - MULTIPLE_PANEL - opens multiple completion panel which allows to select how many times must be completed.

    Example: 
    ```yaml
      data:
        type: CHALLENGE
      actions:
        left:
          type: COMPLETE
          tooltip: challenges.gui.tips.click-to-complete
        right:
          type: MULTIPLE_PANEL
          tooltip: challenges.gui.tips.right-click-multiple-open
        shift_left:
          type: COMPLETE_MAX
          tooltip: challenges.gui.tips.shift-left-click-to-complete-all
    ```


??? question "What does `LEVEL` button type?"
    This button is available in main_panel.
    The LEVEL button creates a dynamic entry for a challenge level. Button will be filled only if there exist a level. F.e. if you have only 3 levels, but defined 7 spots for level in the GUI, then only 3 spots will be filled. Other spots will be left empty.

    By default levels will be ordered in their progression, however, you can specify a specific level to be in a specific slot with `id` parameter under data.
    
    ```yaml
      data:
        type: LEVEL
        id: example_level
    ```

    Specifying title, description and icon will overwrite dynammic generation based on database data. By default these values will be generated from database entries.
    
    Example: 
    ```yaml
      data:
        type: LEVEL
      actions:
        left:
          tooltip: challenges.gui.tips.click-to-select
    ```
    
??? question "What does `UNASSIGNED_CHALLENGES` button type?"
    This button is available in main_panel.
    The UNASSIGNED_CHALLENGES button allows to select a button for free challenges.
    It does not have any extra functions or dynamic generations.

??? question "What does `GAMEMODE` button type?"
    This button is available in gamemode_panel
    It generates a button for each GameMode addon that has Challenges installed.

??? question "What does `INCREASE`|`REDUCE` button type"
    This button is available in multiple_panel.
    These types allow increasing/reducing the number of challenge completion.

    Specifying `value: <number>` under `data` allows to set different custom number of increment/reducement.

??? question "What does `ACCEPT` button type"
    This button is available in multiple_panel.
    This type allows accepting input number and complete challenge that much time.

    Specifying `type: ACCEPT` under action allows to complete challenge. 
    Specifying `type: INPUT` under action allows request player to write number in chat.

## Commands

!!! tip
    `[player_command]` and `[admin_command]` are commands that differ depending on the gamemode you are running.
    The Gamemodes' `config.yml` file contains options that allows you to modify these values.
    As an example, on BSkyBlock, the default `[player_command]` is `island`, and the default `[admin_command]` is `bsbadmin`.

=== "Player commands"
    - `/challenges`: Access Player Challenges GUI. Contains either Challenges in current world or list of worlds where are Challenges enabled. This must be enabled in configuration.
    - `/[player_command] challenges [challenge] [number]`: Access BSkyBlock Player Challenges GUI. If challenge name is provided, than this method will complete that challenge once. If number is provided, than it will complete challenge from 0-number times.

=== "Admin commands"
    - `/challengesadmin`: Access Admin Challenges GUI. Contains list of worlds where Challenges are enabled. This must be enabled in configuration.
    - `/[admin_command] challenges`: Access BSkyBlock Admin Challenges GUI
    - `/[admin_command] challenges reload [hard]`: Ability to reload Challengs addon configuration. This method clears also cache data. Parameter hard allows to reset database connection.

## Permissions

!!! tip
    `[gamemode]` is a prefix that differs depending on the gamemode you are running.
    The prefix is the lowercased name of the gamemode, i.e. if you are using BSkyBlock, the prefix is `bskyblock`.
    Similarly, if you are using AcidIsland, the prefix is `acidisland`.

=== "Player permissions"
    - `[gamemode].challenges` - (default: `true`) - Let the player use the '/[player_command] challenges' command.
    - `[gamemode].challenges.multiple` - (default: `true`) - Allows the player complete challenge multiple times at once.
    - `[gamemode].challenges.complete` - (default: `false`) - Let the player use the '/[player_command] challenges complete <challenge> <number>' command.
    - `addon.challenges` - (default: `true`) - Allows the access to '/challenges' command if it is enabled in the config.
    - `[gamemode].command.challengeexempt` - (default: `false`) - Allows blocking reward command executing for player.

=== "Admin permissions"
    - `[gamemode].admin.challenges` - (default: `op`) - Let the player use the '/[admin_command] challenges' command.
    - `[gamemode].admin.challenges.complete` - (default: `op`) - Let the player use the '/[admin_command] challenges complete' command.
    - `[gamemode].admin.challenges.reset` - (default: `op`) - Let the player use the '/[admin_command] challenges reset' command.
    - `addon.admin.challenges` - (default: `op`) - Allows the access to '/challengesadmin' command if it is enabled in the config. 

??? question "Something is missing?"
    You can find the comprehensive list of permissions in the [addon.yml](https://github.com/BentoBoxWorld/Challenges/blob/develop/src/main/resources/addon.yml) file of this addon.  
    If something is indeed missing from the list below, please let us know!


## Placeholders

{{ placeholders_source(source="Challenges") }}

## FAQ

??? question "Can you add a feature X?"
    Please add it to the list [here](https://github.com/BentoBoxWorld/Challenges/issues).

??? question "How can I add a new challenge?"
    The official way is to add challenge via Admin GUI or Template file.
    Be aware, that template file is imported only after using proper icon in Admin GUI ("Import Template"). The GUI will allow choosing which template you will want to import into gamemode. 
    
    However, there is an option to edit exported database file. It can be done by exporting to file via: `/[admin_command] challenges` and clicking on "Export Database" button.

??? question "Can I enable challenges per island? So all island members has the same challenges?"
    Yes, you can do it via addon config file: `store-island-data: true`

??? question "Can I enable challenges per player?"
    Yes, you can do it via addon config file: `store-island-data: false`

??? question "Reward commands are not working. Why?"
    Most likely reward commands are not working because of incorrect definition. The command does not require `/` symbol before it.
    
    If you want to call command from player perspective, you need to add `[SELF]` before command call, f.e. `[SELF] kill` will result in player calling `/kill` command.

    It also could be caused by permissions. `[gamemode].command.challengeexempt` will prevent player to execute commands. Check if player does not have this permission.

??? question "How to add placeholders in reward commands?"
    Currently, addon do not support placeholders in reward commands. If that is necessary, you can request them in gitHub.
    
    Only placeholder that currently is supported in reward commands is `[player]` which returns player who completed challenge name.

??? question "I do not like order of elements in challenge description. Can I change it?"
    Yes, order of elements are defined in addon locales file.

    [Challenge Description](https://github.com/BentoBoxWorld/Challenges/blob/develop/src/main/resources/locales/en-US.yml#L852-L994)
    [Level Description](https://github.com/BentoBoxWorld/Challenges/blob/develop/src/main/resources/locales/en-US.yml#L995-L1042)

    Switching or removing parts of lore will change the order of elemetns displayed in it.

    ```yaml
        lore: |-
            [description]
            [status]
            [cooldown]
            [requirements]
            [rewards]
    ```

    Each of these parts are generated by tags below, and you can change them too. F.e. [status] part is generated from:

    ```yaml
    status:
        # Status message for completed unrepeatable challenge
        completed: "&2&l Completed"
        # Status message that contains number of completions for unlimited repeatable challenge
        completed-times: "&2 Completed &7&l [number] &r&2 time(-s)"
        # Status message that contains number of completions from max available for repeatable challenge
        completed-times-of: "&2 Completed &7&l [number] &r&2 out of &7&l [max] &r&2 times"
        # Status message that indicates that max completion count reached for repeatable challenge
        completed-times-reached: "&2&l Completed all &7 [max] &2 times"
    ```

## Translations

!!! info "Translations for challenges"
    The translations do not cover the challenges.
    Each challenge has its own "display name" and "description" which are not localized to keep the configuration process as simple as possible for the end user.  
    You can however find or provide translations for various challenges on our [online Challenges Library](https://github.com/BentoBoxWorld/weblink/tree/master/challenges/library) on GitHub.

    There is also option to translate parts via locales [file](https://github.com/BentoBoxWorld/Challenges/blob/develop/src/main/resources/locales/en-US.yml#L1248-L1270)

{{ translations(2896, ["lv", "zh-CN", "zh-TW", "cs", "fr", "de", "hu", "pl", "pt", "ru"]) }}

## API

Since Challenges 1.0 and BentoBox 1.17 other plugins can access to the Challenges addon data directly. However, addon requests are still a good solution for a plugins that do not want to use too many dependencies.

### Maven Dependency

Challenges provides an API for other plugins. This covers version 1.1.0 and onwards.

!!! note
    Add the Challenges dependency to your Maven POM.xml:

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
                <artifactId>challenges</artifactId>
                <version>1.1.0</version>
                <scope>provided</scope>
            </dependency>
        </dependencies>
    ```

Use the latest Challenges version.

The JavaDocs for Challenges can be found [here](https://ci.codemc.io/job/BentoBoxWorld/job/Challenges/ws/target/apidocs/index.html).

### Events

Since BentoBox 1.17 API implemented a feature that solved an issue with classloaders. Plugins that wants to use events directly, now can do it.

=== "ChallengeCompletedEvent"
    !!! summary "Description"
        Event that is triggered when player completes a challenge.

        Event is only informative. Cannot be cancelled.

        Link to the class: [ChallengeCompletedEvent](https://github.com/BentoBoxWorld/Challenges/blob/develop/src/main/java/world/bentobox/challenges/events/ChallengeCompletedEvent.java)


    !!! question "Variables"
        - `String challengeId` - id of the challenge that was completed.
        - `UUID user` - id of the player who completed the challenge.
        - `Boolean admin` - indicates if challenge was completed by admin.
        - `Integer completionCount` - count of challenge completion.
        
    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onLevelCompletion(ChallengeCompletedEvent event) {
            UUID user = event.getPlayerUUID();
            String challenge = event.getChallengeID();
            boolean isAdmin = event.isAdmin();
            int count = event.getCompletionCount();
        }
        ``` 

=== "LevelCompletedEvent"
    !!! summary "Description"
        Event that is triggered when player completes a level.

        Event is only informative. Cannot be cancelled.

        Link to the class: [LevelCompletedEvent](https://github.com/BentoBoxWorld/Challenges/blob/develop/src/main/java/world/bentobox/challenges/events/LevelCompletedEvent.java)


    !!! question "Variables"
        - `String levelId` - id of the level that was completed.
        - `UUID user` - id of the player who completed the level.
        - `Boolean admin` - indicates if level was completed by admin.
        
    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onLevelCompletion(LevelCompletedEvent event) {
            UUID user = event.getPlayerUUID();
            String levelId = event.getLevelID();
            boolean isAdmin = event.isAdmin();
        }
        ``` 

=== "ChallengeResetAllEvent"
    !!! summary "Description"
        Event that is triggered when all challenges are reset for player. It includes challenges level data.

        Event is only informative. Cannot be cancelled.

        Link to the class: [ChallengeResetAllEvent](https://github.com/BentoBoxWorld/Challenges/blob/develop/src/main/java/world/bentobox/challenges/events/ChallengeResetAllEvent.java)

    !!! question "Variables"
        - `String worldName` - name of the world where challenges were reset.
        - `UUID playerUUID` - id of the player who was targeted.
        - `Boolean admin` - indicates if reset was done by admin.
        - `String reason` - contains the reason for a reset.

    !!! warning "Constant Values"
        - `reason` - is set to "ISLAND_RESET" if done my player or "RESET_ALL" if done by admin.

    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onLevelCompletion(ChallengeResetAllEvent event) {
            UUID user = event.getPlayerUUID();
            String worldName = event.getWorldName();
            boolean isAdmin = event.isAdmin();
            String reason = event.getReason();
        }
        ``` 

=== "ChallengeResetEvent"
    !!! summary "Description"
        Event that is triggered when challenge is reset by admin.

        Event is only informative. Cannot be cancelled.

        Link to the class: [ChallengeResetEvent](https://github.com/BentoBoxWorld/Challenges/blob/develop/src/main/java/world/bentobox/challenges/events/ChallengeResetEvent.java)

    !!! question "Variables"
        - `String challengeID` - id of the challenge that was reset.
        - `UUID playerUUID` - id of the player who was targeted.
        - `Boolean admin` - indicates if challenge was reset by admin.
        - `String reason` - contains the reason for a reset.

    !!! warning "Constant Values"
        - `admin` -  is set to true. Non-admin reset for single challenge is not implemented yet.
        - `reason` - is set to "RESET".

    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onLevelCompletion(ChallengeResetEvent event) {
            UUID user = event.getPlayerUUID();
            String challengeId = event.getChallengeID();
            boolean isAdmin = event.isAdmin();
            String reason = event.getReason();
        }
        ```

### Addon Request Handlers

Till BentoBox 1.17 we had an issue with accessing data outside BentoBox environment doe to the class loader we used to load addons.
This meant that data was accessible only from other addons. But BentoBox implemented PlAddon functionality, which means that request
handlers are not necessary anymore.

More information about addon request handlers can be found [here](/en/latest/BentoBox/Request-Handler-API---How-plugins-can-get-data-from-addons/)

=== "challenge-list"
    !!! summary "Description"
        Returns a list of all challenges' uniqueIds that are defined in a given world.

    !!! question "Input"
        - `world-name`: String - the name of the world.

    !!! success "Output"
        The output is a `List<String>` containing the list of the uniqueIds of the challenges that are defined for the specified world.

    !!! failure
        This handler will return an empty list if the `world-name` has not been provided or if the `world-name` does not exist or is not a gamemode world.

    !!! example "Code example"
        ```java
        public List<String> getChallenges(String worldName) {
            return (List<String>) new AddonRequestBuilder()
                .addon("Challenges")
                .label("challenge-list")
                .addMetaData("world-name", worldName)
                .request();
        }
        ```

=== "challenge-data"
    !!! summary "Description"
        Returns a `Map<String, Object>` containing all the information about the requested challenge.

    !!! question "Input"
        - `challenge-name`: String - the unique ID of the requested challenge.

    !!! success "Output"
        The output is a `Map<String, Object>` with the following keys:

        - `uniqueId`: String - the unique ID of the requested challenge.
        - `name`: String - the display name for the challenge.
        - `icon`: ItemStack - the item that represents the challenge in GUIs.
        - `levelId`: String - the uniqueId of level for which requested challenge is assinged.
        - `order`: Integer - the order number for the given challenge.
        - `deployed`: Boolean - `true` if the challenge is deployed, `false` otherwise.
        - `description`: List&lt;String&gt; - the description for the challenge.
        - `type`: String - the name of requested challenge type.
        - `repeatable`: Boolean - `true` if the challenge is repeatable, `false` otherwise.
        - `maxTimes`: Integer - the maximal completion count for requested challenge.

    !!! failure
        This handler will return an empty map if the `challengeId` has not been provided or if the `challengeId` could not be found in the database.

    !!! example "Code example"
        ```java
        public Map<String, Object> getChallengeDataMap(String challengeId) {
            return (Map<String, Object>) new AddonRequestBuilder()
                .addon("Challenges")
                .label("challenge-data")
                .addMetaData("challenge-name", challengeId)
                .request();
        }
        ```

=== "level-list"
    !!! summary "Description"
        Returns a list of all levels' uniqueIds that are defined in a given world.

    !!! question "Input"
        - `world-name`: String - the name of the world.

    !!! success "Output"
        The output is a `List<String>` containing the list of the uniqueIds of the levels that are defined for the specified world.

    !!! failure
        This handler will return an empty list if the `world-name` has not been provided or if the `world-name` does not exist or is not a gamemode world.

    !!! example "Code example"
        ```java
        public List<String> getChallengeLevels(String worldName) {
            return (List<String>) new AddonRequestBuilder()
                .addon("Challenges")
                .label("level-list")
                .addMetaData("world-name", worldName)
                .request();
        }
        ```

=== "level-data"
    !!! summary "Description"
        Returns a `Map<String, Object>` containing all the information about the requested level.

    !!! question "Input"
        - `level-name`: String - the unique ID of the requested level.

    !!! success "Output"
        The output is a `Map<String, Object>` with the following keys:

        - `uniqueId`: String - the unique ID of the requested level.
        - `name`: String - the display name for the level.
        - `icon`: ItemStack - the item that represents the level in GUIs.
        - `world`: String - the world name where level operates.
        - `order`: Integer - the order number for the given level.
        - `message`: String - the unlock message for given level.
        - `waiveramount`: Integer - the number of challenges that can be left uncompleted, before unlocking.
        - `challenges`: List&lt;String&gt; - the list of assigned challenges' ids.

    !!! failure
        This handler will return an empty map if the `levelId` has not been provided or if the `levelId` could not be found in the database.

    !!! example "Code example"
        ```java
        public Map<String, Object> getChallengeLevelData(String levelId) {
            return (Map<String, Object>) new AddonRequestBuilder()
                .addon("Challenges")
                .label("level-data")
                .addMetaData("level-name", levelId)
                .request();
        }
        ```

=== "completed-challenges"
    !!! summary "Description"
        Returns a list of completed challenges' uniqueIds that are defined in a given world and completed by given player.

    !!! question "Input"
        - `player`: UUID - the UUID of the player.
        - `world-name`: String - the name of the world.

    !!! success "Output"
        The output is a `Set<String>` containing the set of the uniqueIds of the challenges that are completed by player for the specified world.

    !!! failure
        This handler will return an empty set if the `world-name` has not been provided or if the `world-name` does not exist or is not a gamemode world.
        This handler will return an empty set if the `player` has not been provided or if the `player` does not exist.

    !!! example "Code example"
        ```java
        public List<String> getCompletedChallenges(UUID playerUUID, String worldName) {
            return (List<String>) new AddonRequestBuilder()
                .addon("Challenges")
                .label("completed-challenges")
                .addMetaData("player", playerUUID)
                .addMetaData("world-name", worldName)
                .request();
        }
        ```

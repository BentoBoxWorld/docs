# Challenges

**Challenges** lets your players **complete various customizable challenges and receive rewards**!

Created and maintained by [BONNe](https://github.com/BONNe).

!!! warning
    0.8.0 stores data in a different format that in 0.7.5 and below.
    You will need to migrate data with `/[gamemode_admin] challenges migrate` if you are using older versions.

{{ addon_description("Challenges") }}

## Installation

1. Place the addon jar in the addons folder of the BentoBox plugin
2. Restart the server
3. Run the admin challenges command, e.g., `/bsbadmin challenges` to configure the addon

## Configuration

By default, the challenges addon comes without any challenge or levels. On first runtime only the Admin GUI will be accessible.
Admins can create their own challenges or load a set of default challenges. Default challenges contains 5 levels and 57 challenges.
There also exist a Web Library, where admins can download public challenges. It is accessible via the Admin GUI by clicking on the Web icon.

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
    - `/[admin_command] challenges import [overwrite]`: Ability to import ASkyBlock challenges. Requires challenges.yml file in ./plugins/BentoBox/addons/Challenges/ folder. Parameter overwrite allows to overwrite existing challenges.
    - `/[admin_command] challenges defaults import`: Ability to import Default challenges. This method will not work, if in current world already exist challenges or levels.
    - `/[admin_command] challenges defaults generate`: Ability to export existing challenges. This method will generate defaults.json file in ./plugins/BentoBox/addons/Challenges/ folder.

## Permissions

!!! tip
    `[gamemode]` is a prefix that differs depending on the gamemode you are running.
    The prefix is the lowercased name of the gamemode, i.e. if you are using BSkyBlock, the prefix is `bskyblock`.
    Similarly, if you are using AcidIsland, the prefix is `acidisland`.

Permissions can be found [here](Permissions).

=== "Player permissions"
    - `[gamemode].challenges` - (default: `true`) - Let the player use the '/[player_command] challenges' command.
    - `[gamemode].challenges.multiple` - (default: `true`) - Allows the player complete challenge multiple times at once.
    - `[gamemode].challenges.complete` - (default: `false`) - Let the player use the '/[player_command] challenges complete <challenge> <number>' command.
    - `addon.challenges` - (default: `true`) - Allows the access to '/challenges' command if it is enabled in the config. 

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
    The official way is to add challenge via Admin GUI.
    
    However, there is an option to edit exported database file. It can be done by exporting to file via: `/[admin_command] challenges defaults generate`. To import file you will need to remove all existing challenges. It can be done by clicking on TNT button in Admin GUI. After that you need to import your file via `/[admin_command] challenges defaults import`.

??? question "Reward commands are not working. Why?"
    Most likely reward commands are not working because of incorrect definition. The command does not require `/` symbol before it.
    
    If you want to call command from player perspective, you need to add `[SELF]` before command call, f.e. `[SELF] kill` will result in player calling `/kill` command.

??? question "How to add placeholders in reward commands?"
    Currently, addon do not support placeholders in reward commands. If that is necessary, you can request them in gitHub.
    
    Only placeholder that currently is supported in reward commands is `[player]` which returns player who completed challenge name.

??? question "I do not like order of elements in challenge description. Can I change it?"
    Yes, order of elements are defined in addon settings. It can be easily changed in Admin GUI under settings. Challenges description is under Challenges Lore, while challenges levels are under Levels Lore.

## Translations

!!! info "Translations for challenges"
    The translations do not cover the challenges.
    Each challenge has its own "display name" and "description" which are not localized to keep the configuration process as simple as possible for the end user.  
    You can however find or provide translations for various challenges on our [online Challenges Library](https://github.com/BentoBoxWorld/weblink/tree/master/challenges/library) on GitHub.

{{ translations(2896, ["cs", "de", "es", "fr", "ja", "lv", "ru", "zh-CN", "zh-TW"]) }}

## API

### Addon Request Handlers

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
                .addMetadata("world-name", worldName)
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
                .addMetadata("challenge-name", challengeId)
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
                .addMetadata("world-name", worldName)
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
                .addMetadata("level-name", levelId)
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
                .addMetadata("player", playerUUID)
                .addMetadata("world-name", worldName)
                .request();
        }
        ```
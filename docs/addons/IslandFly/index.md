# IslandFly

**IslandFly** allows players to fly on their island.

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("IslandFly") }}

## Installation

0. Install BentoBox and run it on the server at least once to create its data folders.
1. Place this jar in the addons folder of the BentoBox plugin.
2. Restart the server.
3. The addon will create a data folder and inside the folder will be a config.yml.
4. Stop the server.
5. Edit config.yml how you want.
7. Restart the server.

## Configuration

After addon is successfully installed, it will create config.yml file. Every option in this file comes with comments about them. Please check file for more information.
You can find the latest config file: [config.yml](https://github.com/BentoBoxWorld/IslandFly/blob/develop/src/main/resources/config.yml)

=== "fly-timeout"
    !!! summary "Description"
        How many seconds the addon will wait before disabling fly mode when a player exit his island.

=== "logout-disable-fly"
    !!! summary "Description"
        If the fly mode should be disabled when a player disconnect.

=== "disabled-gamemode"
    !!! summary "Description"
        This list stores GameModes in which islandFly addon should not work. To disable addon it is necessary to write its name in new line that starts with -. 
        
    !!! example "Example"
        ```yaml
            disabled-gamemodes:
            - BSkyBlock
        ```   

=== "allow-command-outside-protection-range"
    !!! summary "Description"
        This allows the player to use the command outside the island protection range.

## Commands

!!! tip
    `[player_command]` and `[admin_command]` are commands that differ depending on the gamemode you are running.
    The Gamemodes' `config.yml` file contains options that allows you to modify these values.
    As an example, on BSkyBlock, the default `[player_command]` is `island`, and the default `[admin_command]` is `bsbadmin`.

=== "Player commands"
    - `/[player_command] fly`: toggles flight on / off.

## Permissions

!!! tip
    `[gamemode]` is a prefix that differs depending on the gamemode you are running.
    The prefix is the lowercased name of the gamemode, i.e. if you are using BSkyBlock, the prefix is `bskyblock`.
    Similarly, if you are using AcidIsland, the prefix is `acidisland`.

=== "Permissions"
    - `[gamemode].island.fly` - (default: `true`) - Allows the player to use '/[player_command] fly' command.
    - `[gamemode].island.flyspawn` - (default: `op`) - Allows the player to fly at spawn island.
    - `[gamemode].island.flybypass` - (default: `op`) - Allows the player to fly on other player islands.

## FAQ

??? question "Can you add a feature X?"
    Please add it to the list [here](https://github.com/BentoBoxWorld/IslandFly/issues).

??? question "I have a bug, where should I report it?"
    Please add it to the list [here](https://github.com/BentoBoxWorld/IslandFly/issues).

## Translations

{{ translations(4728, ["cs", "de", "es", "fr", "ja", "lv", "zh-CN", "hu", "id", "it", "ko", "pl", "pt", "ro", "ru", "tr", "vi"]) }}

# Visit Addon

**Visit** is a simple BentoBox addon that allows visiting other player islands. 
This is an alternative to the Warps addon. 

Created and maintained by [BONNe](https://github.com/BONNe).

{{ addon_description("Visit") }}

## Installation

1. Place the addon jar in the addons folder of the BentoBox plugin
2. Restart the server
3. Run the `/[admincmd] visit` command to configure the addon

## Configuration

A lot of addon settings are exposed in Admin GUI, however, some of them are not.
The latest config options, and their detailed explanations can be found [here](https://github.com/BentoBoxWorld/Visit/blob/develop/src/main/resources/config.yml).

## Commands

!!! tip
    `[player_command]` and `[admin_command]` are commands that differ depending on the gamemode you are running.
    The Gamemodes' `config.yml` file contains options that allows you to modify these values.
    As an example, on BSkyBlock, the default `[player_command]` is `island`, and the default `[admin_command]` is `bsbadmin`.
    Be aware, that this addon allows changing player commands aliases in addon `config.yml` file. 

=== "Player commands"
    - `/[player_command] visit <player>`: opens GUI or visits targeted player island.
    - `/[player_command] visit configure`: opens GUI that allows to manage visiting settings.
    - `/[player_command] visit setlocation`: allows to change visitor spawn location.

=== "Admin commands"
    - `/[admin_command] visit <player>`: opens GUI that allows editing addon settings and configure island data.

## Permissions

!!! tip
    `[gamemode]` is a prefix that differs depending on the gamemode you are running.
    The prefix is the lowercased name of the gamemode, i.e. if you are using BSkyBlock, the prefix is `bskyblock`.
    Similarly, if you are using AcidIsland, the prefix is `acidisland`.

=== "Player permissions"
    - `[gamemode].visit` - Let the player use the '/[player_command] visit' command.
    - `[gamemode].visit.configure` - Let the player use the '/[admin_command] visit configure' command.
    - `[gamemode].visit.setlocation` - Let the player use the '/[admin_command] visit setlocation' command.
    - `visit.icon.[material]` - Allows changing icon for a player owned island in Visit GUI.

=== "Admin permissions"
    - `[gamemode].admin.visit` - Let the player use the '/[admin_command] visit' command and its subcommands.
    
??? question "Something is missing?"
    You can find the comprehensive list of permissions in the [addon.yml](https://github.com/BentoBoxWorld/Visit/blob/develop/src/main/resources/addon.yml) file of this addon.  
    If something is indeed missing from the list below, please let us know!
   
## Flags

Addon introduces 2 BentoBox protection flags:

- ![pumpkin_pie](https://static.wikia.nocookie.net/minecraft_gamepedia/images/a/ac/Pumpkin_Pie_JE2_BE2.png){: loading=lazy width=16px } ALLOW_VISITS_FLAG: flag in island settings that allows enabling/disabling island visiting.
- ![pumpkin](https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/fc/Pumpkin_JE2_BE2.png){: loading=lazy width=16px } VISIT_CONFIG_PERMISSION: flag in island permissions that allows changing which member group can change island visit settings.

## FAQ

??? question "Can you add a feature X?"
    Please add it to the list [here](https://github.com/BentoBoxWorld/Visit/issues).

## Translations

{{ translations(5740, ["cs", "es", "de", "hu", "ja", "lv", "pl", "tr", "zh-CN"]) }}

## Api
### Events

This addon introduces a new event: [VisitEvent](https://github.com/BentoBoxWorld/Visit/blob/develop/src/main/java/world/bentobox/visit/events/VisitEvent.java)

This event is triggered before processing teleportation and it can be cancelled. 

# Border

**Border** shows a world border around islands. The world border is the Minecraft world border and players cannot go outside of it.

Created and maintained by [tastybento](https://github.com/tastybento).

!!! warning "Requirements"
    This addon requires [WorldBorderPlugin](https://github.com/yannicklamprecht/WorldBorderAPI/releases) from **WorldBorderAPI**.  
    Make sure you downloaded the plugin and put it in your server's `plugins` folder.

{{ addon_useful_links }}

## Installation

1. Put the WorldBorderPlugin jar into the `plugins` folder.
2. Put the addon jar into the `plugins/BentoBox/addons` folder.
3. Restart the server.

## Commands

!!! tip
    `[player_command]` is a command that differs depending on the gamemode you are running.
    The Gamemodes' `config.yml` file contains options that allows you to modify this value.
    As an example, on BSkyBlock, the default `[player_command]` is `island`.

- `/[player_command] border`: toggles whether the border is shown or not.

## Permissions

!!! tip
    `[gamemode]` is a prefix that differs depending on the gamemode you are running.
    The prefix is the lowercased name of the gamemode, i.e. if you are using BSkyBlock, the prefix is `bskyblock`.
    Similarly, if you are using AcidIsland, the prefix is `acidisland`.

- `[gamemode].border.toggle` (default: *unknown*): enables/disables the use of the command.

## Translations

{{ translations(3896, ["cs", "it", "lv"]) }}

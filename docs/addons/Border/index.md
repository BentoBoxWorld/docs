# Border

**Border** shows a world border around islands. The world border is the Minecraft world border and players cannot go outside of it or a barrier block border that can show up when required.

Created and maintained by [tastybento](https://github.com/tastybento).

!!! warning "Requirements"
    This addon requires [WorldBorderPlugin](https://github.com/yannicklamprecht/WorldBorderAPI/releases) from **WorldBorderAPI**.  
    Make sure you downloaded the plugin and put it in your server's `plugins` folder.

{{ addon_description("Border") }}

## Installation

1. Put the WorldBorderPlugin jar into the `plugins` folder if you want the vanilla world border.
2. Put the addon jar into the `plugins/BentoBox/addons` folder.
3. Restart the server.
4. Edit the config.yml (Optional)
5. Restart the server to take the new settings

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

- `[gamemode].border.toggle` (default: Op): enables/disables the use of the command.

## Configuration

The config.yml file contains a number of options.

### Disabled GameModes
By default, Border will operate in all game mode worlds on the BentoBox server. To disable a game mode it is necessary to write its name on new line that starts with -. Example:
```
 disabled-gamemodes:
   - BSkyBlock
```

### Use WorldBorderAPI (WBAPI)
If you want to use the vanilla world border then you must download the WorldBorderAPI plugin. You can find them here: https://github.com/yannicklamprecht/WorldBorderAPI/releases

Players cannot exit past the vanilla world border, so it will completely block movement outside of a player's protected island area. If you do not want this, then do not use WBAPI.

To activate/deactivate WBAPI, set this to true/false in the config.yml:

```
use-wbapi: true
```

### Use barrier blocks.
This only applies if you are not using WBAPI.

If true, the the border will use barrier blocks to prevent most players from exiting the border. If players do manage to exit it, they will get teleported back inside it. 

If false, the border is indicated by particles only.

The default is to use barrier blocks.

```
use-barrier-blocks: true
```

### Default border behavior
Players can turn the border on and off if they have the right permission using the border command. This setting makes the default on or off:

``` 
show-by-default: true
```

### Show max-protection range border.

This only applies if you are not using WBAPI.

This is a visual border only and not a barrier. It displays the 🚫 particle. This is useful for game modes like Boxed where the player's protection area can move around.

```
show-max-border: true
```

## Translations

{{ translations(3896, ["cs", "it", "lv"]) }}

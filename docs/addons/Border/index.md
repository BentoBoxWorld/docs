# Border

**Border** can create and show a border around islands which players cannot pass.  
The border can be:

- the vanilla world border (using [**WorldBorderAPI**](https://github.com/yannicklamprecht/WorldBorderAPI/releases) plugin)
- a custom border that shows up when the player is near (visuals can be configured).

Created and maintained by [tastybento](https://github.com/tastybento).

!!! warning "Dependencies"
    This addon is configured by default to use the **WorldBorderAPI** to show the border, 
    **but it can be turned off**, see the `use-wbapi` setting.

{{ addon_description("Border") }}

## Installation

1. Restart the server (to enable the addon and have the `config.yml` file generated)
2. If you want to enable the vanilla border type, put the WorldBorderPlugin jar into the `plugins` folder and make sure to set `use-wbapi: true` in `config.yml`. Otherwise, set `use-wbapi: false` in the configuration.
3. Put the addon jar into the `plugins/BentoBox/addons` folder
4. Customize settings in `config.yml` (optional)
5. Restart the server to apply new settings

## Commands

!!! tip
    `[player_command]` is a command that differs depending on the gamemode you are running.
    The Gamemodes' `config.yml` file contains settings that allows you to modify this value.
    As an example, on BSkyBlock, the default `[player_command]` is `island`.

### border
**Command**: `/[player command] border`  
**Description**: Turns the border on/off.  
**Permission**: `[gamemode].border.toggle`. Default: `op`.  
**Notes**: Since Version 3.0.0 it requires a permission.  

### border type {...}
**Command**: `/[player command] border type {barrier | vanilla}`  
**Description**: Sets the border type.  
**Permission**: `[gamemode].border.set-type`. Default: `true`.  
**Example**: `/[player command] border type barrier`  

!!! tip
    `[gamemode]` is a prefix that differs depending on the gamemode you are running.
    The prefix is the lowercased name of the gamemode, i.e. if you are using BSkyBlock, the prefix is `bskyblock`.
    Similarly, if you are using AcidIsland, the prefix is `acidisland`.

## Configuration

The `config.yml` file contains settings.  
The default value is usually the example value unless explicitly stated.

### Disable game modes
You can disable the addon with this setting.  
By default, Border will operate in all game mode worlds on the BentoBox server.

You can disable a game mode by writing its name on a new line that starts with `-`.  
Example to disable BSkyBlock:

```yml
disabled-gamemodes:
  - BSkyBlock
```

Default value:

```yml
disabled-gamemodes: []
```

### Use WorldBorderAPI (WBAPI)
Enables or disables the usage of **WorldBorderAPI**.  
If you want to use it then download and enable the [WorldBorderAPI plugin](https://github.com/yannicklamprecht/WorldBorderAPI/releases).

Set it to `true` to enable (and require) the WBAPI integration.

```yml
use-wbapi: true
```

### Return teleport
Controls whether if players somehow manage to pass through the border (e.g. teleport in the same world), should they be teleported back to their islands.

Set to `true` if you want players to be teleported back.

**Warning**: If you set this value to `false` along with having `use-barrier-blocks` as `false`, players will be able to just simply walk through the border.

```yml
return-teleport: true
```

!!! tip
    If you want to use this addon **only to show** the borders for the players, use the following settings:
    ```yml
    use-barrier-blocks: false
    return-teleport: false
    ```

### Use barrier blocks.
Only applies for players who are **not** using the vanilla border type.

- `true`: the border will be made of barrier blocks.  
- `false`: there will be no barrier block-based border. This means it is up to the `return-teleport` setting whether players are teleported back when leaving the island.

```yml
use-barrier-blocks: true
```

### Default border behavior
Players can turn the border on and off with a command if they have the right permission.  
This setting makes the default on or off; set it to `true` to have it on by default.

```yml
show-by-default: true
```

### Show max-protection range border.
Only applies for players who are **not** using the vanilla border type.

Set to `true` to show barrier (🚫) particles shown at the max protection range.  
This is useful for game modes like Boxed where the player's protection area can move around.

Note that these are **not barrier blocks** but _particles_, so the "air" just _looks like_ them.

```yml
show-max-border: true
``` 

### Show particles
Enables/disables all types of wall particles shown by the addon (border and max-protection range particles).

Set to `false` if you don't want **any** wall particles to be shown.

```
show-particles: true
```

## Translations

{{ translations(3896, ["cs", "it", "lv", "fr", "de", "hu", "id", "zh-TW", "ko", "pl", "ru", "es", "vi", "zh-CN", "hr", "ja", "pt", "ro", "tr", "uk"]) }}

## Source
Want to contribute? See this documentation's source code at [GitHub](https://github.com/BentoBoxWorld/docs/blob/master/docs/addons/Border/).

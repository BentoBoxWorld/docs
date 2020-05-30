# IslandFly

**IslandFly** allows players to fly on their island.

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("IslandFly") }}

## Installation

1. Place the .jar in the addons folder of the BentoBox plugin
2. Restart the server
3. The addon will create a data folder and inside the folder will be a config.yml
4. Edit the config.yml if required
5. Restart the server if you make a change

## Config.yml

There are only three options in the config:

**fly-timeout**
How many seconds the addon will wait before disabling fly mode when a player exit his island.

**logout-disable-fly**
If the fly mode should be disabled when a player disconnect.

**disabled-gamemode**
This list stores GameModes in which islandFly addon should not work. To disable addon it is necessary to write its name in new line that starts with -. 

Example:
```
 disabled-gamemodes:
 - BSkyBlock
```

## Commands
**/is fly** - This command toggles flight **On** and **Off**

## Permissions
**[gamemode].island.fly** - For usage of flight command

Example:
    **bskyblock.island.fly**

**[gamemode].island.flybypass** - Enables user to use fly command on other islands too


Example:
**caveblock.island.flybypass**

## Translations

{{ translations(4728, ["cs", "de", "es", "fr", "ja", "lv", "zh-CN", "hu", "id", "it", "ko", "pl", "pt", "ro", "ru", "tr", "vi"]) }}

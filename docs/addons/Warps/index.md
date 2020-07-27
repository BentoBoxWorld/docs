# Warps

**Warps** enables players to add a personal warp signs to their island.

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("Warps") }}

## Installation

1. Place the Warps addon jar in the addons folder of the BentoBox plugin
2. Restart the server
3. The addon will create a data folder and inside the folder will be a config.yml
4. Edit the config.yml how you want.
5. Restart the server if you make a change

## Commands

* warp <player> - warp to the player's warp sign. Tab complete will find the name after the first letter.
* warps - open the warp sign panel.


## Setup - Config.yml

### Warp Restriction

This limits warp sign creation to players who have at least a certain level of island. It requires the Level addon
and the default level is 10.

### Welcome text
This is the text that player must put on sign to make it a warp sign, e.g., [Welcome]. It is not case sensitive!

### Warps GUI icons
The default is to use SIGN. SIGN counts for any kind of sign and the type of wood used will be reflected in the panel
if the server supports it.
It is possible to use 'PLAYER_HEAD', which if you have BentoBox 1.14.1 or later, should work lag-free.

### Disabled Game Modes
This list stores GameModes in which Level addon should not work.
To disable addon it is necessary to write its name in new line that starts with -. Example:
```
  disabled-gamemodes:
   - BSkyBlock
```

### Warp panel name formatting.
Example: &c will make names red, &f is white

### Warp panel default lore formatting.
Example: &c will make lore red. &f is white

### Random teleport
This adds a button to the warp panel that goes to a random warp sign

### Allow use in other worlds.
This enables warp signs to be placed in *any* world, even non-BentoBox worlds. Players must have the `welcomewarpsigns.warp` permission to use.

### Warp and warps commands.
You can change them if they clash with other addons or plugins.


## Permissions

Usage permissions are (put the gamemode name, e.g. acidisland at the front):

```
   [gamemode].island.warp:
    description: Player can use warp or warps commands
    default: true
  [gamemode].island.addwarp:
    description: Player can create a welcome warp sign
    default: true

```

Permissions are also listed [here](Permissions).

## Translations

{{ translations(2973, ["cs", "de", "es", "fr", "hu", "ja", "lv", "pl", "tr", "zh-CN"]) }}


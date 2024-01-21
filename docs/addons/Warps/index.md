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

## Configuration

### config.yml

After addon is successfully installed, it will create config.yml file. Every option in this file comes with comments about them. Please check file for more information.
You can find the latest config file: [config.yml](https://github.com/BentoBoxWorld/Warps/blob/develop/src/main/resources/config.yml)

??? question "What is warp restriction?"
    This limits warp sign creation to players who have at least a certain level of island. It requires the Level addon
    and the default level is 10.

??? question "What is welcome text"
    This is the text that player must put on sign to make it a warp sign, e.g., [Welcome]. It is not case sensitive!
    
    This text must be in the top line.

??? question "What is disabled GameModes?"
    This list stores GameModes in which Warps addon should not work.

    To disable addon it is necessary to write its name in new line that starts with -. Example:
    ```
      disabled-gamemodes:
       - BSkyBlock
    ```

??? question "What is lore format?"
    Lore format allows changing default color for description lines in sign. Description lines are used in GUI. 

    Description lines contains sign lines that are bellow [welcome] text.

??? question "What is doing allow in other worlds?"
    This enables warp signs to be placed in *any* world, even non-BentoBox worlds. 

    Players must have the `welcomewarpsigns.warp` permission to use.

??? question "What is warp and warps?"
    The command `warp` requires `<player>` to which warp should happen, while `warps` opens menu that allows to choose a player.

    If you have enabled `allow in other worlds` then it will be as a main command `/warp`
    
    While for each BentoBox GameMode it still will be `/[player_cmd] warp`
    

### Customizable GUI's

BentoBox 1.17 API introduced a function that allows to implement customizable GUI's. This addon is one of the first one which uses this functionality. We tried to be as simple as possible for customization, however, some features requires explanation.
You can find more information how BentoBox custom GUI's works here: [Custom GUI's](/en/latest/Tutorials/generic/Customizable-GUI/)

??? question "How can I customize GUI's"
    To customize Addon GUI's you need to have version 1.12. This is a first version that has implemented them. Addon will create a new directory under `/plugins/BentoBox/addons/Warps` with a name `panels`

??? question "What does `PREVIOUS`|`NEXT` button type?"
    The PREVIOUS and NEXT button types allows creating automatic paging, when you have more islands than spaces in GUI.
    These types have extra parameters under data:
 
    - `indexing` - indicates if button will show page number.

    Example: 
    ```yaml
        icon: tipped_arrow{CustomPotionColor:11546150}
        title: warps.gui.buttons.previous.name
        description: warps.gui.buttons.previous.description
        data:
          type: PREVIOUS
          indexing: true
        action:
          left:
            action: PREVIOUS
            tooltip: warps.gui.tips.click-to-previous
    ```

??? question "What is `RANDOM` button type?"
    This button allows players teleporting to a random warp.
    It is available only if there are more than 1 warp.

    Example: 
    ```yaml
        icon: DROPPER
        title: warps.gui.buttons.random.name
        description: warps.gui.buttons.random.description
        data:
          type: RANDOM
        actions:
          warp:
            click-type: left
            tooltip: warps.gui.tips.click-to-warp
    ```

??? question "What is `WARP` button type?"
    The WARP button creates a dynamic entry for a warp object.

    Specifying title, description and icon will overwrite dynammic generation based on sign and database data. By default these values will be generated from database entries.
    
    Icon PLAYER_HEAD will be replaced with owner player head. However, currently there is no option to specify differnet player head.

    Example: 
    ```yaml
        warp_button:
          icon: PLAYER_HEAD
          title: warps.gui.buttons.warp.name
          description: warps.gui.buttons.warp.description
          data:
            type: WARP
          actions:
            warp:
              click-type: left
              tooltip: warps.gui.tips.click-to-warp
    ```


## Commands

!!! tip
    `[player_command]` is command that differ depending on the gamemode you are running.
    The Gamemodes' `config.yml` file contains options that allows you to modify these values.
    As an example, on BSkyBlock, the default `[player_command]` is `island`.
    Be aware, that this addon allows changing player commands aliases in addon `config.yml` file. 

=== "Player commands"
    - `/[player_command] warp <player>`: warps player to targeted sign.
    - `/[player_command] warps`: opens GUI that allows to view all available warp signs.

## Permissions

!!! tip
    `[gamemode]` is a prefix that differs depending on the gamemode you are running.
    The prefix is the lowercased name of the gamemode, i.e. if you are using BSkyBlock, the prefix is `bskyblock`.
    Similarly, if you are using AcidIsland, the prefix is `acidisland`.

=== "Player permissions"
    - `[gamemode].island.warp` - Player can use `/[player_command] warp` and `/[player_command] warps` commands. Enabled by default.
    - `[gamemode].island.addwarp` - Players can create warp signs. Enabled by default.
    - `welcomewarpsigns.warp` - Player can use `/warp` and `/warps` commands. Disabled by default. Requires `allow-in-other-worlds`.
    - `welcomewarpsigns.addwarp` - Players can create warp signs. Disabled by default. Requires `allow-in-other-worlds`.
 
??? question "Something is missing?"
    You can find the comprehensive list of permissions in the [addon.yml](https://github.com/BentoBoxWorld/Warps/blob/develop/src/main/resources/addon.yml) file of this addon.  
    If something is indeed missing from the list below, please let us know!

## FAQ

??? question "Can you add a feature X?"
    Please add it to the list [here](https://github.com/BentoBoxWorld/Warps/issues).

??? question "I have a bug, where should I report it?"
    Please add it to the list [here](https://github.com/BentoBoxWorld/Warps/issues).

## Translations

{{ translations(2973, ["cs", "de", "es", "fr", "hu", "ja", "lv", "pl", "tr", "zh-CN", "zh-TW", "id", "it", "ru", "vi", "uk"]) }}

## Api

### Events

Since BentoBox 1.17 API implemented a feature that solved an issue with classloaders. Plugins that wants to use events directly, now can do it.

You just need to add Visit to your project as dependency. You can use Maven for that:

```xml
<dependency>
    <groupId>world.bentobox</groupId>
    <artifactId>warps</artifactId>
    <version>1.11.2</version>
    <scope>provided</scope>
</dependency>
```

=== "WarpInitiateEvent"
    !!! summary "Description"
        Event that is triggered after player created a new warp sign.

        Link to the class: [WarpInitiateEvent](https://github.com/BentoBoxWorld/Warps/blob/develop/src/main/java/world/bentobox/warps/event/WarpInitiateEvent.java)

    !!! question "Variables"
        - `UUID player` - id of the player who creates warp sign.
        - `Location warpLoc` - the location of warp sign.
 
    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onWarpInitiate(WarpInitiateEvent event) {
            UUID player = event.getPlayer();
            Location warpLoc = event.getWarpLoc();
        }
        ```

=== "WarpRemoveEvent"
    !!! summary "Description"
        Event that is triggered after player created a new warp sign.

        Link to the class: [WarpRemoveEvent](https://github.com/BentoBoxWorld/Warps/blob/develop/src/main/java/world/bentobox/warps/event/WarpRemoveEvent.java)

    !!! question "Variables"
        - `UUID owner` - id of the player who owns warp sign.
        - `UUID remover` - id of the player who removes warp sign.
        - `Location warpLoc` - the location of warp sign.
 
    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onWarpRemove(WarpRemoveEvent event) {
            UUID owner = event.getOwner();
            UUID remover = event.getRemover();
            Location warpLoc = event.getWarpLocation();
        }
        ```
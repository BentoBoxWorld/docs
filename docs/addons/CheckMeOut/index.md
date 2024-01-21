# CheckMeOut

This is an island submission addon. This addon enables players to submit their island for consideration by admins. In this way, Admins can set up site-wide challenges or competitions that players can do and then submit their island for consideration. Admins get a GUI that lists submissions and they can teleport to the islands from there. Once an island is reviewed by admins it can be deleted, or when the whole activity is over, all submissions can be cleared.

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("CheckMeOut") }}


## Installation

0. Install BentoBox and run it on the server at least once to create its data folders.
1. Place this jar in the addons folder of the BentoBox plugin.
2. Restart the server.
3. The addon will create a data folder and inside the folder will be a config.yml.
4. Stop the server.
5. Edit config.yml how you want.
7. Restart the server.

## Configuration

The main `config.yml` file contains basic information about game-mode addon setup.

`panels` allows to customize some user accessible panels.


### config.yml

After addon is successfully installed, it will create config.yml file. Every option in this file comes with comments about them. Please check file for more information.
You can find the latest config file: [config.yml](https://github.com/BentoBoxWorld/CheckMeOut/blob/develop/src/main/resources/config.yml)

### Customizable GUI's

BentoBox 1.17 API introduced a function that allows to implement customizable GUI's. This addon is one of the first one which uses this functionality. We tried to be as simple as possible for customization, however, some features requires explanation.
You can find more information how BentoBox custom GUI's works here: [Custom GUI's](/en/latest/Tutorials/generic/Customizable-GUI/)

??? question "How can I customize GUI's"
    To customize Addon GUI's you need to have version 1.1. This is a first version that has implemented them. Addon will create a new directory under `/plugins/BentoBox/addons/CheckMeOut` with a name `panels`

    Currently you can customize 1 GUI:

    - Main Panel: `view_panel` - panel that contains submitted islands.

??? question "What does `PREVIOUS`|`NEXT` button type?"
    The PREVIOUS and NEXT button types allows creating automatic paging, when you have more islands than spaces in GUI.
    These types have extra parameters under data:

    - `indexing` - indicates if button will show page number.

    Example: 
    ```yaml
        icon: tipped_arrow{CustomPotionColor:11546150}
        title: checkmeout.gui.buttons.previous.name
        description: checkmeout.gui.buttons.previous.description
        data:
          type: PREVIOUS
          indexing: true
        action:
          left:
            action: PREVIOUS
            tooltip: checkmeout.gui.tips.click-to-previous
    ```

??? question "What is `RANDOM` button type?"
    This button allows players teleporting view a random submission.
    
    - warp action is available only if you have installed Warps addon and player has existing warps sign.
    - visit action is available only if you have installed Visits addon.
    - check action is a default addon teleportation mekanism.

    Example: 
    ```yaml
        icon: DROPPER
        title: checkmeout.gui.buttons.random.name
        description: checkmeout.gui.buttons.random.description
        data:
          type: RANDOM
        actions:
          # Warp action requires WARP addon. If warp addon is not present, warp action will not work.
          warp:
            click-type: UNKNOWN
            tooltip: checkmeout.gui.tips.click-to-warp
          # Visit action requires Visit addon. If Visit addon is not present, visit action will not work.
          visit:
            click-type: UNKNOWN
            tooltip: checkmeout.gui.tips.click-to-visit
          # Check action requires player to have "[gamemode].checkmeout.admin.check" permission.
          check:
            click-type: UNKNOWN
            tooltip: checkmeout.gui.tips.click-to-check
    ```

??? question "What is `ISLAND` button type?"
    This button is available in main panel.
    The ISLAND button creates a dynamic entry for an island object.

    Specifying title, description and icon will overwrite dynammic generation based on database data. By default these values will be generated from database entries.
    This button supports 3 different action types:

    - warp action is available only if you have installed Warps addon and player has existing warps sign.
    - visit action is available only if you have installed Visits addon.
    - check action is a default addon teleportation mekanism.

    Example: 
    ```yaml
      # icon: PLAYER_HEAD
      title: checkmeout.gui.buttons.island.name
      description: checkmeout.gui.buttons.island.description
      data:
        type: ISLAND
      actions:
        # Warp action requires WARP addon. If warp addon is not present, warp action will not work.
        warp:
          # Click type UNKNOWN means that it accept any click type.
          click-type: UNKNOWN
          tooltip: checkmeout.gui.tips.click-to-warp
        # Visit action requires Visit addon. If Visit addon is not present, visit action will not work.
        visit:
          # Click type UNKNOWN means that it accept any click type.
          click-type: UNKNOWN
          tooltip: checkmeout.gui.tips.click-to-visit
        # Check action requires player to have "[gamemode].checkmeout.admin.check" permission.
        check:
          # Click type UNKNOWN means that it accept any click type.
          click-type: UNKNOWN
          tooltip: checkmeout.gui.tips.click-to-check
    ```

## Commands

!!! tip
    `[player_command]` and `[admin_command]` are commands that differ depending on the gamemode you are running.
    The Gamemodes' `config.yml` file contains options that allows you to modify these values.
    As an example, on BSkyBlock, the default `[player_command]` is `island`, and the default `[admin_command]` is `bsbadmin`.
    Be aware, that this addon allows changing player commands aliases in addon `config.yml` file. 

=== "Player commands"
    - `/[player_command] checkmeout`: submits island for reviewing.
    - `/[player_command] checkmeout view`: opens GUI that allows to view other submitted islands.

=== "Admin commands"
    - `/[admin_command] checkmeout`: main admin command.
    - `/[admin_command] checkmeout check <player>`: teleports player to a submitted island.
    - `/[admin_command] checkmeout clearall`: removes all submitted islands.
    - `/[admin_command] checkmeout delete <player>`: removes <player> submitted island.
    - `/[admin_command] checkmeout seesubs`: opens a menu to view all submitted islands.


## Permissions

!!! tip
    `[gamemode]` is a prefix that differs depending on the gamemode you are running.
    The prefix is the lowercased name of the gamemode, i.e. if you are using BSkyBlock, the prefix is `bskyblock`.
    Similarly, if you are using AcidIsland, the prefix is `acidisland`.

=== "Player permissions"
    - `[gamemode].checkmeout` - Let the player use the '/[player_command] checkmeout' command to submit island. By default, true.
    - `[gamemode].checkmeout.view` - Let the player use the '/[admin_command] checkmeout view' command to view all submitted islands. By default, true.
    - `checkmeout.icon.[material]` - Allows changing icon for a player owned island in View GUI. By default, false.

=== "Admin permissions"
    - `[gamemode].checkmeout.admin.check` - Let the player use the '/[admin_command] checkmeout check' command. By default, OP.
    - `[gamemode].checkmeout.admin.delete` - Let the player use the '/[admin_command] checkmeout delete' command. By default, OP.
    - `[gamemode].checkmeout.admin.clearsubmissions` - Let the player use the '/[admin_command] checkmeout clearall' command. By default, OP.
    - `[gamemode].checkmeout.admin.seesubs` - Let the player use the '/[admin_command] checkmeout seesubs' command. By default, OP.
    
??? question "Something is missing?"
    You can find the comprehensive list of permissions in the [addon.yml](https://github.com/BentoBoxWorld/Visit/blob/develop/src/main/resources/addon.yml) file of this addon.  
    If something is indeed missing from the list below, please let us know!

## FAQ

??? question "Can you add a feature X?"
    Please add it to the list [here](https://github.com/BentoBoxWorld/CheckMeOut/issues).

## Api

### Events

Since BentoBox 1.17 API implemented a feature that solved an issue with classloaders. Plugins that wants to use events directly, now can do it.

You just need to add CheckMeOut to your project as dependency. You can use Maven for that:

```xml
<dependency>
    <groupId>world.bentobox</groupId>
    <artifactId>checkmeout</artifactId>
    <version>1.1.0</version>
    <scope>provided</scope>
</dependency>
```

=== "IslandSubmittedEvent"
    !!! summary "Description"
        Event that is triggered after player submitted his island for reviewing.

        Link to the class: [IslandSubmittedEvent](https://github.com/BentoBoxWorld/CheckMeOut/blob/develop/src/main/java/world/bentobox/checkmeout/events/IslandSubmittedEvent.java)

    !!! question "Variables"
        - `UUID uuid` - id of the player who submitted island.
        - `Location location` - the location of sumbission.
 
    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onSubmittion(IslandSubmittedEvent event) {
            UUID player = event.getUUID();
            Location location = event.getLocation();
        }
        ```

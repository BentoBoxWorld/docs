# Visit Addon

**Visit** is a simple BentoBox addon that allows visiting other player islands. 
This is an alternative to the Warps addon. 

Created and maintained by [BONNe](https://github.com/BONNe).

{{ addon_description("Visit") }}

## Installation

1. Place the addon jar in the addons folder of the BentoBox plugin
2. Restart the server
3. Run the `/[admin_cmd] visit` command to configure the addon

## Configuration

A lot of addon settings are exposed in Admin GUI, however, some of them are not. 
Changing command labels requires for server restart.

### config.yml

After addon is successfully installed, it will create config.yml file. Every option in this file comes with comments about them. Please check file for more information.
You can find the latest config file: [config.yml](https://github.com/BentoBoxWorld/Visit/blob/develop/src/main/resources/config.yml)

### Customizable GUI's

BentoBox 1.17 API introduced a function that allows to implement customizable GUI's. This addon is one of the first one which uses this functionality. We tried to be as simple as possible for customization, however, some features requires explanation.
You can find more information how BentoBox custom GUI's works here: [Custom GUI's](/en/latest/Tutorials/generic/Customizable-GUI/)

??? question "How can I customize GUI's"
    To customize Addon GUI's you need to have version 1.5. This is a first version that has implemented them. Addon will create a new directory under `/plugins/BentoBox/addons/Visit` with a name `panels`

    Currently you can customize 2 GUI's:

    - Main Panel: `main_panel` - panel that contains all islands.
    - Manage Panel: `manage_panel` - panel that contains some configuration options.

    Each GUI contains functions that is supported only by itself.

??? question "What does `PREVIOUS`|`NEXT` button type?"
    The PREVIOUS and NEXT button types allows creating automatic paging, when you have more islands than spaces in GUI.
    These types have extra parameters under data:
 
    - `indexing` - indicates if button will show page number.

    Example: 
    ```yaml
        icon: tipped_arrow{CustomPotionColor:11546150}
        title: visit.gui.buttons.previous.name
        description: visit.gui.buttons.previous.description
        data:
          type: PREVIOUS
          indexing: true
        action:
          left:
            action: PREVIOUS
            tooltip: visit.gui.tips.click-to-previous
    ```

??? question "What is `SEARCH` button type?"
    This button is available in main panel.
    It creates a button that allows to search for a specific island.

    Example: 
    ```yaml
        icon: PAPER
        title: visit.gui.buttons.search.name
        # Deccription is generated dynamically. However, you can set it manualy.
        # description: visit.gui.buttons.search.description
        data:
          type: SEARCH
        actions:
          left:
            type: INPUT
            tooltip: visit.gui.tips.left-click-to-edit
          right:
            type: CLEAR
            tooltip: visit.gui.tips.right-click-to-clear
    ```

??? question "What is `FILTER` button type?"
    This button is available in main panel.
    It creates a button that allows to filter islands by some property.

    Example: 
    ```yaml
        # Icon is generated dynamically. However, you can set it manualy.
        # icon: SANDSTONE
        title: visit.gui.buttons.filter.name
        # Deccription is generated dynamically. However, you can set it manualy.
        # description: visit.gui.buttons.filter.description
        data:
          type: FILTER
        actions:
          left:
            type: UP
            tooltip: visit.gui.tips.left-click-to-cycle
          right:
            type: DOWN
            tooltip: visit.gui.tips.right-click-to-cycle
    ```

??? question "What is `ISLAND` button type?"
    This button is available in main panel.
    The ISLAND button creates a dynamic entry for an island object.

    Specifying title, description and icon will overwrite dynammic generation based on database data. By default these values will be generated from database entries.
    This button supports 3 different action types:

    - `VISIT` type allows player to visit island
    - `CONFIRM` type allows player to confirm visiting if ask-payment-confirmation is enabled in config.  
    - `CANCEL` type allows player to cancel visiting if ask-payment-confirmation is enabled in config. 

    Example: 
    ```yaml
      # Data is generated dynamicaly. However, setting them will overwrite it.
      # icon: PLAYER_HEAD
      # title: visit.gui.buttons.island.name
      # description: visit.gui.buttons.island.description
      data:
        type: ISLAND
      actions:
        - click-type: left
          type: VISIT
          tooltip: visit.gui.tips.click-to-visit
        - click-type: left
          type: CONFIRM
          tooltip: visit.gui.tips.left-click-to-confirm
        - click-type: right
          type: CANCEL
          tooltip: visit.gui.tips.right-click-to-cancel
    ```

??? question "What is `PAYMENT` button type?"
    This button is available in manage panel.
    It creates a button that allows to set payment value for visiting player island.

    Example: 
    ```yaml
        icon: ANVIL
        title: visit.gui.buttons.payment.name
        # Deccription is generated dynamically. However, you can set it manualy.
        # description: visit.gui.buttons.payment.description
        data:
          type: PAYMENT
        actions:
          left:
            type: CHANGE
            tooltip: visit.gui.tips.click-to-change
    ```

??? question "What is `OFFLINE` button type?"
    This button is available in manage panel.
    It creates a button that allows to set if players can visit island while none of island members is online.

    Example: 
    ```yaml
        icon: REDSTONE_LAMP
        title: visit.gui.buttons.offline.name
        # Deccription is generated dynamically. However, you can set it manualy.
        # description: visit.gui.buttons.offline.description
        data:
          type: OFFLINE
        actions:
          left:
            type: TOGGLE
            tooltip: visit.gui.tips.click-to-toggle
    ```

??? question "What is `ALLOWED` button type?"
    This button is available in manage panel.
    It creates a button that allows to disable visiting with one click. This is the shortcut for changing flag `ALLOW_VISITS_FLAG` value via settings.

    Example: 
    ```yaml
        icon: PUMPKIN_PIE
        title: visit.gui.buttons.enabled.name
        # description: visit.gui.buttons.enabled.description
        data:
          type: ALLOWED
        actions:
          left:
            type: TOGGLE
            tooltip: visit.gui.tips.click-to-toggle
    ```

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
- ![paper](https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f2/Paper_JE2_BE2.png){: loading=lazy width=16px } RECEIVE_VISIT_MESSAGE_FLAG: flag in island settings that allows enabling/disabling island members to receive visiting/leaving messages.


## FAQ

??? question "Can you add a feature X?"
    Please add it to the list [here](https://github.com/BentoBoxWorld/Visit/issues).

??? question "Can players change a spot where visitors are teleported?"
    Yes, players can set it with command: `/[player_cmd] visit setlocation` command. However, be aware, that visitors will not be teleported in "dangerous" spots, and if location is not safe, they will be teleported to a safer location.

??? question "Can admins change a spot where visitors are teleported?"
    Yes, admins can set it with command: `/[admin_cmd] setspawnpoint` command. However, be aware, that visitors will not be teleported in "dangerous" spots, and if location is not safe, they will be teleported to a safer location.

??? question "Can players have customized icons?"
    Yes, island icon in Visit panel can be changed by adding permissions `visit.icon.[material]` to island owner.

??? question "I do not want to use economy. Can I disable it completely?"
    Yes, the config option `disable-economy` will completely disable all economy parts.

??? question "How can I allow|disallow island members to change visiting values?"
    Island owners (and members with `CHANGE_SETTINGS` allowance) can edit `RANKED_COMMANDS` access via Settings panel. There will be `/[player_cmd] visit configure` command in listing.

??? question "How can I allow|disallow island members to change visiting location?"
    Island owners (and members with `CHANGE_SETTINGS` allowance) can edit `RANKED_COMMANDS` access via Settings panel. There will be `/[player_cmd] visit setlocation` command in listing.

## Translations

{{ translations(5740, ["cs", "es", "de", "hu", "ja", "lv", "pl", "tr", "zh-CN", "zh-TW", "fr", "id"]) }}

## Api

Since Visit 1.4.0 and BentoBox 1.17 other plugins can access to the Visit addon data directly.

### Maven Dependency

Visit provides an API for other plugins. This covers version 1.5.0 and onwards.

!!! note
    Add the Visit dependency to your Maven POM.xml:

    ```xml
        <repositories>
            <repository>
                <id>codemc-repo</id>
                <url>https://repo.codemc.io/repository/maven-public/</url>
            </repository>
        </repositories>
        
        <dependencies>
            <dependency>
                <groupId>world.bentobox</groupId>
                <artifactId>visit</artifactId>
                <version>1.5.0</version>
                <scope>provided</scope>
            </dependency>
        </dependencies>
    ```

Use the latest Visit version.

The JavaDocs for Visit can be found [here](https://ci.codemc.io/job/BentoBoxWorld/job/Visit/ws/target/apidocs/index.html).

### Events

=== "VisitEvent"
    !!! summary "Description"
        Event that is triggered before player is teleported to the island, but after payments.

        Can be cancelled. (payments are not returned on cancellation)

        Link to the class: [VisitEvent](https://github.com/BentoBoxWorld/Visit/blob/develop/src/main/java/world/bentobox/visit/events/VisitEvent.java)

    !!! question "Variables"
        - `User player` - id of the player who tries to visit an island.
        - `Island island` - the island which player tries to visit.
        - `boolean cancelled` - the boolean that indicates if event is cancelled.
 
    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onVisit(VisitEvent event) {
            UUID player = event.getPlayer();
            User user = event.getUser();
            Island island = event.getIsland();

            boolean cancelled = event.isCancelled();
        }
        ```

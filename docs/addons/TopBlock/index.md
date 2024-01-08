# TopBlock

Add-on for BentoBox to calculate island levels for AOneBlock specifically. Ranks are determined by how many magic blocks have been mined - the count.

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("TopBlock") }}

## Installation

1. Place the top block addon jar in the addons folder of the BentoBox plugin
2. Restart the server
3. The addon will create a data folder and inside the folder will be a config.yml
4. Edit the config.yml how you want.
5. Restart the server if you make a change

## Configuration

TopBlock addon has 2 general configuration things:

- config.yml file contains default addon configuration files.
- /panels/ contains files that manages player GUI's

### config.yml

Config file contains main functions for the addon. 

The latest config.yml can be found [here](https://github.com/BentoBoxWorld/TopBlock/blob/develop/src/main/resources/config.yml).

This section defines a number of overall settings for the add-on.

??? note "refresh-time"
    How often the Top Ten should be refreshed in minutes. Minimum is 1 minute, default is 5.
    Each refresh requires reading every island from the database, so this should not be done too often.

    Default: `5`

??? note "shorthand"
    Allows to show shorter island level numbers.

    Shows large level values rounded down, e.g., 10,345 -> 10k

    Default: `false`

### Customizable GUI's

BentoBox 1.17 API introduced a function that allows to implement customizable GUI's. We tried to be as simple as possible for customization, however, some features requires explanation.
You can find more information how BentoBox custom GUI's works here: [Custom GUI's](/en/latest/Tutorials/generic/Customizable-GUI/)

??? question "How can I customize GUI's"
     Addon will create a new directory under `/plugins/bentobox/addons/topblock` with a name `panels`

    Currently you can customize GUI's:

    - Top panel: `top_panel` - allows to see top 10 islands.

??? question "What does `TOP` button type?"
    This button is available in top_panel. It shows island at the top X by island top.
    
    The `icon` by default will be `PLAYER_HEAD` with a proper player skin. Enabling it will replace it with specified material.

    `index` in the data field allows to specify which place of Top 10 should be showed in current spot.

    Top panel has 2 implemented actions which funstion requires extra addon:
    
    - `warp` - requires Warps addon. Will be shown only if warp sign exists on players island.
    - `visit` - requires Visit addon. Will be shown only if visiting is allowed on players island.

    Fallback allows to change background icon, when there are no player in top spot.

    Example:
    ```yaml
        #icon: PLAYER_HEAD
        title: topblock.gui.buttons.island.name
        description: topblock.gui.buttons.island.description
        data:
          type: TOP
          index: 1
        actions:
          warp:
            click-type: LEFT
            tooltip: topblock.gui.tips.click-to-warp
          visit:
            click-type: RIGHT
            tooltip: topblock.gui.tips.right-click-to-visit
        fallback:
          icon: LIME_STAINED_GLASS_PANE
          title: topblock.gui.buttons.island.empty
    ```

??? question "What does `VIEW` button type?"
    This button is available in top_panel. It shows viewer island topblock value.

    The `icon` by default will be `PLAYER_HEAD` with a proper player skin. Enabling it will replace it with specified material.
    
    The action `view` allows to see detailed menu of players island.

    Example:
    ```yaml
        #icon: PLAYER_HEAD
        title: topblock.gui.buttons.island.name
        description: topblock.gui.buttons.island.description
        data:
          type: VIEW
        actions:
          view:
            click-type: unknown
            tooltip: topblock.gui.tips.click-to-view
    ```

## Commands

!!! tip
    `[player_command]` and `[admin_command]` are commands that differ depending on the gamemode you are running.
    The Gamemodes' `config.yml` file contains options that allows you to modify these values.
    As an example, on BSkyBlock, the default `[player_command]` is `island`, and the default `[admin_command]` is `bsbadmin`.

=== "Player commands"
    - `/[player_command] topblock`: access to the top panel. Requires `aoneblock.island.topblock` permission.

## Permissions

=== "Player permissions"
    - `aoneblock.island.topblock` - (default: `true`) - Allows player to use the `/[player_command] top` command.

??? question "Something is missing?"
    You can find the comprehensive list of permissions in the [addon.yml](https://github.com/BentoBoxWorld/TopBlock/blob/develop/src/main/resources/addon.yml) file of this addon.  
    If something is indeed missing from the list below, please let us know!


## Placeholders

{{ placeholders_source(source="TopBlock") }}

## FAQ

??? question "Can you add a feature X?"
    Please add it to the list [here](https://github.com/BentoBoxWorld/TopBlock/issues).

## Translations

{{ translations(3013, ["cs", "de", "es", "fr", "hu", "id", "lv", "pl", "ro", "tr", "zh-CN", "ko", "pt", "vi", "ru"]) }}

## API

### Maven Dependency
TopBlock provides an API for other plugins.

!!! note
    Add the TopBlock dependency to your Maven POM.xml:

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
                <artifactId>topblock</artifactId>
                <version>1.0.1</version>
                <scope>provided</scope>
            </dependency>
        </dependencies>
    ```

The JavaDocs for TopBlock can be found [here](https://ci.codemc.io/job/BentoBoxWorld/job/TopBlock/ws/target/apidocs/index.html).
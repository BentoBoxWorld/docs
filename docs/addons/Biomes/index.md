# Biomes

**Biomes** lets your players **change the biome** on their island.

Created and maintained by [BONNe](https://github.com/BONNe).

{{ addon_description("Biomes", beta=True) }}

## Installation

1. Put the addon jar in the `plugins/BentoBox/addons` folder.
2. Start and stop the server to let Biomes generate its configuration files.
3. Edit the [`config.yml`](#config.yml) and [`biomesTemplate.yml`](#Template) files (you can find them in the `plugins/BentoBox/addons/Biomes` folder).
4. Restart the server.
5. Import the biomes into the gamemode.

## Configuration

### config.yml

After addon is successfully installed, it will create config.yml file. Every option in this file comes with comments about them. Please check file for more information.
You can find the latest config file: [config.yml](https://github.com/BentoBoxWorld/Biomes/blob/develop/src/main/resources/config.yml)

### Template

!!! warning
    Unlike usual configuration files, the changes you make to the `biomesTemplate.yml` file are not automatically taken into account when starting the server.  
    You must import manually the changes you made and eventually override them if you already imported a previous configuration.

This file contains all necessary information about default biomes.
If you change values in biomes.yml, then to apply them, you must run **/[admin_command] biomes**.

Default template file can be found here: [biomesTemplate.yml](https://github.com/BentoBoxWorld/Biomes/blob/develop/src/main/resources/biomesTemplate.yml)

!!! info "Useful resources about biomes"
    - [Comprehensive list of available biomes on Spigot](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/block/Biome.html)
    - ["Biome" page on the official Minecraft wiki](https://minecraft.gamepedia.com/Biome)

??? Template file Structure
    ```
    biomes:                                      # Internal Data Structure. DO NOT CHANGE!
      <unique_name>:                             # Unique name for the biome. Required!
        biome: <BIOME>                           # Spigot BIOME TYPE. Valid values can be found in link below. Required!
        environment: <ENVIRONMENT>               # Spigot WORLD ENVIRONMENT TYPE. World environment value. Default Normal.
        name: <String>                           # String. Custom name for biome. Default <unique_name>.
        description: <String>                    # String. Some extra description in icon lore. Default empty.
        icon: <Item>                             # BentoBox ItemParser type. Write format can be found in: https://docs.bentobox.world/en/latest/BentoBox/ItemParser/. Default Paper.
        order: <Integer>                         # Integer. Order of current biome. Default -1.
        unlock:                                  # Section that configures biomes unlock/buy options. Not required.
          level: <Long>                          # Minimal island level for biome to be unlockable. Requires Level addon. Default 0.
          permissions: [<String>]                # Set of permissions for biome to be unlockable. Default empty.
          cost: <Double>                         # Purchase cost (once) for biome. Requires Vault and Economy plugins. Default 0.
          items: [<Item>]                        # Set of items for purchasing biome (once). Write format for each item can be found in: https://docs.bentobox.world/en/latest/BentoBox/ItemParser/. Default empty.
        change:                                  # Section that configures cost for each biome usage. Not required.
          mode: <Mode>                           # Mode how cost is applied. Supported values: STATIC - price never changes, PER_BLOCK - cost is applied for each block in area, PER_USAGE - cost increases by [increment] after each usage. Default STATIC.
          cost: <Double>                         # Biome change cost. Requires Vault and Economy plugins. Default 0.
          items: [<Item>]                        # Set of items for changing biome. Write format for each item can be found in: https://docs.bentobox.world/en/latest/BentoBox/ItemParser/. Default empty.
          increment: <Double>                    # Increment for all costs (money and items) if usage is set to PER_USAGE. Default 0. (works as static)
    # Here starts the Bundle List
    bundles:                                     # Internal Data Structure.
      <unique_name>:                             # Unique name for the bundle. Required!
        name: <String>                           # String. Custom name for bundle. Default <unique_name>.
        description: <String>                    # String. Some extra description in icon lore. Default empty.
        icon: <Item>                             # BentoBox ItemParser type. Write format can be found in: https://docs.bentobox.world/en/latest/BentoBox/ItemParser/. Default Paper.
        biomes: [<String>]                       # Set of <unique_names> that you used in biomes section. Default empty.
    ```

### Customizable GUI's

BentoBox 1.17 API introduced a function that allows to implement customizable GUI's. This addon is one of the first one which uses this functionality. We tried to be as simple as possible for customization, however, some features requires explanation.
You can find more information how BentoBox custom GUI's works here: [Custom GUI's](/en/latest/Tutorials/generic/Customizable-GUI/)

??? question "How can I customize GUI's"
    To customize Addon GUI's you need to have version 2.0. This is a first version that has implemented them. Addon will create a new directory under `/plugins/BentoBox/addons/Biomes` with a name `panels`

    Currently you can customize 3 GUI's:

    - Main Panel: `main_panel` - panel that contains all biomes that users can purchase or use them.
    - Advanced Panel: `advanced_panel` - panel that contains different ways how biome can be applied on island.
    - Buy Panel: `buy_panel` - panel that contains biomes which player can buy.

    Each GUI contains functions that is supported only by itself.

??? question "What does `PREVIOUS`|`NEXT` button type?"
    The PREVIOUS and NEXT button types allows creating automatic paging, when you have more biomes than spaces in GUI.
    These types have extra parameters under data:
 
    - `indexing` - indicates if button will show page number.

    Example: 
    ```yaml
        icon: tipped_arrow{CustomPotionColor:11546150}
        title: biomes.gui.buttons.previous.name
        description: biomes.gui.buttons.previous.description
        data:
          type: PREVIOUS
          indexing: true
        action:
          left:
            tooltip: biomes.gui.tips.click-to-previous
    ```

??? question "What is `RETURN` button type?"
    This button is available in all panels.
    It creates a button that allows to return to previous menu or exit the gui. Description is generated by addon, however, like with all buttons, you can specify your own text in panel.

    Example: 
    ```yaml
        data:
          type: RETURN
    ```

??? question "What is `BIOME` button type?"
    This button is available in main_panel and buy_panel.
    The BIOME button creates a dynamic entry for a biomes object. Button will be filled only if there exist a biome. F.e. if you have only 3 biomes, but defined 7 spots for them in the GUI, then only 3 spots will be filled. Other spots will be left empty.

    By default biomes will be ordered by their order numbers, however, you can specify a specific biome to be in a specific slot with `id` parameter under data.
    
    ```yaml
      data:
        type: BIOME
        id: example_biome
    ```

    Specifying title, description and icon will overwrite dynammic generation based on database data. By default these values will be generated from database entries.
    This button supports 3 different action types:

    - CHANGE - changes biome based on default update mode and default range values. Available in main_panel.
    - ADVANCED_PANEL - opens advanced panel that allows to choose different biome update modes. Available in main_panel.
    - BUY - purchases selected biome. Available in buy_panel.

    Example: 
    ```yaml
      data:
        type: BIOME
      actions:
        left:
          type: CHANGE
          # Supports ISLAND | CHUNK:NUMBER | RANGE:NUMBER
          content: ISLAND
          tooltip: biomes.gui.tips.left-click-to-apply
        right: 
          type: ADVANCED_PANEL
          tooltip: biomes.gui.tips.right-click-to-open
    ```

??? question "What is `PURCHASE` button type?"
    This button is available in main_panel.
    It creates a button that opens a new panel that contains biomes which player can buy.

    Example: 
    ```yaml
        data:
          type: PURCHASE
        action:
          left:
            tooltip: biomes.gui.tips.click-to-view
    ```


??? question "What is `INCREASE|REDUCE` button type?"
    This button is available in advanced_panel.
    It creates a button that increases/reduces "range" for changing biome. The number by how much it increases/reduces, can be defined alongside with the button type.

    Example: 
    ```yaml
        data:
          type: INCREASE
          value: 5
        actions:
          left:
            tooltip: biomes.gui.tips.click-to-increase
    ```

??? question "What is `MODE` button type?"
    This button is available in advanced_panel.
    It creates a button that allows to change biome update mode between ISLAND, CHUNK and RANGE modes. Mode is defined alongside with button type.

    Example: 
    ```yaml
        data:
          type: MODE
          value: CHUNK
        actions:
          left:
            tooltip: biomes.gui.tips.click-to-choose
    ```

??? question "What is `ACCEPT` button type?"
    This button is available in advanced_panel.
    It creates a button that allows to start biome update with selected settings. It has two actions: 
      
       - ACCEPT: starts biome update
       - INPUT: allows to manually input number via chat.

    Example: 
    ```yaml
        data:
          type: ACCEPT
        actions:
          left:
            type: ACCEPT
            tooltip: biomes.gui.tips.left-click-to-accept
          right:
            type: INPUT
            tooltip: biomes.gui.tips.right-click-to-write
    ```

## Commands

!!! tip
    `[player_command]` and `[admin_command]` are commands that differ depending on the gamemode you are running.
    The Gamemodes' `config.yml` file contains options that allows you to modify these values.
    As an example, on BSkyBlock, the default `[player_command]` is `island`, and the default `[admin_command]` is `bsbadmin`.

!!! info
    Biomes Addon player commands is completely configurable. You can change them in the Biomes Addon config file. Bellow is just default names for these commands.

=== "Player commands"
    - `/[player_command] biomes`: This method opens GUI that allows to change biome on User island.
    - `/[player_command] biomes help`: Show help for all the commands
    - `/[player_command] biomes set <biome> [<type>] [<size>]`: This command allows to change biome on island without opening GUI. If prarameters < type> and < size> are not provided, command uses default values from addon config.
    - `/[player_command] biomes buy <biome>`: This command allows to buy biome without opening GUI.

    !!! info
        - `<biome>` may not be the actual Minecraft biome name. It is defined by the admin.
        - `<type>` is one of the three biome change types. It offers to change biome on whole island (`ISLAND`), in current chunk(s) (`CHUNK`) or by distance around player (`RANGE`).


=== "Admin commands"
    - `/[admin_command] biomes`: opens the Admin Biomes GUI.
    - `/[admin_command] biomes help`: displays the help for all the Biomes-related admin commands.
    - `/[admin_command] biomes import [<file>]`: imports biomes from the `biomesTemplate.yml` configuration file, or from provided file.
    - `/[admin_command] biomes set <player> <biome> [<type>] [<size>]`: works the same as user biome set command, but it is necessary to provide also player, which island biome will be updated.
    - `/[admin_command] biomes migrate`: migrates biomes addon data. Usually used when upgrade from older version to a new version.
    - `/[admin_command] biomes unlock <player> <biome_id> [true]`: unlocks (and buys if added `true` at the end) passed biome for a player island.

## Permissions

!!! tip
    `[gamemode]` is a prefix that differs depending on the gamemode you are running.
    The prefix is the lowercased name of the gamemode, i.e. if you are using BSkyBlock, the prefix is `bskyblock`.
    Similarly, if you are using AcidIsland, the prefix is `acidisland`.

??? question "Something is missing?"
    You can find the comprehensive list of permissions in the [addon.yml](https://github.com/BentoBoxWorld/Biomes/blob/develop/src/main/resources/addon.yml) file of this addon.  
    If something is indeed missing from the list below, please let us know!

=== "Player permissions"
    - `[gamemode].biomes` (default: `true`): player can use biomes command that opens GUI.
    - `[gamemode].biomes.info` (default: `true`): player can use biomes info command.
    - `[gamemode].biomes.set` (default: `true`): player can use biomes set command.
    - `[gamemode].biomes.buy` (default: `true`): player can use biomes buy command.

=== "Admin permissions"
    - `[gamemode].admin.biomes` (default: `op`): player can use admin biomes command that opens GUI.

## Translations

{{ translations(2894, ["lv", "zh-CN", "fr", "pl", "es", "uk"]) }}

## API

Since Biomes 2.0 and BentoBox 1.17 other plugins can access to the Biomes addon data directly. However, addon requests are still a good solution for a plugins that do not want to use too many dependencies.

### Maven Dependency

Biomes provides an API for other plugins. This covers version 2.1.0 and onwards.

!!! note
Add the Biomes dependency to your Maven POM.xml:

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
                <artifactId>biomes</artifactId>
                <version>2.1.0</version>
                <scope>provided</scope>
            </dependency>
        </dependencies>
    ```

Use the latest Biomes version.

The JavaDocs for Biomes can be found [here](https://ci.codemc.io/job/BentoBoxWorld/job/Biomes/ws/target/apidocs/index.html).

### Events

=== "BiomeUnlockedEvent"
    !!! summary "Description"
        Event that is triggered when player unlocks a new biome.

        Event is cancellable. Cancelling evnet will prevent user from unlocking the biomesObject.

        Link to the class: [BiomeUnlockedEvent](https://github.com/BentoBoxWorld/Biomes/blob/develop/src/main/java/world/bentobox/biomes/events/BiomeUnlockedEvent.java)

    !!! summary "Since"
        Event is added in Biomes 2.0 version.

    !!! question "Variables"
        - `@NotNull BiomesObject biomesObject` - the biomesOjbect that is unlocked.
        - `@Nullable User user` - the user who unlocks the biomesObject.
        - `@NotNull Island island` - the island on which biomesObject is unlocked.
        
    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.LOW)
        public void onBiomesUnlock(BiomeUnlockedEvent event) {
            User user = event.getUser();
            BiomesObject biomesOjbect = event.getBiomesObject();
            Island island = event.getIsland();
            
            // There is also converted methods, that do not use Biomes Addon objects.
            UUID userUUID = event.getUserUUID();
            String islandUUID = event.getIslandUUID();
            String biomeId = event.getBiomeId();
            Biome biome = event.getBiome();

            event.setCancelled(false);
        }
        ```

=== "BiomePurchasedEvent"
    !!! summary "Description"
        Event that is triggered when player purchases a new biome.

        Event is only informative. Cannot be cancelled.

        Link to the class: [BiomePurchasedEvent](https://github.com/BentoBoxWorld/Biomes/blob/develop/src/main/java/world/bentobox/biomes/events/BiomePurchasedEvent.java)

    !!! summary "Since"
        Event is added in Biomes 2.0 version.

    !!! question "Variables"
        - `@NotNull BiomesObject biomesObject` - the biomesOjbect that is purchased.
        - `@NotNull User user` - the user who purchase the biomesObject.
        - `@NotNull Island island` - the island on which biomesObject is purchased.
        
    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onBiomesPurchase(BiomePurchasedEvent event) {
            User user = event.getUser();
            BiomesObject biomesOjbect = event.getBiomesObject();
            Island island = event.getIsland();
            
            // There is also converted methods, that do not use Biomes Addon objects.
            UUID userUUID = event.getUserUUID();
            String islandUUID = event.getIslandUUID();
            String biomeId = event.getBiomeId();
            Biome biome = event.getBiome();
        }
        ```

=== "BiomePreChangeEvent"
    !!! summary "Description"
        Event that is triggered before withdrawing items and changing biome in area.

        Event is only informative. Cannot be cancelled.

        Link to the class: [BiomePreChangeEvent](https://github.com/BentoBoxWorld/Biomes/blob/develop/src/main/java/world/bentobox/biomes/events/BiomePreChangeEvent.java)

    !!! summary "Since"
        Event is added in Biomes 2.0 version.

    !!! question "Variables"
        - `@NotNull BiomesObject biomesObject` - the biomesOjbect that is used.
        - `@Nullable User user` - the user who triggered biome change.
        - `@NotNull Island island` - the island on which biome is changed.
        - `@NotNull BlockVector minCoordinate` - the minimal coordinate for biome change.
        - `@NotNull BlockVector maxCoordinate` - the maximal coordinate for biome change.
        
    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onBiomesPreChange(BiomePreChangeEvent event) {
            User user = event.getUser();
            BiomesObject biomesOjbect = event.getBiomesObject();
            Island island = event.getIsland();
            
            BlockVector minCoordinate = event.getMinCoordinate();
            BlockVector maxCoordinate = event.getMaxCoordinate();
            
            // There is also converted methods, that do not use Biomes Addon objects.
            UUID userUUID = event.getUserUUID();
            String islandUUID = event.getIslandUUID();
            String biomeId = event.getBiomeId();
            Biome biome = event.getBiome();

            int minX = event.getMinX();
            int minY = event.getMinY();
            int minZ = event.getMinZ();

            int maxX = event.getMaxX();
            int maxY = event.getMaxY();
            int maxZ = event.getMaxZ();
        }
        ```


=== "BiomeChangedEvent"
    !!! summary "Description"
        Event that is triggered after biome is changed on whole area. It is triggered even if biome change failed.

        Event is only informative. Cannot be cancelled.

        Link to the class: [BiomeChangedEvent](https://github.com/BentoBoxWorld/Biomes/blob/develop/src/main/java/world/bentobox/biomes/events/BiomeChangedEvent.java)

    !!! summary "Since"
        Event is added in Biomes 2.0 version.

    !!! question "Variables"
        - `@NotNull BiomesObject biomesObject` - the biomesOjbect that was used.
        - `@Nullable User user` - the user who triggered biome change.
        - `@NotNull Island island` - the island on which biome was changed.
        - `@NotNull BlockVector minCoordinate` - the minimal coordinate for biome change.
        - `@NotNull BlockVector maxCoordinate` - the maximal coordinate for biome change.
        - `@Nullable Result result` - the result value after biome change. The result values may be:
                                        - FINISHED: biomes change was succesfull.
                                        - TIMEOUT: biomes change took longer then timeout value and failed.
                                        - FAILED: biomes change failed for some other reason.

    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onBiomeChanged(BiomeChangedEvent event) {
            User user = event.getUser();
            BiomesObject biomesOjbect = event.getBiomesObject();
            Island island = event.getIsland();
            
            BlockVector minCoordinate = event.getMinCoordinate();
            BlockVector maxCoordinate = event.getMaxCoordinate();
            
            Result result = event.getResult();            

            // There is also converted methods, that do not use Biomes Addon objects.
            UUID userUUID = event.getUserUUID();
            String islandUUID = event.getIslandUUID();
            String biomeId = event.getBiomeId();
            Biome biome = event.getBiome();

            int minX = event.getMinX();
            int minY = event.getMinY();
            int minZ = event.getMinZ();

            int maxX = event.getMaxX();
            int maxY = event.getMaxY();
            int maxZ = event.getMaxZ();

            String resultName = event.getResultName();
        }
        ```

### Addon Request Handlers

Till BentoBox 1.17 we had an issue with accessing data outside BentoBox environment doe to the class loader we used to load addons. 
This meant that data was accessible only from other addons. But BentoBox implemented PlAddon functionality, which means that request
handlers are not necessary anymore.


=== "biome-data"
    !!! summary "Description"
        Returns a `Map<String, Object>` containing all the information about the requested biome.

    !!! question "Input"
        - `biomeId`: String - the unique ID of the requested biome.

    !!! success "Output"
        The output is a `Map<String, Object>` with the following keys:

        - `uniqueId`: String - the unique ID of the requested biome.
        - `world`: String - the name of the world where the biome is available.
        - `biome`: String - the name of the corresponding Minecraft biome.
        - `name`: String - the display name for the biome.
        - `deployed`: Boolean - `true` if the biome is deployed, `false` otherwise.
        - `description`: List&lt;String&gt; - the description for the biome.
        - `icon`: ItemStack - the item that represents the biome in GUIs.
        - `order`: Integer - the order number for the given biome.
        - `cost`: Integer - the cost to use the biome.
        - `level`: Long - the minimum Island Level required in order to use the biome.
        - `permissions`: Set&lt;String&gt; - the list of permissions required in order to use the biome.

    !!! failure
        This handler will return an empty map if the `biomeId` has not been provided or if the `biomeId` could not be found in the database.

    !!! example "Code example"
        ```java
        public Map<String, Object> getBiomeData(String biomeId) {
            return (Map<String, Object>) new AddonRequestBuilder()
                .addon("Biomes")
                .label("biome-data")
                .addMetaData("biomeId", biomeId)
                .request();
        }
        ```

=== "biomes-list"
    !!! summary "Description"
        Returns a list of all biomes' uniqueIds that are defined in a given world.

    !!! question "Input"
        - `world-name`: String - the name of the world.

    !!! success "Output"
        The output is a `List<String>` containing the list of the uniqueIds of the biomes that are defined for the specified world.

    !!! failure
        This handler will return an empty list if the `world-name` has not been provided or if the `world-name` does not exist or is not a gamemode world.

    !!! example "Code example"
        ```java
        public List<String> getBiomesList(String worldName) {
            return (List<String>) new AddonRequestBuilder()
                .addon("Biomes")
                .label("biomes-list")
                .addMetaData("world-name", worldName)
                .request();
        }
        ```

=== "biome-request-change"
    !!! summary "Description"
        Requests a biome change with the provided parameters.

    !!! question "Input"
        - Mandatory parameters:
            - `player`: UUID - the UUID of the targetted player.
            - `world-name`: String - the name of the world where the biome will be changed.
            - `biomeId`: String - the uniqueId of the biome.
        - Optional parameters:
            - `updateMode`: String - the mode to use when changing the biome.
                                     Can be either ISLAND, RANGE or CHUNK.
                                     (Default: config)
            - `range`: Integer - the range within which the biome will be changed.
                                 (Default: config)
            - `checkRequirements`: Boolean - if `true`, the player will have to fulfill all the requirements for the specified biome.
                                   (Default: true)
            - `withdraw`: Boolean - if `true`, the money will be withdrawn from the player's bank account.
                          (Default: true)

    !!! success "Output"
        The output is a `Map<String, Object>` with the following keys:

        - `status`: Boolean - `true` if the biome was changed successfully, `false` otherwise.
        - `reason`: String - message explaining what happened (whether the change was successful or not).

    !!! failure
        This handler will return `false` as its status with an appropriate reason if it failed.

    !!! example "Code example"
        ```java
        public Map<String, Object> requestBiomeChange(UUID player, String worldName, String biomeId, String mode, int range, boolean requirements, boolean withdraw) {
            return (Map<String, Object>) new AddonRequestBuilder()
                .addon("Biomes")
                .label("biome-request-change")
                .addMetaData("player", player)
                .addMetaData("world-name", worldName)
                .addMetaData("biomeId", biomeId)
                .addMetaData("updateMode", mode)
                .addMetaData("range", range)
                .addMetaData("checkRequirements", requirements)
                .addMetaData("withdraw", withdraw)
                .request();
        }
        ```

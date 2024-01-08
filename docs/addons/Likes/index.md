# Likes

**Likes** lets players rate other islands with likes, dislikes or stars.

Created and maintained by [BONNe](https://github.com/BONNe).

{{ addon_description("Likes") }}

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
You can find the latest config file: [config.yml](https://github.com/BentoBoxWorld/Likes/blob/develop/src/main/resources/config.yml)

Some config options can be changed via administration GUI in game. However, some options cannot.

The most important config option is mode:

!!! summary "Likes mode"
    mode: allows changing which mode addon works

    - LIKES - Allows adding only Like to island.
    - LIKES_DISLIKES - Allows adding only Like and Dislikes to island.
    - STARS - Allows adding Starts to island.

You can use only one mode at the time.

### Customizable GUI's

BentoBox 1.17 API introduced a function that allows to implement customizable GUI's. This addon is one of the first one which uses this functionality. We tried to be as simple as possible for customization, however, some features requires explanation.
You can find more information how BentoBox custom GUI's works here: [Custom GUI's](/en/latest/Tutorials/generic/Customizable-GUI/)

??? question "How can I customize GUI's"
    To customize Addon GUI's you need to have version 2.2. This is a first version that has implemented them. Addon will create a new directory under `/plugins/BentoBox/addons/Likes` with a name `panels`

    Currently you can customize 3 GUI:

    - View Panel: `view_panels` - panel that allows to view who liked player island.
    - Top Panel: `top_panel` - panel that contains top islands by certain value.
    - Manage Panel: `manage_panels` - panel that allows to add like/dislike or stars.

    View and Manage panels contains 3 different panels for each mode.


## Commands

!!! tip
    `[player_command]` and `[admin_command]` are commands that differ depending on the gamemode you are running.
    The Gamemodes' `config.yml` file contains options that allows you to modify these values.
    As an example, on BSkyBlock, the default `[player_command]` is `island`, and the default `[admin_command]` is `bsbadmin`.

=== "Player commands"
    - `/[player_command] likes`: opens GUI for adding / removing likes, dislikes or star. 
    - `/[player_command] likes top`: opens GUI that display Top islands by Likes, Dislikes or Stars
    - `/[player_command] likes view <player>`: opens GUI that shows who add likes or stars to the island.

=== "Admin commands"
    - `/[admin_command] likes`: opens Admin GUI.
    - `/[admin_command] likes settings`: opens Admin Settings GUI.

## Permissions

!!! tip
    `[gamemode]` is a prefix that differs depending on the gamemode you are running.
    The prefix is the lowercased name of the gamemode, i.e. if you are using BSkyBlock, the prefix is `bskyblock`.
    Similarly, if you are using AcidIsland, the prefix is `acidisland`.

=== "Player permissions"
    - `[gamemode].likes` - (default: `true`) - Allows the player to use '/[player_command] likes' command.
    - `[gamemode].likes.top` - (default: `true`) - Allows the player to use '/[player_command] likes top' command.
    - `[gamemode].likes.view` - (default: `true`) - Allows the player to use '/[player_command] likes top' command.
    - `[gamemode].likes.icon.[MATERIAL]` - (default: `false`) - Allows changing island owner icon in Top GUIs.

=== "Admin permissions"
    - `[gamemode].likes.view.others` - (default: `op`) - Allows the player to use '/[player_command] likes view <player>' command.
    - `[gamemode].likes.bypass-cost` - (default: `op`) - Allows bypassing cost for operations in addon.
    - `[gamemode].likes.admin` - (default: `op`) - Allows using '/[admin_command] likes' command.
    - `[gamemode].likes.admin.settings` - (default: `op`) - Allows using '/[admin_command] likes settings' command.

??? question "Something is missing?"
    You can find the comprehensive list of permissions in the [addon.yml](https://github.com/BentoBoxWorld/Likes/blob/develop/src/main/resources/addon.yml) file of this addon.  
    If something is indeed missing from the list below, please let us know!

## Placeholders

{{ placeholders_source(source="Likes") }}

## FAQ

??? question "Can you add a feature X?"
    Please add it to the list [here](https://github.com/BentoBoxWorld/Likes/issues).

??? question "Can I disable dislikes?"
    Yes, Likes addon supports 3 working modes:

    - Likes: allows adding only likes to the island
    - LikesDislikes: allows adding likes and dislikes
    - Stars: allows to rate player islands with 1 till 5 stars
       
??? question "Can I view other player likes?"
    Yes, but you need a permission: `[gamemode].likes.view.others`. 
    
    With that permission players can use `/[playercmd] likes view <player>` to view other player likes. 
    
??? question "Can I change display icon just for some islands?"
    Yes, it is possible. 
    
    There are 2 ways:
    
    1. using Admin GUI you can choose island and block that will be displayed for it.
    2. adding permission to island owner: `[gamemode].likes.icon.[MATERIAL]`
        
    Be aware, PLAYER_HEAD will be converted to island owner head.

## Translations

{{ translations(3331, ["zh-CN", "de", "id", "pl", "ru", "vi", "es"]) }}

## API

Since Likes 2.2.0 and BentoBox 1.17 other plugins can access to the Likes addon data directly.

### Maven Dependency

Likes provides an API for other plugins. This covers version 2.2.0 and onwards.

!!! note
    Add the Likes dependency to your Maven POM.xml:

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
                <artifactId>likes</artifactId>
                <version>2.2.0</version>
                <scope>provided</scope>
            </dependency>
        </dependencies>
    ```

Use the latest Likes version.

The JavaDocs for Likes can be found [here](https://ci.codemc.io/job/BentoBoxWorld/job/Likes/ws/target/apidocs/index.html).

### Events

=== "LikeAddEvent"
    !!! summary "Description"
        Event that is triggered when player adds a new like to the island.

        Event is only informative. Cannot be cancelled.

        Link to the class: [LikeAddEvent](https://github.com/BentoBoxWorld/Likes/blob/develop/src/main/java/world/bentobox/likes/events/LikeAddEvent.java)


    !!! question "Variables"
        - `UUID user` - id of the player who added the like.
        - `String islandId` - id of the island which receive the like.
        
    !!! example "Example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onLike(LikeAddEvent event) {
            UUID user = event.getUser();
            String islandId = event.getIslandId();
        }
        ```  

=== "LikeRemoveEvent"
    !!! summary "Description"
        Event that is triggered when player removes his like from the island.

        Event is only informative. Cannot be cancelled.

        Link to the class: [LikeRemoveEvent](https://github.com/BentoBoxWorld/Likes/blob/develop/src/main/java/world/bentobox/likes/events/LikeRemoveEvent.java)

    !!! question "Variables"
        - `UUID user` - id of the player who removed the like.
        - `String islandId` - id of the island which lose the like.
        
    !!! example "Example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onLikeRemove(LikeRemoveEvent event) {
            UUID user = event.getUser();
            String islandId = event.getIslandId();
        }
        ```  
   
=== "DislikeAddEvent"
    !!! summary "Description"
        Event that is triggered when player adds a new dislike to the island.

        Event is only informative. Cannot be cancelled.

        Link to the class: [DislikeAddEvent](https://github.com/BentoBoxWorld/Likes/blob/develop/src/main/java/world/bentobox/likes/events/DislikeAddEvent.java)

    !!! question "Variables"
        - `UUID user` - id of the player who added the dislike.
        - `String islandId` - id of the island which receive the dislike.

    !!! example "Example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onDislike(DislikeAddEvent event) {
            UUID user = event.getUser();
            String islandId = event.getIslandId();
        }
        ```  

=== "DislikeRemoveEvent"
    !!! summary "Description"
        Event that is triggered when player removes his dislike from the island.

        Event is only informative. Cannot be cancelled.

        Link to the class: [DislikeRemoveEvent](https://github.com/BentoBoxWorld/Likes/blob/develop/src/main/java/world/bentobox/likes/events/DislikeRemoveEvent.java)

    !!! question "Variables"
        - `UUID user` - id of the player who removed the dislike.
        - `String islandId` - id of the island which lose the dislike.

    !!! example "Example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onDislikeRemove(DislikeRemoveEvent event) {
            UUID user = event.getUser();
            String islandId = event.getIslandId();
        }
        ```  

=== "StarsAddEvent"
    !!! summary "Description"
        Event that is triggered when player adds new stars to the island.

        Event is only informative. Cannot be cancelled.

        Link to the class: [StarsAddEvent](https://github.com/BentoBoxWorld/Likes/blob/develop/src/main/java/world/bentobox/likes/events/StarsAddEvent.java)

    !!! question "Variables"
        - `UUID user` - id of the player who added the stars.
        - `String islandId` - id of the island which receive the stars.
        - `int value` - the value of added stars (from 1 till 5)

    !!! example "Example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onStarsAdd(StarsAddEvent event) {
            UUID user = event.getUser();
            String islandId = event.getIslandId();
            int value = event.getValue();
        }
        ```  

=== "StarsRemoveEvent"
    !!! summary "Description"
        Event that is triggered when player removes his stars from the island.

        Event is only informative. Cannot be cancelled.

        Link to the class: [StarsRemoveEvent](https://github.com/BentoBoxWorld/Likes/blob/develop/src/main/java/world/bentobox/likes/events/StarsRemoveEvent.java)

    !!! question "Variables"
        - `UUID user` - id of the player who added the stars.
        - `String islandId` - id of the island which lose the stars.

    !!! example "Example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onStarsRemove(StarsRemoveEvent event) {
            UUID user = event.getUser();
            String islandId = event.getIslandId();
        }
        ```  

### Addon Request Handlers

Till BentoBox 1.17 we had an issue with accessing data outside BentoBox environment doe to the class loader we used to load addons.
This meant that data was accessible only from other addons. But BentoBox implemented PlAddon functionality, which means that request
handlers are not necessary anymore.

More information about addon request handlers can be found [here](/en/latest/BentoBox/Request-Handler-API---How-plugins-can-get-data-from-addons/)

=== "island-likes"
    !!! summary "Description"
        Returns island likes data that is stored for island in given world.

    !!! question "Input"
        - `world-name`: String - the name of the world.
        - `island`: String - the UUID of the island.

    !!! success "Output"
        The output is a `Map<String, Object>` with the following keys:

        - `likes`: long - the number of likes that are set for given island.
        - `dislikes`: long - the number of dislikes that are set for given island.
        - `rank`: long - the number of rank for given island.
        - `stars`: double - the average stars value for given island.
        - `placeByLikes`: integer - the place in ranking by likes that are set for given island.
        - `placeByDislikes`: integer - the place in ranking by dislikes that are set for given island.
        - `placeByRank`: integer - the place in ranking by rank that are set for given island.
        - `placeByStars`: integer - the place in ranking by stars that are set for given island.
        - `likedBy`: List&lt;UUID&gt; - the list of player UUIDs who liked given island.
        - `dislikedBy`: List&lt;UUID&gt; - the list of player UUIDs who disliked given island.
        - `staredBy`: Map&lt;UUID, Integer&gt; - the map of player UUIDs who stared given island with a number of stars that they added.


    !!! failure
        This handler will return an empty map if the `world-name` has not been provided or if the `world-name` does not exist or is not a gamemode world or island is not provided or data for island is empty. 

    !!! example "Code example"
        ```java
        public Map<String, Object> getLikesData(String worldName, String islandUUID) {
            return (Map<String, Object>) new AddonRequestBuilder()
                .addon("Likes")
                .label("island-likes")
                .addMetaData("world-name", worldName)
                .addMetaData("island", islandUUID)
                .request();
        }
        ```

=== "top-ten-likes"
    !!! summary "Description"
        Returns a `Map<String, Number>` containing top 10 island UUID's, and their values in given top.

    !!! question "Input"
        - `world-name`: String - the name of the world.
        - `type`: String - the type of the Top. Supports: STARS, LIKES, DISLIKES, RANK.

    !!! success "Output"
        A Map containing the UUIDs of the islands is in the Top 10, mapped to the top value of their island.

    !!! failure
        This handler will return an empty map if the `world-name` has not been provided or if the `world-name` does not exist or is not a gamemode world or provided top type does not have any data in it.

    !!! example "Code example"
        ```java
        public Map<String, Number> getTopTenLikes(String worldName, String type) {
            return (Map<String, Number>) new AddonRequestBuilder()
                .addon("Likes")
                .label("top-ten-likes")
                .addMetaData("world-name", worldName)
                .addMetaData("type", type)
                .request();
        }
        ```
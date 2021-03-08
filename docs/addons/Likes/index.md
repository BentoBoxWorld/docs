# Likes

**Likes** lets players rate other islands with likes, dislikes or stars.

Created and maintained by [BONNe](https://github.com/BONNe).

{{ addon_description("Likes") }}

## Installation

1. Place the addon jar in the addons folder of the BentoBox plugin
2. Start the server
3. Stop the server
4. Edit configuration located in `/plugins/BentoBox/addons/Likes` folder.
5. Start the server.

## Configuration

Some config options can be changed via administration GUI in game. However, some options cannot.

There are 2 important config options:

- mode: allows changing which mode addon works
    - LIKES - Allows adding only Like to island.
    - LIKES_DISLIKES - Allows adding only Like and Dislikes to island.
    - STARS - Allows adding Starts to island.

- disabled-gamemode: allows disabling addon in some gamemode addons completely.

All other options can be changed via ingame GUI.

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
    Please add it to the list [here](https://github.com/BentoBoxWorld/Challenges/issues).

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

{{ translations(3331, []) }}

## API

### Addon Request Handlers

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
                .addMetadata("world-name", worldName)
                .addMetadata("island", islandUUID)
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
                .addMetadata("world-name", worldName)
                .addMetadata("type", type)
                .request();
        }
        ```

### Events

=== "LikeAddEvent"
    !!! summary "Description"
        Event that is triggered when player adds a new like to the island.

        Event is only informative. Cannot be cancelled.

        Link to the class: [LikeAddEvent](https://github.com/BentoBoxWorld/Likes/blob/develop/src/main/java/world/bentobox/likes/events/LikeAddEvent.java)


    !!! question "Variables"
        - `UUID user` - id of the player who added the like.
        - `String islandId` - id of the island which receive the like.

    !!! warning "Class Loader Issue"
        Due Java Class Loader hierarchy, plugins cannot listen for the event directly. 
        Only BentoBox addons can use event class directly.

    !!! example "Code example for Plugins"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onLike(BentoBoxEvent event) {
            if (event.getEventName().equals("LikeAddEvent")) {
                UUID user = (UUID) event.getKeyValues().get("user");
                String islandId = (String) event.getKeyValues().get("islandId");
            }
        }
        ```
        
    !!! example "Code example for Addons"
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

    !!! warning "Class Loader Issue"
        Due Java Class Loader hierarchy, plugins cannot listen for the event directly. 
        Only BentoBox addons can use event class directly.

    !!! example "Code example for Plugins"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onLikeRemove(BentoBoxEvent event) {
            if (event.getEventName().equals("LikeRemoveEvent")) {
                UUID user = (UUID) event.getKeyValues().get("user");
                String islandId = (String) event.getKeyValues().get("islandId");
            }
        }
        ```
        
    !!! example "Code example for Addons"
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

    !!! warning "Class Loader Issue"
        Due Java Class Loader hierarchy, plugins cannot listen for the event directly. 
        Only BentoBox addons can use event class directly.

    !!! example "Code example for Plugins"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onDislike(BentoBoxEvent event) {
            if (event.getEventName().equals("DislikeAddEvent")) {
                UUID user = (UUID) event.getKeyValues().get("user");
                String islandId = (String) event.getKeyValues().get("islandId");
            }
        }
        ```
        
    !!! example "Code example for Addons"
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

    !!! warning "Class Loader Issue"
        Due Java Class Loader hierarchy, plugins cannot listen for the event directly. 
        Only BentoBox addons can use event class directly.

    !!! example "Code example for Plugins"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onDislikeRemove(BentoBoxEvent event) {
            if (event.getEventName().equals("DislikeRemoveEvent")) {
                UUID user = (UUID) event.getKeyValues().get("user");
                String islandId = (String) event.getKeyValues().get("islandId");
            }
        }
        ```
        
    !!! example "Code example for Addons"
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

    !!! warning "Class Loader Issue"
        Due Java Class Loader hierarchy, plugins cannot listen for the event directly. 
        Only BentoBox addons can use event class directly.

    !!! example "Code example for Plugins"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onStarsAdd(BentoBoxEvent event) {
            if (event.getEventName().equals("StarsAddEvent")) {
                UUID user = (UUID) event.getKeyValues().get("user");
                String islandId = (String) event.getKeyValues().get("islandId");
                int value = (int) event.getKeyValues().get("value");
            }
        }
        ```
        
    !!! example "Code example for Addons"
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

    !!! warning "Class Loader Issue"
        Due Java Class Loader hierarchy, plugins cannot listen for the event directly. 
        Only BentoBox addons can use event class directly.

    !!! example "Code example for Plugins"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onStarsRemove(BentoBoxEvent event) {
            if (event.getEventName().equals("StarsRemoveEvent")) {
                UUID user = (UUID) event.getKeyValues().get("user");
                String islandId = (String) event.getKeyValues().get("islandId");
            }
        }
        ```
        
    !!! example "Code example for Addons"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onStarsRemove(StarsRemoveEvent event) {
            UUID user = event.getUser();
            String islandId = event.getIslandId();
        }
        ```  

# The Request Handler API
This API enables plugin authors to request data from addons. Addon authors can decide exactly what data they wish to expose. Plugins cannot directly access any classes inside an addon because of Java security rules on class loaders.

## Example with Level addon

The Level addon exposes two request handlers [LevelRequestHandler](https://github.com/BentoBoxWorld/Level/blob/develop/src/main/java/world/bentobox/level/requests/LevelRequestHandler.java) and [TopTenRequestHandler](https://github.com/BentoBoxWorld/Level/blob/develop/src/main/java/world/bentobox/level/requests/TopTenRequestHandler.java). Here is how a plugin would obtain a player's level from LevelRequestHandler:

### LevelRequestHandler

Label: `island-level`

Input map:

* Key: `world-name` -> String
* Value: `player` -> UUID

    !!! example "Code example"
        ```java
            /**
             * Returns the level of this player's island in the given world.
             * @param playerUUID UUID of the player, not null.
             * @param worldName Name of the world (Overworld) the island is in, not null.
             * @return the player's island level or {@code 0L} if the input was invalid or
             *         if this player does not have an island in this world.
             */
            public long getIslandLevel(UUID playerUUID, String worldName) {
                return (Long) new AddonRequestBuilder()
                    .addon("Level")
                    .label("island-level")
                    .addMetaData("world-name", worldName)
                    .addMetaData("player", playerUUID)
                    .request();
            }
        ```

You can find out what data is exposed by addons by looking at their code or at their documentation.

# Exposing data from an addon
To expose data, create classes for each element that extend [AddonRequestHandler](https://bentoboxworld.github.io/BentoBox/world/bentobox/bentobox/api/addons/request/AddonRequestHandler.html). Then register the request handlers in your addon. For example:

```
        // Register request handlers
        registerRequestHandler(new LevelRequestHandler(this));
        registerRequestHandler(new TopTenRequestHandler(this));
```

The handler should define its label in its constructor, for example:

```
    public LevelRequestHandler(Level addon) {
        super("island-level"); // the label is "island-level"
        this.addon = addon;
    }
```

The label must be unique for your addon.

Then, override the `handle` method that takes a map as a parameter:

```
    @Override
    public Object handle(Map<String, Object> map) {
```

You can define the contents of the map but the Object must NEVER be any unique class in your addon. It can only be classes that exist for all plugins. If you try to reference a hidden class, the plugin will generate an exception. So, integers, longs, Bukkit Locations, worlds, etc. are fine.

It is good practice to document what your map will be because plugin authors will be using it:

```
        /*
            What we need in the map:
            0. "world-name" -> String
            1. "player" -> UUID
            What we will return:
            - 0L if invalid input/player has no island
            - the island level otherwise (which may be 0)
         */
```

After that process the map and provide the result:

```

        if (map == null || map.isEmpty()
                || map.get("world-name") == null || !(map.get("world-name") instanceof String)
                || map.get("player") == null || !(map.get("player") instanceof UUID)
                || Bukkit.getWorld((String) map.get("world-name")) == null) {
            return 0L;
        }

        return addon.getIslandLevel(Bukkit.getWorld((String) map.get("world-name")), (UUID) map.get("player"));
    }
```

Note that you are returning an `Object` so the plugin author will need to cast it to the correct form, in this case, a `long`. It is good practice to protect your addon from erroneous map formats by performing an appropriate level of parameter checking.






## Introduction

**Addon Requests** allow plugins and addons to access to internal addon data without necessarily injecting or overwriting the said addon.

This is especially useful for plugins, whose access to addon's classes is restricted by [Java's ClassLoader visibility principle](https://www.javatpoint.com/classloader-in-java) (which can be summed up as the following: *child ClassLoader can see all the classes loaded by the parent ClassLoader, but the parent ClassLoader cannot see the classes loaded by the child ClassLoader*).

## Available Addon Requests

### Get an island's level: `island-level`

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

Possible values returned:
* `0L` if the input is invalid or the specified player does not have an island in the specified world;
* the player's island level as a `long`.

### Get the Top 10: `top-ten-level`

```java
/**
 * Returns the players whose island they own is in the Top 10 mapped to the level of their island.
 * @param worldName Name of the world (Overworld) the island is in, not null.
 * @return a Map containing the UUIDs of the island owners whose island is in the Top 10, mapped to the level of their island,
 *         or an empty map if the specified world doesn't exist or doesn't contain islands.
 */
public Map<UUID, Long> getTopTen(String worldName) {
    return (Map<UUID, Long>) new AddonRequestBuilder()
        .addon("Level")
        .label("top-ten-level")
        .addMetaData("world-name", worldName)
        .request();
}
```

Possible values returned:
* an empty Map if the specified world doesn't exist or doesn't contain islands;
* a Map containing the UUIDs of the island owners whose island is in the Top 10, mapped to the level of their island.
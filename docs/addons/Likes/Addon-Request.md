## Introduction

**Addon Requests** allow plugins and addons to access to internal addon data without necessarily injecting or overwriting the said addon.

This is especially useful for plugins, whose access to addon's classes is restricted by [Java's ClassLoader visibility principle](https://www.javatpoint.com/classloader-in-java) (which can be summed up as the following: *child ClassLoader can see all the classes loaded by the parent ClassLoader, but the parent ClassLoader cannot see the classes loaded by the child ClassLoader*).

## Available Addon Requests

### Get Island Likes Data: `island-likes`

```java
/**
 * Returns a map that contains all known values about island likes for given island in given world.
 * @param worldName Name of the world (Overworld) the island is in, not null.
 * @param islandId Island Id who's likes object data must be returned, not null.
 * @return a Map that contains all known island likes object data,
 *         or empty map.
 */
public Map<String, Object> getIslandLikesData(String islandId, String worldName) {
    return (Map<String, Object>) new AddonRequestBuilder()
        .addon("Likes")
        .label("island-likes")
        .addMetaData("world-name", worldName)
        .addMetaData("island", islandId)
        .request();
}
```

Possible values returned:
* a empty Map if challenge with the given id is not found;
* a map that contains some internal challenges object data:
	* `likes`: Long object that represents number of likes added by players. (`Entry<String, Long>`)
	* `dislikes`: Long object that represents number of dislikes added by players. (`Entry<String, Long>`)
	* `rank`: Long object that represents rank calculated from likes and dislikes. (`Entry<String, Long>`)
	* `placeByLikes`: Long object that represents index of island in list that is sorted by like count. (`Entry<String, Long>`)
	* `placeByDislikes`: Long object that represents index of island in list that is sorted by dislike count. (`Entry<String, Long>`)
	* `placeByRank`: Long object that represents index of island in list that is sorted by rank number. (`Entry<String, Long>`)
	* `likedBy`: List of UUID who has liked this island. (`Entry<String, List<UUID>>`)
	* `dislikedBy`: List of UUID who has disliked this island. (`Entry<String, List<UUID>>`)  


### Get Top Ten Ratings: `top-ten-likes`

```java
/**
 * Returns top 10 islands and their corresponding value in top, that is defined by type. 
 * @param worldName Name of the world (Overworld) the island is in, not null.
 * @param type String that represents a type of top, may be null.
 *             Valid values: LIKES, DISLIKES, RANK
 * @return a Linked Hash Map that contains islands ordered by their place in top and rating value,
 *         or empty map if top is empty.
 */
public Map<String, Long> getTopTenData(String type, String worldName) {
    return (Map<String, Long>) new AddonRequestBuilder()
        .addon("Likes")
        .label("top-ten-likes")
        .addMetaData("world-name", worldName)
        .addMetaData("type", type)
        .request();
}
```

Possible values returned:
* a empty Map if a challenge level with the given id is not found;
* a map that contains some internal challenge level object data:
	* `Entry<String, Long>`: where String is an island uniqueId, but Long is a rating value.

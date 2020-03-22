## Introduction

**Addon Requests** allow plugins and addons to access to internal addon data without necessarily injecting or overwriting the said addon.

This is especially useful for plugins, whose access to addon's classes is restricted by [Java's ClassLoader visibility principle](https://www.javatpoint.com/classloader-in-java) (which can be summed up as the following: *child ClassLoader can see all the classes loaded by the parent ClassLoader, but the parent ClassLoader cannot see the classes loaded by the child ClassLoader*).

## Available Addon Requests

### Get Challenge List: `challenge-list`

```java
/**
 * Returns a list of challenges that are active in the given world.
 * @param worldName Name of the world (Overworld) the island is in, not null.
 * @return a List containing the strings that represents unique challenge id's in the given world,
 *         or an empty list if the specified world doesn't exist or doesn't contain any challenge.
 */
public List<String> getChallenges(String worldName) {
    return (List<String>) new AddonRequestBuilder()
        .addon("Challenges")
        .label("challenge-list")
        .addMetaData("world-name", worldName)
        .request();
}
```

Possible values returned:
* an empty List if the specified world doesn't exist or doesn't contain any challenge;
* a List containing the strings that represents unique challenge id's.

### Get Challenge Data: `challenge-data`

```java
/**
 * Returns the challenge data for given challenge id.
 * @param challengeId String ID of the challenge, not null.
 * @return a Map that contains some internal challenge object data,
 *         or empty map if challenge is not defined.
 */
public Map<String, Object> getChallengeDataMap(String challengeId) {
    return (Map<String, Object>) new AddonRequestBuilder()
        .addon("Challenges")
        .label("challenge-data")
        .addMetaData("challenge-name", challengeId)
        .request();
}
```

Possible values returned:
* a empty Map if challenge with the given id is not found;
* a map that contains some internal challenges object data:
	* `uniqueId`: the same id that was passed to this handler. (`Entry<String, String>`)
	* `name`: String object of display name for a challenge. (`Entry<String, String>`)
	* `icon`: ItemStack object that represents a challenge. (`Entry<String, ItemStack>`)
	* `levelId`: String object of levelId that this challenge is linked. (`Entry<String, String>`)
	* `order`: Integer object of order number for a given challenge. (`Entry<String, Integer>`)
	* `deployed`: a boolean object of deployment status. (`Entry<String, Boolean>`)
	* `description`: List of strings that represents challenges description. (`Entry<String, List<String>>`)
	* `type`: String object that represents challenges type. (`Entry<String, String>`)
	* `repeatable`: a boolean object of a repeatable option. (`Entry<String, Boolean>`)
	* `maxTimes`: Integer object that represents how many times challenge can be completed. (`Entry<String, Integer>`)


### Get Challenge Level List: `level-list`

```java
/**
 * Returns a list of challenge levels that are active in the given world.
 * @param worldName Name of the world (Overworld) the island is in, not null.
 * @return a List containing the strings that represents unique challenge level id's in the given world,
 *         or an empty list if the specified world doesn't exist or doesn't contain any challenge level.
 */
public List<String> getChallengeLevels(String worldName) {
    return (List<String>) new AddonRequestBuilder()
        .addon("Challenges")
        .label("level-list")
        .addMetaData("world-name", worldName)
        .request();
}
```

Possible values returned:
* an empty List if the specified world doesn't exist or doesn't contain any challenge level;
* a List containing the strings that represents unique challenge level id's.

### Get Challenge Level Data: `level-data`

```java
/**
 * Returns the challenge level data for given challenge level id.
 * @param levelId String ID of the challenge level, not null.
 * @return a Map that contains some internal challenge level object data,
 *         or empty map if challenge level is not defined.
 */
public Map<String, Object> getChallengeLevelData(String levelId) {
    return (Map<String, Object>) new AddonRequestBuilder()
        .addon("Challenges")
        .label("level-data")
        .addMetaData("level-name", levelId)
        .request();
}
```

Possible values returned:
* a empty Map if a challenge level with the given id is not found;
* a map that contains some internal challenge level object data:
	* `uniqueId`: the same id that was passed to this handler. (`Entry<String, String>`)
	* `name`: String object of display name for a challenge level. (`Entry<String, String>`)
	* `icon`: ItemStack object that represents a challenge level. (`Entry<String, ItemStack>`)
	* `world`: String object that represents world name where level operates. (`Entry<String, String>`)
	* `order`: Integer object of order number for a given challenge level. (`Entry<String, Integer>`)
	* `message`: String object that represents level unlock message. (`Entry<String, String>`)
	* `waiveramount`: Integer object of waiver amount for a given challenge level. (`Entry<String, Integer>`)
	* `challenges`: List of strings that represents challenges that are owned by the given level. (`Entry<String, List<String>>`)


### Get Completed Challenges: `completed-challenges`

```java
/**
 * Returns a list of challenge's id which given player is completed in the given world.
 * @param playerUUID Player UUID who's data must be returned, not null.
 * @param worldName Name of the world (Overworld) the island is in, not null.
 * @return a Set containing the strings that represents unique challenge id's in the given world that are completed,
 *         or an empty set if the specified world doesn't exist or player hasn't completed any challenge.
 */
public Set<String> getCompletedChallenges(UUID playerUUID, String worldName) {
    return (Set<String>) new AddonRequestBuilder()
        .addon("Challenges")
        .label("completed-challenges")
        .addMetaData("player", playerUUID)
        .addMetaData("world-name", worldName)
        .request();
}
```

Possible values returned:
* an empty Set if the specified world doesn't exist or player hasn't completed any challenge.;
* a Set containing the strings that represents unique challenge id's that are completed by given player in the given world.


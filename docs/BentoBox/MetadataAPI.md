# BentoBox Persistent Metadata API

BentoBox has a persistent metadata API that enables metadata to be stored on Users, Players or Islands persistently.
This enables addons that do not need or want to handle their own database storage to store data using this API instead.
For example, the Border addon only needs to store a simple boolean that records whether the border is switched on or off
for the user. It would be overkill to store this in a database table, so instead, the addon can place this boolean into
the Player object by way of the User class.

## Quick Example

### Setting metadata
Set the metadata by supplying a string key and a new `MetaDataValue` with the object you want to store.
```
// Place a boolean tag on the user with the value of true and name it Border_state
user.putMetaData("Border_state", new MetaDataValue(true));
```

### Checking metadata
Metadata is read by supplying a string key. The return is an `Optional` that you can check to see if it exists or not
```
// Check if the user has the metadata called Border_state
boolean on = user.getMetaData("Border_state").map(md -> md.asBoolean()).orElse(false);
```

Remember, `getMetaData` returns an `Optional` so if you check for a metadata key and it does not exist, then you will get an `Optional.empty()`.
So if you wish to check explicitly if a tag exists or not, use `isPresent()`:

```
if (user.getMetaData("My_key").isPresent()) {
    // Do something
} else {
    // Do something else
}
```

Of course, you can also use the `ifPresent()` method to perform an action like this:

```
user.getMetaData("My_key").ifPresent(key -> System.out.println("Your key value is " + key.asInt()));
```

However, usually, you want to grab the value and do something with it, so the `map()` and `orElse()` syntax is the most helpful.

### Removing metadata
Metadata can be removed from an Island or User by key.

Example:
```
island.removeMetaData("Bank_balance");
```
If you wish to check that the data was actually removed, then `removeMetaData` returns a `MetaDataValue` which will be the data that was removed or `Optional.empty()` / `null` if it did not exist.

## Supported values
You can store the following types of metadata:

* String
* Integer
* Float
* Double
* Long
* Short
* Byte
* Boolean

## Getters
Although you can store the data without having to specify the type of data, when you get the data you must use the correct getter.
If you do not, your data will be `null`. The getters are as follows:

* `asInt()`
* `asFloat()`
* `asDouble()`
* `asLong()`
* `asShort()`
* `asByte()`
* `asBoolean()`
* `asString()`

Example:
```
String nameTag = user.getMetaData("Level_nametag").map(MetaData::asString).orElse("No nametag");
```

## Key naming convention
Although keys can be named anything, you should avoid clashing with other addons, so the convention is to prefix the key with your addon's name. Examples:

* Level_name
* Challenges_latestChallenge
* Border_state
* etc.

## Island and Player Object Metadata
The Island and Player objects have the same API for metadata as the User class. Although it's possible to manitfulate Player object metadata, it is best done though the User class API.

Island metadata is saved when the server shuts down or when the database is saved periodically.

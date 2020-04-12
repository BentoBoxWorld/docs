# Introduction

BentoBox provides a database API for developers so you do not have to make one yourself. The BentoBox database can be chosen to store data in a flat-file, MySQL, Mongo, SQLite, PostGreSQL, MariaDB, etc. You do not have to worry or care about which one is used. Note that YAML is no longer supported as a database, however it is used for configuration files via the Config API.

## Philosophy

We have taken a "NoSQL" approach to the BentoBox database. i.e., we store serialized Java objects as JSON "blobs" in the database. Each table in the database is assigned to store a specific Java object, e.g., islands, players, challenges, etc. and each entry in the table is one object. The tables have two columns - a unique ID and the JSON object. Databases such as PostgreSQL can store these JSON objects in a binary form, which makes them handle this approach efficiently. 

### How do I access the data from outside BentoBox?
Most of the supported databases, e.g., MySQL, PostgreSQL, etc. support queries on the JSON data directly. The only ones that do not are flat-file based, i.e., JSON and SQLite. Therefore, you should look up the documentation on how to make JSON queries for your database. 

## How To

To store a class in the BentoBox database do the following:

1. Create a class that extends DataObject
2. Define the fields of the class
3. One field must be a string called **uniqueId**. This is the unique id (key) of the object that will be used by the database to identify the object
5. Expose every field you want to store in the database with an @Expose annotation
6. Ensure the class has a [zero argument constructor](https://en.wikipedia.org/wiki/Nullary_constructor)
7. Create a getter and setter for every field - most IDEs should be able to do that for you automatically

**WARNING:** The full canonical name of the class is used to create the table in the database, but the maximum length of that name can only be **64 characters**. So when you define the data object class, make sure that the package and class names are short enough to fit. **ALSO** as BentoBox allows database tables to have a prefix, make sure your canonical name is less than about 60 characters in total to allow for a prefix.

For some field types, especially custom ones, you may have to define your own Adapter class that will handle serialization and deserialization of the field's data.

## Example
```
public class Names implements DataObject {

    @Expose
    private String uniqueId = ""; // name
    @Expose
    private UUID uuid;
    
    public Names() {}
    
    public Names(String name, UUID uuid) {
        this.uniqueId = name;
        this.uuid = uuid;
    }
    
    @Override
    public String getUniqueId() {
        return uniqueId;
    }

    @Override
    public void setUniqueId(String uniqueId) {
        this.uniqueId = uniqueId;        
    }

    /**
     * @return the uuid
     */
    public UUID getUuid() {
        return uuid;
    }

    /**
     * @param uuid the uuid to set
     */
    public void setUuid(UUID uuid) {
        this.uuid = uuid;
    }


}
```

## uniqueID

The DataObject interface contract requires you to override getUniqueId() and a setUniqueID() methods. The uniqueId is a string that is used to identify the data object in the database. A typical uniqueId is the player's UUID (converted to String). If there is only ever going to be one database object, this uniqueId can be a constant, e.g., "TopTen". The uniqueId only has to be to be unique within the scope of data objects of the type you made. It does not have to be unique for every data object ever.

# Instantiating the database object

Once you have created the data object, you must instantiate it to use it. You do that by creating a new BSBDatabase object with BSkyBlock as the first argument and your class as the second. For example:

`BSBDatabase<Names> names = new BSBDatabase<>(plugin, Names.class);`

# Saving data to the database

To write data to the database, do the following:

1. Create an instance of your database object, in this example, the Names class
2. Put data into it, either via the constructor or using the setters
3. Save it to the database using the saveObject() method

For example:

`names.saveObject(new Names(user.getName(), user.getUniqueId()));`

You can save multiple objects to the database by repeating the saveObject method calls. If the object has the same uniqueId as a previously saved object, it will be automatically overwritten.

# Loading data from the database

There are two ways to load data - load specific records (objects) by uniqueId, or load all the objects of this type in one go.

## Loading a single object

To do this, you must know the uniqueId of the record you want. Then use the loadObject method with the uniqueId as the argument. For example:

`Names loadedName = names.loadObject("tastybento");`

If you know what data you want from the loaded object and you are sure it exists, you can grab it directly:

`UUID uuid = names.loadObject(string).getUuid();`

## Loading all the objects

Sometimes you need to load the whole database into memory so it can be accessed all the time. Try not to do this unless you need it. To load all the objects, use the loadObjects() method. This will load them all in as a List. For example:

`List<UUID> uuids = names.loadObjects();`

Note that loading from a database may take a long time and so should not be done on the main thread during the game. You should be able to load objects in an async thread.

# Checking if an object exists in the database

To check if an object exists, you must have its uniqueId. Check it like this example:

`return names.objectExists("tastybento") ? "he exists in the db" : "who?";'

Checking for object existence can also take a long time, so do not do this on the main thread if you can avoid it. 

# Deleting an object in the database

Removing an object requires that you know the uniqueId. Delete objects like this:

`names.deleteObject("tastybento");`

The method will log an error in the console if it cannot delete the object, but otherwise it will be silent.

Currently, there is no way to delete all objects in the database.

# Closing the database

Database connections are set to auto close when the plugin is disabled, but if you wish to explicitly close the connection to save resources, use this method:

`names.close()`

This will release the connection object's database and any JDBC resources immediately instead of waiting for them to be automatically released.

# Object type support

*YAML database is no longer supported!*
The database uses GSON to serialize the object. This handles most generic object types and all Bukkit classes that implement the [ConfigurationSerializable](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/configuration/serialization/ConfigurationSerializable.html) interface, for example:

* World
* Location
* Vector (Bukkit's Vector)
* PotionEffectType
* etc.

If you implement an object that must be serialized and stored in the database then it should implement Bukkit's [ConfigurationSerializable](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/configuration/serialization/ConfigurationSerializable.html) interface. 
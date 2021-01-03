# BentoBox Config API

This is an optional API that enhances the Bukkit config API for YAML files. The BentoBox Config API adds the following features:

1. The config file can retain comments even after saving
2. The config file can be updated with new settings when you update your addon
3. The config class is also where you go to get and set settings

If you do not want to use this API, you can use the standard Bukkit API methods such as saveDefaultConfig(), getConfig(), etc.

## Getting started - an example

Let's say we want to make a config file for our new plugin. Perhaps it will look like this:

```yaml
# This is my config.yml file
# It is for my addon

world:
  # This is the name of the world.
  name: My_world_name
  # Size - minimum is 10, max is 100
  size: 100
```

### ConfigObject
To use the config API, we create a new class that implements `ConfigObject`:

```java
public class Settings implements ConfigObject {

}
```

We now must specify where this config object will be saved. The location is relative to the addon's data folder.

```java
@StoreAt(filename="config.yml") // Explicitly call out what name this should have.
public class Settings implements ConfigObject {

}
```

### @ConfigEntry
Next, we must add the data fields we want in the config. To do that, we use the `@ConfigEntry` annotation:

```java
@StoreAt(filename="config.yml") // Explicitly call out what name this should have.
public class Settings implements ConfigObject {
    @ConfigEntry(path = "world.name")
    private String worldName = "My_world_name";

    @ConfigEntry(path = "world.size")
    private int worldSize = 100;
}
```

Note how the fields have a default value assigned to them.

### Getters and Setters
Next, we must add getters and setters to access these fields. The names of the getters and setters and parameter names must meet the [JavaBeans Naming Conventions](https://www.oreilly.com/library/view/javaserver-pages-3rd/0596005636/ch20s01s01.html):

```java
@StoreAt(filename="config.yml") // Explicitly call out what name this should have.
public class Settings implements ConfigObject {
    @ConfigEntry(path = "world.name")
    private String worldName = "My_world_name";

    @ConfigEntry(path = "world.size")
    private int worldSize = 100;

    public String getWorldName() {
        return worldName;
    }
    public void setWorldName(String worldName) {
        this.worldName = worldName;
    }
    public int getWorldSize() {
        return worldSize;
    }
    public void setWorldSize(int worldSize) {
        this.worldSize = worldSize;
    }
}
```

### `@ConfigComment`
Next, we can add comments using the `ConfigComment` annotation:

```java
@StoreAt(filename="config.yml") // Explicitly call out what name this should have.
@ConfigComment("This is my config.yml file") // Note that the comment will automatically
@ConfigComment("It is for my addon") // be proceeded with a # and space
public class Settings implements ConfigObject {
    @ConfigEntry(path = "world.name")
    @ConfigComment("This is the name of the world.")
    private String worldName = "My_world_name";

    @ConfigEntry(path = "world.size")
    @ConfigComment("Size - minimum is 10, max is 100")
    private int worldSize = 100;

    public String getWorldName() {
        return worldName;
    }
    public void setWorldName(String worldName) {
        this.worldName = worldName;
    }
    public int getWorldSize() {
        return worldSize;
    }
    public void setWorldSize(int worldSize) {
        this.worldSize = worldSize;
    }
}
```

### Loading and Saving

To load a config with the Addon class, do this:

```java
Settings settings = new Config<>(this, Settings.class).loadConfigObject();
```

To save a config in the Addon class, do this:

```java
Settings settings = new Settings();
new Config<>(this, Settings.class).saveConfigObject(settings);
```

It is good practice for an addon to load the settings, then save them immediately. This will keep the config file up to date with the latest options and comments. To create the initial config, use the Addon's `saveDefaultConfig()` method to save the default config.yml stored in the addon's jar. If you are using a different file that config.yml, you can use the `saveResource(resourcePath, replace)` method.

### Default config file
Set up a default config.yml file in your addon jar. Then save it to the file system in your addon using the standard `saveDefaultConfig()` method. So the overall approach is as follows:

1. saveDefaultConfig() - this will save the default config.yml from the jar if it does not exist.
2. Load config using Config API to obtain the admins settings
3. Save config using Config API to update config.yml with the latest setting options and comments

That's it! Please read the JavaDocs for more information on this API.

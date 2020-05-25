# Introduction

BentoBox relies on **_Addons_ to provide new features or new _Gamemodes_**.
This tutorial will guide you through the process of **creating your first addon**.

Creating an Addon is often easier and quicker than creating a plugin from scratch, because BentoBox provides [wrappers](https://en.wikipedia.org/wiki/Wrapper_function) and key API features.
Addons also have direct access to the other addons' API, unlike plugins, due to the [visibility principle of Java Classloaders](https://www.javatpoint.com/classloader-in-java).
Moreover, they have access to BentoBox's [Config API](../../BentoBox/Config-API.md) and [Database API](../../BentoBox/Database-API.md).

In order to comfortably follow this tutorial, you should have previous experience in plugin development.
The addon development process is indeed very similar to the latter, and we will consider throughout this tutorial that you understand the key Java concepts, for the sake of concision.

# Prepare the project

## Using the pre-made Addon template

The template currently does not exist.

## Manually creating the project

### Import BentoBox as a dependency

BentoBox holds all the API you will need to create and register your addon.
Therefore, you should add it as a dependency of your project.

BentoBox uses Maven and our Maven repository is kindly provided by [CodeMC](https://codemc.org/).
However, you can also use Gradle to grab BentoBox.

#### Maven

Add the following to your `pom.xml` file.

```xml
<repositories>
  <repository>
    <id>codemc-repo</id>
    <url>https://repo.codemc.org/repository/maven-public/</url>
  </repository>
</repositories>

<dependencies>
  <dependency>
    <groupId>world.bentobox</groupId>
    <artifactId>bentobox</artifactId>
    <version>PUT-VERSION-HERE</version>
    <scope>provided</scope>
  </dependency>
</dependencies>
```

#### Gradle

Add the following to your `build.gradle` file.

```groovy
repositories {
  maven { url "https://repo.codemc.org/repository/maven-public/" }
}

dependencies {
  compileOnly 'world.bentobox:bentobox:PUT-VERSION-HERE'
}
```

If you have any issues, please have a look at [Gradle's documentation about declaring dependencies](https://docs.gradle.org/current/userguide/declaring_dependencies.html).

### Setup the project architecture

# Create the main Addon class

The **main class of an Addon** works similarly as to one of a plugin.
It most notably handles the code that runs when laoding, enabling, reloading and disabling the addon.

The main class **extends `Addon`**. 

*Example:*
```java
import world.bentobox.bentobox.api.addons.Addon;

public class MyAddon extends Addon {

}
```

!!! tip
    When naming your main class, consider the following:
    We recommend you to keep its name as close to the addon's name as possible.
    You can also append "Addon" to the class name to further disambiguate its purpose.

*Genuine examples*: [Greenhouses](https://github.com/BentoBoxWorld/Greenhouses/blob/develop/src/main/java/world/bentobox/greenhouses/Greenhouses.java),
[Chat](https://github.com/BentoBoxWorld/Chat/blob/develop/src/main/java/world/bentobox/chat/Chat.java),
[Biomes](https://github.com/BentoBoxWorld/Biomes/blob/develop/src/main/java/world/bentobox/biomes/BiomesAddon.java).

## Mandatory methods

Like Bukkit plugins, Addons must override a few methods in order to be properly enabled.

As such, your main Addon class should look like the following:

```java
import world.bentobox.bentobox.api.addons.Addon;

public class MyAddon extends Addon {
    @Override
    public void onEnable() {}
    
    @Override
    public void onDisable() {}
}
```

### onEnable()

This method is called after `#onLoad()`.

### onDisable()

## Optional methods

Additional methods can be overridden if needs be.

```java
import world.bentobox.bentobox.api.addons.Addon;

public class MyAddon extends Addon {
    @Override
    public void onLoad() {}

    @Override
    public void onEnable() {}

    @Override
    public void onReload() {}
    
    @Override
    public void onDisable() {}
}
```

### onLoad()

### onReload()

# Create the addon.yml


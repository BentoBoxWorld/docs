# Introduction

BentoBox relies on **_Addons_ to provide new features or new _Gamemodes_**.
This tutorial will guide you through the process of **creating your first addon**.

Creating an Addon is often easier and quicker than creating a addon from scratch, because BentoBox provides [wrappers](https://en.wikipedia.org/wiki/Wrapper_function) and key API features.
Addons also have direct access to the other addons' API, unlike plugins, due to the [visibility principle of Java Classloaders](https://www.javatpoint.com/classloader-in-java).
Moreover, they have access to BentoBox's [Config API](../../BentoBox/Config-API.md) and [Database API](../../BentoBox/Database-API.md).

In order to comfortably follow this tutorial, you should have previous experience in addon development.
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

The **main class of an Addon** works similarly as to one of a addon.
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

This method is called when the Addon is being disabled, which usually occurs when the server is being shutdown.

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
The code in the onLoad() method is run when the Addon is loaded and before onEnable(). It is a good place to load configs and set up commands if this addon is a game mode:
```
    @Override
    public void onLoad() {
        // Save the default config from config.yml
        saveDefaultConfig();
        // Load settings from config.yml. This will check if there are any issues with it too.
        loadSettings();
        // Register game mode commands
        playerCommand = new DefaultPlayerCommand(this)

        {
            @Override
            public void setup()
            {
                super.setup();
                new IslandAboutCommand(this);
            }
        };
        adminCommand = new DefaultAdminCommand(this) {};
    }
```

### onReload()
The code in this method is run when (or if) the admin reloads Addons using the `bbox reload` command.

# Create the addon.yml
The addon.yml is required to describe your addon to BentoBox. It is almost identical to plugin.yml used by Bukkit. Here is a minimal example:

```
name: Bank
main: world.bentobox.bank.Bank
version: 1.0.0
api-version: 1.15.4
authors: tastybento
```
The above tags are mandatory and must be included in every addon.yml.<br>

<table cellspacing="0" cellpadding="4" border="1">
   <caption>addon.yml Attributes
   </caption>
   <tbody>
       <tr>
           <th>Attribute
           </th>
           <th>Required
           </th>
           <th>Description
           </th>
           <th>Example
           </th>
           <th>Notes
           </th>
       </tr>
       <tr style="font-weight: bold;">
           <td>name
           </td>
           <td>yes
           </td>
           <td>The name of your addon.
           </td>
           <td>
               <code>name: MyAddon</code>
           </td>
           <td>
               <ul>
                   <li>Alphanumeric characters and underscores (a-z,A-Z,0-9, _)</li>
                   <li>Used to determine the name of the addon's data folder. Data folders are placed in the ./addons/ directory by default.</li>
                   <li>It is good practice to name your jar the same as this, for example 'Bank.jar'</li>
               </ul>
           </td>
       </tr>
       <tr style="font-weight: bold;">
           <td>version
           </td>
           <td>yes
           </td>
           <td>The version of this addon.
           </td>
           <td>
               <code>version: 1.3.1</code>
           </td>
           <td>
               <ul>
                   <li>Version is an arbitrary string, however the most common format is MajorRelease.MinorRelease.Build (eg: 1.4.1).</li>
                   <li>Typically you will increment this every time you release a new feature or bug fix.</li>
                   <li>
                       Displayed when a user types 
                       <code>/bbox version</code>
                   </li>
               </ul>
           </td>
       </tr>
       <tr>
           <td>description
           </td>
           <td>no
           </td>
           <td>Person friendly description of the functionality your addon provides.
           </td>
           <td>
               <code>description: This addon is so boxy.</code>
           </td>
           <td>
               <ul>
                   <li>The description can have multiple lines.</li>
                   <li>
                       Displayed when a user types 
                       <code>/version addonName</code>
                   </li>
               </ul>
           </td>
       </tr>
       <tr>
           <td>authors
           </td>
           <td>yes
           </td>
           <td>Allows you to list one or multiple authors, if it is a collaborative project. If you list more than one then use a YAML string list format.
           This is actually a mandatory item.
           </td>
           <td>
<code>authors:
- BONNe
- tastybento</code><br>
or<br>
<code>authors: tastybento</code>
           </td>
           <td>
               <ul>
                   <li>You can list one author or multiple authors.</li>
               </ul>
           </td>
       </tr>
       <tr style="font-weight: bold;">
           <td>main
           </td>
           <td>yes
           </td>
           <td>Points to the class that extends Addon or Pladdon
           </td>
           <td>
               <code>main: world.bentobox.acidisland.AcidIsland</code>
           </td>
           <td>
               <ul>
                   <li>Note that this must contain the full namespace including the class file itself.</li>
                   <li>
                       If your namespace is 
                       <code>world.bentobox.addon</code>
                       , and your class file is called 
                       <code>Myaddon</code>
                        then this must be 
                       <code>world.bentobox.addon.Myaddon</code>
                   </li>
               </ul>
           </td>
       </tr>
       <tr>
           <td>depend
           </td>
           <td>no
           </td>
           <td>A list of addons that your addon requires to load.
           </td>
           <td>
               <code>depend: Oneaddon, Anotheraddon</code>
           </td>
           <td>
               <ul>
                   <li>
                       The value is comma delimited
                   </li>
                   <li>Use the "name" attribute of the required addon in order to specify the dependency.</li>
                   <li>If any addon listed here is not found your addon will fail to load.</li>
                   <li>If multiple addons list each other as a depend, so that there are no addons without an unloadable dependency, all will fail to load.</li>
               </ul>
           </td>
       </tr>
       <tr>
           <td>softdepend
           </td>
           <td>no
           </td>
           <td>A list of addons that your addon may require but are not mandatory.
           </td>
           <td>
               <code>softdepend: AcidIsland, BSkyBlock, SkyGrid, CaveBock, AOneBlock</code>
           </td>
           <td>
               <ul>
                   <li>
                       The value is comma delimited.
                   </li>
                   <li>Use the "name" attribute of the desired addon in order to specify the dependancy.</li>
                   <li>Your addon will load after any plugins listed here.</li>
                   <li>Circular soft dependencies are loaded arbitrarily.</li>
               </ul>
           </td>
       </tr>
       <tr>
           <td>permissions
           </td>
           <td>no
           </td>
           <td>Permissions that the addon wishes to register. Each node represents a permission to register. Each permission can have additional attributes.
           </td>
           <td>
               <pre>permissions:    
  '[gamemode].intopten':
    description: Player is in the top ten.
    default: true
  '[gamemode].island.level':
    description: Player can use level command
    default: true
  '[gamemode].island.top':
    description: Player can use top ten command
    default: true</pre>
           </td>
           <td>
               <ul>
                   <li>Permission registration is optional, can also be done from code</li>
                   <li>Permission registration allows you to set descriptions, defaults, and child parent relationships</li>
                   <li>Permission names can include the <code>[gamemode]</code> tag to enable the permission to apply to all the loaded game modes on the server.</li>
               </ul>
           </td>
       </tr>
   </tbody>
</table>

# Pladdons
Pladdons are a combination of a Bukkit Plugin and Addon. The main benefit of a Pladdon is that it is loaded with the Bukkit Server class loader and so data within it can be accessed directly by Plugins. If you are writing a utility Addon, for example, a Level addon, then other Plugin writers may want to access the data it generates in code via an API. The simplest way to do this is to make a Pladdon and they can call methods in your code directly. If you do **not** want plugins to access data in your addon, then keep it as an Addon.

## Making the Addon a Pladdon
To do this, make a class with the recommended name of `MyAddonPladdon.java`, where MyAddon is the same name as your Addon and extend `Pladdon`. Instead of creating a `plugin.yml` the components are declared using Annotations. The annotations should be as below. The ApiVersion may be updated to the latest server version if you require it.

```
@Plugin(name="Pladdon", version="1.0")
@ApiVersion(ApiVersion.Target.v1_16)
@Dependency(value = "BentoBox")
public class LevelPladdon extends Pladdon {
    @Override
    public Addon getAddon() {
        return new Level();
    }
}
```

The only method that should be defined is the `getAddon()` method that must return an instance of your Addon.

Once this is done, the Addon will be loaded just like a plugin and will be able to be accessed via other plugins.





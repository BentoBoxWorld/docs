= Table of Contents
:toc:

= Introduction
A game mode is an add-on like BSkyBlock or AcidIsland. What makes it a game mode add-on is that it will create and register a *world* with BentoBox and supply BentoBox with a WorldSettings class object.

Currently, worlds registered with BentoBox must be over-worlds, but once a world is registered, any associated Nether and End worlds will also belong to this game mode add-on.

To show how this all works, let's look at the BSkyBlock code (some lines removed for clarity):

[source,java]
----
    @Override
    public void onLoad() {
        // Save the default config from config.yml
        saveDefaultConfig();
        // Load settings from config.yml. This will check if there are any issues with it too.
        settings = new Config<>(this, Settings.class).loadConfigObject();
        // Load or create worlds
        bsbWorlds = new BSkyBlockWorld(this);
    }
----

The comments are pretty clear, but the first two calls are to set up the config.yml file and the settings. In this case, we are using the Config class from the BentoBox Configuration API which enables dynamic saving of YAML files with comments. This is a powerful config API. You do *not* have to use it if you do not want to. Instead, you can just use the regular Bukkit-style config system. We used it because it enables us to keep the config.yml file up to date automatically.

= The Settings Class

Let's look at the Settings class (again, some lines have been removed for clarity):

[source,java]
----
@StoreAt(filename="config.yml", path="addons/BSkyBlock") // Explicitly call out what name this should have.
@ConfigComment("BSkyBlock Configuration [version]")
@ConfigComment("This config file is dynamic and saved when the server is shutdown.")
@ConfigComment("You cannot edit it while the server is running because changes will")
@ConfigComment("be lost! Use in-game settings GUI or edit when server is offline.")
@ConfigComment("")
public class Settings implements DataObject, WorldSettings {

    @ConfigComment("Allow obsidian to be scooped up with an empty bucket back into lava")
    @ConfigEntry(path = "general.allow-obsidian-scooping")
    private boolean allowObsidianScooping = true;

...
----

What you see here are a lot of notations followed by the class declaration, followed by more notations around a field declaration. Let's take these one by one:

. The @StoreAt annotation before the class defines where this config file will be stored. It is relative to the data folder of the BentoBox plugin. Files should only ever be stored within the BentoBox folder. It is very important that you declare this location explicitly!
. The @Comment annotation is used to add a line of comment into the YAML file. The "[version]" placeholder is automatically replaced with the version number of the add-on.
. The class must implement both DataObject and WorldSettings. DataObject is used so the class can be saved in the database (via BBConfig) and WorldSettings is used because this is a Game Mode add-on
. The field "allowObsidianScooping" is declared, along with a default value and it has a comment annotation and a @ConfigEntry annotation. This one is used to define where this value will be placed in the YAML file. Note that YAML entries are generally placed in the same order as they are written in the code unless the @ConfigEntry forces them to be placed elsewhere.
. After the field is declared, you also need to create a getter and setter for the field. (Not shown in the code)

Note that by implementing the WorldSetting interface, you will have to @Override a number of getters for mandatory world settings. In the BSkyBlock Settings class almost all of these are loaded from the config file. One exception is the *Optional<Addon> getAddon()*. This must return the add-on instance. Right now, the add-on must set this. In the future, BentoBox may set it.

= Registering the World with BentoBox

Now let's take a closer look at the BSkyBlockWorld class mentioned above. This class does three main things:

. Makes the worlds for BSkyBlock (creates the worlds and defines generators for them)
. Registers the main over world and the settings class with BentoBox
. Registers the schems that will be used when creating new islands with the IslandCreate class

This is how it does it:

[source,java]
----
// Create the world if it does not exist
islandWorld = WorldCreator.name(worldName).type(WorldType.FLAT).environment(World.Environment.NORMAL)
    .generator(new ChunkGeneratorWorld(addon)).createWorld();

// Register the world and settings with BentoBox
addon.getPlugin().registerWorld(islandWorld, addon.getSettings());

// Make the nether and end worlds if required (not shown)

// Load schematics
addon.getPlugin().getSchemsManager().loadIslands(islandWorld);
----

In this code, *addon* is the add-on instance. getPlugin() is used to get BentoBox and registerWorld() is used to register the world. Note that you do *NOT* register the nether and end worlds with BentoBox. You only register the overworld. BentoBox will assume that any associated Nether or End are also owned by your add-on if they exist.

For schems, (BentoBox's own proprietary schematics file format), you should have schems for the default island for each world in your add-on's schems folder. They must be named as follows:

* island.schem (Mandatory)
* nether-island.schem (Optional)
* end-island.schem (Optional)

To make schems, use BentoBox's schem command (or BSkyBlock's or AcidIsland's schem command).

= Registering commands

After you have registered the world, the associated world/game mode settings and the schems, the next step is to make your add-on do something. If it requires commands, you can make them by extending CompositeCommand. Let's look at how BSkyBlock registers it's top-level command */island* and sub commands under it:

[source,java]
----
public class IslandCommand extends CompositeCommand {

    public IslandCommand(BSkyBlock addon) {
        super(addon, "island", "is");
    }

    @Override
    public void setup() {
        setOnlyPlayer(true);
        // Permission
        setPermissionPrefix("bskyblock");
        setPermission("island");
        setWorld(((BSkyBlock)getAddon()).getIslandWorld());
        // Set up subcommands
        new IslandAboutCommand(this);
        new IslandCreateCommand(this);
        new IslandGoCommand(this);
        new IslandResetCommand(this);
        new IslandSetnameCommand(this);
        new IslandResetnameCommand(this);
        new IslandSethomeCommand(this);
        new IslandSettingsCommand(this);
        new IslandLanguageCommand(this);
        new IslandBanCommand(this);
        new IslandUnbanCommand(this);
        new IslandBanlistCommand(this);
        // Team commands
        new IslandTeamCommand(this);
    }
----

The key line for registering the command is:

```
super(addon, "island", "is");
```

This tells BentoBox that "/island" is a top-level command for BSkyBlock add-on and it has an alias of "/is". Then in the setup() method, there are a number of very important (mandatory for top-level commands) declarations:

```
setWorld(((BSkyBlock)getAddon()).getIslandWorld());
```

This is extremely important. It defines the world that this command will operate in. All sub-commands will refer to this using the getWorld() method. 

After that, the command instantiates a number of sub-commands, passing itself as a parameter. These classes will use that parameter as the parent in their respective super() calls.

= Conclusion

The above describes what should be done if you are creating a new game mode type add-on. We are continuing to work on the API, so some things may become simpler in the future to accomplish.


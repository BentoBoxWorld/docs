# Level API

Level provides an API for other plugins. This covers Level 2.8.1 and onwards.

Add the Level dependency to your Maven POM.xml:

```
        <dependency>
            <groupId>world.bentobox</groupId>
            <artifactId>level</artifactId>
            <version>2.8.1</version>
            <scope>provided</scope>
        </dependency>
```
Use the latest Level version.

Then you can obtain the level for a player by asking Level once you have the world that the island is in and confirming that the player is the owner of an island in that world.


```
// Get the game mode world for the game mode you are requesting, e.g., BSkyBlock 
World w = BentoBox.getInstance().getIWM().getOverWorld("BSkyBlock");
if (w == null) {
    // World does not exist - is BSkyBlock loaded?
    return;
}
UUID owner = BentoBox.getInstance().getIslandsManager().getOwner(w, playerUUID);
if (owner == null) {
    // This player is not the owner of an island in this world
    return;
}
// Get the level
long level = BentoBox.getInstance().getAddonsManager().getAddonByName("Level").map(l -> ((Level) l).getIslandLevel(w, owner)).orElse(0L);
```

The JavaDocs for Level can be found [here](https://ci.codemc.io/job/BentoBoxWorld/job/Level/ws/target/apidocs/index.html).


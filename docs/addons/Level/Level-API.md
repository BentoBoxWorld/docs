# Level API

Level provides an API for other addons and plugins. This covers Level 2.3.0 and onwards.

## For Plugins

As Level is loaded by BentoBox, it is not possible to directly interact with the classes it uses due to Java Classloader protections. So, you must use the key-value API provided by BentoBox.

Here is an example plugin that shows how to obtain the key-value pairs and change them:

```
package us.tastybento.test;

import org.bukkit.Bukkit;
import org.bukkit.event.EventHandler;
import org.bukkit.event.EventPriority;
import org.bukkit.event.Listener;
import org.bukkit.plugin.java.JavaPlugin;

import world.bentobox.bentobox.api.events.addon.AddonEvent.AddonGeneralEvent;

public class TestPlugin extends JavaPlugin implements Listener {

    @Override
    public void onEnable() {
        Bukkit.getPluginManager().registerEvents(this, this);
    }

    @EventHandler(priority = EventPriority.NORMAL, ignoreCancelled = true)
    public void onLevel(AddonGeneralEvent e) {
        Bukkit.getLogger().info("DEBUG: " + e.getEventName());
        e.getKeyValues().entrySet().stream().forEach(en -> Bukkit.getLogger().info("Key " + en.getKey() + " Value " + en.getValue()));
        // Set the new value
        if (e.getKeyValues().containsKey("eventName") && e.getKeyValues().get("eventName").equals("IslandLevelCalculatedEvent")) {
            Bukkit.getLogger().info("DEBUG: setting new values");
            e.getKeyValues().compute("level", (k,v) -> 500L);
            e.getKeyValues().compute("deathHandicap", (k,v) -> 5);
            e.getKeyValues().compute("pointsToNextLevel", (k,v) -> 50L);
            e.getKeyValues().compute("initialLevel", (k,v) -> 1L);
        }
        Bukkit.getLogger().info("DEBUG: Now set to:");
        e.getKeyValues().entrySet().stream().forEach(en -> Bukkit.getLogger().info("Key " + en.getKey() + " Value " + en.getValue()));
    }

}
```

You do not need to include Level as a dependency in your POM because you never directly interact with it.

The specific key values that Level provides are:

* eventName: which will always be "IslandLevelCalculatedEvent"
* targetPlayer, (UUID) targetPlayer's
* islandUUID - (String) the unique id of the island
* level - (Long) the calculated island level
* pointsToNextLevel - (Long) points to the next level as calculated
* deathHandicap - (int) the number of levels lost due to deaths in this world
* initialLevel - (Long) the initial level of the island. This is deducted from the overall island level
* isCancelled - (Boolean) will be false. If set to true, then island calculation will just stop

Don't forget to cast the key values to their correct types otherwise you will cause errors



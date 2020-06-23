# Blueprints
**Blueprints** are a simple a quick way to make your own custom starter islands inside the game.

Blueprints are *like* WorldEdit schematics but are **not** compatible. Blueprints are optimized for BentoBox addons and do not require any other plugin or library to use.

Blueprints are managed with the **Blueprint Manager** and can be bundled together into a **Blueprint Bundle** to contain a set of up to 3 islands (normal world, nether and end world). Blueprint Bundles can have their own icon, description and can contain other settings, like requiring permission to use.

### FAQ: I have a lot of schematics - how do I convert them to Blueprints?

It's quite easy, but you have to do it in-game because you'll need to add some signs to it.

Steps:

1. Load the schematic using WorldEdit
2. Paste it somewhere, I recommend some space in the BSKyBlock world away from everything
3. Find where you want the player to spawn and place a sign there with the text [spawn_here] on it.
4. (Optional) Place a welcome sign facing the place that has the text [start] on it. For details on these signs, look below
5. Select the island using the admin blueprint commands pos1 and pos2 (Remember to use the blueprint command and not WE!)
6. Copy the island using the admin blueprint copy command
7. Save the island using the admin blueprint save command
8. Repeat for all your islands including Nether and End islands.

Tips: Make sure you have a bedrock block in the center of the island. This is where the island will be centered around.

## Asynchronous
All Blueprint copying and pasting is done async and should __never__ lag the server no matter how large the Blueprint. It can take a number of seconds to paste very large Blueprints. You can set how many blocks will be copied or pasted by editing the paste speed in BentoBox's config.yml. The default should be acceptable for most systems. If you run timings, you may see the pasting process taking a long time, but it is just doing about 1000 blocks per tick and should not be lagging your system.

## Operation
The basic flow for making a custom island:

1. Create a bounding box by setting two positions at opposite corners of the box - set pos1 and pos2
2. Copy the contents of the box to the clipboard
3. Save the contents. If you just want to overwrite the default islands, save as "island", "nether-island" or "end-island" - you will be asked to confirm the overwriting.
4. Open up the Blueprint Manager, e.g., /bsb blueprint to make a new Bundle, set icons, group Blueprints, etc.

### Video
*Click on the thumbnail!*
[![thumbnail](https://user-images.githubusercontent.com/20014332/62939503-be4c5980-bdd1-11e9-8814-2253845cecd0.png)](https://youtu.be/4gvaG89uxAs)

## Commands
The commands are almost the same as WorldEdit schematic commands. You must be Op or an admin with permissions to use blueprints. Use the admin command and **blueprint** or its alias **bp**:

* /bsb bp pos1 - set one corner of the bounding box to the position of your player
* /bsb bp pos2 - set the other corner
* /bsb bp copy - copy the blocks and entities inside the box to the clipboard
* /bsb bp copy air - copy the blocks, entities, and air inside the box to the clipboard. This is important if you plan to paste the island into water (AcidIsland) or rock (CaveBlock).
* /bsb bp paste - paste the clipboard to your location
* /bsb bp save <name> - saves the clipboard to a file (appends a .schem suffix)
* /bsb bp load <name> - load a blueprint file (do not append the .schem suffix)
* /bsb bp - open the Blueprint Manager GUI

For AcidIsland, use /acid instead of /bsb.

## Blueprint Manager GUI
The Blueprint Manager GUI enables you to create, edit and configure the island sets that players can select when they start a new island or reset. The sets of islands (normal world, nether world, and end world) are called "bundles". There is a default bundle that can be customized, but not deleted.

To create a new bundle, click on the green banner in the bottom left corner of the GUI. Text entry is done via the chat interface. Enter a name for the new bundle. You can change it later.

The new bundle will have a default red wool icon and a name. It has three slots to the right that represent the places where you can put 3 blueprints:

* Green glass pane - this is the normal world blueprint slot
* Red glass pane - this is the nether world blueprint slot
* Yellow glass pane - this is the end world blueprint slot

Right click on these slots to clear them.

Below the line of dark gray glass panes, you will see a number of blueprints to choose. Click on the one you want and it will glow. Then click on the slot where you want to put it. You can put the same blueprint in all three slots or have different blueprints for each one, it is up to you.

To add a description to the bundle right click on the bundle icon and enter a description in the chat. Keep each line short so the GUI does not look too big. You can set the text color using Bukkit color codes, like &c for red.

To change a bundle's icon, click on an item in your inventory and it will replace the bundle's icon. To change a blueprint's icon, select the blueprint and then click on the inventory item.

To limit a bundle to players with the right permission, click the picture item to toggle whether permission is required or not. The icon will show what permission is required in its text (it is based on the name of the bundle). The permission is `GameModeAddonName.island.create.uniqueId` of blueprint bundle. e.g. `bskyblock.island.create.vip`.

To delete a bundle, right click on the TNT.

Bundles and blueprints must be renamed in the GUI. Do not try to rename them using the file system.

## Files and Editing
When using blueprints in the game, always use just the name of the blueprint. On the file system, blueprints are saved in a compressed format with the **.blu** suffix and blueprint bundles are saved as **.json** text files. You can edit the JSON blueprint bundles with a text editor, but you should never edit .blu files outside of the game.

## Incomplete bundles
Bundles must always have an Overworld/Normal world blueprint. If they do not, then the default island (island.blu) blueprint will be used and an error logged in the console.
Bundles do not have to have Nether or End World blueprints, but if they do not, no island will be pasted in those worlds (obviously).

## Entities

!!! new "Coming in BentoBox 1.14.0"
    In this upcoming release, you will also be able to use `[name]`, which will be replaced by the island owner's name when creating the island.

You can use placeholders in entities' names.
Rename a name tag with the placeholder in an anvil, then apply the name tag to the entity.

## Signs
Blueprints can have two special signs in them to help you place where a player will spawn and to give them a welcome message.

### Spawn Here Sign
Place a sign with the first line as [spawn_here] where you want the player to spawn. They will appear in this position and the sign will not be pasted. This applies to all world islands, so you can specify where players will appear in the Nether when they go through a portal, for example.

### Welcome Sign
The welcome sign provides a friendly way to give players a hint about the game and what to do, or not do! Place a sign with [start] on the first line. The sign's text will be replaced by the sign text in the GameModeAddon's locale file.

## Tips & Recommendations
* We recommend that you keep starting islands small to make the game a challenge. Put just enough items and blocks on an island for players to be able to grow their island.
* Try making split islands (think up and down, side to side) to give players a target to build to when they have the resources.
* If you are copying with air, try to make your bounding box as small as possible to keep the file size small.
* After copying a blueprint, try pasting it to check it was copied correctly. Then save it.

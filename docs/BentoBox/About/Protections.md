# Protection
BentoBox provides a full-featured world and island protection system for island GameModes.  Configuration is done in-game via the admin or player settings, and out of game via permissions and config files.

## What is Protection?
Multiplayer Minecraft provides no built-in protection for the map except for the area immediately around spawn. As a result, any random player can damage or "grief" someone else's area that they have put time into. With BentoBox, players have their own islands and the protection system prevents or limits what other players can do in this space.

Protection also extends to limiting which commands can be executed. For example, an admin can prevent teleportation commands from being run when a player is falling to prevent them cheating fall damage. 

### What about WorldGuard?
WorldGuard is a protection plugin that also provides protection functions. BentoBox does not use WorldGuard and it is recommended that it is turned off in BentoBox worlds to avoid clashes. Admins can use WorldGuard if they like in BentoBox worlds, but they should consider that there may be clashes between the two systems.

## How is Protection Managed In BentoBox?
BentoBox uses the concept of "flags" to manage protection settings. There are three types of flags:

 1. **Protection flags** - these are explicitly designed to allow or disallow some facet of world or island protection.
 2. **Settings flags** - these are generally true/false or on/off settings that can be applied. They may provide protection.
 3. **World Settings flags** - these are settings flags that determine how things operate in the game world in general.

### Protected areas
BentoBox has two areas of protection:

 1. The player's island
 2. Everywhere else, the rest of the world

These areas are generally handled independently, but certain world settings may apply to the player's island. Island owners generally have the ability to set the settings for their own island and admins configure the settings for everywhere else. Admins also can determine the default settings for an island to have by adjusting the game mode's `config.yml`.

The player's island protection area is set by default in the game mode's `config.yml` and can be expanded or reduced in-game via admin commands or by the player having a permission. The maximum protection size is governed by the distance between islands, which is also set in the game mode `config.yml`.

### Changing Settings
BentoBox provides an island settings GUI to island owners that enables them to see the island settings. Admins can reduce the island settings visible via the admin settings GUI. Admins can allow players to change settings via permissions. The default is that players can change all the settings they can see.

## Protection Provided
There are a lot of protection flags and new ones are added. This section covers the most important levels of protection. Protections can be restricted for the various ranks available, i.e.:

 - Visitor
 - Coop
 - Trusted
 - Member
 - Sub-Owner

Owners can always do everything.

Every time a player tries to do something in a protected area, BentoBox will determine if they have the right to do it or not. If they do not, they will be blocked from doing it and depending on the type of activity told that they cannot do it. 

### Finding out why something can or cannot be done
BentoBox provides an admin tool to explain why something can or cannot be done. It is the admin `why <player>` command, e.g., `/bsb why tastybento`. When this is used, the console will record the reason why the player can do something or cannot. This can help admins understand their settings. Also, if the why command says that a player can do something but in-game they cannot, then that indicates another plugin (or the server itself) is preventing the action.

### Protections
* Breaking and Placing Blocks
* Block Interaction
  * Containers
  * Anvils
  * Buttons
  * Beds
  * Doors and trap doors
  * Beacons
  * Brewing stands
  * Cauldrons
  * Barrels
  * Beehives
  * Bee nests
  * Composters
  * Furnaces, smokers, and campfires
  * Enchanting tables
  * Jukeboxes and note blocks
  * Crafting tables
  * Levers
  * Redstone-related blocks
  * Dragon Eggs
  * Item Frames
  * Berry picking
  * Cake eating
  * Gate usage
* Breeding
* Bucket use
* Dye use
* Egg use
* Elytra use
* Interaction with:
  * Vehicles, including boats, minecrarts and ridable animals like horses, etc.
  * Villager trading
  * Name tag protection
* Item or experience pickup or item dropping
* Fire-related: prevention of ignition, spreading, burning, lightning-related, etc.
* Damaging or hurting monsters or animals
* Leash use
* Lectern use
* Physical interactions
* Portal use
* Sheering
* Teleportation, e.g., using chorus fruit or ender pearls
* Throwing of items, including potions
* TNT or other explosion protections

### Island Settings

These are settings that an owner can change for their island. Admins should configure permissions appropriately to allow or disallow them.

 - PVP - Player vs Player - see the PVP Section below
 - Leaf decay - determines whether leaf blocks decay or not
 - Mob spawning - handles whether monsters or animals should spawn on the island, either naturally or due to spawner blocks
 
### World Settings
These settings are for admins to determine. Players may be able to view them as well in a read-only mode. This may help players understand what type of server they are playing on and what is allowed or not.

 - Chest explosion damage - this protects chests from being damaged by explosions. Explosions could be due to Creepers, TNT cannons, Wither or Ghast explosions, etc. The default is to prevent chests from being broken. Although this provides good protection for players, it does provide a somewhat exploitable system whereby indestructible rooms can be made with chests, e.g., to hold a Wither. Admins should consider the tradeoff.
 - Cleaning up a super-flat world - in rare situations, the world generation of a BentoBox world may not be running or malfunction. As most BentoBox worlds are officially "super-flat" worlds according to the server, new world chunks will be created as super-flat chunks. These are a few layers of blocks starting at y=0 and covered in grass. Admins can recover from a world where super-flat chunks exist by switching this setting on. It will detect super-flat chunks and try to convert them to the game mode's chunk type, e.g. void. This process can lag the server so it should not be left on unless it is required. Recovered chunks are reported in the console log.
 - Coarse Dirt Tilling Prevention - this setting is to prevent players from making dirt out of coarse dirt. In a number of BentoBox game modes, dirt is highly prized because it cannot be crafted, but it can be used to grow crops, feed sheep, etc. The Level addon will score dirt blocks higher than other blocks for this reason. Dirt is rare and given out sparingly. Coarse dirt enables dirt to be created by mixing it with gravel. If the Game Mode allows players to obtain gravel easily, e.g., via the vanilla Nether world, then coarse dirt making can be exploited to make dirt. The default setting is to disallow coarse dirt tilling, but it can probably be allowed so long as gravel is not too readily available.
 - Creeper protection - Creepers explode and BentoBox provides a few ways to handle them
     -  Prevent damage from the explosion - this will switch off the explosive damage of a creeper. Creepers are the number one way that an island can be destroyed and admins may not want to deal with players crying about their island being blown up. However, preventing this makes the game a lot easier.
     - Prevent visitors from lighting creepers on other islands - this is a type of griefing where a visitor can use flint & steel to prime a creeper and make it explode with the purpose of getting access to parts of another island, or just for fun. BentoBox is able to identify whether the player is a visitor or not and prevent this action.
- Ender Chests - access and crafting of Ender Chests are prevented by default because they provide a method for players to obtain items from other worlds. If the admin has a per-world Ender Chest plugin, then this setting can be switched off.
- Enderman protection - Endermen will randomly pick up blocks from islands. BentoBox. As this can lead to players complaining to admins about missing blocks, there is a setting to prevent this.
- Geo-Limiting of mobs - Some mobs, especially flying mobs can be spawned on one island and then potentially move outside of that island and enter other player's islands. For destructive mobs like the Wither, this is undesirable. This setting prevents the specified mobs from exiting the island. If they do, they are removed from the game.
- Visitor Protection - part of the fun of a multi-player game is having other players visit your island and see all the hard work you have done. However, some players see visitors as prey and try to develop ways to kill or harm them. BentoBox by default protects visitors from most harm. All types of Minecraft damage can be switched off. If a visitor falls into the void, they can be teleported to safety. Admins can configure what type of damage is prevented via the admin settings menu.
- Item frame protection - these have their own protection because they can be used in a variety of ways. The default is to protect them from being damaged and dropping the item in them. 
- Global mob spawning limitations - admins can use this setting to decide which mob types can spawn in the world. For example, Phantoms can be switched off. This setting overrides any other settings or spawning mechanisms, e.g. spawn eggs or spawner blocks.
- Liquid management - players can abuse the ability of liquids to flow outside of their protection zone and cause blocks to form, e.g., by letting lava and water mingle to make cobblestone. This setting stops the liquids from flowing.
- Natual Mob Spawning Outside Of Islands - this setting can prevent mobs from spawning outside of island boundaries. This can help concentrate mob spawning to be within islands. For worlds like AcidIsland, this is not recommended because it appears unnatural.
- Obsidian scooping - one classic newbie mistake on SkyBlock is to turn your one bucket of lava into obsidian by accidentally having it touch water in the wrong way. This is very common when players make a cobblestone generator and get it wrong. This setting by default enables a "cheat" that enables the player to use a bucket on a block of obsidian to return it to lava. This helps prevent players from reseting their island or bothering the admin for more lava. BentoBox checks that the obsidian block is a single block and that there are no other obsidian blocks close to it (+/- 2 blocks) before allowing the scooping. This limits exploitation of this cheat.
- Offline Growth Management - in general, plants will not grow on a BentoBox island unless the chunk is loaded on the server. Therefore, when players are offline, the plants do not usually grow. However, as visitors may visit an island and cause the chunks to be loaded, the plants can grow and mature. If players are complaining about this edge case, maybe because they have a Redstone machine that handles harvesting, then plant growth can be switched off when island members are not present.
- Offline Redstone Management - similar to the plant growth option, it may be desirable to disable all Redstone operations when team members are not present. This enables that to happen.
- Piston management - pistons can be used to create self-powered machines that fly through the air and invade other player's islands. This prevents pistons from operating (pushing) if they are outside the island's protection area. The default is for this prevention to be active because it is a favorite exploit of players.
- Remove mobs on teleport - this setting will clear the area of any hostile mobs when a player teleports. Admins can adjust what mobs will not be removed via the game mode's `config.yml` file. This feature helps prevent instant or surprise deaths due to a player teleporting to their home. The default is on.
- Spawner block protection - For some reason, spawner blocks are often given to SkyBlock players by admins, either as a reward or as a result of a purchase. However, spawner blocks have a vanilla function that enables the mob to be spawned to be changed by a player tapping it with a spawn egg. This prevents that function so that spawner blocks stay the same time. BentoBox also prevents the use of the `/spawner` or related commands by visitors to an island that can be used to change the type of spawner.
- Tree growth handling - This prevents trees from growing outside the island's protection range. If trees can do that, it can enable players to intrude into adjacent islands or result in blocks that they cannot access. 
- Wither protection - the Wither has the ability to destroy so much so this flag enables admins to limit the damage the Wither can do.

 

 

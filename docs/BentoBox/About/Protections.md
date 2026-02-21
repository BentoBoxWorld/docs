# Protection
BentoBox provides a full-featured world and island protection system for island GameModes. Configuration is done in-game via the admin or player settings, and out of game via permissions and config files.

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
There are a lot of protection flags and new ones are added regularly. Protections can be restricted by rank, so you can allow trusted players to do things visitors cannot:

 - Visitor
 - Coop
 - Trusted
 - Member
 - Sub-Owner

Owners can always do everything.

Every time a player tries to do something in a protected area, BentoBox checks whether they have the right to do it. If they do not, they are blocked and told why.

### Finding out why something can or cannot be done
BentoBox provides an admin diagnostic tool: the `why <player>` command, e.g., `/bsb why tastybento`. When active, the server console logs the reason for every action that player takes — allowed or blocked, and which flag caused it. This makes it easy to diagnose misconfigured settings.

If the `why` command says a player *can* do something but in-game they cannot, that indicates another plugin or the server itself is blocking the action, not BentoBox.

### What is protected

- Breaking and placing blocks
- Block interaction: containers, furnaces, crafting tables, enchanting tables, anvils, brewing stands, cauldrons, barrels, beehives, composters, jukeboxes, note blocks, levers, buttons, doors, trapdoors, beds, beacons, dragon eggs, item frames, gates, cake, berry bushes
- Redstone-related blocks
- Breeding animals
- Bucket use
- Dye, egg, and elytra use
- Vehicles: boats, minecarts, ridable animals
- Villager trading
- Name tag use
- Item/experience pickup and item dropping
- Fire: ignition, spreading, burning, lightning
- Damaging or killing mobs and animals
- Leash and lectern use
- Portal use
- Shearing
- Teleportation (chorus fruit, ender pearls)
- Throwing items including potions
- TNT and other explosion damage

## Settings Island Owners Can Change

Island owners open the settings GUI with `/island settings`. Admins can hide individual settings from players if they prefer to control them centrally.

| Setting | What it does |
|---|---|
| **PVP (Player vs Player)** | Whether players can attack each other on this island. Off by default. |
| **Leaf decay** | Whether leaf blocks decay naturally when logs are removed. |
| **Mob spawning** | Whether monsters or animals can spawn on the island, including from spawner blocks. |

## World Settings Admins Control

These settings apply to the whole game mode world. Only admins can change them, via `/[admin_command] settings`. Players can view (but not change) these in a read-only mode so they understand the server rules.

| Setting | What it does | Default |
|---|---|---|
| **Chest explosion damage** | Protects chests from being destroyed by explosions (Creepers, TNT, Withers, Ghasts). Prevents grief but means chests can be used to make explosion-proof rooms. | On |
| **Clean Super Flat** | If the world generator stops working, new chunks generate as flat grass. This setting detects and repairs those chunks. Leave it off unless you have this problem — it is resource-intensive. | Off |
| **Coarse Dirt Tilling** | Prevents players from converting coarse dirt into regular dirt using a hoe. Dirt is scarce and valuable in most game modes; coarse dirt tilling can be exploited to generate it cheaply if gravel is easy to obtain. | Off (prevention on) |
| **Creeper explosions** | Prevent Creeper explosion damage to island blocks. Creepers are the most common cause of island destruction. Preventing this makes the game easier, but reduces admin support load. | On |
| **Creeper visitor ignition** | Prevent visitors from using flint & steel to prime Creepers on someone else's island — a common griefing method. | On |
| **Ender Chests** | Block access to and crafting of Ender Chests, which can smuggle items between game mode worlds. Disable if you use a per-world Ender Chest plugin. | On (blocked) |
| **Enderman block theft** | Prevent Endermen from picking up blocks from islands. Without this, players lose blocks they did not remove themselves. | On |
| **Geo-limiting mobs** | Prevent certain mobs (e.g. the Wither, flying mobs) from leaving the island they were spawned on. If they cross the boundary they are removed. | On |
| **Visitor protection** | Protect visitors from most types of damage while on another player's island. Also teleports visitors to safety if they fall into the void. | On |
| **Item frame protection** | Prevent item frames from being broken or having their items knocked out by non-members. | On |
| **Global mob spawning** | Set which mob types can spawn anywhere in the world, overriding all other spawning settings. For example, disable Phantoms server-wide. | Varies |
| **Liquid flow outside islands** | Stop lava and water from flowing beyond island protection boundaries, preventing cobblestone formation between islands or floods. | On |
| **Mob spawning outside islands** | Prevent mobs from spawning in the areas between islands, concentrating spawning inside island zones. Not recommended for AcidIsland as it looks unnatural. | Off |
| **Obsidian scooping** | Allow players to right-click an isolated single obsidian block with an empty bucket to recover lava. Helps new players who accidentally make obsidian during cobblestone generator setup. | On |
| **Offline plant growth** | Stop crops and plants from growing on an island when no team members are online, even if a visitor is loading the chunks. | Off |
| **Offline Redstone** | Disable Redstone circuits on an island when no team members are online. | Off |
| **Piston outside boundary** | Stop pistons from pushing blocks beyond the island's protection boundary — a common exploit for griefing adjacent islands. | On |
| **Remove mobs on teleport** | Clear hostile mobs from the area when a player teleports to their island home, preventing surprise deaths on arrival. | On |
| **Spawner type protection** | Prevent players from changing the mob type of spawner blocks using spawn eggs. Useful when spawners are given as rewards. | On |
| **Tree growth boundary** | Prevent trees from growing beyond the island protection boundary. Without this, trees can intrude on other islands or create unreachable blocks. | On |
| **Wither damage** | Limit the destruction the Wither can cause on and between islands. | On |

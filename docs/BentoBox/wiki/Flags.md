# What are the Flags ?

Flags are island settings that are similar to [WorldGuard's region flags](https://worldguard.enginehub.org/en/latest/regions/flags/) : they define whether something is allowed or is likely to happen inside the island boundaries.

## Here is a list of what they do
(Updated Aug 16, 2019)

* ANIMAL_SPAWN: Active = animals can spawn. Disabled: Animals cannot spawn
* ANVIL: Toggle interaction with Anvils
* ARMOR_STAND: Toggles interaction with Armor stands
* BEACON: Toggles interaction with Beacons
* BED: Toggles interaction with Beds
* BOAT:Toggle boats interactions
* BREAK_BLOCKS: Toggle Block breaking
* BREEDING:Toggle Animal breeding
* BREWING: Toggle Brewing stand use
* BUCKET: Toggle bucket use
* BUTTON: Toggle button use
* CONTAINER: Toggle interaction with chests, shulker boxes and flower pots.Other containers are handled by dedicated flags.
* DISPENSER: Toggle dispenser interaction
* DROPPER: Toggle dropper interaction
* ELYTRA: Toggle elytra allowed or not
* HOPPER: Toggle hopper interaction
* CHEST_DAMAGE: Toggle chest damage from explosions
* CHORUS_FRUIT: Toggle teleportation via Chorus fruits
* CLEAN_SUPER_FLAT: Enable to clean any super-flat chunks in island worlds. This is an emergency admin flag used if for some reason the generator fails (or the world is loaded without BentoBox running) and super flat is generated. It will automatically regenerate any superflat chunks. It should never need to be active.
* COARSE_DIRT_TILLING: Toggle tilling coarse dirt and breaking podzol to obtain dirt
* COLLECT_LAVA:Toggle collecting lava (override Buckets)
* COLLECT_WATER: Toggle collecting water (override Buckets)
* COMMAND_RANKS: Command Ranks - Configure command ranks - not a flag, but an option in the settings menu
* CRAFTING: Toggle use of Workbenches
* CREEPER_DAMAGE: Toggle creeper damage
* CREEPER_GRIEFING: Toggle creeper griefing - prevents visitors from triggering a creeper to blow up island blocks
* CROP_TRAMPLE: Toggle crop trampling
* DOOR: Toggle door usage
* DRAGON_EGG: Prevents interaction with Dragon Eggs. This does not protect them from being placed or broken.
* DYE: Prevent dye use
* EGGS: Toggle egg throwing
* ENCHANTING: Toggle Enchanting table use
* ENDER_CHEST:Toggle use/crafting
* ENDERMAN_DEATH_DROP: Endermen will drop any block they are holding if killed.
* ENDERMAN_GRIEFING: Allow Endermen to remove blocks from islands
* ENDER_PEARL: Toggle use of Ender Pearls
* ENTER_EXIT_MESSAGES: Display entry and exit messages
* EXPERIENCE_BOTTLE_THROWING: Toggle throwing experience bottles
* FIRE_BURNING: Toggle whether fire can burn blocks or not.
* FIRE_EXTINGUISH: Toggle extinguishing fires
* FIRE_IGNITE: Toggle whether fire can be ignited by non-player means or not.
* FIRE_SPREAD: Toggle whether fire can spread to nearby blocks or not.
* FISH_SCOOPING: Allow scooping of fishes using a bucket
* FLINT_AND_STEEL: Allow players to ignite fires using flint and steel or fire charges.
* FURNACE: Toggle use
* GATE: Toggle use
* GEO_LIMIT_MOBS: Remove mobs that go outside protected island space
* HURT_ANIMALS: Toggle hurting
* HURT_MONSTERS: Toggle hurting
* HURT_VILLAGERS: Toggle hurting
* ITEM_FRAME: Toggle interaction
* ITEM_FRAME_DAMAGE: Mobs can damage item frames
* INVINCIBLE_VISITORS: Configure invincible visitor settings. Setting in settings menu.
* ISLAND_RESPAWN: Players respawn on island
* ITEM_DROP: Toggle dropping
* ITEM_PICKUP: Toggle pickup
* JUKEBOX: Toggle usage
* LEAF_DECAY: Allow leaves to naturally decay
* LEASH: Toggle use
* LEVER: Toggle use
* LIQUIDS_FLOWING_OUT: Toggle whether liquids can flow outside of the island's protection range. Disabling it helps avoiding lava and water generating cobblestone in the area between two islands. Note that liquids will still flow vertically. They will also not spread horizontally if they are placed outside an island's protection range.
* LOCK: Toggle island lock
* MILKING: Toggle cow milking
* MINECART: Toggle minecart interactions
* MONSTER_SPAWN: Toggle spawning
* MOUNT_INVENTORY: Toggle access to mount inventory
* NAME_TAG: Toggle use
* NATURAL_SPAWNING_OUTSIDE_RANGE: Toggle whether creatures (animals and monsters) can spawn naturally outside an island's protection range. Note that it doesn't prevent creatures to spawn via a mob spawner or a spawn egg.
* NOTE_BLOCK: Toggle use
* OBSIDIAN_SCOOPING: Allow obsidian to be scooped up with an empty bucket back into lava. Protects newbies. Reduces resets.
* OFFLINE_GROWTH: When disabled, plants will not grow on islands when all members are offline. May help reduce lag.
* OFFLINE_REDSTONE: When disabled, redstone will not operate on islands when all members are offline. May help reduce lag.
* PISTON_PUSH: When active, prevents pistons to push blocks outside island. Can prevent piston fliers.
* PLACE_BLOCKS: Toggle placing
* POTION_THROWING: Toggle throwing potions. This includes splash and lingering potions.
* NETHER_PORTAL: Toggle use
* END_PORTAL: Toggle use
* PRESSURE_PLATE: Toggle usage
* PVP_END: Enable/Disable PVP in the End.
* PVP_NETHER: Enable/Disable PVP in the Nether.
* PVP_OVERWORLD: Enable/Disable PVP on island.
* REDSTONE: Toggle use of any Redstone items
* REMOVE_END_EXIT_ISLAND: Prevents the end exit island from generating at coordinates 0,0. Paper has a system setting to prevent this.
* REMOVE_MOBS: Remove monsters when teleporting to island. Range and whitelists can be set in config.
* RIDING: Toggle riding
* SHEARING: Toggle shearing
* SPAWN_EGGS: Toggle use
* TNT_DAMAGE: Allow TNT and TNT minecarts to break blocks and damage entities.
* TNT_PRIMING: Prevents priming TNT. It does not override the Flint and steel protection.
* TRADING: Toggle trading with villagers or possibly other entities
* TRAPDOOR: Toggle access
* TREES_GROWING_OUTSIDE_RANGE: Toggle whether trees can grow outside an island's protection range or not. Not only will it prevent saplings placed outside an island's protection range from growing, but it will also block generation of leaves/logs outside of the island, thus cutting the tree.
* TURTLE_EGGS: Toggle crushing
* FROST_WALKER: Toggle Frost Walker enchantment
* EXPERIENCE_PICKUP: Toggle experience orb pickup
* PREVENT_TELEPORT_WHEN_FALLING: Prevent players from teleporting back to their island using commands if they are falling.
* WITHER_DAMAGE: If active, withers can damage blocks and players
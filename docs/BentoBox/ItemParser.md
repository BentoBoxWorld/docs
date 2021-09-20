# BentoBox ItemParser

There is not a good way how to define an item stack from the config files. 
As each item has different meta-data that can be assigned. 
So BentoBox uses very weird format that comes from ASkyBlock times.

## Quick Example

### General Translation

By default, all items are translated in format:
    
    - [TYPE]<:QUANTITY>

Quantity is not necessary, however, if you provide it, then you need to add `:` before it.

All types you can find here: [Material](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)

However there are some exceptions that have some more customizations available. You can check them below.

### Damageable Items

You also can define damageable items following this format:

    - [TYPE]:<DAMAGE_AMOUNT>:<QUANTITY>

Damage Amount and quantity is optional.

### Potions and Tipped Arrows

Potions, Splash Potions, Lingering Potions and Tipped Arrows follows the same pattern:

    - [TYPE]:PotionType:<LEVEL>:<EXTENDED>:<SPLASH/LINGER>:QUANTITY

[TYPE] you can replace with POTION, SPLASH_POTION, LINGERING_POTION or TIPPED_ARROW.

Level is a number 1 or 2 that indicates which potion level it is. (upgraded or not.)

EXTENDED is a word that you must write if you want your potion to have extended effect.

SPLASH and LINGER is a necessary parts to indicate if potion is that type. (leftover from ASkyBlock)

All potion types you can find by this link: [PotionTypes](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/potion/PotionType.html)

Examples:

    - POTION:STRENGTH:1:EXTENDED:SPLASH:1 - Will create splash potion with extended strength 1 effect.
    - POTION:INSTANT_DAMAGE:2::LINGER:2 - Will create 2 lingering potions with instant damage 2 effect
    - POTION:JUMP:2:::1 - Will create Jump 2 potion.
    - POTION:WEAKNESS::::1 - Will create weakness 1 potion.

### Banners

Banners have a custom parsing options that follows scheme:

    - [color]_BANNER:QUANTITY<:PatternType:DyeColor>

You can specify as many patterns as you want, but they must follow given sequence, pattern and then dye color.

You can find all pattern types here: [PatternType](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/block/banner/PatternType.html)

You can find all dye colors here: [DyeColor](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/DyeColor.html)


### Player Heads

Player Heads has a custom parsing options. It follows this scheme:

 - PLAYER_HEAD:<Name/Trimmed UUID/UUID/Texture>:<QUANTITY>

PLAYER_HEAD - indicates that the item will be Player Head.
In next part you can specify:

    - Player Name
    - Player Trimmed UUID (without -)
    - Player UUID (with -)
    - Texture Link

At the end you can specify the amount of player heads in the stack.
As example: `PLAYER_HEAD:BONNe1704` - will give 1 player head with BONNe1704 skin.


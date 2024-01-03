# BentoBox ItemParser

There is not a good way how to define an item stack from the config files. 
As each item has different meta-data that can be assigned. 
So BentoBox uses very weird format that comes from ASkyBlock times.

## Quick Example

### Generic Minecraft Item Translations

Since BentoBox 2.0.0 you can use minecraft item translations like in give command:

    - minecraft:diamond_sword{display:{Lore:["\"A legendary weapon\""]}}
    - minecraft:stone
    - diamond_chestplate{Enchantments:[{id:mending,lvl:1},{id:protection,lvl:4},{id:unbreaking,lvl:3}]}

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

    - [TYPE]:<POTION_TYPE>:QUANTITY

[TYPE] you can replace with POTION, SPLASH_POTION, LINGERING_POTION or TIPPED_ARROW.
All potion types you can find by this link: [PotionTypes](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/potion/PotionType.html)

Examples:

    - POTION:STRENGTH:1 - Will create splash potion with extended strength 1 effect.
    - SPLASH_POTION:INSTANT_DAMAGE:2 - Will create 2 splash potions with instant damage 2 effect
    - LINGERING_POTION:STRONG_LEAPING:1 - Will create Jump 2 lingering potion.
    - TIPPED_ARROW:WEAKNESS:1 - Will create weakness 1 tipped arrow.

### Banners

Banners have a custom parsing options that follows scheme:

    - [color]_BANNER:QUANTITY<:PatternType:DyeColor>

You can specify as many patterns as you want, but they must follow given sequence, pattern and then dye color.

You can find all pattern types here: [PatternType](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/block/banner/PatternType.html)

You can find all dye colors here: [DyeColor](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/DyeColor.html)


### Player Heads

Player Heads has a custom parsing options. It follows this scheme:

 - PLAYER_HEAD:<Name|Trimmed UUID|UUID|Texture>:<QUANTITY>

PLAYER_HEAD - indicates that the item will be Player Head.
In next part you can specify:

    - Player Name
    - Player Trimmed UUID (without -)
    - Player UUID (with -)
    - Texture Link

At the end you can specify the amount of player heads in the stack.
As example: `PLAYER_HEAD:BONNe1704` - will give 1 player head with BONNe1704 skin.

### Custom Model Data

Custom Model data can be added to any parsable item stack. The custom model data text can be added at any part of parsable string. The scheme for custom model data:

- `CMD-[number]`

Examples:

- IRON_INGOT:2:CMD-12345678 => Creates an item stack with 2 iron ingots and custom model data `12345678` 
- GOLD_INGOT:CMD-12345678 => Creates an item stack with gold ingot and custom model data `12345678`
- PLAYER_HEAD:BONNe1704:CMD-12345678 => Creates an item stack with BONNe1704 player head and custom model data `12345678` 
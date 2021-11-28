# CauldronWitchery

**CauldronWitchery** lets your players **summon any kind of mob or item using a cauldron** filled with water, lava or snow and a magic stick.

Created and maintained by [BONNe](https://github.com/BONNe).

{{ addon_description("CauldronWitchery", beta=True) }}

## Installation

1. Place the addon jar in the addons folder of the BentoBox plugin
2. Start the server
3. Run the admin command, e.g., `/[admin_cmd] witchery` to configure the addon

## Configuration

Similar to the challenges, biomes and generators, Cauldron Witchery stores all data inside the database. The config file contains generic option about the addon and how it should operate, while everything else, like magic sticks and player data are stored into database.

### config.yml

The latest config.yml can be found [here](https://github.com/BentoBoxWorld/CauldronWitchery/blob/develop/src/main/resources/config.yml).

### Template

CauldronWitchery addon contains a template file which can be used to import magic sticks into database. This file is useful for bulk data adding for people that do not like to use ingame-gui. However, be aware, that not all functions are available for the template file, and some items/options can be added only via GUI.
You can have as many template files as you want. Admin GUI will allow choosing which one you want to import.
The example template file: [template.yml](https://github.com/BentoBoxWorld/CauldronWitchery/blob/develop/src/main/resources/template.yml)

!!! tip
    The template file must contain `magic-sticks`.

??? question "Can I specify an enchantment for magic stick?"
    Unfortunately Spigot does not have a general item parsing mechanics. So plugin authors need to create their own. CauldronWitchery addon uses BentoBox [Item Parser](/en/latest/BentoBox/ItemParser/). If function is not supported by it, then you cannot. 

    However, you can always use in-game admin GUI to set any items you want. There is not any limitation.

??? question "The recipe I added is not picked up. What could be the reason?"
    There could be several reasons for that. If there is obvious error, log file should contain the error message with it.
    
    However, you can start with checking if all recipes starts with `- ` and every item (ingredient, cauldron, level, etc) are alligned by the left side.
    
    Another reason could be that the entity, item or book does not exist. You should check if the input for them are correct.

### Books

Books are the way how players could find recipes. The books are very customizable, however, be aware that title, author and pages has limitation of characters. I would suggest trying creating book in game with written book, and only after that put it in translation files.

??? question "Can add my own translations for books?"
    Yes, definitely you can. You can add it via [book_id]-[locale_code].yml or changing existing one. 

??? question "Can I disable automatic recipe generation?"
    Yes, just remove `recipe` section from the book.

??? question "Can I add more books?"
    Yes, just create a new file under `books` directory. File must be named `[book_id]-[locale_code].yml` and it must start with `[book_id]:`.

## FAQ

??? question "How does recipes works?"
    All recipes require 3 things:
    
    - Magic Stick in the player main hand
    - Main Ingredient in the player offhand
    - Extra Ingredients

    Extra Ingredients must be dropped into cauldron or kept in inventory. This depends on addon config option: `mix-in-cauldron`. If option is disabled, then items must be in player inventory.
    
    If nothing is missing, recipe will work.

??? question "Can I add custom magic stick item?"
    Yes, as long as Spigot supports them. However, you will not be able to do it via template file. Only Admin GUI supports custom item adding.

??? question "Can you add a feature X?"
    Please add it to the list [here](https://github.com/BentoBoxWorld/CauldronWitchery/issues).


## Translations

{{ translations(2976, ["lv"]) }}

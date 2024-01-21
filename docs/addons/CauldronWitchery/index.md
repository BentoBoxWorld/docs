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

## Customizable GUI's

BentoBox 1.17 API introduced a function that allows to implement customizable GUI's. This addon is one of the first one which uses this functionality. We tried to be as simple as possible for customization, however, some features requires explanation.
You can find more information how BentoBox custom GUI's works here: [Custom GUI's](/en/latest/Tutorials/generic/Customizable-GUI/)

??? question "How can I customize GUI's"
    To customize Addon GUI's you need to have version 2.0. This is a first version that has implemented them. Addon will create a new directory under `/plugins/BentoBox/addons/CauldronWitchery` with a name `panels`

    Currently you can customize 2 GUI's:

    - Stick Panel: `stick_panel` - panel that contains all magic sticks and users can purchase or get them.
    - Recipe Panel: `recipe_panel` - panel that contains all recipes that are available for the magic stick.

    Each GUI contains functions that is supported only by itself.

??? question "What does `PREVIOUS`|`NEXT` button type?"
    The PREVIOUS and NEXT button types allows creating automatic paging, when you have more sticks or recipes than spaces in GUI.
    These types have extra parameters under data:
 
    - `indexing` - indicates if button will show page number.

    Example: 
    ```yaml
        icon: tipped_arrow{CustomPotionColor:11546150}
        title: cauldron-witchery.gui.buttons.previous.name
        description: cauldron-witchery.gui.buttons.previous.description
        data:
          type: PREVIOUS
          indexing: true
        action:
          left:
            tooltip: cauldron-witchery.gui.tips.click-to-previous
    ```

??? question "What does `RETURN` button type?"
    The RETURN button type is available in recipe_panel. It allows returning to the sticks panel.

    Example: 
    ```yaml
        icon: OAK_DOOR
        title: cauldron-witchery.gui.buttons.return.name
        description: cauldron-witchery.gui.buttons.return.description
        data:
          type: RETURN
        action:
          left:
            tooltip: cauldron-witchery.gui.tips.click-to-return
    ```

??? question "What is `STICK` button type?"
    This button is available in stick_panel.
    The STICK button creates a dynamic entry for a magic stick. Button will be filled only if there exist a magic stick. F.e. if you have only 3 magic sticks, but defined 7 spots for them in the GUI, then only 3 spots will be filled. Other spots will be left empty.

    By default sticks will be ordered by their order numbers, however, you can specify a specific stick to be in a specific slot with `id` parameter under data.
    
    ```yaml
      data:
        type: STICK
        id: example_stick
    ```

    Specifying title, description and icon will overwrite dynammic generation based on database data. By default these values will be generated from database entries.
    This button supports 2 different action types:

    - RECIPES - opens a recipe view panel
    - PURCHASE - purchases or gives the magic stick for a player.

    Example: 
    ```yaml
      data:
        type: STICK
      actions:
        left:
          type: RECIPES
          tooltip: cauldron-witchery.gui.tips.left-click-to-view
        right:
          type: PURCHASE
          tooltip: cauldron-witchery.gui.tips.right-click-to-buy
    ```


??? question "What is `RECIPE` button type?"
    This button is available in recipe_panel.
    The RECIPE button creates a dynamic entry for a recipe. Button will be filled only if there exist a recipe. F.e. if you have only 3 recipes, but defined 7 spots for level in the GUI, then only 3 spots will be filled. Other spots will be left empty.

    By default recipes will be ordered by their order number and then by their reward item name.
    Specifying title, description and icon will overwrite dynammic generation based on database data. By default these values will be generated from database entries.
    
    Example: 
    ```yaml
      data:
        type: RECIPE
    ```

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

??? question "How players can get magic sticks?"
    Players can buy magic sticks using `/[player_cmd] witchery` command. 

    Admins can also create their own way how to distribute sticks. There is an admin command to generate them:
   
    `/[admin_cmd] witchery get stick <stick_id>`

??? question "What is the difference between main ingredient and extra ingredient?"
    The main ingredient is always the "last" item player needs to have for recipe. It is always an item in player offhand.

    Extra ingredients are items that must be either in player inventory or dropped into cauldron (depending on config).

??? question "Items are not burning in lava cauldron, and they are not despawning?"
    If `mix-in-cauldron` option is enabled in addon settings, then no items will burn in lava cauldron and they will not despawn.
    It is necessary for addon operation, as there can be recipes that requires lava cauldron. These recipes would not be possible
    to fulfill if items were burning off. Item depsawning inside cauldron is disabled just as protective measure. 

??? question "Anyone on my island can use magic sticks. Can I prevent it?"
    Yes, you can limit which user groups can use the sticks using Island Protection Flags.
    CauldronWitchery adds `CAULDRON_WITCHERY_ISLAND_PROTECTION` which can be toggled from island visitor till owner.

    Users outside member group will not be able to use magic sticks on island.

??? question "Can you add a feature X?"
    Please add it to the list [here](https://github.com/BentoBoxWorld/CauldronWitchery/issues).


## Translations

{{ translations(2976, ["lv", "zh-CN"]) }}

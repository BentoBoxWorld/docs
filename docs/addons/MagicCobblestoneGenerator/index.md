# MagicCobblestoneGenerator

**MagicCobblestoneGenerator** turns the plain and boring cobblestone generators to an awesome and reliable source of configurable blocks!

Created and maintained by [BONNe](https://github.com/BONNe).

{{ addon_description("MagicCobblestoneGenerator") }}

## Installation

1. Place the addon jar in the addons folder of the BentoBox plugin
2. Restart the server
3. Run the `/[admincmd] generator` command to configure the addon

## Configuration

By default, the addon tries to import all data from template file, to simplify first setup. A lot of addon settings are exposed in Admin GUI, however, some of them are not.
The latest config options, and their detailed explanations can be found [here](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/blob/develop/src/main/resources/config.yml).

Template file are mostly for users who do not like to use ingame editing GUI. However, template file is not automatically imported on each change. It requires importing via command or Admin GUI.

??? question "Template File Structure"
    ```
    # Start the listing of all generator tiers.
    tiers:
      # Unique Id for generator. Used in internal storage and accessing to each generator data.
      generator_unique_id: 
        # Display name for users. Supports colour codes.
        # Default value: generator_unique_id without _
        name: "Something fancy"
        # Description in lore message. Supports colour codes.
        # Can be defined empty by replacing eveything with [].
        # Default value: []
        description: -|
          First Line Of lore Message
          &2Second Line Of lore Message
        # Icon used in GUI's. Number at the end allows to specify stack size for item.
        # Default value: Paper.
        icon: "PAPER:1"
        # Generator type: COBBLESTONE, STONE or BASALT. Self explanatory.
        # Default value: COBBLESTONE
        type: COBBLESTONE
        # Indicates if genertor is default generator. Default generators ignores requirement section.
        # It is activated for each new island. Can be only one per each generator type.
        # Default value: false
        default: false
        # Users selects active generators.
        # Priority indicates which generator will be used
        # if multiple of them fulfills requirements.
        # Default value: 1
        priority: 1
        # There are several requirements that can be defined here.
        requirements:
          # Can define minimal island level for generator to work. Required Level Addon.
          # Default value: 0
          island-level: 10
          # List of required permissions for users to select this generator.
          # Default value: []
          required-permissions: []
          # List of required biomes for generator to work.
          # Empty means that there is no limitation in which biome generator works.
          # Default value: [].
          required-biomes: []
          # Cost for purchasing this generator. Requires Vault and any economy plugin.
          # Currently implemented by clicking on purchase icon in generator view GUI.
          # Default value: 0
          purchase-cost: 5.0
        # Cost for activating current generator tier. Requires Vault and any economy plugin.
        # Will be payed only on active switching between generators.
        # Default value: 0.
        activation-cost: 0.0
        # Materials and their chances. Use actual blocks please.
        # Chance supports any positive number, including double value.
        # Everything in the end will be normalized.
        # Default value: []
        blocks:
          FIRST_BLOCK_NAME_ID: NUMBER
          SECOND_BLOCK_NAME_ID: NUMBER
        # Treasure that has a chance to be dropped when block is generated.
        # ONLY on generation, not on block break.
        # Default value: []
        treasure:
          # Chance from 0 till 1. 0 - will not be possible to get a treasure.
          # Default value: 0
          chance: 0.001
          # Materials that can be dropped. Applies to the same rules as block section.
          # Default value: []
          material:
            FIRST_BLOCK_NAME_ID: NUMBER
            SECOND_BLOCK_NAME_ID: NUMBER
          # Maximal amount of items dropped.
          # It will be from 1 till defined amount.
          # Default value: 1
          amount: 1
    
    # Start the listing of all bundles
    bundles:
      # bundle_id
      bundle_unique_id:
        # Display name for users
        name: "Something fancy"
        # Description in lore message. Supports colour codes.
        # Can be defined empty by replacing eveything with [].
        # Default value: []
        description: -|
          First Line Of lore Message
          &2Second Line Of lore Message
        # Icon used in GUI's. Number at the end allows to specify stack size for item.
        # Default value: Paper.
        icon: "PAPER:1"
        # List of generators that bundle will work have access.
        generators:
          - generator_id_1
          - generator_id_2
    ```

### Generator exhaustion (rate limiting)

Since **2.8.0** generators can be capped so they only produce a set number of blocks within a time period before going on cooldown — useful for discouraging fully-automated AFK farms. The feature is **opt-in and disabled by default** (a limit of `0`), so existing setups are unaffected until you enable it. When a generator is temporarily on cooldown, players receive a `generator-exhausted` message.

=== "exhaustion.limit"
    !!! summary "Description"
        The default number of blocks a generator may produce during a single exhaustion period. `0` or less disables the limitation (the default). Each generator tier can override this via the per-tier `exhaustion-limit` key (see below).

        Default: `0`

=== "exhaustion.period"
    !!! summary "Description"
        The length of the exhaustion period, in **minutes**. The block count resets at the end of each period.

        Default: `60`

=== "exhaustion.cooldown"
    !!! summary "Description"
        How long, in **minutes**, a generator stays on cooldown after reaching its exhaustion limit.

        Default: `1440` (24 hours)

=== "exhaustion.notification-cooldown"
    !!! summary "Description"
        The minimum time, in **seconds**, between two exhaustion warning messages shown to the same player.

        Default: `60`

!!! tip "Per-tier limit"
    Each generator tier can override the global limit with an `exhaustion-limit` key in the generator template (and in the admin GUI), so different tiers can be throttled independently.

### Per-block height ranges

Also since **2.8.0**, generators — and individual blocks within a generator — can be limited to a minimum and maximum Y level, so different materials are produced at different heights. New GUI buttons let admins set and clear the range, and the generator lore shows players where each generator operates. Legacy templates without a height range remain fully compatible.

### Unlock progression and requirements

Since **2.9.0** generators can be gated behind richer requirements so you can design proper unlock trees instead of a flat list of tiers. All of these are configured from the generator edit panel in the Admin GUI:

- **Prerequisite generators** — require one or more other generators to be unlocked first, building multi-step progressions.
- **AOneBlock phase requirement** — on AOneBlock game modes, gate a generator behind a specific island phase, so tiers unlock as the island advances.
- **OneBlock block-count requirement** — gate a generator behind the number of blocks broken on a OneBlock island.
- **Activate on unlock** — a per-generator option that activates a generator automatically the moment it is unlocked, saving players a trip to the GUI.
- **Purchase confirmation** — optionally require an explicit confirmation before any money is taken when buying a generator, preventing accidental purchases.

=== "lose-tiers-on-level-loss"
    !!! summary "Description"
        *Added in 2.9.0.* Restores the pre-2.0.0 behaviour where a generator unlocked by island level is re-locked if the island level later drops below its requirement. Purchased tiers are always kept — only free, level-unlocked tiers are re-locked. Written to `config.yml` automatically on first load after upgrading.

        Default: `false`

!!! warning "Permission-gated generators are now revoked"
    Since **2.9.0**, a generator unlocked via permission is re-checked and **revoked** from an island's unlocked and active lists when the current (online) owner no longer holds the required permission — for example after an ownership transfer. Purchased tiers are preserved, so access returns if the permission is regained; offline owners are left untouched. Previously such a grant was permanent.

### Custom block outputs (ItemsAdder, CraftEngine, Oraxen, Nexo)

Since **2.10.0** a generator tier can produce **custom blocks** from ItemsAdder, CraftEngine, Oraxen and Nexo, not just vanilla materials — for example a diamond-encrusted ItemsAdder ore rolls into the weighted-random mix alongside everything else. All access to those plugins is routed through BentoBox core hooks, so the addon never depends on them directly.

- Blocks are stored as string IDs: vanilla names such as `COBBLESTONE`, or provider-prefixed IDs `itemsadder:namespace:id`, `craftengine:namespace:id`, `oraxen:id`, `nexo:id`. **Existing databases and templates load unchanged.**
- The admin edit panel gains an **Add Custom Block** button — enter the ID in chat and it is validated against the hook registry. Panels render custom blocks with the provider's own texture and display name.
- If a picked custom block is unavailable at generation time (the provider or block is missing), the generator falls back to the vanilla block and reports why via `/[admin_command] generator why`, rather than failing silently. Unregistered custom blocks in a template import with a warning so templates stay portable across servers.

!!! note "Provider availability"
    ItemsAdder and CraftEngine generate blocks today. Oraxen and Nexo are wired up and will generate once the matching BentoBox core hooks ship (BentoBox 3.20.0 adds the Nexo hook and `OraxenHook.placeBlock`).

!!! warning "Requires BentoBox 3.19.1 or newer"
    2.10.0 depends on the custom-block hook API added in BentoBox 3.19.1 and **will not load on an older core**. Update BentoBox before dropping in this jar.

## Commands

!!! tip
    `[player_command]` and `[admin_command]` are commands that differ depending on the gamemode you are running.
    The Gamemodes' `config.yml` file contains options that allows you to modify these values.
    As an example, on BSkyBlock, the default `[player_command]` is `island`, and the default `[admin_command]` is `bsbadmin`.
    Be aware, that this addon allows changing player commands aliases in addon `config.yml` file. 

=== "Player commands"
    - `/[player_command] generator`: Access to generator Selection GUI. 
    - `/[player_command] generator view <generator>`: Access to specific generator detailed view. 
    - `/[player_command] generator activate <generator> [false]`: Allows to activate (or deactivate) specific generator.
    - `/[player_command] generator buy <generator>`: Allows to buy specific generator.

=== "Admin commands"
    - `/[admin_command] generator`: Access to addon Admin GUI
    - `/[admin_command] generator import`: Imports default template file - `/plugins/BentoBox/addons/MagicCobblestoneGenerator/generatorTemplate.yml`.
    - `/[admin_command] generator database import <file>`: Ability to import database exported <file>.
    - `/[admin_command] generator database export <file>`: Ability to export database into <file> saved in `/plugins/BentoBox/addons/MagicCobblestoneGenerator/` folder.
    - `/[admin_command] generator why <player>`: A debugging command that allows finding issues with generators for each player.
    - `/[admin_command] generator reset <player>`: Resets a player's island generator data — unlocked, purchased, and active generators — after a confirmation prompt. *(Added in 2.9.0.)*

## Permissions

!!! tip
    `[gamemode]` is a prefix that differs depending on the gamemode you are running.
    The prefix is the lowercased name of the gamemode, i.e. if you are using BSkyBlock, the prefix is `bskyblock`.
    Similarly, if you are using AcidIsland, the prefix is `acidisland`.

=== "Player permissions"
    - `[gamemode].stone-generator` - Let the player use the '/[player_command] generator' command and its subcommands.
    - `[gamemode].stone-generator.active-generators.3` - Sets the maximum number of active generators the island owner can have. 3 can be replaced with any positive integer. This is just an example.
    - `[gamemode].stone-generator.max-range.30` - Sets the maximum distance from the generator so it continues to work. 30 can be replaced with any positive integer. This is just an example.
    - `[gamemode].stone-generator.bundle.[bundle_id]` - Specifies which bundle will be used for user owned island.
    
=== "Admin permissions"
    - `[gamemode].admin.stone-generator` - Let the player use the '/[admin_command] generator' command and its subcommands.
    - `[gamemode].admin.stone-generator.why` - Let the player use a debug command '/[admin_command] why generator <player>'.
    - `[gamemode].admin.stone-generator.database` - Let the player use the '/[admin_command] generator database' command and its subcommands.
    
??? question "Something is missing?"
    You can find the comprehensive list of permissions in the [addon.yml](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/blob/develop/src/main/resources/addon.yml) file of this addon.  
    If something is indeed missing from the list below, please let us know!


## Placeholders

{{ placeholders_source(source="MagicCobblestoneGenerator") }}


## FAQ

??? question "Can you add a feature X?"
    Please add it to the list [here](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/issues).

??? question "How can I add a new generator tier?"
    Currently, addon supports 3 ways how to add a new generator:
    
    - By using ingame GUI that is available via `/[admin] generator` command.
    - By adding generator to a template file. 
    - By adding generator to the exported database file.

??? question "I added generator to the template/database file, but it does not shows up in game."
    For easier configuration with multiple gamemodes, generators are stored in the internal database. After editing template or database file, you need to import them into that memory. You can do it via Admin GUI by clicking on `Import Template` or `Import Database` buttons.
    
    ![template](resources/import_template.png){: loading=lazy }
    ![database](resources/import_database.png){: loading=lazy }

??? question "I have a generator that shows up in Admin GUI, but players do not see it."
    Most likely it is because of "deployment" status. To avoid with issues when players starts to activate generators while an admin is adding them, generators are undeployed and noone can use them. You can activate them by editing generator via Admin GUI and clicking on lever in Edit Generator GUI.
    ![deployed](resources/deployed.png){: loading=lazy }

??? question "What is treasures?"
    Treasures are things that are dropped uppon block generation. It allows to give an extra customization for each generator.

??? question "What is bundles?"
    Bundles is a feature that allows customizing experience for each island even more. If bundle is assigned to an island, then players on that island will be able to use only generators from that bundle. 

??? question "Can I disable showing required permissions in generator description?"
    Yes, addon provides a lot of customization options for displaying each generator. It is located in locales file:
    ```
          # Generator lore message generator. All elements in generator lore is generated
          # based on section below.
          generator:
            # Main lore element content. If you do not want to display treasures at all,
            # just remove them from [treasures] section.
            # [description] comes from each generator tier.
            # Lore does not supports colour codes. Each object separate supports.
            lore: |-
              [description]
              [blocks]
              [treasures]
              [type]
              [requirements]
              [status]
            # Generates [blocks] section
            blocks:
              # First line in blocks section. Empty line will not be displayed.
              title: "&7&l Blocks:"
              # Each block and its value under title. Cannot be empty.
              # Supports [number], [#.#], [#.##], [#.###], [#.####], [#.#####]
              value: "&8 [material] - [#.##]%"
            # Generates [treasures] section
            treasures:
              # First line in blocks section. Empty line will not be displayed.
              title: "&7&l Treasures:"
              # Each treasure and its value under title. Cannot be empty.
              # Supports [number], [#.#], [#.##], [#.###], [#.####], [#.#####]
              value: "&8 [material] - [#.####]%"
            # Generates [requirements] section
            requirements:
              # Allows to change order and content of requirements message.
              description: |-
                [biomes]
                [level]
                [missing-permissions]
              # Generates [level] message.
              level: "&c&l Required Level: &r&c [number]"
              # Generates [missing-permission] message title.
              permission-title: "&c&l Missing Permissions:"
              # Generates [missing-permission] message values.
              permission: "&c  -[permission]"
              # Generates [biomes] message title.
              biome-title: "&7&l Operates in:"
              # Generates [biomes] message values.
              biome: "&8 [biome]"
              # Generates [biomes] message for All Biomes.
              any: "&7&l Operates in &e&o all &r&7&l biomes"
            # Generates [status] section
            status:
              # Message that is showed for Locked generators.
              locked: "&c Locked!"
              # Message that is showed for generators that is not deployed.
              undeployed: "&c Not Deployed!"
              # Message that is showed for Active generators.
              active: "&2 Active"
              # Message that is showed for generators that required purchasing.
              purchase-cost: "&e Purchase Cost: $[number]"
              # Message that is showed for generators that has activation cost.
              activation-cost: "&e Activation Cost: $[number]"
            # Generates [type] section
            type:
              title: "&7&l Supports:"
              cobblestone: "&8 Cobblestone Generators"
              stone: "&8 Stone Generators"
              basalt: "&8 Basalt Generators"
              any: "&7&l Supports &e&o all &r&7&l generators"
    ```

## Changelog

??? warning "What's new in v2.10.0 — custom blocks, requires BentoBox 3.19.1"
    **Released:** 2026-07-11

    Generators can now drop custom blocks from other plugins, routed through BentoBox core hooks.

    - 🔺 **Custom block support.** Generator tiers can produce blocks from **ItemsAdder, CraftEngine, Oraxen and Nexo** as well as vanilla materials. Blocks are stored as string IDs (`COBBLESTONE`, or `itemsadder:namespace:id`, `craftengine:namespace:id`, `oraxen:id`, `nexo:id`); existing databases load unchanged. Fixes [#103](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/issues/103). See the Configuration section above.
    - ✨ **Add Custom Block panel button** with chat-input validation against the hook registry; panels render custom blocks with the provider's own texture and name. Unavailable custom blocks fall back to the vanilla block with a `/why` report instead of failing silently. ItemsAdder and CraftEngine generate today; Oraxen and Nexo generate once BentoBox 3.20.0's hooks are present.
    - 🐛 **Treasure chance edits now save.** Editing a treasure's chance in the admin panel wrote to the deprecated `treasureChanceMap` instead of `treasureItemChanceMap`, so edits were lost — fixed.
    - ⚙️ **Templates accept custom blocks.** `generatorTemplate.yml` now accepts quoted, provider-prefixed block keys. No config action is required for existing setups; unregistered custom blocks import with a warning.
    - 🔡 **Locale note:** new `en-US.yml` keys were added for the custom block UI. Regenerate or update your locale files to pick up the new strings.
    - 🔺 **Requires BentoBox 3.19.1 or newer.** The custom-block hook API this release calls is only available from 3.19.1; the addon will not load on an older core. Update BentoBox first.

    [Release v2.10.0](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/releases/tag/2.10.0)

??? warning "What's new in v2.9.0 — permission-gated generators now revoked"
    **Released:** 2026-07-08

    Adds richer unlock progression and several admin/API improvements.

    - 🔒 **Prerequisite generators.** Gate a generator behind one or more others so tiers unlock in a designed progression. Configured through a new admin GUI selector. Fixes [#88](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/issues/88).
    - 🧱 **OneBlock / AOneBlock gating.** Require a specific AOneBlock phase, or a number of blocks broken on a OneBlock island, before a generator becomes available. Fixes [#121](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/issues/121), [#117](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/issues/117).
    - ⚙️ **Re-lock level tiers on level loss.** A new `lose-tiers-on-level-loss` setting (default `false`) re-locks level-unlocked generators if an island's level drops. Purchased tiers are always kept. Fixes [#118](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/issues/118).
    - ✨ **Activate on unlock.** Generators can now activate automatically the moment they are unlocked. Fixes [#106](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/issues/106).
    - 💰 **Purchase confirmation.** Optionally ask players to confirm before money is taken for a generator. Fixes [#109](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/issues/109).
    - 🛠️ **Admin data reset.** A new `/[admin_command] generator reset <player>` command resets a player's unlocked, purchased, and active generators after a confirmation prompt. Fixes [#149](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/issues/149).
    - 🔌 **New cancellable API events** `GeneratorPreBuyEvent` and `GeneratorTreasureDropEvent` for other addons to hook into (see the API section below).
    - 🔺 **Behaviour change:** permission-gated generators are now **revoked** when an island's online owner no longer holds the required permission — for example after an ownership transfer. Purchased tiers are preserved, so access returns if the permission is regained.
    - 🔡 **Locale note:** new `en-US.yml` keys were added for the prerequisite selector, activate-on-unlock, purchase confirmation, the admin reset command, and OneBlock/AOneBlock requirement messages. Regenerate or update your locale files to pick up the new strings.

    [Release v2.9.0](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/releases/tag/2.9.0)

??? warning "What's new in v2.8.0 — requires BentoBox 3.14.0 / Java 21"
    **Released:** 2026-07-03

    - ⚙️ **Generator exhaustion.** Optionally rate-limit how many blocks a generator produces per period, with a cooldown once the limit is hit. Configurable globally (`exhaustion.*` in `config.yml`) and per generator tier (`exhaustion-limit` in the template). Opt-in and disabled by default. See the Configuration section above.
    - **Per-block height ranges.** Restrict generators and individual blocks to a minimum/maximum Y level, with new GUI controls and player-facing lore.
    - 🔡 **New placeholders** `[gamemode]_magiccobblestonegenerator_generator_exhaustion_status` and `[gamemode]_magiccobblestonegenerator_exhausted_generator_names` expose exhaustion state.
    - 🔡 🔺 **MiniMessage locales + 13 new languages.** Every locale file was converted from legacy `&`/`§` colour codes to MiniMessage (which BentoBox 3.14 renders natively), and translations were added for cs, hr, hu, id, it, ja, ko, lv, nl, pt, pt-BR, ro and zh-HK — 24 locales in total, matching BentoBox core. If you kept custom edits to any `locales/*.yml`, re-apply them in MiniMessage format (or delete the file to regenerate a fresh one).
    - 🔺 **Modernised for BentoBox 3.14 / Java 21.** Updated to the current BentoBox API and Paper, with the test suite migrated to MockBukkit. This release will not load on older BentoBox or Java versions — update BentoBox first.

    [Release v2.8.0](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/releases/tag/2.8.0)

## Translations

{{ translations("MagicCobblestoneGenerator") }}

## API

Since MagicCobblestoneGenerator 2.4.0 and BentoBox 1.17 other plugins can access to the MagicCobblestoneData addon data directly. However, addon requests are still a good solution for a plugins that do not want to use too many dependencies.

### Maven Dependency
MagicCobblestoneGenerator provides an API for other plugins. This covers version 2.5.0 and onwards.

!!! note
    Add the MagicCobblestoneGenerator dependency to your Maven POM.xml:

    ```xml
        <repositories>
            <repository>
                <id>codemc-repo</id>
                <url>https://repo.codemc.io/repository/bentoboxworld/</url>
            </repository>
        </repositories>
        
        <dependencies>
            <dependency>
                <groupId>world.bentobox</groupId>
                <artifactId>magiccobblestonegenerator</artifactId>
                <version>2.5.0</version>
                <scope>provided</scope>
            </dependency>
        </dependencies>
    ```
Use the latest MagicCobblestoneGenerator version.

The JavaDocs for MagicCobblestoneGenerator can be found [here](https://ci.codemc.io/job/BentoBoxWorld/job/MagicCobblestoneGenerator/ws/target/apidocs/index.html).

### Events

=== "GeneratorActivationEvent"
    !!! summary "Description"
        Event that is triggered when player activates/deactivates a generator on their island.
        This event is cancellable.

        Link to the class: [GeneratorActivationEvent](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/blob/develop/src/main/java/world/bentobox/magiccobblestonegenerator/events/GeneratorActivationEvent.java)

    !!! question "Variables"
        - `String islandUUID` - the targeted island id.
        - `UUID targetPlayer` - id of the player who triggered generator activation.
        - `String generator` - the name of activated generator.
        - `String generatorID` - the id of activated generator.
        - `boolean activate` - the boolean that indicates if generator is activated or deactivated.

        
    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.LOW)
        public void onGeneratorActivationChange(GeneratorActivationEvent event) {
            UUID user = event.getTargetPlayer();
            String island = event.getIslandUUID();

            String generator = event.getGenerator();
            String generatorID = event.getGeneratorID();
            boolean activate = event.isActivate();
        }
        ```

=== "GeneratorUnlockEvent"
    !!! summary "Description"
        Event that is triggered when player unlocks a new generator on their island.
        This event is cancellable.

        Link to the class: [GeneratorUnlockEvent](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/blob/develop/src/main/java/world/bentobox/magiccobblestonegenerator/events/GeneratorUnlockEvent.java)

    !!! question "Variables"
        - `String islandUUID` - the targeted island id.
        - `UUID targetPlayer` - id of the player who triggered generator unlock.
        - `String generator` - the name of unlocked generator.
        - `String generatorID` - the id of unlocked generator.

        
    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.LOW)
        public void onGeneratorUnlock(GeneratorUnlockEvent event) {
            UUID user = event.getTargetPlayer();
            String island = event.getIslandUUID();

            String generator = event.getGenerator();
            String generatorID = event.getGeneratorID();
        }
        ```

=== "GeneratorBuyEvent"
    !!! summary "Description"
        Event that is triggered when player buys a new generator on their island.
        This event is NOT cancellable.

        Link to the class: [GeneratorBuyEvent](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/blob/develop/src/main/java/world/bentobox/magiccobblestonegenerator/events/GeneratorBuyEvent.java)

    !!! question "Variables"
        - `String islandUUID` - the targeted island id.
        - `UUID targetPlayer` - id of the player who bought generator.
        - `String generator` - the name of bought generator.
        - `String generatorID` - the id of bought generator.

        
    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.LOW)
        public void onGeneratorBuy(GeneratorBuyEvent event) {
            UUID user = event.getTargetPlayer();
            String island = event.getIslandUUID();

            String generator = event.getGenerator();
            String generatorID = event.getGeneratorID();
        }
        ```

=== "GeneratorPreBuyEvent"
    !!! summary "Description"
        Event that is triggered **before** a generator is purchased, allowing the buy to be cancelled or inspected. Extends the shared `GeneratorEvent` base.
        This event is cancellable.

        Since 2.9.0 version.

        Link to the class: [GeneratorPreBuyEvent](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/blob/develop/src/main/java/world/bentobox/magiccobblestonegenerator/events/GeneratorPreBuyEvent.java)

    !!! question "Variables"
        - `String islandUUID` - the targeted island id.
        - `UUID targetPlayer` - id of the player who is buying the generator.
        - `String generator` - the name of the generator being bought.
        - `String generatorID` - the id of the generator being bought.

        
    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.LOW)
        public void onGeneratorPreBuy(GeneratorPreBuyEvent event) {
            UUID user = event.getTargetPlayer();
            String island = event.getIslandUUID();
            String generatorID = event.getGeneratorID();

            // Veto the purchase if needed
            if (someCondition) {
                event.setCancelled(true);
            }
        }
        ```

=== "GeneratorTreasureDropEvent"
    !!! summary "Description"
        Event that is triggered when a treasure is about to drop from a generator, allowing the drop to be cancelled or altered. Extends the shared `GeneratorEvent` base.
        This event is cancellable.

        Since 2.9.0 version.

        Link to the class: [GeneratorTreasureDropEvent](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/blob/develop/src/main/java/world/bentobox/magiccobblestonegenerator/events/GeneratorTreasureDropEvent.java)

    !!! question "Variables"
        - `String islandUUID` - the targeted island id.
        - `UUID targetPlayer` - id of the player the treasure is dropping for.
        - `String generator` - the name of the generator dropping the treasure.
        - `String generatorID` - the id of the generator dropping the treasure.
        - `Location location` - the location the treasure is about to drop at.
        - `ItemStack itemStack` - the treasure item about to drop (can be modified).

        
    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.LOW)
        public void onTreasureDrop(GeneratorTreasureDropEvent event) {
            Location location = event.getLocation();
            ItemStack treasure = event.getItemStack();

            // Cancel the drop or swap the item
            event.setCancelled(true);
        }
        ```

### Addon Request Handlers

Till BentoBox 1.17 we had an issue with accessing data outside BentoBox environment doe to the class loader we used to load addons.
This meant that data was accessible only from other addons. But BentoBox implemented PlAddon functionality, which means that request
handlers are not necessary anymore.

More information about addon request handlers can be found [here](/en/latest/BentoBox/Request-Handler-API---How-plugins-can-get-data-from-addons/)

=== "active-generator-names"
    !!! summary "Description"
        Returns the names of active generators for the player.

        Since 2.4.0 version.

    !!! question "Input"
        - `world-name`: String - the name of the world.
        - `player`: String - the UUID of the player.

    !!! success "Output"
        The output is a `List<String>` which contains names of active generators.

    !!! failure
        This handler will return null if the `world-name` has not been provided or if the `world-name` does not exist or `player` is not provided.

    !!! example "Code example"
        ```java
        public List<String> getActiveGeneratorNames(String worldName, UUID playerUUID) {
            return (List<String>) new AddonRequestBuilder()
                .addon("MagicCobblestoneGenerator")
                .label("active-generator-names")
                .addMetaData("world-name", worldName)
                .addMetaData("player", playerUUID)
                .request();
        }
        ```


=== "generator-data"
    !!! summary "Description"
        Returns the raw data stored for the requested generator object. 

        Since 2.4.0 version.

    !!! question "Input"
        - `generator`: String - the UUID of the generator.

    !!! success "Output"
        The output is a `Map<String, Object>` which contains raw generator data.
        
        Output map contains:

        - `uniqueId`: String - the unique ID of the generator. Should be the same as in input.
        - `friendlyName`: String - the display name of the generator (unformatted).
        - `description`: List<String> - the list of strings for the lore message (unformatted).
        - `generatorType`: String - the type of the generator. Available types:

            - COBBLESTONE
            - STONE
            - BASALT
            - COBBLESTONE_OR_STONE
            - BASALT_OR_COBBLESTONE
            - BASALT_OR_STONE
            - ANY

        - `generatorIcon`: ItemStack - the itemStack of the generator icon.
        - `lockedIcon`: ItemStack - the itemStack of the locked generator icon.
        - `defaultGenerator`: boolean - the boolean that indicates if generator is default or not.
        - `priority`: int - the priority vaule of the generator.
        - `requiredMinIslandLevel`: int - the minimal island level for generator to work.
        - `requiredBiomes`: Set<Biome> - the set of required biomes for generator to work.
        - `requiredPermissions`: Set<String> - the set of required permissions for generator to be purchasable.
        - `generatorTierCost`: double - the price of the generator.
        - `activationCost`: double - the activation price of the generator.
        - `deployed`: boolean - the boolean that indicates if generator is available for players.
        - `blockChanceMap`: TreeMap<Double, Material> - the map that contains raw data for block chances.
        - `treasureItemChanceMap`: TreeMap<Double, ItemStack> - the map that contains raw data for treasure chances.
        - `treasureChance`: double - the value of the treasure to be dropped from generating block.
        - `maxTreasureAmount`: int - the maximal amount of treasures to be dropped at once.

    !!! failure
        This handler will return null if the `generator` has not been provided or an empty map if `generator` does not exist.

    !!! example "Code example"
        ```java
        public Map<String, Object> getGeneratorData(String generatorId) {
            return (List<String>) new AddonRequestBuilder()
                .addon("MagicCobblestoneGenerator")
                .label("generator-data")
                .addMetaData("generator", generatorId)
                .request();
        }
        ```

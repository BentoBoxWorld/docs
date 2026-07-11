# CaveBlock

No sky. No surface. Just stone in every direction and a pickaxe in your hand.

**CaveBlock** flips the island game on its head: instead of building up into the open air, players carve out their world from solid underground. Dig for ores, hollow out a home, expand through the dark. It's the same satisfying island progression — challenges, levels, teammates — but the whole thing plays out underground. ~~Dwarves~~ Players everywhere love it.

Created and maintained by [BONNe](https://github.com/BONNe).

{{ addon_description("CaveBlock") }}

## Installation

0. Install BentoBox and run it on the server at least once to create its data folders.
1. Place this jar in the addons folder of the BentoBox plugin.
2. Restart the server.
3. The addon will create worlds and a data folder and inside the folder will be a config.yml.
4. Stop the server .
5. Edit the config.yml how you want.
6. Delete any worlds that were created by default if you made changes that would affect them.
7. Restart the server.

## Configuration

The main `config.yml` file contains basic information about game-mode addon setup.

### config.yml

After addon is successfully installed, it will create config.yml file. Every option in this file comes with comments about them. Please check file for more information.

You can find the latest config file: [config.yml](https://github.com/BentoBoxWorld/CaveBlock/blob/develop/src/main/resources/config.yml)

!!! info "World generation reworked in 1.21.0"
    Since **1.21.0** the overworld is carved by Minecraft's own vanilla 1.18+ noise generator, so islands run through genuine cheese, spaghetti, lush, dripstone and deep-dark caves — complete with vanilla ores, decorations, structures and underground biomes. Every column is then capped so the world stays solid rock with no open sky. Because the server now handles carving, ores and biomes, the old block-replacement generation options (`generation-tries`, `use-new-material-generator`, the per-dimension `blocks` lists, and the `natural-*` toggles) were removed. The Nether and End keep a fill-and-decorate approach with a new ore-vein populator. See the changelog at the bottom of this page before upgrading.

=== "world.world-depth"
    !!! summary "Description"
        The depth of world indicates till which height blocks will be generated in world. Setting it to -64 will create just a basic void world.

        Allows to create some fresh air above your cave.

=== "world.structures"
    !!! summary "Description"
        *Added in 1.23.0.* A map of vanilla structures that may generate in the **overworld** cave world. Set a structure to `false` to stop it generating; structures not listed here generate as normal. Use the vanilla structure key, for example `ancient_city`, `trial_chambers`, `mineshaft`, `mineshaft_mesa`, `stronghold`, `mansion`, `monument`, `pillager_outpost`, `ruined_portal`, `trail_ruins`, `village_plains`, `desert_pyramid`, `jungle_pyramid`, `igloo`, `swamp_hut`.

        Large structures like Ancient Cities and Trial Chambers can fill or unbalance a solid cave world, so they are **disabled by default**. Only affects newly generated overworld chunks.

        Default:
        ```yaml
        structures:
          ancient_city: false
          trial_chambers: false
          mansion: false
          mineshaft: true
          stronghold: true
        ```

=== "world.overworld-cave-fill"
    !!! summary "Description"
        *Added in 1.23.0.* Overworld cave density. Vanilla generates a dense 1.18+ cave network (cheese and spaghetti caves) which, on a solid cave world, can feel like "nothing but passageways". This re-solidifies a fraction of that cave air after generation using a low-frequency noise field, so whole regions close up into separate chambers rather than punching random single holes.

        - `0.0` keeps every vanilla cave (densest, the original behaviour).
        - `1.0` fills nearly all caves (almost solid).
        - Try `0.4` – `0.6` to thin them out.

        Underground biomes, ores, decorations and structures are kept either way. Only affects newly generated chunks.

        Default: `0.0`

=== "world.overworld-carvers"
    !!! summary "Description"
        *Added in 1.23.0.* Generate vanilla carver caves (big ravines and long round tunnels) in the overworld. These stack on top of the noise caves. Set to `false` to remove the ravines and wide tunnels while keeping the noise caves.

        !!! warning
            BentoBox does not support changing this value mid-game. If you need to change it, do a full reset of your worlds and databases.

        Default: `true`

=== "world.normal.roof"
    !!! summary "Description"
        Allows toggling if overworld top block should be bedrock block. Otherwise, it will be made of stone.

=== "world.normal.floor"
    !!! summary "Description"
        Allows toggling if overworld bottom block should be bedrock block. Otherwise, it will be made of stone.

=== "world.normal.main-block"
    !!! summary "Description"
        Main block used to cap the sky gaps above the vanilla-generated terrain. Vanilla cave carving, ores, structures and underground biomes (lush caves, dripstone caves, deep dark) are produced by the server; this setting only affects the material used to fill the surface layer. Setting it to AIR will leave open sky above the caves.

=== "world.nether.roof"
    !!! summary "Description"
        Allows toggling if the nether top block should be bedrock block. Otherwise, it will be made of netherrack.

=== "world.nether.floor"
    !!! summary "Description"
        Allows toggling if nether bottom block should be bedrock block. Otherwise, it will be made of netherrack.

=== "world.nether.main-block"
    !!! summary "Description"
        Allows setting main block that will be used for the nether world generation. Setting it to AIR will create void world. Ore veins (ancient debris, nether quartz, obsidian, glowstone and more) are placed on top of this by the vein populator.

=== "world.end.roof"
    !!! summary "Description"
        Allows toggling if the end top block should be bedrock block. Otherwise, it will be made of endstone.

=== "world.end.floor"
    !!! summary "Description"
        Allows toggling if the end bottom block should be bedrock block. Otherwise, it will be made of endstone.

=== "world.end.main-block"
    !!! summary "Description"
        Allows setting main block that will be used for the end world generation. Setting it to AIR will create void world. Ore veins are placed on top of this by the vein populator.

## Commands

!!! tip
    `[player_command]` and `[admin_command]` are commands that differ depending on the gamemode you are running.
    
    The Gamemodes' `config.yml` file contains options that allows you to modify these values.
    
    As an example, on CaveBlock, the default `[player_command]` is `cave`, and the default `[admin_command]` is `cba`.
    
    Be aware, that this addon allows changing player commands aliases in addon `config.yml` file.


By default, BentoBox GameMode addons comes with the default sub-command set, however, each addon may introduce even more sub commands.

[Complete CaveBlock Command List](Commands)

## Permissions

!!! tip
    `[gamemode]` prefix in every place for CaveBlock addon must be replaced with `caveblock`.

By default, BentoBox GameMode addons comes with the default sub-permission set, however, each addon may introduce even more sub-permissions.

[Complete CaveBlock Permission List](Permissions)


## Placeholders

By default, BentoBox GameMode addons comes with [default placeholders set](../../BentoBox/Placeholders), however, each addon may introduce even more placeholders.

[Complete CaveBlock Placeholder List](Placeholders)


## Flags

Addon introduces 1 BentoBox Settings flag:

- ![feather](https://static.wikia.nocookie.net/minecraft_gamepedia/images/e/e2/Feather_JE3_BE2.png){: loading=lazy width=16px } SKY_WALKER_FLAG: flag in world settings that allows enabling/disabling player walking on cave roof.


## FAQ

??? question "Can you add a feature X?"
    Please add it to the list [here](https://github.com/BentoBoxWorld/CaveBlock/issues).

??? question "I have a bug, where should I report it?"
    Please add it to the list [here](https://github.com/BentoBoxWorld/CaveBlock/issues).


## Changelog

??? note "What's new in v1.23.1"
    **Released:** 2026-07-09

    A bugfix release that closes the structure-suppression hole introduced in 1.23.0. Recommended for all servers running 1.23.0 that disable vanilla structures.

    - 🔺 **Disabled structures no longer freeze the server.** Disabling a structure only cancelled its *placement*, not its placement *rules*, so structure searches (`/locate`, Eyes of Ender, explorer/treasure maps, dolphins, villager map trades) kept scanning out to the radius cap and freezing the main thread. A new `StructuresLocateEvent` handler now removes disabled structures from the search up front, returning "not found" instantly. Fixes [#116](https://github.com/BentoBoxWorld/CaveBlock/issues/116).
    - 🔺 **Structures no longer slip through in the spawn area.** The suppression listener is now registered early in `createWorlds()`, before the first spawn chunks generate, so a disabled structure can no longer appear near spawn.

    [Release v1.23.1](https://github.com/BentoBoxWorld/CaveBlock/releases/tag/1.23.1)

??? note "What's new in v1.23.0"
    **Released:** 2026-07-07

    Hands admins direct control over what fills the overworld cave world, building on the 1.22.0 generation work.

    - ⚙️ **Configurable overworld structures.** A new `structures:` section in `config.yml` toggles individual vanilla structures (Ancient Cities, Trial Chambers, Mansions, Mineshafts, Strongholds and more). The largest, world-filling structures are disabled by default. Fixes [#112](https://github.com/BentoBoxWorld/CaveBlock/issues/112).
    - ⚙️ **Overworld cave density control.** A new `overworld-cave-fill` setting (`0.0`–`1.0`, default `0.0`) re-solidifies a fraction of the dense vanilla cave network so worlds feel less like endless passageways, while keeping biomes, ores, decorations and structures intact. Fixes [#111](https://github.com/BentoBoxWorld/CaveBlock/issues/111).
    - ⚙️ **Carver cave toggle.** A new `overworld-carvers` setting (default `true`) removes vanilla ravines and wide tunnels while keeping the noise caves. This one cannot be changed mid-game.

    New options are written to `config.yml` automatically on first run and only affect **newly generated** chunks; defaults preserve the 1.22.0 behaviour, except that the largest structures are now off by default. See the Configuration section above.

    [Release v1.23.0](https://github.com/BentoBoxWorld/CaveBlock/releases/tag/1.23.0)

??? warning "What's new in v1.22.0 — Nether & End generation reworked"
    **Released:** 2026-07-06

    Rebuilds how the **Nether** and **The End** are generated. Previously both dimensions were a solid block of rock peppered with random single blocks — including stray floating fire that caused lag — and had no real caves.

    - 🔺 **Nether & End generation overhaul.** Both dimensions are now filled solid and carved by a 3D noise cave generator into connected tunnels and chambers, with a solid margin against the floor and roof.
    - 🌋 **Nether lava sea.** The lowest cave voids fill with lava rather than open air; the floor and roof stay solid so the world stays enclosed.
    - 🗺️ **Natural Nether biomes.** The five Nether biomes are shared into natural, roughly equal-area regions, so several biomes appear within a single island.
    - 🌿 **Biome-aware decorations.** Crimson/warped nylium, roots, fungi and vines; soul sand valleys with soul fire and bones; basalt deltas with columns and magma fires; glowstone ceiling patches; end rods and chorus in The End.
    - ⚡ **No more laggy floating fire.** Fire is now sparse and grounded on netherrack/magma.

    🔺 **World generation changed:** The new generator only affects **newly generated** chunks. Existing Nether/End chunks keep the old look, so you may see a seam where old meets new. Regenerate those dimensions (or start fresh worlds) if you want a consistent look.

    [Release v1.22.0](https://github.com/BentoBoxWorld/CaveBlock/releases/tag/1.22.0)

??? warning "What's new in v1.21.0 — Breaking: world generation reworked"
    **Released:** 2026-06-27

    A major generation overhaul. CaveBlock now targets **Paper 1.21.11 on Java 21** and the **BentoBox 3.14 API**.

    - 🔺 **Vanilla cave world generation.** The overworld delegates to Minecraft's own 1.18+ noise generator, so islands are carved through genuine cheese, spaghetti, lush, dripstone and deep-dark caves, complete with vanilla ores, decorations, structures (mineshafts, dungeons, trial chambers, amethyst geodes, ancient cities) and underground biomes. The sky is capped with stone so the world stays solid rock from bedrock to the roof.
    - 💎 **Reworked Nether & End ore veins.** The Nether and End keep the fill-and-decorate approach with a new vein populator that places properly sized ore blobs (ancient debris, quartz, obsidian, glowstone and more) instead of single blocks.
    - ⚙️ **Config cleanup.** World-generation settings were reworked and dead options removed — `generation-tries`, `use-new-material-generator`, the per-dimension `blocks` lists, the `natural-surface`/`natural-caves`/`natural-bedrock` toggles and the old `netherBlocks`/`endBlocks`/`debug` settings are gone. Back up your existing `config.yml` before letting the addon write the new defaults.
    - 🔡 **MiniMessage locales.** All locale files were migrated from legacy colour codes to MiniMessage, and the height-limit message key was renamed to `caveblock.general.errors.cave-limit-reached`. Regenerate your locale files if you have customised them.
    - 🧪 A full JUnit 5 + MockBukkit test suite was added to guard generation, height limits and addon lifecycle.

    🔺 **World generation changed:** Newly generated overworld chunks now use vanilla noise caves instead of solid-fill carving. Already-generated chunks are untouched, but new terrain at the edges of your world will look different from older areas. Test on a copy first if this matters to you.

    [Release v1.21.0](https://github.com/BentoBoxWorld/CaveBlock/releases/tag/1.21.0)

## Translations

{{ translations("CaveBlock") }}

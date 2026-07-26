# Greenhouses

Greenhouses is a BentoBox add-on to power-up your island world! It enables players to build their own biome greenhouses complete with weather, friendly mob spawning, unique plant growth, and even block erosion!

Greenhouses are made out of glass and must contain the blocks found in the Biome Recipe to be valid. There is a recipe GUI. Once built, the greenhouse can be used to grow plants with bonemeal, and it may spawn biome-specific mobs. If you include a hopper with water in it, snow will form inside the greenhouse when it rains. If you put bonemeal in the hopper, biome-specific plants will grow. Some blocks can also transform over time due to "erosion".

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("Greenhouses") }}

## Features

* Craft your own self-contained biome greenhouse on an island (or elsewhere if you like)
* Greenhouses can grow plants that cannot normally be grown, like sunflowers
* Friendly mobs can spawn if your greenhouse is well designed - need slimes? Build a swamp greenhouse!
* Blocks change in biomes over time - dirt becomes sand in a desert, dirt becomes clay in a river, for example.
* Greenhouses can run in multiple worlds.
* Easy to use GUI shows greenhouse recipes (e.g. **/is greenhouses**)
* Admins can fully customize biomes and recipes

## How to Build A Greenhouse

This example is for when you are in the BSkyBlock world. For AcidIsland, just use /ai instead of /island.

1. Make glass blocks and build a rectangular set of walls with a flat roof.
2. Put a hopper in the wall or roof.
3. Put a door in the wall so you can get in and out.
4. Type **/island greenhouses** and read the rules for the greenhouse you want.
5. Exit the GUI and place blocks, water, lava, and ice so that you make your desired biome.
6. Type **/island greenhouses** again and click on the biome to make it.
7. Type **/island greenhouses help** to see other options.

### Once made:

* Use bonemeal to grow small plants on grass blocks immediately in the greenhouse.
* Or place bonemeal in the hopper to have the greenhouse sprinkle bonemeal automatically. Come back later to see what grows!
* Place a bucket of water (or more) in the hopper to cause snow to fall in cold biomes. Snow will fall when it rains in the world. Each snowfall empties one bucket of water.
* Friendly biome-specific mobs may spawn in your greenhouse - the usual rules apply (be more than 24 blocks away).

## FAQ

* Can I use stained glass? Yes, you can. It's pretty.
* Can I fill my greenhouse full of water? Yes. That's an ocean.
* Will a squid spawn there? Maybe... okay, yes it will if it's a big enough ocean.
* How do I place a door high up in the wall if the wall is all glass? Place it on a hopper.
* How do I place a door on a hopper? Crouch and then place it.
* Can I use metal doors? Yes.
* Can I use a trap door? Yes.
* Can I grow swamp flowers with this? Yes. Make a swamp biome and use bonemeal.
* How much bonemeal is used to grow plants? One per successful plant.
* How much water do I need to put into the hopper to make it snow? One bucket of water (just the water) is used up every time it rains. This only happens in cold biomes.
* Can I build a Nether greenhouse? Try it and see... (Actually, you may need permission)
* Can I build greenhouses in the Nether? Yes. You can colonize the nether with them.
* What kind of mobs spawn in the biomes? It's what you would expect, wolves in Cold Taiga, horses on plains, etc.

## Required Plugin

This version of Greenhouses is an add-on for BentoBox and will not run stand-alone!

1. BentoBox - make sure you use the latest version!

## Installation and Configuration

1. Download and install BentoBox if you haven't done so already
2. Download the add-on
3. Place into the BentoBox addon's folder
4. Restart your server
5. The addon will make a data folder called greenhouses. Open that folder.
6. Check **config.yml** and edit to be what you want, note the list of world names.
7. Configure the **biomes.yml** if you wish (advanced).
8. Type **/bsbadmin greenhouses reload** in the game to reload the config or restart the server.
9. Done!

To make your first greenhouse, build a glass box and type **/is greenhouses make** to see what kind of greenhouse you get. Type **/is greenhouses** to see the recipes.

## Upgrading

Read the file release notes for changes and instructions on how to upgrade.

## Player Commands

Add these commands to /island, /ai. The command label is `greenhouse`, with the aliases `gh` and `greenhouses`.

* **greenhouses** - opens the recipe GUI; clicking on a recipe tries to make that greenhouse
* **greenhouses help** - lists these commands
* **greenhouses make [recipe]**: Tries to make a greenhouse, by finding the first valid recipe or by using the named one
* **greenhouses remove**: Removes a greenhouse that you are standing in if you are the owner

!!! warning "`list` and `recipe` were removed in 1.10.0"
    These two player commands were documented but never actually registered — they were unreachable stubs, and calling them only ever produced an unknown-command error. They were deleted in 1.10.0. `/is greenhouses` with no arguments opens the recipe GUI, which is what they were supposed to do.

## Admin Commands

!!! new "Added in Greenhouses 1.10.0"
    Before 1.10.0 the addon had no admin command tree at all. If a greenhouse record went bad, the only option was to stop the server and edit the database by hand.

Registered under your game mode's admin command, e.g. `/bsbadmin greenhouses` or `/acid greenhouses`. The label is `greenhouses`, with the aliases `greenhouse` and `gh`.

| Command | What it does |
|---|---|
| `list [player] [page]` | Paginated list of greenhouses, optionally just one player's. Records that failed to load are **always** listed too, with the reason. |
| `info [id]` | Recipe, owner, world, location, bounding box, area, original biome, hopper, broken status and missing blocks. With no ID, uses the greenhouse you are standing in. |
| `delete <id>` | Deletes a record — loaded or not — after asking you to confirm. |
| `tp <id>` | Teleports you to the middle of the greenhouse floor. Alias: `teleport`. |
| `verify [id]` | Re-checks one or all greenhouses against their recipe and reports what is missing. Alias: `check`. |
| `reload` | Re-reads `biomes.yml`, then re-loads the greenhouses from the database. |

- IDs come from `list` and can be shortened to any prefix that matches **only one** greenhouse. An ambiguous prefix is treated as no match rather than a guess, because deleting the wrong greenhouse cannot be undone.
- Everything except `tp` works from the server console.
- Greenhouse records that cannot be loaded — overlapping, unknown recipe, missing world, no location — are kept in memory with the reason instead of being silently dropped. That is what makes them listable and deletable.
- Records are never deleted automatically. Removing a player's greenhouse without being asked would be worse than a recurring warning.

!!! tip "Overlapping greenhouses"
    If two persisted greenhouses overlap, one is skipped at startup and named in the log along with the record it overlaps. Use `/bsbadmin greenhouses list` to see the skipped records and why, then `/bsbadmin greenhouses delete <id>` to remove the one you do not want. No database editing and no restart needed.

## Permissions

A full list of permissions is [here](Permissions).

Permission to use specific biomes can be added in biomes.yml.

For example, the permission for the Nether biome is **greenhouses.biome.nether** and is set here:

 NETHER:

    permission: greenhouses.biome.nether

The permission can be anything you like, e.g., a rank permission, **myserver.VIP**.

### General permissions are:

  greenhouses.player:

     description: Gives access to player commands
     default: true

  greenhouses.admin:

     description: Gives access to admin commands
     default: op

Since 1.10.0 each admin sub-command also has its own node — `greenhouses.admin.list`, `.info`, `.delete`, `.tp`, `.verify` and `.reload` — all defaulting to `op`. Operators need no action, but if you grant admin access through a permissions plugin you will want to add them. They were missing from `addon.yml` entirely before that release, which is why nothing but op access worked.

## Translations

{{ translations("Greenhouses") }}

!!! note "What's new in v1.10.0 — admin commands"
    **Released:** 2026-07-26

    Greenhouses finally has an admin command tree. Compatibility: BentoBox API 2.7.1 · Minecraft 1.21.5+ · Java 21.

    - 🛠️ **Admin commands.** `list`, `info`, `delete`, `tp`, `verify` and `reload`, registered under your game mode's admin command (e.g. `/bsbadmin greenhouses`). See the Admin Commands section above. Greenhouse records that cannot be loaded — overlapping, unknown recipe, missing world, no location — are now kept in memory with the reason instead of being silently dropped, which is what makes them showable and deletable. Records are still never deleted automatically.
    - ⚙️ **New permissions.** The six sub-commands each have their own node under `greenhouses.admin.*`, all defaulting to `op`. They were missing from `addon.yml` entirely before this release, which is why nothing but op access worked.
    - 🐛 **Checking a greenhouse whose recipe no longer exists no longer throws an NPE.** When a database record names a recipe that is not in `biomes.yml`, the check now reports `FAIL_UNKNOWN_RECIPE`.
    - 🐛 **`getFloorHeight` no longer throws on a record with no location** — the very records most likely to be broken. It falls back to the bounding box.
    - 🔺 **Snow now reports success from every column it scanned,** not just the last one. `SnowTracker` was overwriting its result on each column, so a greenhouse that made snow in ninety columns and missed the last reported failure — and that value decides whether water is consumed from the hopper.
    - 🧹 All 68 open SonarCloud issues resolved, five methods refactored below the cognitive-complexity threshold, dead code removed, and the test suite grown from 177 to 224 tests.

    🔡 **Translators wanted.** The admin commands add messages under `greenhouses.commands.admin.*`, currently English only. The other 24 locale files fall back to the key names until they are translated.

    🔺 **Three player commands were deleted — but none of them worked.** `InfoCommand`, `ListCommand` and `RecipeCommand` were unregistered stubs with placeholder bodies. `InfoCommand` even declared itself under the label `make`, which would have collided with the real make command had anyone ever enabled it. This page previously listed `greenhouses list` and `greenhouses recipe` as working player commands; they were not, and that has been corrected. `/is greenhouses` with no arguments still opens the recipe GUI.

    [Release v1.10.0](https://github.com/BentoBoxWorld/Greenhouses/releases/tag/1.10.0)

??? warning "What's new in v1.9.6 — overlapping greenhouses are now diagnosable"
    **Released:** 2026-07-25

    - 🐛 **Overlapping greenhouses are now diagnosable.** If two persisted greenhouses overlap, one is skipped at startup — but the log line used to say only `Greenhouse overlaps with another greenhouse. Skipping...`, which gave you nothing to act on and repeated on every restart. The warning now names **both** records with their `uniqueId`, recipe, owner, world, location and bounding box, and tells you how to fix it. The summary line reads `Loaded 63 greenhouses out of 65 in the database.` and closes with a tally of how many were skipped.
    - 🔺 **Greenhouse load order is now deterministic.** Greenhouses were loaded in whatever order the database returned, so with two overlapping records either could win, and it could flip between restarts. They are now sorted by `uniqueId` before loading, so the outcome is stable until you remove one of the records.
    - ⚙️ **Duplicate `SQUID` entry removed from the `OCEAN` recipe** in `biomes.yml`. It was listed twice, which triggers a duplicate-key warning from SnakeYAML on newer server versions. YAML keeps the last occurrence, so the effective value (`20:WATER`) is preserved and mob spawning is unchanged.

    ⚙️ **The `biomes.yml` fix does not apply itself.** Your server already has its own `biomes.yml` on disk and the addon will not overwrite it. If you see a SnakeYAML duplicate-key warning for `SQUID`, open `plugins/BentoBox/addons/Greenhouses/biomes.yml`, find the `OCEAN` section, and delete the first of the two `SQUID:` lines. First-time installs get the corrected file automatically.

    🔺 **This release reports overlapping greenhouses but does not remove them.** Skipped records are left in the database on purpose — silently deleting a player's greenhouse would be worse than a recurring warning. In 1.9.6 you had to remove the stale record yourself using the `uniqueId`s now printed in the log; 1.10.0 adds admin commands that do it in-game.

    [Release v1.9.6](https://github.com/BentoBoxWorld/Greenhouses/releases/tag/1.9.6)

??? note "What's new in v1.9.5"
    **Released:** 2026-06-03

    A bug-fix release focused on plant growth and the recipe GUI. See the full [Release v1.9.5](https://github.com/BentoBoxWorld/Greenhouses/releases/tag/1.9.5) notes.

    - 🔡 Fixed a GUI colour bleed where the Nether recipe entry's red colour code was never reset, turning the rest of the recipe panel text red. Tall/double plants (sunflowers, lilacs, rose bushes, etc.) now correctly place their upper half.
    - Glow Lichen now grows on land blocks (e.g. `GLOW_LICHEN: 10:STONE`) instead of being treated as underwater-only.
    - The `maxmobs` limit is now enforced on every spawn, so greenhouses can no longer overshoot the configured mob maximum.

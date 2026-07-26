# AcidIsland

It's SkyBlock — but the ocean is trying to kill you.

**AcidIsland** puts players on a tiny island surrounded by a sea of acid. Fall in and you're taking damage. That changes everything: expanding your island becomes a careful, high-stakes operation. Building over the edge is a gamble. And yet players can still boat across to visit each other — if they're brave enough.

It's a familiar premise with one twist that keeps players on their toes the entire time.

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("AcidIsland") }}

## Installation

0. Install BentoBox and run it on the server at least once to create its data folders.
1. Place this jar in the addons folder of the BentoBox plugin.
2. Restart the server.
3. The addon will create worlds and a data folder and inside the folder will be a config.yml.
4. Stop the server.
5. Edit the config.yml how you want.
6. Delete any worlds that were created by default if you made changes that would affect them.
7. Restart the server.

## Configuration

The latest `config.yml` can be found [here](https://github.com/BentoBoxWorld/AcidIsland/blob/develop/src/main/resources/config.yml).

### Purified water

!!! new "Added in AcidIsland 1.22.0"
    Acid water is still dangerous, but you can now purify it. Drinking an acid water bottle applies vanilla Poison; drinking a purified water bottle restores health. Water items carry coloured lore so you can tell them apart at a glance. Purify water by smelting a water bottle or bucket in a furnace, brewing water bottles with coal, or catching drips from a dripstone stalactite into a cauldron.

??? note "acid.purified-water.enabled"
    Master switch for the purified-water feature. When `false`, no tagging, furnace/brewing interception, or cauldron tracking happens.

    Default: `true`

??? note "acid.purified-water.heal-amount"
    Half-hearts restored when a player drinks a purified water bottle. `4.0` = 2 hearts.

    Default: `4.0`

??? note "acid.purified-water.bucket-furnace-enabled"
    Allow smelting a water bucket in a furnace to produce a purified water bucket. Smelting takes 100 seconds (5× a bottle). Set to `false` if this feels too easy for your server's balance.

    Default: `true`

??? note "acid.purified-water.nether-enabled"
    Run the purified-water mechanic in the addon's Nether world (island or vanilla).

    Default: `true`

??? note "acid.purified-water.end-enabled"
    Run the purified-water mechanic in the addon's End world (island or vanilla).

    Default: `true`

### Sulfur ocean

!!! new "Added in AcidIsland 2.0.0"
    On Minecraft 26.2 and later the acid sea is acid-green sulfur water, dotted with bubbling sulfur vents that gas the surface with nausea and periodically erupt as geysers. The ocean floor is a weighted mix of sand, gravel, sandstone and tuff with bubbling magma blocks, plus scatterings of sulfur and cinnabar on 26.2+. The same jar still runs on Minecraft 1.21.x servers, where the 26.2 features disable themselves and the water falls back to the classic warm ocean.

!!! warning "These are world generation settings"
    All three options below bake in when a chunk is generated. BentoBox does not support changing them mid-game — existing chunks keep their current look, so expect a visible seam at old chunk borders unless you start a fresh world.

??? note "world.default-biome"
    The default biome for the overworld. `SULFUR_CAVES` (Minecraft 26.2+) gives acid-green water with matching green fog. On older servers that biome does not exist and `WARM_OCEAN` is used instead.

    Default: `SULFUR_CAVES` (was `WARM_OCEAN` before 2.0.0)

??? note "world.sulfur-vent-chance"
    Chance (0–100) per chunk of a sulfur vent generating just below the sea surface. Vents are made of potent sulfur over a magma block and bubble, gas, and erupt as geysers. They come in four natural shapes — chimney, mound, twin and spiky crag — with random variation. Requires Minecraft 26.2 or later; ignored on older servers.

    Default: `10`

??? note "world.make-structures"
    Generate vanilla structures in the worlds. Trial chambers and other underground structures generate buried beneath the ocean floor, giving players a reason to dig down, and making the trial key in the starter kit earnable.

    Default: `true` (was `false` before 2.0.0)

## Permissions

Permissions can be found [here](Permissions).

## Commands

Commands can be found [here](Commands).

## Placeholders

Placeholders can be found [here](Placeholders).

## Changelog

!!! warning "What's new in v2.0.0 — sulfur ocean (world generation changes)"
    **Released:** 2026-07-20

    AcidIsland embraces Minecraft 26.2's sulfur pools as the signature look of the acid ocean. Compatibility: BentoBox API 3.14.0 · Minecraft 1.21.11 – 26.2 (sulfur features require 26.2+) · Java 21.

    - ⚙️ **Acid-green sulfur water.** The default overworld biome is now `SULFUR_CAVES`, turning all water acid-green with matching green fog. On servers older than 26.2 the biome does not exist and the world falls back to `WARM_OCEAN`.
    - ⚙️ **Sulfur vents and geysers.** Potent sulfur vents generate just below the sea surface: bubbles, a nausea gas cloud on the surface, and periodic geyser eruptions, in four natural shapes with random variation. Per-chunk chance is set by the new `world.sulfur-vent-chance` option (default 10%); requires Minecraft 26.2+.
    - **Varied ocean floor.** The barren sand floor is now a weighted mix of sand, gravel, sandstone and tuff with bubbling magma blocks, plus sulfur and cinnabar on 26.2+. Older servers get gravel and tuff in place of the 26.2 blocks.
    - **New "Sulfur Spring Refuge" starter island.** A hardy spruce outcrop with leaf litter, eyeblossoms, a wither rose, podzol, a tuff sanctum below and a goat, with the same utilitarian starter kit as the cherry grove island. Built entirely from 1.21-safe blocks.
    - ⚙️ **Structures on by default.** `world.make-structures` now defaults to `true`, so trial chambers and other underground structures generate buried beneath the ocean floor.

    🔺 **World generation changes.** The new water biome, vents, ocean floor and structures all bake in at chunk generation. Existing worlds keep their current look in explored chunks; for the full 2.0.0 experience start a fresh world, or expect a visible seam at old chunk borders.

    ⚙️ **Existing configs are not changed.** Your `config.yml` keeps its saved values. To adopt the new defaults on an existing install, set `default-biome: SULFUR_CAVES` and `make-structures: true`, add `sulfur-vent-chance: 10`, or delete the config to regenerate it.

    🔺 **New blueprints on existing installs.** BentoBox only extracts bundled blueprints into a *missing* blueprints folder. To see the new island option on an existing install, copy `sulfur-spring.blueprint` and `sulfur_spring.json` from the jar into `plugins/BentoBox/addons/AcidIsland/blueprints/`.

    [Release v2.0.0](https://github.com/BentoBoxWorld/AcidIsland/releases/tag/2.0.0)

??? note "What's new in v1.22.1"
    **Released:** 2026-06-28

    Maintenance release. No configuration or locale changes are required.

    - 🐛 **Duplicate permission keys in `addon.yml` fixed.** Several commands legitimately share one permission node — `/ai ban`, `/ai unban` and `/ai banlist` all use `acidisland.island.ban` — but they were written as separate YAML entries with identical keys. YAML keeps only the last of a duplicated key, so earlier permission descriptions were silently dropped and the server logged `duplicate keys found` on every load. Each shared node is now a single entry with a combined description, and the startup warnings are gone.
    - Added Minecraft 26.2 (and backfilled 26.1.2) to the published game-versions list.

    [Release v1.22.1](https://github.com/BentoBoxWorld/AcidIsland/releases/tag/1.22.1)

??? note "What's new in v1.22.0 — Purified water mechanic"
    **Released:** 2026-04-15

    Acid water can now be purified so players can safely drink, farm, and bottle it. All water items carry coloured lore — <span style="color:red">Acid Water</span> or <span style="color:green">Purified Water</span> — and cauldrons remember their purity across restarts.

    - ⚙️ **Purified water added** — four ways to purify: smelt a water bottle in a furnace (10 s), brew water bottles with coal, smelt a water bucket in a furnace (100 s, toggleable), or catch dripstone drips into a cauldron.
    - ⚙️ **Drinking effects** — acid water bottles apply vanilla Poison; purified water bottles heal (configurable via `acid.purified-water.heal-amount`).
    - ⚙️ New config block `acid.purified-water.*` (see Configuration section above). Master switch, heal amount, bucket-furnace toggle, and per-dimension Nether/End toggles.
    - 🔡 Two new locale keys under `acidisland.purified-water.*` for the lore tags; synced across all 18 translations.
    - **New events** — `ItemFillWithAcidEvent` and `PlayerDrinkPurifiedWaterEvent` for other plugins to hook.
    - Code hygiene: pattern-matching `instanceof`, `Math.clamp`, reduced complexity in `onPlayerMove`/`getWorld`/`findEntities`/`makeNetherRoof`, test modernisation.

    [Release v1.22.0](https://github.com/BentoBoxWorld/AcidIsland/releases/tag/1.22.0)

??? warning "What's new in v1.21.0 — BentoBox 3.14.0 required, locale migration"
    **Released:** 2026-04-12

    - **Cherry Grove Sanctuary starter island.** A new starter island blueprint themed around the Cherry Grove biome is included for Minecraft 1.21+ servers. To activate it, delete `BentoBox/addons/AcidIsland/blueprints/` so blueprints regenerate on the next startup.
    - 🔺 **BentoBox API 3.14.0 is now required.** Update BentoBox before installing this release.
    - 🔡 **All 24 locale files migrated from `&` codes to MiniMessage.** Delete `BentoBox/locales/AcidIsland/` and restart to regenerate. Any remaining `&` codes in custom files will render as plain text.
    - Bug fix: NullPointerException in the EssentialsX god mode check when EssentialsX fails to load at startup.
    - Several pre-existing locale bugs fixed during migration.

    [Release v1.21.0](https://github.com/BentoBoxWorld/AcidIsland/releases/tag/1.21.0)

## Translations

{{ translations("AcidIsland") }}

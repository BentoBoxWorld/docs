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

## Permissions

Permissions can be found [here](Permissions).

## Commands

Commands can be found [here](Commands).

## Placeholders

Placeholders can be found [here](Placeholders).

## Changelog

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

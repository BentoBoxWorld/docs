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

!!! warning "`default-biome` and `make-structures` are world generation settings"
    These two bake in when a chunk is generated. BentoBox does not support changing them mid-game — existing chunks keep their current look, so expect a visible seam at old chunk borders unless you start a fresh world. `sulfur-vent-chance` is the exception: since 2.1.0 it can be changed on a live server, it simply only affects chunks generated from then on.

??? note "world.default-biome"
    The default biome for the overworld. `SULFUR_CAVES` (Minecraft 26.2+) gives acid-green water with matching green fog. On older servers that biome does not exist and `WARM_OCEAN` is used instead.

    Default: `SULFUR_CAVES` (was `WARM_OCEAN` before 2.0.0)

??? note "world.sulfur-vent-chance"
    Chance (0–100) per chunk of a sulfur vent generating just below the sea surface. Vents are made of potent sulfur over a magma block and bubble, gas, and erupt as geysers. They come in four natural shapes — chimney, mound, twin and spiky crag — with random variation. Requires Minecraft 26.2 or later; ignored on older servers.

    Since 2.1.0 this can be changed without a world reset — the new value applies to newly generated chunks only.

    Default: `10`

??? note "world.make-structures"
    Generate vanilla structures in the worlds. Trial chambers and other underground structures generate buried beneath the ocean floor, giving players a reason to dig down, and making the trial key in the starter kit earnable.

    Default: `true` (was `false` before 2.0.0)

### Geyser offerings

!!! new "Added in AcidIsland 2.1.0, completed in 2.1.1"
    Throw items into the water around a sulfur vent and the geyser swallows them as offerings. When the vent next erupts it spews rewards back out of the plume — transmuted, not returned. What you feed it shapes what comes out: sacrifice ores and it leans towards gems, sacrifice wood and it leans towards living things. The mechanic requires Minecraft 26.2 or later (where sulfur vents exist) and quietly disables itself on older servers.

    Since 2.1.1 a vent **trades rather than gambles**: it works out what your offering was worth and hands back rewards worth roughly the same, so a diamond comes back in gems and a stack of cobble comes back in cobble-grade tat. Items floating near a vent drift into its pool, so a throw does not have to be accurate, and a fed vent is provoked into erupting a few seconds later so the payout lands while the player is still watching.

    Only items thrown by a player count — death drops, block drops and mob drops that wash into a pool are left alone. Items the acid dissolves within a vent's pool count as offerings instead of being lost, and spewed rewards are tagged so they can never be recycled into new offerings. Mining a vent out forfeits its pending offerings.

??? note "world.geyser-offerings.enabled"
    Master switch for the geyser offering mechanic.

    Default: `true`

??? note "world.geyser-offerings.max-rewards"
    Maximum number of rewards a single eruption can spew, however many items were offered.

    Default: `12`

??? note "world.geyser-offerings.match-value"
    Answer an offering with rewards of roughly the same worth, instead of one random reward per item. A vent transmutes rather than destroys: feed it a diamond and it owes a diamond's worth back, feed it cobble and it owes cobble. Worth comes from `geyser-values.yml`, which can defer to the Level addon's block values. Turn this off for the 2.1.0 one-roll-per-item payout.

    Default: `true` (added in 2.1.1)

??? note "world.geyser-offerings.exchange-rate"
    Fraction of the offered worth a vent pays back when matching worth. `1.0` is a fair trade, below `1.0` makes the vent take a cut, above `1.0` makes offering profitable in itself — which players will farm, so raise with care.

    Default: `1.0` (added in 2.1.1)

??? note "world.geyser-offerings.reward-ceiling"
    The most a single reward may be worth, as a multiple of the worth of the richest item offered. A stack of cobble is worth an emerald and a cobble generator is infinite, so without this a vent becomes a gem printer. Rewards named in a `from:` list in `geyser-loot.yml` ignore this — a transmutation the admin has written down is always allowed. Set to `0` for no limit.

    Default: `8.0` (added in 2.1.1)

??? note "world.geyser-offerings.erupt-on-offering"
    Provoke a fed vent into erupting a few seconds after it is fed, instead of waiting for the vanilla eruption cycle, so the reward follows the offering while the player is still there to see it. Turn this off to leave eruption timing entirely to vanilla — offerings are then held until the vent erupts.

    Default: `true` (added in 2.1.1)

#### geyser-loot.yml

Rewards are defined in `geyser-loot.yml`, copied into `plugins/BentoBox/addons/AcidIsland/` on first run. Each entry is either an item or a console command:

```yaml
loot:
  - {item: RAW_IRON, weight: 30, channel: mineral, amount: {min: 1, max: 3}}
  - {item: OBSIDIAN, weight: 10, channel: nether, from: [MAGMA_BLOCK, BASALT, LAVA_BUCKET]}
  - {item: MUSIC_DISC_13, weight: 1, from: [BONE, GUNPOWDER]}
  - {command: "give %player% cod 1", weight: 1, value: 4}
```

| Key | Meaning |
| --- | --- |
| `item` / `command` | The reward. Commands run from the console; `%player%` is substituted. |
| `weight` | Relative chance of the entry rolling — higher is more common. |
| `channel` | Optional. One of `gems`, `nether`, `mineral`, `forestry`, `husbandry`. Offerings pull the table towards their own channel by the share of the offering's *worth* that went into it. |
| `from` | Optional list of materials that transmute into this reward. Offer any of them and the entry becomes eight times as likely — and it ignores `reward-ceiling`, so it is the one way for a vent to hand back something far richer than what went in. |
| `amount` | Optional item count, fixed or a `{min, max}` range. Default `1`. |
| `value` | Optional worth of one of this reward, overriding the material's worth. Command rewards are free unless they set this, so give paid commands a value or they will turn up in every payout. |

!!! warning "Upgrading from 2.1.0"
    `geyser-loot.yml` is only written when it is missing, so a copy left over from 2.1.0 will not gain the `from:` transmutations or `value:` fields and none of the named transmutations will work. Delete the file so it regenerates, then re-apply your edits.

#### geyser-values.yml

`geyser-values.yml` says what a material is worth to a vent. The scale is arbitrary — only the ratios matter — and it is anchored on iron ingot `6`, gold ingot `12`, emerald `15`, diamond `45`, so a diamond comes back as three emeralds, or an emerald and two gold ingots.

Worth is resolved in this order, first hit wins:

1. the `values:` map in the file
2. the **Level addon's** block values for the world, if Level is installed and `use-level-addon: true` — so a server that has already tuned Level does not have to tune this twice. Delete an entry from `values:` to defer that material to Level.
3. the `default:` worth, for anything nothing else knows about

Worth is by material only: enchantments, custom names and the contents of shulker boxes are not counted, so gear is worth its base material.

The file is created automatically on first run.

## Permissions

Permissions can be found [here](Permissions).

## Commands

Commands can be found [here](Commands).

## Placeholders

Placeholders can be found [here](Placeholders).

## API

Other addons can hook into the geyser offering mechanic with two events, both added in 2.1.0:

- `GeyserSacrificeEvent` — fired when a vent swallows an offering. Cancellable.
- `GeyserTransmuteEvent` — fired when a vent spews a reward.

## Changelog

!!! warning "What's new in v2.1.1 — vents trade instead of gamble (delete `geyser-loot.yml`)"
    **Released:** 2026-07-26

    2.1.0 shipped the geyser offering mechanic but not the economy that was supposed to come with it: a vent rolled one reward per item thrown in, so a stack of cobble and a diamond bought the same spin, and the mechanic never said a word to the player. 2.1.1 completes it. Compatibility: BentoBox API 3.14.0 · Minecraft 1.21.5 – 26.2 (geyser features require 26.2+) · Java 21.

    - ⚙️ 🔺 **Worth matching.** A new `geyser-values.yml` says what a material is worth to a vent, anchored on iron ingot 6, gold ingot 12, emerald 15, diamond 45. A vent adds up what it was fed and keeps rolling rewards it can still afford until that worth is spent. Four new options under `world.geyser-offerings`: `match-value`, `exchange-rate`, `reward-ceiling` and `erupt-on-offering` (see Configuration above). Where the file is silent, worth can defer to the **Level addon's** block values via `use-level-addon: true`.
    - ⚙️ **Named transmutations.** Loot entries in `geyser-loot.yml` now take a `from:` list of materials that transmute into them — magma blocks make obsidian, iron makes gold, bones with gunpowder make music discs. A `from:` entry is eight times as likely and ignores `reward-ceiling`, making it the place to put rewards that would otherwise need a mob farm.
    - 🔡 **The vent finally speaks.** A new `acidisland.geyser` locale section adds offering, churning and payout messages plus display names for the five reward channels, in all 24 locales. They are action bar messages by default — remove the `[actionbar]` tag to send them in chat.
    - **Throws no longer have to be accurate.** Items floating near a vent drift into its pool, and a fed vent is provoked into erupting a few seconds later so the payout lands while the player is still watching.
    - **Channel bias by worth.** Offerings still pull the reward table towards their own channel, but the pull is weighted by worth rather than item count — one diamond steers as firmly as the stack of cobble it is worth.

    🔺 **Delete `geyser-loot.yml`** from `plugins/BentoBox/addons/AcidIsland/` if you ran 2.1.0. The file is only written when it is missing, so an existing copy will not gain the `from:` transmutations or `value:` fields. Re-apply your edits to the regenerated file.

    ⚙️ `geyser-values.yml` is created automatically on first run, and the four new config options are added to `config.yml` on start with existing settings preserved. 🔡 Regenerate or update your locale files to pick up the `acidisland.geyser` strings. Servers that preferred the 2.1.0 payout can set `match-value: false` and keep everything else.

    [Release v2.1.1](https://github.com/BentoBoxWorld/AcidIsland/releases/tag/2.1.1)

??? note "What's new in v2.1.0 — geyser offerings"
    **Released:** 2026-07-26

    AcidIsland 2.1.0 turns the sulfur vents from scenery into an economy. Throw items into the water around a vent and the geyser consumes them as offerings, then pays you back on its next eruption, spewing transmuted rewards out of the plume. Compatibility: BentoBox API 3.14.0 · Minecraft 1.21.11 – 26.2 (geyser offerings require 26.2+) · Java 21.

    - ⚙️ **Geyser offerings.** Items floating in the pool around a sulfur vent are consumed with a sizzle as offerings — anywhere within the pool counts, no pixel-perfect aim needed. When the vent next erupts, one reward per item offered (capped, configurable) is spewed from the plume in a radial fountain.
    - **Channels.** Offerings are categorized into **gems**, **nether**, **mineral**, **forestry** and **husbandry**, and bias the reward table towards what was sacrificed.
    - ⚙️ **New `geyser-loot.yml`**, copied to the addon data folder on first run: weighted item entries with amount ranges, plus console command rewards with `%player%` substitution.
    - ⚙️ **New `world.geyser-offerings` config section**: `enabled` (default `true`) and `max-rewards` per eruption (default `12`).
    - **New API events** for other addons: `GeyserSacrificeEvent` (cancellable) and `GeyserTransmuteEvent`.
    - **Works with acid item destruction.** Items the acid dissolves within a vent's pool count as offerings instead of being lost, whatever your `acid.damage.acid.item` destroy time — and spewed rewards are tagged so they can never be recycled into new offerings. Mined-out vents forfeit their pending offerings; the geyser is not a storage unit.
    - ⚙️ **`world.sulfur-vent-chance` no longer demands a world reset** to change. It only affects newly generated chunks, so admins can tune vent density on a live server.

    **No world reset needed.** Offerings work at any existing sulfur vent — this release makes no world generation changes.

    [Release v2.1.0](https://github.com/BentoBoxWorld/AcidIsland/releases/tag/2.1.0)

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

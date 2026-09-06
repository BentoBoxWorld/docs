# Limits

**Limits** allows you to limit island blocks and entities in GameModes like BSkyBlock and AcidIsland.

This addon was made to help limit lag-inducing entities or blocks, e.g., hoppers. It can be used to limit regular blocks and entities but not all can be limited.

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("Limits") }}

## Installation

1. Place the Limits addon jar in the addons folder of the BentoBox plugin
2. Restart the server
3. The addon will create a data folder and inside the folder will be a config.yml
4. Edit the config.yml how you want.
5. Restart the server if you make a change

## Commands
There is a user command and an admin command called "limits". Admins can check the limits of a specific island owner. Both show a GUI panel with the limits and the current count.

## Setup - Config.yml

The config.yml has the following sections:

* blocklimits
* blocklimits-nether
* blocklimits-end
* blockgrouplimits *(1.29.0+)*
* blockgrouplimits-nether / blockgrouplimits-end *(1.29.0+)*
* worlds
* entitylimits
* entitylimits-nether
* entitylimits-end
* entitygrouplimits

It also has these top-level toggles (all added in **1.29.0** unless noted): `apply-member-limit-perms`, `show-limit-messages`, `stacked-plants-count-as-one`, and `log-limits-on-join`.

!!! info "Per-dimension limits (1.28.2+)"
    As of **1.28.2**, block counts, entity counts, limits, and offsets are tracked **independently for the overworld, nether, and end**. A single limit defined in `blocklimits` or `entitylimits` applies separately to each dimension — e.g. `HOPPER: 10` allows 10 hoppers in the overworld, 10 in the nether, and 10 in the end (30 total across the island). Use the optional `-nether` / `-end` sections to override a single dimension.

    On first load after upgrading, your existing single-dimension data is migrated automatically into the **overworld** slot. The on-disk format changes, so take a backup before upgrading and note that downgrading afterwards is not supported.

### blocklimits

This section lists the maximum number of blocks allowed for each block material. Do not use non-block materials because they will not work. The limits apply independently in every dimension (overworld, nether, end).

Growth and damage variants are normalised to their canonical block — `BAMBOO_SAPLING` counts as `BAMBOO`, and since **1.30.0** `KELP_PLANT` counts as `KELP` — so a variant name used as a limit key (e.g. `KELP_PLANT` or `CHIPPED_ANVIL`) configures the canonical block's limit.

### blocklimits-nether / blocklimits-end

Optional sections that override the `blocklimits` defaults for the nether or the end respectively. They are commented out in the default config; uncomment and add entries to set dimension-specific block limits.

### worlds

This section lists block limits for specific worlds. You must name the world specifically, e.g. AcidIsland_world and then list the materials and the limit. World-named limits override the dimension-default limit above for that specific world.

### entitylimits

This section lists the default entity limits within a player's island space (protected area and to island limit). A limit of 5 will allow up to 5 entities. Affects all types of creature spawning. Also includes entities like MINECARTS. As of **1.28.2**, entity limits apply independently per dimension, so the nether and end are now counted and limited correctly (this fixes the long-standing bug where nether/end counts reset to zero on chunk unload).

### entitylimits-nether / entitylimits-end

Optional sections that override the `entitylimits` defaults for the nether or the end respectively. They are commented out in the default config; uncomment and add entries to set dimension-specific entity limits.

Note: Only the first 49 limited blocks and entities are shown in the limits GUI.

### entitygrouplimits

!!! note "Experimental feature"
    The following feature is only available in development builds, which you may find on ci.codemc.io.

```yaml
entitygrouplimits:
  friendly:
    limit: 2
    entities:
      - COW
      - SHEEP
  monsters:
    limit: 4
    entities:
      - ZOMBIE
      - CREEPER
```

### blockgrouplimits

!!! info "Since 1.29.0"
    The block-side counterpart to `entitygrouplimits`: one shared limit across a set of block materials. The counts of every member are summed and checked against the group limit, so players can't dodge a limit by converting between related blocks (e.g. grass → dirt) or splitting across variants (piston / sticky piston). Individual `blocklimits` still apply on top if both are set.

Define a named group with an `icon`, a shared `limit`, and a `materials` list:

```yaml
blockgrouplimits:
  Pistons:
    icon: PISTON
    limit: 10
    materials:
    - PISTON
    - STICKY_PISTON
  Soil:
    icon: GRASS_BLOCK
    limit: 200
    materials:
    - GRASS_BLOCK
    - DIRT
    - DIRT_PATH
    - FARMLAND
```

Per-environment overrides are supported via `blockgrouplimits-nether` / `blockgrouplimits-end`, which override only the numeric limit of a group already defined in `blockgrouplimits`:

```yaml
blockgrouplimits-nether:
  Pistons: 5
```

!!! warning "Run a recount after changing groups"
    After adding a block group (or changing `stacked-plants-count-as-one` below), run `/[player_command] limits recount` so stored counts match the new counting rules.

### ItemsAdder & Oraxen custom blocks

!!! info "Since 1.29.0"
    Custom blocks from **ItemsAdder** and **Oraxen** can be limited using their ids directly in the existing `blocklimits` section (and its `-nether`/`-end` and `worlds:` overrides). Enforcement uses each plugin's own place/break events via BentoBox hooks, registered only when the plugin is installed. Quote keys containing a colon.

```yaml
blocklimits:
  "iafestivities:christmas/christmas_tree/green_orb": 5
  "oraxen:caveblock": 10
```

### Other toggles

=== "apply-member-limit-perms"
    !!! summary "Description"
        (**1.29.0+**) When `true`, a team member's `<gamemode>.island.limit.*` permissions are merged into the island's limits when they log in — the highest value wins. Coop and trusted players are not team members and their permissions never apply.

        Default: `false`

=== "show-limit-messages"
    !!! summary "Description"
        (**1.29.0+**) When `false`, limits are enforced silently — placements and spawns are still blocked, but players receive no hit-limit message.

        Default: `true`

=== "stacked-plants-count-as-one"
    !!! summary "Description"
        (**1.29.0+**) When `true`, a `SUGAR_CANE`, `BAMBOO` or `KELP` (kelp since **1.30.0**) stalk counts as a single plant no matter how tall it grows — only the base segment is counted. Run a recount after changing this option.

        Default: `false`

=== "log-limits-on-join"
    !!! summary "Description"
        Log an island's limits to the console when its owner joins. As of **1.29.0** this **defaults to `false`** (it previously defaulted to `true`) because it flooded the console on servers with many permission-based limits. Set it back to `true` if you relied on that output for debugging.

        Default: `false`

### Automatic entity recounts

!!! info "Since 1.30.2"
    Entity counts are maintained incrementally, so any missed event (sniffer egg hatches, mobs crossing portals, increments lost in a crash before the batched save) can leave them stuck away from reality with no way to recover except a manual recount. These options reconcile counts automatically in the background. They are **off by default** because a recount loads every chunk of the island's protection area: cost scales with the square of the protection range (64 chunks per world at range 50, 2,601 at range 400). Recounts are async, rate-limited to one island at a time, deduplicated and throttled per island, and only rewrite **entity** counts — block counts are left alone. A recount *replaces* counts rather than merging them, so it is only accurate when the island's chunks are loaded.

=== "recount-on-join"
    !!! summary "Description"
        Run a background entity-only recount of an island when its owner logs in.

        Default: `false`

=== "recount-on-join-cooldown"
    !!! summary "Description"
        Minimum seconds between automatic recounts of the same island (shared with the periodic sweep).

        Default: `300`

=== "recount-periodic"
    !!! summary "Description"
        Periodically sweep online islands to reconcile their entity counts, even while owners stay logged in. Same cost and caveats as `recount-on-join`.

        Default: `false`

=== "recount-periodic-interval"
    !!! summary "Description"
        Seconds between periodic sweep cycles.

        Default: `300`

=== "recount-periodic-batch"
    !!! summary "Description"
        Islands to reconcile per sweep cycle. Keep small on high-population servers.

        Default: `2`

=== "recount-max-chunks"
    !!! summary "Description"
        Islands whose protection area covers more than this many chunks per world are never recounted automatically; a warning is logged once per island. 1000 chunks is a protection range of about 240. Manual recounts via the `recount` and `calc` commands are not affected.

        Default: `1000`

## Permissions

Island owners can have exclusive permissions that override the default or world settings. Two formats are supported:

1. `GAME-MODE-NAME.island.limit.MATERIAL.LIMIT` — applied to every dimension.

    example: `bskyblock.island.limit.hopper.10`

2. `GAME-MODE-NAME.island.limit.ENV.MATERIAL.LIMIT` — applied to one dimension only, where `ENV` is one of `overworld`, `nether`, or `end` (1.28.2+).

    example: `bskyblock.island.limit.nether.hopper.5`

Permissions activate when the player logs in.

Usage permissions are (put the gamemode name, e.g. acidisland at the front):

```
  GAMEMODE_NAME.limits.player.limits:
    description: Player can use limits command
    default: true
  GAMEMODE_NAME.mod.bypass:
    description: Player can bypass limits
    default: op
  GAMEMODE_NAME.limits.admin.limits:
    description: Player can use admin limits command
    default: op
```

Full permissions are listed [here](Permissions).

## Placeholders

{{ placeholders_source(source="Limits") }}

!!! note "Block placeholder names"
    `[material]` is the lower-cased Minecraft key without the `minecraft:` namespace, e.g. `%Limits_bskyblock_island_spawner_limit%`. Custom blocks from ItemsAdder or Oraxen use `namespace_key` (for example `itemsadder_ruby_block`), since a colon is not valid in a placeholder name. Between 1.28.0 and 1.30.0 the block `_count`, `_limit` and `_base_limit` placeholders were mistakenly registered with the namespace baked in and did not resolve; fixed in **1.30.1**.


## Translations

{{ translations("Limits") }}

## Items that cannot be limited
Some items cannot be limited (right now). The reasons are usually because there are too many ways to remove the item without it being tracked. If you are a programmer and can work out how to fix these, then please submit a PR!

* Primed TNT
* Evoker Fangs
* Llama Spit
* Dragon Fireball
* Area Effect Cloud
* Ender signal
* Small fireball
* Fireball
* Thrown Exp Bottle
* Shulker Bullet
* Wither Skull
* Tridents
* Arrows
* Spectral Arrows
* Snowballs
* Eggs
* Leashes
* Ender crystals
* Ender pearls
* Ender dragon

!!! tip "Item frames and paintings can now be limited (1.29.0)"
    Item frames, glow item frames, and paintings were previously on this list. Since **1.29.0** entity counting is persistent and event-driven, so all three can now be configured under `entitylimits` like any other entity.


## Changelog

??? note "What's new in v1.30.2 — automatic entity recounts"
    **Released:** 2026-09-06

    A piston-counting fix plus a new opt-in feature. Compatibility: BentoBox API 2.7.1 · Paper Minecraft 1.21.11 – 26.2 · Java 21.

    - ⚙️ **Automatic entity recounts (opt-in).** New `recount-on-join` and `recount-periodic` options reconcile drifting entity counts in the background — see [Automatic entity recounts](#automatic-entity-recounts) above. Six new keys (`recount-on-join`, `recount-on-join-cooldown`, `recount-periodic`, `recount-periodic-interval`, `recount-periodic-batch`, `recount-max-chunks`) are added to `config.yml` automatically with safe defaults, so nothing changes unless you enable them. Read the config comments before turning them on. Thanks @daniel-skopek.
    - 🐛 **Extended pistons no longer count twice.** The admin recount (`calc`) counted both the base and the head of every extended piston, so a redstone build with all its pistons extended doubled the count (16 sticky pistons showing as 32/30) and every recalc put the wrong number back. The recount now counts only the base, and explosions that destroy both parts decrement once.
    - 🐛 **Entities crossing portals off-island decrement correctly.** An entity going through a portal while outside its island's protection range never had its source-dimension count decremented.

    **Piston note:** islands whose piston count is inflated show the right number after one more recount (`/[admin_command] limits calc <player>`) on this version.

    [Release v1.30.2](https://github.com/BentoBoxWorld/Limits/releases/tag/1.30.2)

??? warning "What's new in v1.30.1 — recount if you run Greenhouses"
    **Released:** 2026-09-04

    Two accuracy fixes. Compatibility: BentoBox API 2.7.1 · Paper Minecraft 1.21.11 – 26.2 · Java 21. No config or locale changes.

    - 🐛 **Block count and limit placeholders work again.** Since 1.28.0 every block placeholder was registered with the `minecraft:` namespace baked into its name, so `%Limits_bskyblock_island_spawner_limit%` was really `%Limits_bskyblock_island_minecraft:spawner_limit%` and PlaceholderAPI returned it unparsed. All block `_count`, `_limit` and `_base_limit` placeholders, including the `_overworld`, `_nether` and `_end` variants, are now registered under the documented names. Entity placeholders were never affected.
    - 🔺 🐛 **Entity counts no longer drift when a cancelled spawn is removed.** When Limits cancelled a spawn at the limit and the spawning plugin then called `remove()` on that never-added entity (Greenhouses did this), Paper still fired `EntityRemoveEvent` and Limits decremented the count for a mob that was never counted, so the next spawn slipped through (e.g. 4/3 ghasts). Removals of entities that never entered the world are now ignored.

    🔺 **Recount note:** if you run Greenhouses (or any plugin that removes entities it failed to spawn), entity counts on affected islands may have drifted low under previous versions. Run `/[admin_command] limits calc <player>` on affected islands, or have players run `/[player_command] limits recount`, so counts match reality.

    [Release v1.30.1](https://github.com/BentoBoxWorld/Limits/releases/tag/1.30.1)

??? warning "What's new in v1.30.0 — kelp recount recommended"
    **Released:** 2026-08-15

    Two counting-accuracy fixes. Compatibility: BentoBox API 2.7.1 · Paper Minecraft 1.21.11 – 26.2 · Java 21. No config or locale changes.

    - 🐛 **Bees can always leave their hives.** A bee exiting a hive is not a new bee — its count was already subtracted when it entered — but the exit was still limit-checked. On an island at its bee limit the release was cancelled, the server retried every few ticks, nearby players were spammed with "Bee spawning limited to ..." and the stored bees were trapped forever. Hive exits are now exempt from the check while still being counted, so the enter/exit cycle stays net-zero. A placed hive item carrying never-counted bees can leave the island slightly over its limit; that simply blocks further spawns and breeding until the population drops.
    - 🔺 🐛 **Kelp columns count correctly.** Kelp growth converts the `KELP` tip into a `KELP_PLANT` stalk segment with no Bukkit event, so the old block was never decremented and kelp counts only ever grew, eventually blocking placement at phantom totals. `KELP_PLANT` is now normalised to `KELP` (like `BAMBOO_SAPLING`/`BAMBOO`): growth is count-neutral, breaking the base of a column decrements every segment, `KELP` participates in `stacked-plants-count-as-one`, and variant names such as `KELP_PLANT` or `CHIPPED_ANVIL` used as limit keys configure the canonical limit.

    🔺 **If you limit kelp, run a recount.** Stored kelp counts may have drifted upward under previous versions. Run `/[admin_command] limits calc <player>` on affected islands — or have players run `/[player_command] limits recount` — so counts match reality.

    [Release v1.30.0](https://github.com/BentoBoxWorld/Limits/releases/tag/1.30.0)

??? note "What's new in v1.29.1"
    **Released:** 2026-07-23

    Compatibility: BentoBox API 2.7.1 · Paper Minecraft 1.21.11 – 26.2 · Java 21. No config or locale changes — this is a drop-in replacement.

    - 🐛 **Natural breeding now respects entity limits.** Breeding that happens without a player involved (bees, foxes, villager-run breeders, and similar) bypassed the limit check entirely, so counts could grow past the configured limit. All breeding is now checked. Players with op or the bypass permission are still exempt.
    - 🐛 **Auto-breeders no longer retry every tick.** When a breed attempt is refused at the limit, both parents are put on a breeding cooldown, and no hit-limit message is sent to nearby players unless a player actually fed the animals.
    - 🐛 **Player entries no longer leak into the entity tracking map.** Players were being added to the entity-island tracking map and never removed.
    - 🐛 **Boats are now included in `recount`.** The admin recount counted minecarts but skipped boats, which zeroed boat counts that the live tracker could not then recover.

    Thanks to [@daniel-skopek](https://github.com/daniel-skopek) for the fixes.

    [Release v1.29.1](https://github.com/BentoBoxWorld/Limits/releases/tag/1.29.1)

??? note "What's new in v1.29.0"
    **Released:** 2026-07-10

    Compatibility: BentoBox API 2.7.1 · Paper Minecraft 1.21.11 – 26.2 · Java 21.

    - ⚙️ **Block group limits.** One shared limit across a set of block materials (e.g. pistons + sticky pistons, or grass/dirt/farmland), so players can't dodge a limit by converting between related blocks. Configured under `blockgrouplimits`, with `-nether`/`-end` overrides. See the Configuration section above.
    - ⚙️ **ItemsAdder & Oraxen custom block limits.** Limit custom blocks straight from `blocklimits` using their namespaced ids.
    - ⚙️ **Team member limit permissions (opt-in).** With `apply-member-limit-perms: true`, team members' `island.limit.*` permissions can contribute to the island's limits, not just the owner's.
    - 🔡 **Reached-limits placeholders & API.** New `%Limits_<gamemode>_island_reached_limits%` placeholders (plus `_overworld`/`_nether`/`_end`) list which limits are maxed, backed by a new `Limits#getReachedLimits(...)` API. Closes the oldest open ticket in the tracker (filed in 2018).
    - ⚙️ **Stackable plants can count as one.** Optionally count a whole sugar cane or bamboo stalk as a single plant (`stacked-plants-count-as-one`).
    - ⚙️ **Silent enforcement option.** `show-limit-messages: false` turns off hit-limit chat messages while keeping limits enforced.
    - 🔡 **Manual material/entity name translations.** Locale files can now translate the block/entity names shown in the GUI and hit-limit messages.
    - **Item frames, glow item frames, and paintings can now be limited** under `entitylimits`.
    - 🐛 **Fix: phantom entity counts from portaled mobs** (e.g. `Chicken 10/10` with no chickens on the island) and a copper golem build bypassing the `COPPER_CHEST` limit.
    - ⚙️ **`log-limits-on-join` now defaults to `false`** — set it back to `true` if you relied on that console output.

    !!! warning "New config options are not added automatically"
        New keys do **not** appear in an existing `config.yml` — add the ones you want from the list above, or delete the config to regenerate it. After adding a block group or changing `stacked-plants-count-as-one`, run a recount so stored counts match the new counting rules.

    [Release v1.29.0](https://github.com/BentoBoxWorld/Limits/releases/tag/1.29.0)

??? note "What's new in v1.28.4"
    **Released:** 2026-07-06

    Maintenance release focused on keeping entity counts accurate and reliably persisted. No config or locale changes are required.

    - 🐛 **Entity counts no longer drift above reality.** Under some spawn/removal sequences the tracked entity count could climb above the number of entities actually on the island, eventually blocking spawns that should have been allowed. Counts now stay in sync with the real island population. [[#273](https://github.com/BentoBoxWorld/Limits/pull/273)]
    - 🐛 **Entity count persistence centralized.** All entity count mutations now flow through `BlockLimitsListener`, so changes are enrolled in the normal batch-save cycle instead of only being written on addon disable. This prevents count loss on an unclean shutdown or crash. [[#274](https://github.com/BentoBoxWorld/Limits/pull/274)]

    [Release v1.28.4](https://github.com/BentoBoxWorld/Limits/releases/tag/1.28.4)

??? note "What's new in v1.28.3"
    **Released:** 2026-06-29

    Bug-fix release — no data, config or locale changes; a drop-in replacement that makes per-island **entity counts** reliable across server restarts.

    - 🐛 **Entity counts no longer drift after a restart.** The map linking each entity to its island was kept in memory only and lost on every restart. Entities reloaded from chunks never re-entered it, so when they later died or despawned **off-island** their count was never decremented and slowly crept upward. Entities are now re-registered as their chunks load, so off-island removals decrement correctly again.
    - 🩹 **No more map growth on chunk unload.** The in-memory mapping is now released when a chunk unloads (and rebuilt on reload), preventing unbounded growth on long-running servers.

    [Release v1.28.3](https://github.com/BentoBoxWorld/Limits/releases/tag/1.28.3)

??? warning "What's new in v1.28.0 — Java 21 required"
    **Released:** 2026-04-01

    - **Shulker duplication farms properly limited on Paper.** Uses Paper's `ShulkerDuplicateEvent` to enforce limits before duplication occurs, fixing a bypass where shulkers teleported outside the island before the limit check.
    - **Copper chest limits can no longer be bypassed.** All copper chest variants (oxidized, waxed, scraped, golem-created) are now normalized to a single tracked material. Block state transitions are properly counted.
    - **Invalid config entries handled gracefully.** Malformed namespaced keys, non-block materials, and uncountable materials (lava, water, air) in `blocklimits` config now produce clear warning messages instead of NPEs.
    - 🔺 **Java 21 is now required** (previously Java 17). Ensure your server runs Java 21 before upgrading.
    - Bumped Spigot target to 1.21.11.

    [Release v1.28.0](https://github.com/BentoBoxWorld/Limits/releases/tag/1.28.0)

??? note "What's new in v1.28.1"
    **Released:** 2026-04-07

    Hotfix for two regressions in 1.28.0:

    - **Existing databases load again.** In 1.28.0 the `IslandBlockCount` map fields changed from `Map<Material, Integer>` to `Map<NamespacedKey, Integer>`, breaking reads of pre-1.28.0 JSON files. A backwards-compatible Gson `TypeAdapter` now reads legacy enum names, namespaced strings, and the complex array form. **No manual migration required** — old files load as-is.
    - **Block names in the limits GUI are readable again.** Items were showing as `Minecraft:hopper` due to incorrect key formatting.

    [Release v1.28.1](https://github.com/BentoBoxWorld/Limits/releases/tag/1.28.1)

??? warning "What's new in v1.28.2 — Per-dimension limits (data migration)"
    **Released:** 2026-06-13

    - 🔺⚙️ **Per-dimension limits.** Block counts, entity counts, limits, and offsets are now tracked independently for the overworld, nether, and end, fixing the long-standing bug where nether/end counts reset to zero on chunk unload ([#43](https://github.com/BentoBoxWorld/Limits/issues/43)). A single `blocklimits`/`entitylimits` value now applies to each dimension separately, with new optional `blocklimits-nether`, `blocklimits-end`, `entitylimits-nether`, and `entitylimits-end` override sections.
    - 🔺 **Data migration.** Existing single-dimension data is migrated into the **overworld** slot on first load. The on-disk format changes, so take a backup before upgrading; downgrading afterwards is not supported.
    - 🔺 **Per-dimension permissions.** A new 6-segment format, `<gamemode>.island.limit.<overworld|nether|end>.<KEY>.<NUMBER>`, scopes a limit to a single dimension. The existing 5-segment format still applies to all dimensions.
    - 🐛 Accurate counting fixes: double-counted beds/doors ([#86](https://github.com/BentoBoxWorld/Limits/issues/86)), golem/snowman block removal anchored on the pumpkin ([#127](https://github.com/BentoBoxWorld/Limits/issues/127)), three entity-counting bugs, spawn eggs no longer consumed at the limit ([#134](https://github.com/BentoBoxWorld/Limits/issues/134)), and count leaks during recount.
    - 🩹 Resolves a `NoSuchFieldError` crash on Minecraft 1.21.8 and earlier caused by referencing 1.21.9 copper blocks; these are now resolved by name.
    - 🔡 All bundled locale files converted from legacy `&` colour codes to MiniMessage, and missing keys synced across all 21 languages. Review any customised locale strings against the new files.

    Compatibility: BentoBox API 2.7.1 · Minecraft 1.21.5 – 26.1.2 · Java 21.

    [Release v1.28.2](https://github.com/BentoBoxWorld/Limits/releases/tag/1.28.2)

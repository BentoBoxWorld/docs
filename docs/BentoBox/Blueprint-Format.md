# Blueprint File Format

**Specification version 2**

This page documents the on-disk JSON format BentoBox uses for island blueprints (`.blueprint` files) and blueprint bundles (bundle `.json` files). It is the human-readable companion to the machine-readable [JSON Schemas](https://github.com/BentoBoxWorld/BentoBox/tree/develop/schemas) shipped in the BentoBox repository, which can be used to validate files in editors or CI.

If you want to *make* blueprints in game, see the [Blueprints page](Blueprints.md). This page is for developers and power users who generate, edit, or validate blueprint files directly.

## Revision history

| Version | Date | BentoBox version | Description |
|---|---|---|---|
| 1 | 2019-06-09 | [1.5.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/1.5.0) | Initial version, derivative of the BentoBox Schem format |
| 1.1 | 2026 | 2.x | Storage changed from zipped binary to plain JSON; `.blueprint` became the primary extension |
| 2 | 2026-08-14 | 3.22.x | Full field-level specification generated from the source; JSON Schemas published |

## File types

| Extension | Format | Status |
|---|---|---|
| `.blueprint` | Plain UTF-8 JSON containing a single [Blueprint](#blueprint) object | Current |
| `.blu` | ZIP archive containing a single entry of the same JSON | Legacy — still loadable, never written |
| `<uniqueId>.json` | Plain UTF-8 JSON containing a single [BlueprintBundle](#blueprintbundle) object | Current |

Both kinds of file live in a game mode addon's `blueprints/` folder, e.g. `plugins/BentoBox/addons/BSkyBlock/blueprints/`. A bundle references its blueprints by `name`, and the referenced `.blueprint` files must sit in the same folder.

## Serialization rules

Blueprints are written with Gson. These rules apply throughout and explain the shapes you will see below:

- Only the fields listed in this specification are emitted; producers must not add other keys.
- **Vectors** (`org.bukkit.util.Vector`) are a 3-element JSON array of numbers: `[x, y, z]`. Block positions customarily hold integers, but the underlying type is double.
- **Maps keyed by a Vector** use Gson's complex-map-key form: a JSON *array of pairs* — `[[<vector>, <value>], ...]` — **not** a JSON object. This applies to `blocks`, `attached`, and `entities`.
- **Maps keyed by an enum** (e.g. a bundle's `blueprints` map) are ordinary JSON objects with the enum name as the key.
- **Maps keyed by an integer** (inventory slot → item) are JSON objects with stringified integer keys (`"0"`, `"13"`, …).
- **ItemStacks** are serialized to Bukkit YAML (via `ConfigurationSerializable`) and stored as a JSON *string*. Treat the value as an opaque YAML document parseable by `YamlConfiguration#loadFromString`.
- **Enums** are serialized by their Java `name()`.
- **Colors** (`org.bukkit.Color`) are serialized as `{"ALPHA": int, "RED": int, "GREEN": int, "BLUE": int}`.
- Files are pretty-printed by the writer; consumers must not rely on whitespace.
- All field names are **case sensitive**.

## Blueprint

The top-level object of a `.blueprint` file. It describes a block volume, attached blocks, and entities relative to an anchor (`bedrock`).

| Field | Type | Description |
|---|---|---|
| `name` | string | Unique identifier, used to look the blueprint up from a bundle. Conventionally matches the filename stem. |
| `displayName` | string | Human-readable name shown in UIs. May contain legacy `§` colour codes or MiniMessage tags. |
| `icon` | string | Icon material: a Bukkit `Material` name (`DIAMOND`), a vanilla key (`minecraft:diamond`), or a resource-pack custom model key. Default `PAPER`. |
| `description` | string[] | Lore lines shown under the icon in selection UIs. |
| `bedrock` | Vector | Anchor point. When pasted, blueprint `(0,0,0)` is translated so `bedrock` lands on the paste target. If omitted, BentoBox auto-creates one at `(xSize/2, ySize/2, zSize/2)` at load time. |
| `xSize`, `ySize`, `zSize` | integer | Bounding-box dimensions in blocks. |
| `sink` | boolean | If true, the blueprint descends until it finds a surface at paste time instead of pasting at the anchor's exact Y. |
| `blocks` | Vector-keyed map | Primary blocks, keyed by position relative to the blueprint origin (`0..size-1` on each axis). See [BlueprintBlock](#blueprintblock). |
| `attached` | Vector-keyed map | Blocks pasted **after** `blocks` because they attach to a support: torches, ladders, rails, beds, doors, signs, etc. Same coordinate conventions as `blocks`. |
| `entities` | Vector-keyed map of lists | Entities to spawn per block position. Multiple entities may share one key; fine in-block offsets live on [BlueprintEntity](#blueprintentity). |

A minimal example:

```json
{
  "name": "island",
  "displayName": "&aStarter island",
  "icon": "GRASS_BLOCK",
  "description": ["A tiny island"],
  "bedrock": [2.0, 1.0, 2.0],
  "xSize": 5, "ySize": 3, "zSize": 5,
  "blocks": [
    [[2.0, 1.0, 2.0], {"blockData": "minecraft:bedrock"}],
    [[2.0, 2.0, 2.0], {"blockData": "minecraft:grass_block[snowy=false]"}]
  ],
  "attached": [
    [[2.0, 3.0, 2.0], {"blockData": "minecraft:oak_sign[rotation=0,waterlogged=false]", "signLines": ["[spawn_here]", "", "", ""]}]
  ],
  "entities": [
    [[1.0, 2.0, 1.0], [{"type": "COW", "adult": true}]]
  ]
}
```

## BlueprintBlock

One block cell. Only `blockData` is required; every other field is applied only when the block type supports it.

| Field | Type | Description |
|---|---|---|
| `blockData` | string | **Required.** Bukkit `BlockData` string, i.e. the output of `BlockData#getAsString()` — e.g. `minecraft:chest[facing=north,type=single,waterlogged=false]`. |
| `signLines` | string[] (≤4) | Front-side sign lines. Legacy `§` colour codes supported. Deprecated since 1.24.0 in favour of side-specific fields but still written and read. |
| `signLines2` | string[] (≤4) | Back-side sign lines (dual-sided signs, added in 1.24.0). |
| `glowingText` | boolean | Front side of the sign has glowing text. |
| `glowingText2` | boolean | Back side of the sign has glowing text. |
| `inventory` | slot map | Container contents (chests, barrels, hoppers, shulkers, furnaces, brewing stands, …). Keys are stringified slot indexes; values are YAML-encoded ItemStacks. |
| `bannerPatterns` | object[] | Banner pattern layers, applied in order. Each entry has `pattern` (legacy short code, e.g. `bri`) and `color` (a `DyeColor` name). |
| `biome` | string | Biome override for this block cell (Bukkit `Biome` name). |
| `creatureSpawner` | object | Present only when `blockData` is a spawner. See [BlueprintCreatureSpawner](#blueprintcreaturespawner). |
| `trialSpawner` | object | Present only when `blockData` is a trial spawner (1.21+, added in BentoBox 3.4.2). Mutually exclusive with `creatureSpawner`. See [BlueprintTrialSpawner](#blueprinttrialspawner). |
| `itemsAdderBlock` | string | ItemsAdder custom block id (e.g. `myserver:custom_ore`). Only meaningful when ItemsAdder is installed; otherwise the block falls back to `blockData`. |

### BlueprintCreatureSpawner

Vanilla (non-trial) mob spawner configuration.

| Field | Type | Description |
|---|---|---|
| `spawnedType` | string | Bukkit `EntityType` name. |
| `delay` | integer | Current countdown (ticks) until the next spawn attempt. |
| `maxNearbyEntities` | integer | Spawning pauses while at least this many of the spawned type are within tracking range. |
| `minSpawnDelay`, `maxSpawnDelay` | integer | Bounds (ticks) of the randomised delay picked after each spawn. |
| `requiredPlayerRange` | integer | Maximum player distance (blocks) that keeps the spawner active. |
| `spawnRange` | integer | Radius (blocks) within which mobs may spawn. |

### BlueprintTrialSpawner

Trial spawner configuration (Minecraft 1.21+). Use `spawnedType` **or** `potentialSpawns`, not both.

| Field | Type | Description |
|---|---|---|
| `ominous` | boolean | Whether the spawner is in its ominous (cursed) state. |
| `spawnedType` | string | Single `EntityType` to spawn. |
| `potentialSpawns` | object[] | Weighted spawn candidates. Each entry: `snapshot` (opaque `EntitySnapshot#getAsString` value), `spawnrule` (Bukkit `SpawnRule` object; keys vary by server version), and required `spawnWeight` (integer ≥ 1). |
| `delay` | integer | Spawn delay. |
| `baseSimEnts` / `addSimulEnts` | number | Base simultaneous entities kept alive / additional per extra player. |
| `baseSpawnsB4Cool` / `addSpawnsB4Cool` | number | Base total spawns before cooldown / additional per extra player. |
| `spawnRange`, `requiredPlayerRange`, `playerRange` | integer | Ranges in blocks. |
| `lootTableMap` | array of pairs | Candidate reward loot tables with relative weights: `[[{"nameSpace": "minecraft", "key": "chests/trial_chambers/reward"}, 1], ...]`. |

## BlueprintEntity

One entity to spawn. Only `type` is required. Unset fields mean "leave the Bukkit default alone"; each field is applied only when the entity class supports it.

**General**

| Field | Type | Description |
|---|---|---|
| `type` | string | **Required.** Bukkit `EntityType` name (`VILLAGER`, `ARMOR_STAND`, `ITEM_FRAME`, …). |
| `customName` | string | Display name; legacy `§` colour codes supported. |
| `x`, `y`, `z` | number | Fine offset within the position cell (typically `0.0 ≤ v < 1.0`). |
| `glowing` | boolean | Glow effect. |
| `gravity` | boolean | Whether gravity applies. |
| `visualFire` | boolean | Render fire regardless of `fireTicks`. |
| `silent` | boolean | Suppress ambient sounds. |
| `invulnerable` | boolean | Immune to all damage. |
| `fireTicks` | integer | Remaining fire duration (ticks). |

**Mobs**

| Field | Type | Description |
|---|---|---|
| `adult` | boolean | Ageable entities — `false` spawns a baby. |
| `color` | string | `DyeColor` name, for colourable entities (sheep, shulker, wolf collar, …). |
| `tamed` | boolean | Tameable entities; the owner is not restored. |
| `chest` | boolean | Chest-carrying horses/llamas. |
| `domestication` | integer (0–100) | Horse domestication level. |
| `inventory` | slot map | Horse/llama inventory. |
| `style` | string | Horse coat style: `WHITE`, `WHITEFIELD`, `WHITE_DOTS`, `BLACK_DOTS`, `NONE`. |
| `profession` | string | Villager profession (enum name or namespaced key). |
| `level` | integer (1–5) | Villager level. |
| `experience` | integer | Villager experience. |
| `villagerType` | string | Villager biome variant (enum name or namespaced key). |

**Plugin integrations** (only meaningful when the plugin is installed)

| Field | Type | Description |
|---|---|---|
| `npc` | string | Citizens NPC id. |
| `MMtype`, `MMLevel`, `MMpower`, `MMStance` | string / number | MythicMobs type, level, power, and stance. |

**Display entities and item frames**

| Field | Type | Description |
|---|---|---|
| `displayRec` | object | Properties common to all display entities — see [DisplayRec](#displayrec). |
| `blockDisp` | object | BlockDisplay payload: the displayed block, as a [BlueprintBlock](#blueprintblock). |
| `itemDisp` | object | ItemDisplay payload: `item` (YAML-encoded ItemStack) and `itemDispTrans` (an `ItemDisplayTransform` name: `NONE`, `HEAD`, `GUI`, `GROUND`, `FIXED`, `THIRDPERSON_LEFTHAND`, …). |
| `textDisp` | object | TextDisplay payload — see below. |
| `itemFrame` | object | ItemFrame payload (since 3.2.6): `item` (YAML-encoded ItemStack), `rotation` (Bukkit `Rotation` name), `isFixed`, `isVisible`, `dropChance` (0.0–1.0). |

TextDisplay payload fields: `text` (legacy `§` codes accepted), `alignment` (`CENTER`/`LEFT`/`RIGHT`), `bgColor` (Color object), `face` (a `BlockFace` name), `lWidth` (line-wrap width in pixels), `opacity` (signed byte, −1 = default), `isShadowed`, `isSeeThrough`, `isDefaultBg`.

### DisplayRec

| Field | Type | Description |
|---|---|---|
| `billboard` | string | `FIXED`, `VERTICAL`, `HORIZONTAL`, or `CENTER` — how the display faces the viewer. |
| `brightness` | object | Bukkit `Display.Brightness`, typically `{"block": int, "sky": int}`. |
| `width`, `height` | number | Display size. |
| `glowColorOverride` | Color | Glow outline colour. |
| `interpolationDelay`, `interpolationDuration`, `teleportDuration` | integer | Animation timings. |
| `shadowRadius`, `shadowStrength` | number | Shadow rendering. |
| `transformation` | object | Bukkit `Transformation` (translation, rotations, scale). Opaque. |
| `range` | number | View range. |

## BlueprintBundle

A bundle groups up to three blueprints — one per world environment — into a single option in the island-creation UI, and controls that option's cost, permission, GUI slot, usage cap, and post-creation commands. Persisted as `<uniqueId>.json` in the game mode's `blueprints/` folder; the filename stem **must** equal `uniqueId`.

| Field | Type | Description |
|---|---|---|
| `uniqueId` | string | **Required.** Unique id; also the permission suffix when `requirePermission` is true. |
| `displayName` | string | Name shown in the selection GUI. |
| `icon` | string | Icon material, same forms as a blueprint icon. Default `PAPER`. |
| `description` | string[] | Lore lines under the icon. |
| `blueprints` | object | Map from environment (`NORMAL`, `NETHER`, `THE_END`, `CUSTOM`) to the `name` of a blueprint in the same folder. Environments with no entry are not generated. |
| `requirePermission` | boolean | If true, players need `<gamemode>.island.create.<uniqueId>`. |
| `slot` | integer | Preferred 0-based GUI slot; clamped at runtime. |
| `times` | integer | Maximum islands a single player may create with this bundle; `0` = unlimited. |
| `cost` | number | Vault-economy cost; `0` = free. Requires an economy plugin. |
| `commands` | string[] | Commands run when an island is created with this bundle (added in 2.6.0). `[player]` and `[owner]` are substituted; entries prefixed `[SUDO]` run as the player, others as console. |

Example `default.json`:

```json
{
  "uniqueId": "default",
  "displayName": "Default Island",
  "icon": "GRASS_BLOCK",
  "description": ["A standard island", "with grass and dirt"],
  "blueprints": {
    "NORMAL": "island",
    "NETHER": "nether",
    "THE_END": "end"
  },
  "requirePermission": false,
  "slot": 0,
  "times": 0,
  "cost": 0.0,
  "commands": ["[SUDO] me has arrived!"]
}
```

## Validating files

The BentoBox repository publishes two JSON Schemas (draft 2020-12):

- [`schemas/blueprint.schema.json`](https://github.com/BentoBoxWorld/BentoBox/blob/develop/schemas/blueprint.schema.json) — validates a `.blueprint` file or a bundle
- [`schemas/blueprint-bundle.schema.json`](https://github.com/BentoBoxWorld/BentoBox/blob/develop/schemas/blueprint-bundle.schema.json) — validates a bundle file on its own

Point your editor or CI validator at them, e.g. with [ajv](https://ajv.js.org/):

```bash
ajv validate --spec=draft2020 -s blueprint.schema.json -d island.blueprint
```

Note that YAML-encoded ItemStack strings and a few Bukkit `ConfigurationSerializable` objects (transformations, spawn rules) are opaque to the schema — a schema-valid file can still fail to load if those embedded documents are malformed.

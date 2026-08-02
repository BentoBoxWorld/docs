# Customizing AOneBlock Phases

Everything a player mines out of the magic block comes from a **phase file**. This page explains how those files work, what every number in them means, and how to build your own phases.

!!! tip "The short answer"
    The numbers after a material or entity — `COBBLESTONE: 900` — are **weights**, not counts and not percentages. A phase adds up every weight it has and picks one entry at random in proportion to its weight. `blocks:`, `mobs:` and `custom-blocks:` all draw from that same single pool.

## Where the files live

After the addon has run once, the files are in:

```
plugins/BentoBox/addons/AOneBlock/
├── config.yml
├── phases_index.yml          ← which phases load, in what order, and how long each is
└── phases/
    ├── 0_plains.yml          ← the blocks, mobs, holograms and settings of a phase
    ├── 0_plains_chests.yml   ← the loot tables of that phase
    ├── 700_underground.yml
    ├── 700_underground_chests.yml
    └── ...
```

Every phase is a pair of files: `<name>.yml` and `<name>_chests.yml`. The chest file is paired **by file name**, so if you rename one you must rename the other.

!!! info "`0_plains.yml` is the reference file"
    The shipped `0_plains.yml` is heavily commented and documents every option. If you only read one file, read that one. This page covers the same ground with worked examples.

After editing any of these files, reload the addon (`/bbox reload`) or restart the server.

---

## The three kinds of number

This is the part that trips people up. A phase file contains three completely different kinds of number, and which is which depends entirely on **the section it is in**.

| Where | What the number is |
|---|---|
| `blocks:`, `mobs:`, `custom-blocks:` | A **weight** — this entry's share of the random pool. |
| Keys in `fixedBlocks:` and `holograms:` | A **position** — how many blocks into *this phase*, counting from 0. |
| The top-level key of the file (`'0':`, `'2500':`) | The phase's **section name**, historically its start block. Phase order and length now come from `phases_index.yml`. |

---

## Weights — the `blocks:` and `mobs:` sections

### How the roll works

Every time a player breaks the magic block, AOneBlock:

1. Adds up **every** weight in the current phase — all of `blocks:`, all of `mobs:`, and all of `custom-blocks:`.
2. Picks a random number in that range and returns whichever entry it lands on.

So:

```
chance of an entry = its weight ÷ total of all weights in the phase
```

A weight is not a quantity. `STONE: 1000` does not mean a thousand stone will be generated during the phase — it means stone gets 1000 tickets in the raffle, and it is rolled fresh on every single block break.

### Worked example

```yaml
'2500':
  name: Winter
  firstBlock: SNOW_BLOCK
  biome: SNOWY_TAIGA
  blocks:
    COBBLESTONE: 900
    SAND: 100
    DIRT: 200
    STONE: 1000
    SPRUCE_LEAVES: 500
```

The weights total `900 + 100 + 200 + 1000 + 500 = 2700`, so:

| Block | Weight | Chance per break |
|---|---:|---:|
| `STONE` | 1000 | 1000 / 2700 = **37.0%** |
| `COBBLESTONE` | 900 | 900 / 2700 = **33.3%** |
| `SPRUCE_LEAVES` | 500 | 500 / 2700 = **18.5%** |
| `DIRT` | 200 | 200 / 2700 = **7.4%** |
| `SAND` | 100 | 100 / 2700 = **3.7%** |

Over a 1000-block phase you would *expect* about 370 stone, but every break is an independent roll, so the real count wobbles around that figure.

### Only the ratio matters

```yaml
blocks:
  STONE: 1000
  DIRT: 200
```

behaves **identically** to

```yaml
blocks:
  STONE: 10
  DIRT: 2
```

The shipped files use large numbers on purpose: with a total in the thousands you can add a rare entry at weight `5` without having to rescale everything else to keep the percentages sensible.

### Blocks and mobs share one pool

!!! warning "Mob weights count towards the same total as block weights"
    `mobs:` is not a separate roll. A mob entry is just another ticket in the same raffle, so `CHICKEN: 200` is exactly as likely as a block with weight 200 — and adding mobs makes every block slightly rarer.

The shipped Plains phase makes this concrete. Its `blocks:` weights total 11450 and its `mobs:` weights total 665, for a phase total of **12115**:

| Entry | Weight | Chance per break |
|---|---:|---:|
| `GRASS_BLOCK` | 2000 | 16.5% |
| `OAK_LOG` | 2000 | 16.5% |
| `CHEST` | 200 | 1.7% |
| `CHICKEN` *(mob)* | 200 | 1.7% |
| `COW` *(mob)* | 150 | 1.2% |
| `DIAMOND_ORE` | 30 | 0.25% |
| `VILLAGER` *(mob)* | 15 | 0.12% |
| `EMERALD_ORE` | 10 | 0.08% |

### Tuning recipes

| You want to… | Do this |
|---|---|
| Make something twice as common | Double its weight |
| Remove something | Delete the line (or comment it out) |
| Add a block at roughly *X*% | Weight ≈ `X/100 × current total ÷ (1 − X/100)` — or just take the current total, and for ~1% add an entry of weight ≈ total/100 |
| Rebalance a whole phase | Change one weight at a time — every change shifts every other percentage, because the total moves |
| Make mobs rarer without touching blocks | Lower the `mobs:` weights; the block percentages rise automatically |

### Rules and gotchas

- A weight must be a **whole number of 1 or more**. `0`, a negative value or a decimal is rejected and logged as `Bad item weight for <phase>: <material>`.
- The material must be a real Bukkit [Material](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html) **that is a block**. Items like `DIAMOND` will be logged as `Bad block material`.
- Mobs must be a live, spawnable [EntityType](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/EntityType.html). Invalid names log the full list of valid ones on startup.
- If a phase has no valid weights at all, it logs `has zero probability of generating blocks` and falls back to a single block type — check the section name spelling.

### `CHEST` is a special case

When `CHEST` is rolled from the pool, AOneBlock fills it from that phase's `_chests.yml` file. So the `CHEST` weight is the chance of getting **a** chest; which chest you get is a **second, separate roll on rarity**:

| Rarity | Chance |
|---|---:|
| `COMMON` | 62% |
| `UNCOMMON` | 25% |
| `RARE` | 9% |
| `EPIC` | 4% |

These rarity chances are fixed in code and are not configurable. If a rarity has no chests defined for the phase, the `COMMON` list is used instead; if there are no chests at all, a plain empty chest is placed.

### Mobs

When a mob is rolled, the magic block becomes `STONE` if it was empty and the mob spawns on top of it. With `clear-blocks: true` in `config.yml`, blocks in the way are cleared so large mobs fit.

```yaml
mobs:
  COW: 150
  SPIDER: 75
  SHEEP: 75
  PIG: 150
  VILLAGER: 15
  CHICKEN: 200
```

---

## Positions — `fixedBlocks` and `holograms`

The keys in these two sections are **positions within the phase**, counting from 0. Position `0` is the first block of the phase, `1` the second, and so on. They are *not* the player's overall block count, and a position larger than the phase length is simply never reached.

### `fixedBlocks`

Fixed blocks are guaranteed — they bypass the weighted pool entirely. Use them for scripted moments.

```yaml
fixedBlocks:
  0: GRASS_BLOCK
  1: GRASS_BLOCK
  2: GRASS_BLOCK
  3: OAK_LOG
  4: OAK_LOG
  5: OAK_LOG
  700: CHEST_WITH_WATER_BUCKET
```

- Defining position `0` here replaces `firstBlock`, which is then no longer needed.
- `CHEST_WITH_<ITEM>` is a shorthand that places a chest holding a single item of that material — handy for giving players a water bucket before the Ocean phase.
- Prefer blocks that do not need support. A torch, rail or sapling placed as the magic block just pops off.
- A fixed block entry can also be a [custom block](#custom-blocks) definition.

### `holograms`

Same numbering, but the value is the text to float above the magic block. `&` colour codes work.

```yaml
holograms:
  0: "&aFirst block is grass!"
  1: "&aSecond block is grass!"
  3: "&aGood Luck!"
```

The very first hologram — the one shown before phase 1 begins — lives in the addon's locale file, not here.

---

## Phase order and length — `phases_index.yml`

!!! new "Since AOneBlock 1.26.0"
    Phase order and length are **not** taken from the file names or the top-level keys any more. `phases_index.yml` is the source of truth.

```yaml
phases:
  - file: 0_plains
    section: '0'
    name: Plains
    length: 700
  - file: 700_underground
    section: '700'
    name: Underground
    length: 1300
gotoAtEnd: 0
```

| Field | Meaning |
|---|---|
| `file` | Base name of the phase file, without `.yml`. The chest file is `<file>_chests.yml`. |
| `section` | The top-level key inside that phase file. |
| `name` | Display name, used in logs and in `/[admin_command] phases`. |
| `length` | How many blocks this phase lasts. |
| `enabled` | Optional, defaults to `true`. Set `false` to leave the phase out entirely. |
| `requiredMinecraftVersion` | Optional. The phase is skipped on older servers, taking up no blocks at all. |

Start blocks are **computed**: each phase starts at the running total of the lengths of the enabled phases above it, beginning at 0. Reorder phases freely; a disabled or skipped phase collapses out of the progression. After the last phase the block count jumps to `gotoAtEnd`.

The easiest way to change all of this is in game with `/[admin_command] phases`, which edits the index for you. See the [phase order editor](index.md#commands) notes. Once you edit a length there, `adminLengths: true` is written into the index and your lengths are never recomputed.

!!! tip "The number in a file name is only a hint"
    `0_plains`, `2500_winter` and so on are historical. A custom phase can be `my_phase.yml` with a `my_phase:` top-level key and no numbers anywhere. The numbers are still useful for a brand-new file: they tell the index reconciler where the phase belongs in the running order.

---

## Anatomy of a phase file

```yaml
'0':                          # section name (see phases_index.yml)
  name: Plains                # display name
  icon: GRASS_BLOCK           # icon in the phases GUI (BentoBox ItemParser)
  firstBlock: GRASS_BLOCK     # the block for position 0 (optional)
  biome: PLAINS               # biome at the magic block location
  requiredMinecraftVersion: '1.21.6'   # optional version gate

  fixedBlocks: { ... }        # guaranteed blocks at positions
  holograms: { ... }          # text at positions

  blocks: { ... }             # weighted pool of blocks
  mobs: { ... }               # weighted pool of mobs — same pool
  custom-blocks: [ ... ]      # weighted pool of custom entries — same pool

  start-commands: [ ... ]
  end-commands: [ ... ]
  end-commands-first-time: [ ... ]
  requirements: { ... }
```

=== "name"
    The display name, shown in the phases GUI, the boss bar, log lines and the `[phase]` command placeholder.

=== "icon"
    The icon used in the phases GUI only. Parsed with the [BentoBox ItemParser](../../BentoBox/ItemParser.md), so custom player heads and any displayable item work. A phase with no icon falls back to its first block.

=== "firstBlock"
    The block placed at position 0 of the phase. Optional — defining `0:` under `fixedBlocks` does the same job and takes precedence.

=== "biome"
    Changes the biome at the **magic block location only**, not the whole island. To rebiome a whole island on a phase change, call the Biomes addon from a `start-commands` entry. An invalid biome name logs the complete list of valid biomes on startup.

=== "requirements"
    Gates entry to the phase. Until every requirement is met the player is held at the end of the previous phase.

    - `economy-balance` — minimum player balance (requires Vault and an economy plugin)
    - `bank-balance` — minimum island bank balance (requires the Bank addon)
    - `level` — minimum island level (requires the Level addon)
    - `permission` — a permission string the player must have
    - `cooldown` — seconds that must pass since the phase was last started

    ```yaml
    requirements:
      bank-balance: 10000
      level: 10
      permission: ready.for.battle
      cooldown: 60
    ```

---

## Commands on phase change

Commands run as the **console** unless prefixed with `[SUDO]`, in which case they run as the player who triggered them.

| Section | When it runs |
|---|---|
| `start-commands` | When the phase begins |
| `end-commands` | Every time the phase is completed |
| `end-commands-first-time` | Only the **first** time this island completes the phase |

Placeholders substituted into the command string:

| Placeholder | Value |
|---|---|
| `[island]` | Island name |
| `[owner]` | Island owner's name |
| `[player]` | Name of the player who broke the block |
| `[phase]` | Name of this phase |
| `[blocks]` | Number of blocks broken |
| `[level]` | Island level (requires the Level addon) |
| `[bank-balance]` | Island bank balance (requires the Bank addon) |
| `[eco-balance]` | Player's economy balance (requires Vault and an economy plugin) |

```yaml
start-commands:
- 'give [player] WOODEN_AXE 1'
- 'broadcast [player] just started OneBlock!'
end-commands-first-time:
- 'broadcast &c&l[!] &b[player] &fhas completed the &d&n[phase]&f phase for the first time.'
```

---

## Chests

Chests live in the phase's `_chests.yml` file, under the same top-level section name:

```yaml
'0':
  chests:
    '1':
      rarity: COMMON
      contents:
        0: ==: org.bukkit.inventory.ItemStack ...
    '2':
      rarity: EPIC
      contents:
        ...
```

- The number keying each chest (`'1'`, `'2'`) is just a **unique id** — it is neither a weight nor a position. When a chest of a given rarity is due, one of the chests of that rarity is picked at random with equal probability.
- `contents` keys are **inventory slot numbers**.
- `rarity` is `COMMON`, `UNCOMMON`, `RARE` or `EPIC`.

!!! tip "Build chests in game, not by hand"
    Fill a real chest with what you want, look at it, and run `/[admin_command] setchest <phase> <rarity>`. The chest is serialized straight into the phase's chest file, correctly, first time. Hand-editing serialized item YAML is error-prone; use `/[admin_command] sanity [<phase>]` afterwards to check your loot tables. Deleting a chest still means editing the file and reloading.

---

## Custom blocks

`custom-blocks:` is a list of entries that are not plain materials. Each entry has a `probability:` field which — despite the name — is a **weight**, in exactly the same pool as `blocks:` and `mobs:`. `probability: 10` is as likely as a block with weight `10`.

```yaml
custom-blocks:
  - type: block-data
    data: minecraft:chest[waterlogged=true]
    probability: 10
  - type: mob
    mob: ZOMBIE
    underlying-block: STONE
    probability: 5
  - type: itemsadder
    id: mypack:ruby_ore
    probability: 10
```

| `type` | What it does | Requires |
|---|---|---|
| `block` / `block-data` | Runs `/setblock` with full block data — block states, NBT, and an optional `destroy`\|`keep`\|`replace` mode. Prefer `block` when using NBT. | — |
| `mob` | Spawns a vanilla entity using the Spawn Entity API. | `mob`; optional `underlying-block` (default `STONE`) |
| `mob-data` | Runs `/summon` with vanilla NBT/components. Blocks inside the mob's (scaled) bounding box are cleared a tick after spawn so it fits. | `data` |
| `mythic-mob` | Spawns a MythicMob through BentoBox's hook. | MythicMobs plugin |
| `itemsadder` | Block from [ItemsAdder](https://itemsadder.devs.beer/). | ItemsAdder plugin |
| `nexo` | Block from [Nexo](https://polymart.org/resource/nexo.6901). | Nexo plugin |
| `craftengine` | Block from [CraftEngine](https://github.com/Xiao-MoMi/craft-core). | CraftEngine plugin, BentoBox 3.15.0+ |

Custom blocks can also be used in `fixedBlocks`, as an object instead of a material name:

```yaml
fixedBlocks:
  0:
    type: block-data
    data: minecraft:chest[waterlogged=true]
  1: GRASS_BLOCK
```

!!! warning "Quote your data strings"
    Custom block `data` strings contain `{`, `}`, `[`, `]` and double quotes. Wrap the whole value in **single** quotes so the inner double quotes do not clash with YAML's string delimiters.

    ```yaml
    - type: mob-data
      data: 'breeze{CustomName:[{text:"Breezy",color:"#f90606"}],Glowing:1b}'
      underlying-block: STONE
      probability: 10
    ```

!!! tip "Spawner gotcha"
    A `spawner` placed without the timing fields is inactive in vanilla 1.21 (`Delay:-1` means "never tick"). Set `Delay`, `MinSpawnDelay`, `MaxSpawnDelay` and friends explicitly, or the spawner appears and does nothing. `Delay:0` makes the first spawn happen on the very next tick.

If a custom block's plugin is not installed, the block falls back to `STONE` and a line is written to the log.

---

## Version gating

A phase, an individual block or an individual mob can declare the minimum Minecraft version it needs. Anything the server is too old for is skipped with one info line in the log instead of a `Tried to load invalid item` error.

**Whole phase** — put `requiredMinecraftVersion` in `phases_index.yml` so the file is not even parsed on an old server. The phase then takes up no blocks and the phases after it collapse up.

**A single block or mob** — use the object form, which swaps the bare weight for a `weight:` field:

```yaml
blocks:
  NETHERRACK: 300
  DRIED_GHAST:
    weight: 25
    requiredMinecraftVersion: '1.21.6'

mobs:
  ZOMBIFIED_PIGLIN: 100
  HAPPY_GHAST:
    weight: 5
    requiredMinecraftVersion: '1.21.6'
```

Chest files are read item by item, so an item your server version does not know is skipped on its own and the rest of the chest still loads.

---

## Building a new phase

1. **Copy an existing pair of files** in the `phases` folder — say `4000_jungle.yml` and `4000_jungle_chests.yml` — to `volcano.yml` and `volcano_chests.yml`.
2. **Change the top-level key** in both files to something unique, e.g. `volcano:`. It must match in both.
3. **Set `name:` and `icon:`**, then edit `blocks:` and `mobs:` with the weights you want. Remember the percentages are relative to the *phase* total.
4. **Restart or reload.** The addon notices the new file, adds it to `phases_index.yml` at the end of the order with the default length of 500, and logs:
   `Phase index: added Volcano from volcano.yml at the end of the phase order. Move it with the admin phases GUI.`
5. **Position it** with `/[admin_command] phases` — left-click to pick it up, click where it should go, shift-left-click to set its length.
6. **Test it** with `/[admin_command] setcount <player> <number>` to jump straight to the phase's start block.

!!! tip "Test on a scratch island"
    Break a couple of hundred blocks and see what actually comes out. Weights read very differently on paper than they play. `/[player_command] count` shows where you are in the phase.

---

## Troubleshooting

| Symptom | Likely cause |
|---|---|
| `Bad block material in <phase>: X` | `X` is not a Bukkit material, or is an item rather than a block |
| `Bad item weight for <phase>: X. Must be positive number above 1` | The weight is 0, negative or not a whole number |
| `Bad entity type in <phase>: X` | Not a valid `EntityType`; the log lists the valid ones |
| `<phase> has zero probability of generating blocks` | The `blocks:` section is missing, empty, or under the wrong section key |
| `Phase name trying to be set to X but already set to Y. Duplicate phase file?` | Two files use the same top-level section key |
| A phase never appears | It is `enabled: false` in `phases_index.yml`, or its `requiredMinecraftVersion` is newer than the server |
| Chests come out empty | The chest file's top-level key does not match the phase file's, or its items failed to load — run `/[admin_command] sanity` |
| Edits do nothing | The addon was not reloaded, or you edited the file in `src/main/resources` in the jar rather than `plugins/BentoBox/addons/AOneBlock/phases/` |

Watch the server log at startup. Every phase file loaded is logged, as is every rejected block, mob and item, and every change the index reconciler makes (lines beginning `Phase index:`).

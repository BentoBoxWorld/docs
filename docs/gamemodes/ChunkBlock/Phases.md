# The Magic Block and Phases

ChunkBlock's magic block is the AOneBlock engine, carried over deliberately unchanged. Everything about phase files — the weighted block and mob pools, `fixedBlocks`, holograms, chests and rarities, custom blocks, version gating, start and end commands, requirements, the phase index — works exactly as it does in AOneBlock, and the file formats are identical.

That means:

- **Community phase packs work verbatim.** A phase file written for AOneBlock drops into ChunkBlock's `phases` folder and runs.
- **You can copy your own AOneBlock phases across** without editing them.
- **Fixes and features from upstream arrive here too**, because the engine is kept in step rather than forked.

!!! abstract "Full field reference: [Customizing AOneBlock Phases](../AOneBlock/Phases.md)"
    That guide is the complete walkthrough — what every number means, how the weighted raffle works with worked examples, chests, custom blocks, version gating and how to build a phase from scratch. All of it applies here unchanged.

    Only the **command names** differ: read `/oba` as `/chadmin` and `/ob` as `/ch` throughout.

This page covers what is specific to ChunkBlock.

---

## What ships

Twenty phases, 15,500 blocks of content on a Minecraft 26.2+ server:

| # | Phase | Length | Starts at |
|---:|---|---:|---:|
| 1 | Plains | 700 | 0 |
| 2 | Underground | 1300 | 700 |
| 3 | Winter | 1000 | 2000 |
| 4 | Ocean | 1000 | 3000 |
| 5 | Jungle | 1000 | 4000 |
| 6 | Swamp | 1000 | 5000 |
| 7 | Dungeon | 1000 | 6000 |
| 8 | Desert | 500 | 7000 |
| 9 | The Nether | 1000 | 7500 |
| 10 | Plenty | 1000 | 8500 |
| 11 | Desolation | 1000 | 9500 |
| 12 | Deep Dark | 1000 | 10500 |
| 13 | The End | 500 | 11500 |
| 14 | Lush Caves | 500 | 12000 |
| 15 | Dripstone Caves | 500 | 12500 |
| 16 | Mangrove Swamp | 500 | 13000 |
| 17 | Meadow | 500 | 13500 |
| 18 | Cherry Grove | 500 | 14000 |
| 19 | Jagged Peaks | 500 | 14500 |
| 20 | Sulfur Caves | 500 | 15000 |

**Sulfur Caves needs Minecraft 26.2 or later.** It declares `requiredMinecraftVersion: '26.2'` in the index, so on older servers it is skipped with a single info log line — the phase takes up no blocks at all and Jagged Peaks simply runs to the loop point instead. That server has 19 phases and 15,000 blocks.

After the last phase the block count jumps back to `gotoAtEnd` in `phases_index.yml`, which is `0` by default, so the progression loops.

---

## Where the files live

```
plugins/BentoBox/addons/ChunkBlock/
├── config.yml
├── phases_index.yml          ← order, length, enabled, version gate
├── panels/
│   └── phases_panel.yml      ← the /ch phases GUI template
└── phases/
    ├── 0_plains.yml          ← blocks, mobs, holograms, commands
    ├── 0_plains_chests.yml   ← the loot for that phase
    ├── 700_underground.yml
    └── …
```

Files in `phases/` are **never overwritten** on upgrade, so your edits survive. New phases shipped in a later jar are restored into the index automatically by reconciliation.

---

## The phase index

`phases_index.yml` is the source of truth for which phases load, in what order, how long each one is, and which Minecraft version each one needs. It is read **before** any phase file is parsed, so a phase that needs a newer Minecraft version is skipped without its YAML — or any item inside it — ever being touched.

Each entry takes these fields:

| Field | Meaning |
|---|---|
| `file` | Base name of the phase file in the `phases` folder, without `.yml`. The chest file is `<file>_chests.yml`. |
| `section` | The top-level key inside the phase file (historically the start block). |
| `name` | Display name, used in logs and in the `/chadmin phases` panel. |
| `length` | Number of blocks in the phase. |
| `enabled` | Optional, defaults to `true`. Set `false` to leave a phase out. |
| `requiredMinecraftVersion` | Optional. The phase is skipped — taking up no blocks at all — on servers older than this version. |

Start blocks are **computed**: the running sum of the lengths of the enabled phases above, starting at 0. Phases can be reordered freely, and a skipped phase collapses out of the progression.

A top-level `adminLengths: true` is written automatically the first time you edit a length in the panel. From then on reconciliation never recomputes lengths, so your values survive later file additions, renames and upgrades.

### Reconciliation

The index is reconciled against the files actually on disk on every load and on every save from the admin panel, so what `/chadmin phases` shows is what your server really runs. Watch the startup log for lines beginning `Phase index:` — they say exactly what changed.

- An entry whose file was **renamed across addon versions** is re-pointed at your file by phase name.
- An entry whose file is **missing but shipped in the jar** is restored automatically. This is how new phases appear on upgraded servers, given that `phases/` is never overwritten.
- **Custom phase files** dropped into the folder are added automatically. A numeric key slots in at its legacy start block; anything else is appended at the end for you to arrange in the panel.
- Entries whose files are gone for good are removed with a warning.

!!! warning "Deleting a phase"
    To remove a phase permanently, delete its files, or toggle it off in `/chadmin phases`. Deleting only its index entry does not work — reconciliation re-adds any phase file it finds in the folder.

    A malformed index falls back to direct file loading, so a bad edit cannot leave the addon stuck.

!!! tip "Numbers in file names are optional"
    A custom `desert.yml` with a `desert:` section works fine. Chest files still pair by file name (`<file>_chests.yml`). The numbers in the shipped files are historical: with the index in charge, the panel's start and length values are the truth.

---

## The phase order editor

`/chadmin phases` (permission `chunkblock.admin.phases`, OP by default) shows every phase in order with its computed start block, length and state. It edits `phases_index.yml`, and drops and toggles save the index and reload the phases immediately.

- **Left-click** a phase to pick it up — the rest shrink left. Click where it should go to shove the others right and drop it, or use the drop-at-end slot. Click anywhere else, or close the panel, to put it back without saving.
- **Right-click** toggles a phase on or off.
- **Shift-left-click** sets a phase's length. The panel closes and a chat prompt shows the current length; type a whole number to apply it, or `cancel` to keep it. Invalid input re-prompts and the prompt times out after 60 seconds. The first length edit writes `adminLengths: true` into the index.

Disabled phases show as grey glass and version-locked ones as barriers — both can still be reordered. A phase with no configured icon uses its first block.

---

## Players and phases

- `/ch count` — the current block count and phase, in chat.
- `/ch phases` — the phases GUI. Requires `chunkblock.phases`, which is **off by default**.
- `/ch setcount <number>` — replay a phase already reached. Requires `chunkblock.island.setcount` (OP by default) and obeys the `set-count-cooldown` config value, 5 minutes by default.
- `/ch check` — respawn the magic block if it has gone missing, or show its particles so you can find it.
- `/ch bossbar` / `/ch actionbar` — toggle the progress displays, if `bossbar` / `actionbar` are enabled in `config.yml`.

Holograms above the magic block are on by default (`world.holograms: true`), use native Minecraft text entities, and disappear after `hologram-duration` seconds.

---

## Admin phase tools

- `/chadmin setcount <player> <number> [lifetime]` — set a player's block count, or their lifetime count.
- `/chadmin setchest <phase> <rarity>` — the easy way to build loot. Fill a chest in-game with what you want, look at it, and run the command with the phase name and a rarity of `COMMON`, `UNCOMMON`, `RARE` or `EPIC`. The chest is written into that phase's chest file, ready to use. Deleting chests still means editing the file and reloading.
- `/chadmin sanity [<phase>]` — reports the phase probabilities in the console, so you can see what your weights actually add up to.
- `/chadmin phases` — the order editor described above.

---

## ChunkBlock-specific notes

!!! warning "The magic block is in the centre chunk, always"
    The centre chunk can never be locked, so the magic block is always reachable. This is guaranteed by the data model rather than by a check: the claim list always starts with the centre chunk and re-locking can never remove it.

!!! note "Mob-spawn block clearing respects the border"
    `mobs-clear-blocks: true` lets spawning mobs break blocks to make room — a cheat prevention carried over from AOneBlock so players cannot box the magic block in and suffocate everything. Locked chunks are never modified, so this only ever affects your own territory.

!!! tip "Phases and territory pull against each other"
    Blocks the magic block produces raise island level, and island level buys chunks — so a generous phase is also a fast-expanding phase. If expansion feels too quick on your server, raising `levels-per-chunk` is usually a better lever than rebalancing phase weights.

!!! note "The Nether and End phases still run"
    The Nether and The End phases are part of the progression regardless of whether the Nether and End *worlds* are generated (both are off by default). They deliver nether and end blocks and mobs through the overworld magic block.

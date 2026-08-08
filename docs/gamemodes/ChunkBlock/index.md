# ChunkBlock

One magic block. One chunk. A wall you cannot walk through.

**ChunkBlock** takes the OneBlock loop everyone knows — mine the magic block, it comes back as something else, phases roll past — and puts a hard border 16 blocks away. Everything outside your starting chunk is a forbidden zone: you cannot walk, fly, glide, pearl, ride or dig your way into it. The only way out is to get *richer*.

Island levels are the currency. Build up your level, walk to the wall, and **hit it in the direction you want to grow**. The chunk on the other side opens up and the border moves out one step. Lose levels and the wall comes back in — newest chunks first — and your farm is behind it until you earn them back.

Created and maintained by [tastybento](https://github.com/tastybento). The magic-block engine comes from [AOneBlock](../AOneBlock/index.md), so phase files are interchangeable; the chunk gating is original to ChunkBlock.

{{ addon_description("ChunkBlock") }}

## Why players get hooked

- 🔒 **A border you genuinely cannot cross.** Walking, sprint-jumping, elytra, riptide tridents, ender pearls (refunded), chorus fruit, horses, boats, minecarts and creative flight are all gated — at *every* height, from the void to above the build limit. There is no fly-over corridor and no dig-under.
- 💰 **Levels are territory.** Not a shop, not a rank, not a timer. The thing your players already optimise — island level — is the thing that buys space. Every block placed is a down payment on the next chunk.
- 👊 **Expansion is a physical gesture.** No GUI, no `/buy chunk`. The owner stands at the wall, punches it, and the world opens up with a sound and a green sweep of particles. They choose the direction, so no two islands grow the same shape.
- ⚠️ **Loss has teeth — without being cruel.** Level drops re-lock the most recently claimed chunks in exact reverse order. Nothing inside is touched: the builds, the chests, the mobs are all still there when the levels come back. Prefer a gentler game? One config line makes territory a ratchet that never shrinks.
- 🗺️ **You can see the frontier.** A per-player particle curtain marks every locked face near you (optionally with client-side barrier blocks), and `/ch chunks` prints a coloured map of what you own, what you can claim next, and what it costs.
- 🧱 **Nothing leaks across.** Pistons, flowing liquids, dispensers, tree growth, fire and grass spread, explosions and natural mob spawns all stop at the line, and dropped items bounce back rather than being lost to the forbidden zone.
- ⛏️ **The full OneBlock game underneath.** 20 themed phases, 15,500 blocks of content, weighted block and mob pools, rarity chests, holograms, boss bar and action bar progress — all of it, in a box that grows.

## How a session feels

You spawn on a grass block in the middle of nowhere with a red wall in every direction. Mine. Mine again. Cobble, dirt, a chicken that immediately walks off the edge. Somewhere around the fiftieth block the chat says you have credit, so you turn to face the sunrise side, punch the wall, and it *falls away* — twice the world you had a second ago, and now you can actually build a wheat farm without knocking your own tower over.

Fifty levels later your island is a 3×3 block of chunks and you are picking directions deliberately: the ocean phase is coming, and you want the room for it on the east side where the drop is. Then you die badly in the Dungeon phase, lose a chunk's worth of levels, and the newest chunk snaps shut with your furnace bank inside it. It is not gone. It is just *behind the wall* until you get those levels back.

## Setup

!!! warning "The Level addon is required"
    Island level is the only chunk currency, so ChunkBlock will not run without [Level](../../addons/Level/index.md). If Level is missing, ChunkBlock disables itself with a clear message in the console rather than half-starting.

0. Install BentoBox and run the server once so its folders exist.
1. Install the **Level** addon into `plugins/BentoBox/addons/`.
2. Drop the **ChunkBlock** jar into `plugins/BentoBox/addons/` and restart.
3. ChunkBlock creates `chunkblock_world`, a data folder, a `config.yml`, a `phases` folder and `phases_index.yml`.
4. Stop the server, edit `config.yml` to taste, and delete any world it created if your changes affect generation.
5. Restart.

ChunkBlock runs happily beside AOneBlock, CaveBlock and the rest — its own world, commands (`/ch`, `/chadmin`), permissions (`chunkblock.*`), flags and database table.

!!! tip "Recommended companions"
    - **Level** — required, and worth tuning: its death penalty and block values are, in ChunkBlock, *territory* settings.
    - **Border** — compatible. It draws the island's overall protection limit; the chunk frontier inside it is ChunkBlock's own curtain.
    - **InvSwitcher** — keeps inventories separate from your other game modes.
    - Challenges, Warps, Likes, Biomes, Greenhouses and friends all work as usual inside unlocked chunks.

## Compatibility

| Feature | Supported |
|---|---|
| Server | ✅ Paper / Spigot, Minecraft 1.21+ |
| BentoBox version | ✅ 3.13.0 or later |
| Java version | ✅ Java 21 |
| Level addon | ⚠️ Required — island level is the chunk currency |
| Nether / End | ⚪ Generated off by default; see below |

## Configuration

`config.yml` is the standard BentoBox game-mode file plus one ChunkBlock-only block. Every option is commented in the file itself; the latest copy lives at [config.yml](https://github.com/BentoBoxWorld/ChunkBlock/blob/develop/src/main/resources/config.yml).

### The chunk settings

```yaml
chunkblock:
  # How many island levels one chunk costs to claim. Minimum 1.
  levels-per-chunk: 1
  # Maximum number of chunks an island can claim, including the center chunk.
  # 441 is a full 21 x 21 chunk square. -1 means "whatever the protection range holds".
  max-chunks: 441
  # Losing levels below what has been spent re-locks chunks, newest first.
  # false = 'ratchet mode': chunks never re-lock once claimed.
  relock-on-level-loss: true
  # Move players out of a chunk that re-locks under their feet.
  eject-players-on-relock: true
  # Cancel natural mob spawning inside locked chunks.
  deny-mob-spawns-in-locked: true
  # Bounce dropped items back at the border instead of losing them.
  bounce-back-items: true
  border:
    # Per-player particle curtain on locked chunk faces.
    show-particles: true
    particle-color:
      ==: Color
      ALPHA: 255
      RED: 255
      GREEN: 0
      BLUE: 0
    # Also send client-side barrier blocks. Purely visual; the world is never modified.
    client-side-barrier-blocks: false
```

!!! abstract "Full guide: [Claiming Chunks](Chunks.md)"
    What each setting does to the feel of the game, worked credit examples, the re-lock rules, and how to tune the pace for a casual or a hardcore server.

### World settings that matter more than usual

=== "distance-between-islands"
    !!! summary "Must be a multiple of 8"
        Island centres have to land in the middle of a chunk (x ≡ 8, z ≡ 8) or the magic block would sit on a chunk seam. ChunkBlock snaps this value to the nearest multiple of 8 on load, so a hand-edited `250` quietly becomes `248`. The default is `256`.

=== "protection-range"
    !!! summary "A second, hard size cap"
        Claimed chunks must fit entirely inside the island's protection range, so the range caps territory no matter what `max-chunks` says. The largest ring radius that fits is `(protection-range − 8) ÷ 16`, rounded down, giving `(2r + 1)²` chunks.

        With the defaults — `protection-range: 240` — that is a radius of 14, or 841 chunks, so `max-chunks: 441` is the setting that actually bites. If you raise `max-chunks`, check the range holds it, and remember the range can never exceed `distance-between-islands`.

=== "offset-x / offset-z"
    !!! summary "Deliberately absent"
        Other game modes expose world offsets. ChunkBlock computes them internally from `start-x`/`start-z` so the magic block is always chunk-centred, and does not offer the settings at all.

=== "nether and end"
    !!! summary "Off by default"
        Both `nether.generate` and `end.generate` default to `false`. Turn either on and that dimension gets its own centre chunk and the same claim rules, driven by the same island level. The magic block only ever exists in the overworld.

### Phases

The magic block, the phase files and `phases_index.yml` behave exactly as they do in AOneBlock — the formats are byte-for-byte compatible, so community phase packs drop straight in.

!!! abstract "Full guide: [The Magic Block and Phases](Phases.md)"
    The shipped 20-phase progression, the phase index, the admin phase editor, and where to find the complete field reference.

### Customizable GUIs

ChunkBlock uses the BentoBox templated-panel API for its phases GUI. On first run it creates a `panels` folder under `plugins/BentoBox/addons/ChunkBlock` containing `phases_panel.yml`. See [Customizable GUIs](../../Tutorials/generic/Customizable-GUI.md) for the mechanics; the `PREVIOUS`, `NEXT` and `PHASE` button types work as described in the [AOneBlock documentation](../AOneBlock/index.md#customizable-guis).

## Commands

!!! tip
    The default player command is `/ch` (alias `/chunkblock`) and the default admin command is `/chadmin` (aliases `/chunkblockadmin`, `/cha`). Both are configurable under `chunkblock.command` in `config.yml`.

=== "ChunkBlock unique player commands"
    - `/ch chunks` — your chunk count, spendable credit and a chat map of your territory.
    - `/ch count` — the current magic-block count and phase.
    - `/ch phases` — the phases GUI.
    - `/ch setcount <number>` — replay a phase you have already reached.
    - `/ch check` — respawn the magic block, or show its particles.
    - `/ch bossbar` / `/ch actionbar` — toggle the phase progress displays.

=== "ChunkBlock unique admin commands"
    - `/chadmin chunks <player> [reset]` — inspect a player's chunks, spending and credit, or re-lock them back to the centre chunk.
    - `/chadmin bypass` — toggle chunk-lock enforcement for yourself.
    - `/chadmin setcount <player> <number> [lifetime]` — set a player's block count.
    - `/chadmin setchest <phase> <rarity>` — save the chest you are looking at into a phase.
    - `/chadmin sanity [<phase>]` — check phase probabilities in the console.
    - `/chadmin phases` — the phase order editor.

[Complete ChunkBlock command list](Commands.md)

## Permissions

!!! tip
    Every ChunkBlock permission is prefixed `chunkblock.`.

!!! warning "`chunkblock.mod.bypasschunks` is not given to ops"
    The chunk-lock bypass defaults to `false` — **not** `op` — so staff play by the same rules as everyone else until you grant it explicitly in your permissions plugin. It is deliberately a separate node from BentoBox's `chunkblock.mod.bypasslock`, which bypasses the island *lock* and is a different feature.

=== "Player permissions"
    - `chunkblock.island.chunks` — use `/ch chunks`. Default `true`.
    - `chunkblock.count` — use `/ch count`. Default `true`.
    - `chunkblock.phases` — use `/ch phases`. Default `false`.
    - `chunkblock.island.setcount` — use `/ch setcount`. Default OP.
    - `chunkblock.respawn-block` — use `/ch check`. Default `true`.
    - `chunkblock.island.bossbar` / `chunkblock.island.actionbar` — toggle the progress displays. Default `true`.

=== "Admin permissions"
    - `chunkblock.admin.chunks` — use `/chadmin chunks`. Default OP.
    - `chunkblock.mod.bypasschunks` — exempt from chunk locking, and use `/chadmin bypass`. **Default `false`.**
    - `chunkblock.admin.setcount`, `chunkblock.admin.setchest`, `chunkblock.admin.sanity`, `chunkblock.admin.phases` — default OP.

[Complete ChunkBlock permission list](Permissions.md)

## Flags

ChunkBlock registers its own flag IDs so it can run alongside AOneBlock without either addon losing its flags to a duplicate registration.

| Flag | Type | Description | Default |
|---|---|---|---|
| `CHUNKBLOCK_START_SAFETY` | World Setting | Players cannot move for a short time after creating an island, so they cannot immediately fall off. Duration is `starting-safety-duration` in config. | false |
| `CHUNKBLOCK_BOSSBAR` | Island Setting | Show the phase progress boss bar. Only available with `bossbar: true` in config. | true |
| `CHUNKBLOCK_ACTIONBAR` | Island Setting | Show the phase progress action bar. Only available with `actionbar: true` in config. | true |
| `MAGIC_BLOCK` | Protection | Minimum island rank required to break the magic block. | COOP |

!!! warning "Upgrading from 1.0.0"
    These flags were called `START_SAFETY`, `ONEBLOCK_BOSSBAR` and `ONEBLOCK_ACTIONBAR` in 1.0.0. If you changed any of them from the default, re-apply the setting once after upgrading — the old values are no longer read.

## Placeholders

Alongside the phase placeholders inherited from the magic-block engine, ChunkBlock adds five territory placeholders:

| Placeholder | Description |
|---|---|
| `%chunkblock_island_chunks%` | Unlocked chunk count, including the centre chunk |
| `%chunkblock_island_max_chunks%` | Maximum chunks this island can claim |
| `%chunkblock_island_chunk_credit%` | Level credit available to spend right now |
| `%chunkblock_island_next_chunk_level%` | Total island level needed to afford the next chunk |
| `%chunkblock_island_ring%` | Ring number of the outermost claimed chunk |

[Complete ChunkBlock placeholder list](Placeholders.md)

## FAQ

??? question "Why can't I walk past the glowing red wall?"
    That chunk is still locked. If you are the island owner and you have level credit, hit the wall and it opens. `/ch chunks` shows your credit and what is claimable.

??? question "Can team members claim chunks?"
    No — claiming is the island owner's call. Everyone on the team benefits from the space, sees the credit announcements and can use `/ch chunks`, but only the owner's punch at the border spends the levels.

??? question "I lost levels and my farm is behind the wall now. Is it gone?"
    No. Nothing inside a re-locked chunk is touched — the blocks, chests and mobs are exactly as you left them. Regain the levels and claim it back; re-locking always takes the newest chunks first, so you get them back in the order you lost them. Admins can disable re-locking entirely with `relock-on-level-loss: false`.

??? question "A chunk re-locked while I was standing in it. What happens to me?"
    You are moved to the nearest unlocked spot inside your own island — flight state preserved, fall damage cancelled, and a landing block created underneath you if the spot was not safe. Nobody is ever stranded or dropped into the void. Players who do not belong to that island are sent to their own island home instead.

??? question "How do I get more chunks faster?"
    Raise your island level: place more, and more valuable, blocks. Lower `levels-per-chunk` if you want expansion to feel generous, or raise it if you want the map to open slowly.

??? question "Can I claim diagonally?"
    Not directly. A new chunk must share a **face** with territory you already own, so a corner chunk needs one of its two neighbours claimed first.

??? question "How big can an island get?"
    Whichever is smaller: `max-chunks` (default 441, a 21×21 square) or the largest square of chunks that fits inside the island's protection range. `/ch chunks` shows the effective maximum.

??? question "Why do I keep falling and dying?"
    A chunk is not much room at the start. Build out before you build up — and remember that deaths can cost levels, and levels are territory.

??? question "What phases are there?"
    The same progression as AOneBlock: Plains, Underground, Winter, Ocean, Jungle, Swamp, Dungeon, Desert, The Nether, Plenty, Desolation, Deep Dark, The End, Lush Caves, Dripstone Caves, Mangrove Swamp, Meadow, Cherry Grove, Jagged Peaks and Sulfur Caves. See [Phases](Phases.md).

??? question "Is there a Nether or an End?"
    Both are turned off by default. Enable them in `config.yml` and each gets its own centre chunk and the same claim rules. The magic block only exists in the overworld.

??? question "Do I need the Border addon?"
    No, and you do not need to remove it either. Border draws the island's outer protection limit; ChunkBlock draws the chunk frontier inside it. They show different things and coexist fine.

??? question "I have a bug, or a feature idea. Where do I put it?"
    On the [issue tracker](https://github.com/BentoBoxWorld/ChunkBlock/issues).

## Translations

{{ translations("ChunkBlock") }}

## API

ChunkBlock stores its data in its own database table, `ChunkBlockIslands`, and exposes its territory state through events, a request handler and the addon class.

Add it to your project as a provided dependency:

```xml
<dependency>
    <groupId>world.bentobox</groupId>
    <artifactId>chunkblock</artifactId>
    <version>1.0.1</version>
    <scope>provided</scope>
</dependency>
```

### Data object

=== "OneBlockIslands"
    !!! summary "Description"
        Per-island state: the magic-block progress inherited from the AOneBlock engine, plus the chunk territory.

        Link to the source: [OneBlockIslands](https://github.com/BentoBoxWorld/ChunkBlock/blob/develop/src/main/java/world/bentobox/chunkblock/dataobjects/OneBlockIslands.java)

    !!! question "Variables"
        - `uniqueId` — the island unique ID, equal to the Island's `uniqueId`.
        - `blockNumber` — the current broken block number.
        - `lifetime` — the total number of blocks ever broken.
        - `phaseName` — the current phase name.
        - `hologram` — the hologram text being shown.
        - `unlockedChunks` — the ordered `"dx,dz"` claim list, relative to the centre chunk. `"0,0"` is always first and can never be removed.
        - `lastKnownLevel` — the island level as of the last calculation, used to detect gains and losses.

    !!! example "Code example"
        ```java
        public void accessChunkBlockData(@NonNull Island island) {
            BentoBox.getInstance().getAddonsManager().<ChunkBlock>getAddonByName("ChunkBlock")
                .ifPresent(chunkBlock -> {
                    OneBlockIslands data = chunkBlock.getOneBlocksIsland(island);
                    int chunks = data.getUnlockedChunkCount();
                    List<String> claimOrder = data.getUnlockedChunks();

                    ChunkManager cm = chunkBlock.getChunkManager();
                    long credit = cm.getCredit(island);
                    long spent = cm.getSpentLevels(island);
                    int max = cm.getMaxChunks(island);
                    boolean here = cm.isUnlocked(island, someLocation);
                });
        }
        ```

### Events

ChunkBlock fires the AOneBlock magic-block events (`BlockClearEvent`, `MagicBlockEntityEvent`, `MagicBlockEvent`, `MagicBlockPhaseEvent` — see the [AOneBlock API section](../AOneBlock/index.md#events), same fields, in the `world.bentobox.chunkblock.events` package) plus two of its own.

=== "ChunkUnlockEvent"
    !!! summary "Description"
        Fired once for each chunk an island claims. **Not cancellable** — the claim has already been decided and paid for; this is a notification.

        Link to the class: [ChunkUnlockEvent](https://github.com/BentoBoxWorld/ChunkBlock/blob/develop/src/main/java/world/bentobox/chunkblock/events/ChunkUnlockEvent.java)

    !!! question "Variables"
        - `@NonNull Island island` — the island that claimed the chunk.
        - `@NonNull Vector chunkOffset` — the chunk offset relative to the island's centre chunk (x and z; y is always 0).
        - `int unlockIndex` — the chunk's position in the island's claim order. The centre chunk is 0.

    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onChunkUnlock(ChunkUnlockEvent event) {
            Island island = event.getIsland();
            Vector offset = event.getChunkOffset();
            int index = event.getUnlockIndex();
        }
        ```

=== "ChunkRelockEvent"
    !!! summary "Description"
        Fired once for each chunk an island loses when its level drops. **Not cancellable.** Events arrive most-recently-claimed first, matching the order the chunks are actually taken back.

        Link to the class: [ChunkRelockEvent](https://github.com/BentoBoxWorld/ChunkBlock/blob/develop/src/main/java/world/bentobox/chunkblock/events/ChunkRelockEvent.java)

    !!! question "Variables"
        - `@NonNull Island island` — the island that lost the chunk.
        - `@NonNull Vector chunkOffset` — the chunk offset relative to the island's centre chunk.
        - `int unlockIndex` — the position the chunk held in the claim order.

    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onChunkRelock(ChunkRelockEvent event) {
            Island island = event.getIsland();
            Vector offset = event.getChunkOffset();
            int index = event.getUnlockIndex();
        }
        ```

### Request handlers

Plugins that do not want a compile-time dependency can use the [Addon Request API](../../BentoBox/Request-Handler-API---How-plugins-can-get-data-from-addons.md). ChunkBlock registers `island-stats` and `location-stats` from the magic-block engine, plus:

=== "unlocked-chunks"
    !!! summary "Description"
        Territory information for a player's island. Submit `"player"` → `UUID`. Returns an empty map if the player has no island in the ChunkBlock world.

    !!! question "Returned map"
        - `count` — `Integer`, unlocked chunks including the centre.
        - `max` — `Integer`, the maximum this island can unlock.
        - `ring` — `Integer`, the ring number of the outermost unlocked chunk.
        - `spent` — `Long`, levels already spent on chunks.
        - `credit` — `Long`, level credit available to spend.
        - `chunks` — `List<String>`, the `"dx,dz"` offsets in claim order.

    !!! example "Code example"
        ```java
        Map<String, Object> request = Map.of("player", player.getUniqueId());
        @SuppressWarnings("unchecked")
        Map<String, Object> result = (Map<String, Object>) new AddonRequestBuilder()
                .addonName("ChunkBlock")
                .label("unlocked-chunks")
                .addMetaData(request)
                .request();
        int chunks = (int) result.getOrDefault("count", 0);
        ```

## Changelog

??? note "What's new in v1.0.0"
    **Released:** 2026-07-28

    The first release. The OneBlock loop, in a chunk that grows when you pay for it.

    - **Claim chunks by hitting the border.** Island levels are spendable credit (`levels-per-chunk` per claim, default 1). The owner aims at the wall and punches or right-clicks to open the next chunk, in any direction.
    - **Territory has consequences.** Every claim is recorded in order; if the island level drops below what has been spent, the most recently claimed chunks re-lock, newest first. Builds inside are untouched. `relock-on-level-loss: false` gives ratchet mode.
    - **A border you truly cannot cross.** Walking, sprint-jumping, elytra, riptide, ender pearls (refunded), chorus fruit, mounts, boats and flight are gated at any height. Pistons, liquids, dispensers, tree growth, spread and explosions cannot reach across, and dropped items bounce back.
    - **A frontier you can see.** A per-player particle curtain marks locked chunk faces, with optional client-side barrier blocks, plus celebration effects when credit is earned and chunks are claimed. The world itself is never modified.
    - **`/ch chunks`** — a coloured chat map of your territory, what you can claim next, and your credit.
    - **Safe by design.** Players caught in a re-locking chunk are moved to the nearest unlocked spot with flight preserved and no fall damage.
    - **Requires the Level addon** — island level is the one and only chunk currency.

    [Release 1.0.0](https://github.com/BentoBoxWorld/ChunkBlock/releases/tag/1.0.0)

!!! warning "What's new in v1.0.1 — flag IDs and default commands changed"
    **Released:** 2026-07-30

    Patch release fixing every bug reported against 1.0.0, plus two compatibility problems that only appear when running ChunkBlock alongside other game modes.

    - 🐛 **Mining near the border no longer spams claim messages.** Claim detection ignored the block you actually clicked and passed through walls, so mining a generator a few blocks from a locked chunk nagged *"You need X more level(s) of credit"* on every swing. Claims now only trigger on a genuine aim at the border, and failure feedback is rate-limited. Fixes [#14](https://github.com/BentoBoxWorld/ChunkBlock/issues/14).
    - 🐛 **Respawns can no longer strand players on a stranger's island.** A respawn landing in a locked chunk of an old or abandoned island used to relocate the player *within that island*, generating a landing block. Players who do not belong to the island are now sent to their own island home. Fixes [#13](https://github.com/BentoBoxWorld/ChunkBlock/issues/13).
    - 🔡 **The phases GUI respects the setcount permission.** *"Click to change"* is no longer offered to players without `chunkblock.island.setcount`, and the GUI title says *ChunkBlock* Phases. Fixes [#11](https://github.com/BentoBoxWorld/ChunkBlock/issues/11).
    - 🔺 ⚙️ **Own flag IDs, no more AOneBlock collision.** The boss bar, action bar and start-safety flags are now `CHUNKBLOCK_BOSSBAR`, `CHUNKBLOCK_ACTIONBAR` and `CHUNKBLOCK_START_SAFETY`. They previously shared AOneBlock's IDs, and BentoBox rejects duplicate flag registrations — so on servers running both, whichever addon loaded second silently lost its flags.
    - 🔺 ⚙️ **Default commands changed from `/cb` to `/ch`.** CaveBlock already uses `/cb` and `/cbadmin`, so the defaults are now `ch chunkblock` (player) and `chadmin chunkblockadmin cha` (admin). Existing servers keep whatever aliases are in their `config.yml`; only fresh installs get the new defaults.
    - **Clean shutdown when Level is missing.** ChunkBlock now disables itself with a clear message instead of leaving half-registered listeners that spammed errors on every join and move.

    🔺 **After upgrading:** if you changed the boss bar, action bar or start-safety world settings from their defaults, re-apply them once — the old `ONEBLOCK_*` / `START_SAFETY` values are no longer read.

    🔡 **Locale note:** keys were renamed (`protection.flags.CHUNKBLOCK_*`, phases GUI titles). Regenerate or update customised locale files.

    **Compatibility:** BentoBox API 3.13.0+, Minecraft 1.21+, Java 21.

    [Release 1.0.1](https://github.com/BentoBoxWorld/ChunkBlock/releases/tag/1.0.1)

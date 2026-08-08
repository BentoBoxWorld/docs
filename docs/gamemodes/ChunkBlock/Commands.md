# ChunkBlock Commands

The default player command is **`/ch`** (alias `/chunkblock`) and the default admin command is **`/chadmin`** (aliases `/chunkblockadmin`, `/cha`). Both, and several of the sub-command labels, are configurable under `chunkblock.command` in `config.yml`:

```yaml
chunkblock:
  command:
    island: ch chunkblock
    admin: chadmin chunkblockadmin cha
    # Sub-command run on a player's very first /ch
    new-player-action: create
    # Sub-command run on every later bare /ch
    default-action: go
    count-command: count
    phases-command: phases
    set-count-command: setCount
    bossbar-command: bossbar
    actionbar-command: actionbar
    respawn-block-command: respawnBlock check
```

Bare `/ch` creates an island the first time and teleports the player home thereafter.

!!! note "Why `/ch` and not `/cb`"
    ChunkBlock's defaults were `/cb` and `/cbadmin` in 1.0.0, which collide with CaveBlock. Since 1.0.1 fresh installs get `/ch` and `/chadmin`. Servers that already have a `config.yml` keep whatever aliases are in it.

## ChunkBlock player commands

These are the sub-commands unique to ChunkBlock. Everything else — `go`, `create`, `reset`, `sethome`, `team`, `ban`, `expel`, `settings`, `language`, `info`, `near` and the rest — is the standard BentoBox game-mode set.

| Command | Description | Permission |
|---------|-------------|------------|
| `/ch chunks` | Your unlocked chunk count, maximum, spendable level credit, and a coloured chat map of your territory showing which chunks you can claim next. | `chunkblock.island.chunks` |
| `/ch count` | The island's current magic-block count and phase. | `chunkblock.count` |
| `/ch phases` | Open the phases GUI — browse the phases and, with permission, replay one already reached. Off by default. | `chunkblock.phases` |
| `/ch setcount <number>` | Jump the block count to a previously completed phase's start value. Subject to `set-count-cooldown` (5 minutes by default). | `chunkblock.island.setcount` |
| `/ch check` (alias `respawnBlock`) | Show the magic block's particles, or respawn it if it has gone missing. | `chunkblock.respawn-block` |
| `/ch bossbar` | Toggle the phase progress boss bar. Requires `bossbar: true` in config. | `chunkblock.island.bossbar` |
| `/ch actionbar` | Toggle the phase progress action bar. Requires `actionbar: true` in config. | `chunkblock.island.actionbar` |

## ChunkBlock admin commands

`/chadmin` carries the full standard BentoBox admin set (`version`, `tp`, `info`, `getrank`, `setrank`, `range`, `resets`, `deaths`, `purge`, `blueprint`, `register`, `delete`, `settings`, `reload`, `why`, `switch`, `team`, and so on) plus the ChunkBlock-specific commands below.

| Command | Description | Permission |
|---------|-------------|------------|
| `/chadmin chunks <player>` | Show a player's unlocked chunk count, their effective maximum, the levels they have spent, and their remaining credit. | `chunkblock.admin.chunks` |
| `/chadmin chunks <player> reset` | Re-lock everything back to the centre chunk and clear the spending record. Builds are untouched — the territory simply has to be re-earned. | `chunkblock.admin.chunks` |
| `/chadmin bypass` | Toggle chunk-lock enforcement for yourself. While bypassing you can move through locked chunks and the border curtain is hidden for you. | `chunkblock.mod.bypasschunks` |
| `/chadmin setcount <player> <number> [lifetime]` | Set a player's magic-block count, or their lifetime count. | `chunkblock.admin.setcount` |
| `/chadmin setchest <phase> <rarity>` | Save the chest you are looking at into a phase's chest file with the given rarity (`COMMON`, `UNCOMMON`, `RARE`, `EPIC`). The chest must be a filled single chest. | `chunkblock.admin.setchest` |
| `/chadmin sanity [<phase>]` | Print a sanity check of the phase probabilities to the console. | `chunkblock.admin.sanity` |
| `/chadmin phases` | Open the phase order editor — reorder, resize, enable and disable phases. | `chunkblock.admin.phases` |

!!! tip "`/chadmin bypass` needs a permission that ops do not have"
    `chunkblock.mod.bypasschunks` defaults to `false`, so even an op has to be granted it explicitly before the command works. That is deliberate: staff play by the same rules until they opt in. Spectator mode is always exempt regardless.

!!! tip "Using the phase order editor"
    `/chadmin phases` lists every phase in order with its computed start block, length and state, and writes `phases_index.yml`.

    - **Left-click** picks a phase up; click where it should go, or the drop-at-end slot, to place it. Click anywhere else or close the panel to put it back unchanged.
    - **Right-click** toggles a phase on or off.
    - **Shift-left-click** sets a phase's length via a chat prompt. The first length edit writes `adminLengths: true` into the index so your lengths are never recomputed again.

    Disabled phases show as grey glass and version-locked ones as barriers; both can still be reordered. See [Phases](Phases.md) for the full picture.

## Reading `/ch chunks`

```
Chunks: 9/441. Credit: 3 level(s) — a chunk costs 1.
Your island territory (9/441 chunks):
□ □ □ □ □
□ ▣ ▣ ▣ □
□ ▣ ■ ■ ▣
□ ▣ ■ ◆ ▣
□ □ ▣ ▣ □
■ yours  ▣ claimable (1 level(s) each)  □ locked
```

| Glyph | Meaning |
|---|---|
| `■` green | A chunk you own |
| `▣` yellow | Claimable right now — adjacent, in range, under the limit |
| `□` grey | Locked, and not claimable yet |
| `◆` blue | The chunk you are standing in |

The map widens as the island grows, up to a 15 × 15 view.

# Claiming Chunks

This is the part of ChunkBlock that is not AOneBlock. The magic block is the engine; **the chunk is the game**.

Every island starts as exactly one chunk — 16 × 16 blocks, from bedrock to sky, with the magic block in the middle of it. Everything else in the island's protection range is locked. The island owner opens it up one chunk at a time by spending island levels at the border.

---

## The currency model

Island level is the currency. There is no separate balance to track, no shop and no cooldown.

```
credit = island level − levels already spent
spent  = (chunks claimed) × levels-per-chunk
```

The centre chunk is free and does not count as spending. With the default `levels-per-chunk: 1`:

| Island level | Chunks owned | Spent | Credit | Can claim? |
|---:|---:|---:|---:|:--|
| 0 | 1 | 0 | 0 | No — nothing to spend |
| 1 | 1 | 0 | 1 | Yes, one chunk |
| 1 | 2 | 1 | 0 | Not until the level rises |
| 7 | 3 | 2 | 5 | Yes, five more chunks |
| 4 | 6 | 5 | −1 | **Over-spent** — one chunk re-locks |

Because credit is derived rather than stored, there is nothing to get out of sync: change `levels-per-chunk` in the config and every island is re-priced on the next level calculation.

!!! tip "Setting the pace"
    `levels-per-chunk` is the single biggest dial on how the game feels.

    - `1` (default) — generous. Early expansion is quick and the map opens as fast as players can build.
    - `5`–`10` — deliberate. Players choose directions carefully and a chunk is an event.
    - `50`+ — a long game. Suits servers where island level already runs into the thousands.

    Remember it interacts with the Level addon's block values: doubling the value of the blocks your players farm halves the real cost of a chunk.

---

## Claiming: hit the border

Expansion is a gesture, not a menu.

1. The **island owner** stands inside their own territory.
2. They face the locked chunk they want.
3. They **left-click or right-click toward the wall**.

If everything checks out, the chunk opens with a sound, a green particle sweep and a chat message telling everyone on the team how big the island is now and how much credit is left.

!!! note "Only the owner can claim"
    Team members share the territory, see the credit announcements and can run `/ch chunks`, but spending the island's levels is the owner's decision.

### What is checked, in order

| Check | Failure | What the player sees |
|---|---|---|
| Already yours? | `ALREADY_UNLOCKED` | Nothing — it is just an ordinary click |
| Inside the protection range and under `max-chunks`? | `BEYOND_LIMIT` | *"That chunk is beyond your island's protection area."* |
| Shares a face with a chunk you own? | `NOT_ADJACENT` | Nothing — diagonal aims are silently ignored |
| Enough credit? | `NO_CREDIT` | *"You need N more level(s) of credit to claim this chunk."* |

Adjacency is by **face, not corner**: a diagonal chunk needs one of its two orthogonal neighbours claimed first. Territory therefore always stays a single connected blob.

### How the aim is read

The listener is careful not to turn ordinary mining into accidental claim attempts:

- Clicking a block that is inside your own territory is never a claim, whatever is behind it. Mining a cobble generator two blocks from the wall does nothing.
- Clicking a block that is itself in a locked chunk targets that chunk directly.
- Clicking air walks a short ray (5 blocks) along your line of sight and takes the first locked chunk it enters — stopping at the first solid block, so you cannot claim through your own walls.
- Looking straight up or straight down never claims.
- Failure messages are rate-limited to one every two seconds per player, so a mining swing cannot spam chat.

!!! tip "Bumping into the wall tells you what to do"
    Walking into a locked chunk gives the owner a contextual hint rather than a flat refusal: *"Hit the border to claim this chunk for N level(s)!"* if they can afford it, or how many levels they still need if they cannot. Everyone else just gets *"That chunk is locked."*

---

## Losing chunks

If the island level drops below what has been spent, the most recently claimed chunks re-lock — **last claimed, first lost** — until the spending fits the new level. This is why the claim order is recorded.

Nothing inside a re-locked chunk is touched. The builds, the chests, the mobs, the farms are all exactly where they were; they are simply unreachable until the levels come back. Because re-locking is strictly reverse-order, regaining the levels gives them back in the order they were lost.

Level loss usually comes from one of three places:

- **Deaths**, if the Level addon's death penalty is enabled — in ChunkBlock that penalty is a *territory* setting, so review it deliberately.
- **Removing blocks** — mining out a big cobble tower can genuinely shrink the island.
- **Admins** recalculating or adjusting a level.

### Players standing in a chunk that closes

With `eject-players-on-relock: true` (the default), anyone caught inside is moved to the nearest unlocked position in their own island:

- The spot is the closest point inside a chunk they own, clamped one block in from the boundary so they do not land on the line.
- If the spot is not safe and the player is not flying, a landing block is created underneath them. This is the **only** time ChunkBlock modifies the world, and it always happens in an *unlocked* chunk.
- Flight state is preserved across the move, and fall damage is cancelled for a few seconds afterwards. An ejection never kills.
- A player who is not a member of that island is sent to their own island home instead, so nobody is ever dropped onto a stranger's island.

With `eject-players-on-relock: false` they can walk out but not back in.

### Ratchet mode

```yaml
chunkblock:
  relock-on-level-loss: false
```

Territory never shrinks. Chunks cost levels to claim, but once claimed they are permanent. Good for family servers, or if you would rather not have to explain the death penalty to everyone.

---

## The border you cannot cross

A locked chunk is locked at **every y**, from below the void to above the build limit. There is no fly-over corridor and no dig-under by construction — the check is 2D on purpose.

=== "Players"
    Movement into a locked chunk is cancelled *and* the player is teleported the short hop back, because cancelling alone does not hold at speed (sprint-jumping, elytra, riptide tridents can tunnel through a cancelled move). Gliders intercepted mid-flight get slow-falling so they are not dropped like a stone.

    Ender pearls and chorus fruit into locked chunks are cancelled — and the pearl is refunded, because the throw was an honest mistake. Any other teleport that ends up in locked territory (plugin homes, respawn anchors, commands) is allowed to fire and then quietly corrected a tick later.

    Joining and respawning are both re-checked one tick late, so "the chunk re-locked while I was offline" resolves itself.

=== "Mounts and vehicles"
    Horses, pigs, striders and boats do not reliably fire gated player-move events, so a mounted player is watched once a second and dismounted and moved back if the mount strays across the line.

    Boats and minecarts — ridden or drifting — are bounced back at the chunk edge. A vehicle carrying an exempt player passes freely.

=== "Blocks and physics"
    Nothing reaches across the border:

    - Pistons cannot push or pull blocks across it.
    - Liquids stop flowing at it.
    - Dispensers and droppers cannot fire through it.
    - Trees do not grow into it, and fire, grass, vines and sculk do not spread into it.
    - Explosions do not damage blocks on the other side.
    - Placing, breaking, bucketing and interacting inside a locked chunk are all refused — including reach-across attempts from an unlocked chunk.

=== "Mobs and items"
    Natural mob spawning inside locked chunks is cancelled when `deny-mob-spawns-in-locked: true` (the default), so the forbidden zone does not quietly fill up with hostiles waiting for the day it opens.

    Dropped items are tracked for 20 seconds and bounced back the moment they cross the line, so a mistimed throw or a death near the wall does not feed your gear to the void. Turn it off with `bounce-back-items: false`.

---

## Seeing the frontier

`border.show-particles: true` draws a dust curtain on every face between your territory and a locked chunk, for any player within 5 blocks of it, redrawn a few times a second so it is visible even standing still. The colour is configurable; the section of curtain above the world height limit is drawn in orange so fliers can see where the wall continues.

`border.client-side-barrier-blocks: true` adds a layer of barrier blocks on those same faces. They are sent per-player with `sendBlockChange` — **the world is never modified**, and the real blocks are restored when the player moves away, teleports, changes world or logs out.

Both are purely cosmetic. Turning them off does not make the border any more crossable; it just makes it invisible.

### `/ch chunks`

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

- **`■` green** — a chunk you own.
- **`▣` yellow** — claimable right now: adjacent, in range, under the limit.
- **`□` grey** — locked, and not claimable yet.
- **`◆` blue** — the chunk you are standing in.

The map grows with your island up to a 15 × 15 view, which is as wide as chat comfortably holds.

---

## Limits

Two caps apply, and the smaller wins.

**`max-chunks`** — a flat ceiling including the centre chunk. The default `441` is a full 21 × 21 square. `-1` means "no limit beyond the protection range".

**The protection range** — claimed chunks must fit entirely inside it. The largest ring radius that fits is `(protection-range − 8) ÷ 16` rounded down, giving `(2r + 1)²` chunks:

| `protection-range` | Ring radius | Chunks |
|---:|---:|---:|
| 120 | 7 | 225 |
| 168 | 10 | 441 |
| 240 (default) | 14 | 841 |
| 400 | 24 | 2401 |

With the shipped defaults (`protection-range: 240`, `max-chunks: 441`) the flat cap is the one that bites, and an island tops out at a 21 × 21 square. When an island reaches its maximum, the last claim is announced with *"Your island has reached its maximum size!"*

!!! warning "Raising the cap"
    `protection-range` can never exceed `distance-between-islands`, and neither can be changed mid-game without resetting worlds and databases. Decide the ceiling before you open the server.

!!! note "Why island centres are chunk-centred"
    Island centres always land at x ≡ 8, z ≡ 8 within a chunk so the magic block sits in the middle of its chunk rather than on a seam. ChunkBlock computes the world offsets for this itself and snaps `distance-between-islands` to a multiple of 8 on load — which is why there are no `offset-x`/`offset-z` settings to get wrong.

---

## Admin tools

=== "/chadmin chunks &lt;player&gt;"
    Shows the player's chunk count and effective maximum, the levels they have spent, and their current credit. The first stop for *"the game says I can't claim and I don't know why"*.

=== "/chadmin chunks &lt;player&gt; reset"
    Re-locks everything back to the centre chunk and clears the spending record. Their builds are untouched — they simply have to earn the territory again. Useful for testing, and for cleaning up after a level-calculation accident.

=== "/chadmin bypass"
    Toggles chunk-lock enforcement for yourself. Requires `chunkblock.mod.bypasschunks`, which is **not** granted to ops by default — you have to give it explicitly. While bypassing, you can move freely through locked chunks and the border curtain is hidden for you, which makes inspecting a reported build much easier.

    Spectator mode is always exempt, permission or not.

---

## For developers

Two events fire on every territory change, both after the fact and neither cancellable:

- **`ChunkUnlockEvent`** — once per chunk claimed.
- **`ChunkRelockEvent`** — once per chunk lost, most recently claimed first.

Both carry the island, the chunk offset relative to the centre chunk, and the index the chunk holds in the claim order.

The **`unlocked-chunks`** request handler gives the same information to plugins with no compile-time dependency on ChunkBlock. See the [API section](index.md#api) for both.

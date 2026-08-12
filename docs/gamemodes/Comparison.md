# Choosing a Game Mode

Not sure which game mode to run on your server? This page compares all the official BentoBox game modes to help you decide.

You can also run **more than one** at the same time — many servers offer two or three game modes so players can choose their preferred experience.

---

## Quick Comparison

| Game Mode | Setting | Difficulty | Main Challenge | Multiplayer Focus |
|---|---|---|---|---|
| **BSkyBlock** | Sky (floating islands) | Medium | Expand from a tiny island in the void | Medium |
| **AOneBlock** | Sky (void) | Medium | Mine a single magical block that never runs out | Low–Medium |
| **ChunkBlock** | Sky (void, one chunk) | Medium | Mine the magic block and spend island levels to punch out the walls | Low–Medium |
| **AcidIsland** | Sea (acid ocean) | Medium–Hard | Skyblock with dangerous acid water | Medium |
| **CaveBlock** | Underground | Medium | Carve out space in a solid stone world | Medium |
| **SkyGrid** | Sky (scattered blocks) | Hard | Collect resources from a grid of single blocks | Low |
| **Boxed** | Normal world | Easy–Medium | Complete advancements to grow your confined space | Medium |
| **Poseidon** | Ocean | Medium | Survive entirely underwater | Medium |
| **StrangerRealms** | Overworld + Upside Down | Medium–Hard | Claim land while managing a dangerous mirror dimension | Medium–High |
| **TradeWinds** | Sea (endless trading ocean) | Easy–Hard (by region) | Sail between NPC trading islands, buying low and selling high | Medium |

---

## Which Should I Choose?

### I want the most popular, well-known experience
**BSkyBlock** — Classic Skyblock is what most players already know. It has the largest community, the most resources, and is a safe choice for any server.

### I want something fresh but still approachable
**AOneBlock** — The concept (one magical block) is easy to explain and immediately engaging. The built-in phase progression keeps players motivated for a long time.

### I want the one-block loop with a reason to keep levelling
**ChunkBlock** — The same magic block as AOneBlock (phase files are interchangeable), but the world is one 16×16 chunk behind a border nothing can cross. Island level is the currency: build your level up, walk to the wall, and punch it in the direction you want to grow. Lose levels and the newest chunks re-lock, builds untouched, until you earn them back — or switch that off in the config if you want territory to be a ratchet. Requires the [Level](../addons/Level/index.md) addon.

### I want Skyblock but harder
**AcidIsland** — Same feel as BSkyBlock but falling in the ocean is genuinely dangerous. Good for players who found regular Skyblock too easy.

### I want an underground / mining theme
**CaveBlock** — Instead of building up in the sky, players dig out from solid ground. The experience feels very different despite sharing most of BentoBox's mechanics.

### I want to cater to advanced / hardcore players
**SkyGrid** — The scattered block world is unforgiving. Resources are spread out, movement is dangerous, and survival requires real skill. Not recommended as the only option on a server with new players.

### I want something tied to vanilla progression
**Boxed** — The advancement-driven expansion mechanic connects the game directly to vanilla Minecraft goals. Good for players who enjoy structured progression.

### I want a unique visual theme
**Poseidon** — An entirely aquatic world looks stunning and plays very differently. Great as a secondary option for players who want something visually distinct.

### I want a story-inspired experience with complex mechanics
**StrangerRealms** — The Upside Down mirror dimension adds a layer of strategy. Better suited to players who are comfortable with Minecraft and ready for something more involved.

### I want an economy-driven trading game
**TradeWinds** — Buy low and sell high across an endless procedurally generated ocean of NPC trading ports. Difficulty is geography: the waters near spawn are patrolled and calm, while contraband, pirates, and PvP bounty space are all further out — so it works for a family server and a cut-throat one at the same time. Requires Vault and an economy plugin.

---

## Feature Support by Game Mode

Most BentoBox addons work with all game modes. A few have specific compatibility requirements.

| Feature | BSkyBlock | AOneBlock | ChunkBlock | AcidIsland | CaveBlock | SkyGrid | Boxed | Poseidon | StrangerRealms | TradeWinds |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Level addon | ✅ | ✅ | ⚠️**** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Challenges | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Warps | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| InvSwitcher | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Border addon | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌* | ✅ |
| Nether world | ✅ | ✅ | ⚠️***** | ✅ | ✅ | ✅ | ✅ | ✅ | ❌** | ❌*** |
| End world | ✅ | ✅ | ⚠️***** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌*** |

\* StrangerRealms has its own built-in border system — do not use the Border addon with it.

\*\* StrangerRealms replaces the Nether with the Upside Down dimension.

\*\*\* TradeWinds replaces the Nether with the Interstice (a hostile nether sea reached by warp misjumps) and deliberately has no End world. TradeWinds also requires Vault plus an economy plugin.

\*\*\*\* ChunkBlock **requires** the Level addon — island level is the currency used to claim chunks, and ChunkBlock disables itself if Level is missing.

\*\*\*\*\* ChunkBlock generates the Nether and the End off by default. Enable either one and it gets its own centre chunk and the same level-driven claim rules; the magic block only ever exists in the overworld.

---

## Running Multiple Game Modes

Each game mode runs completely independently — separate worlds, separate island databases, separate configs. Players can have an island in each game mode at the same time.

If you run multiple game modes, strongly consider installing the **InvSwitcher** addon. Without it, players share the same inventory, experience, and health across all game mode worlds, which can cause confusion and exploits.

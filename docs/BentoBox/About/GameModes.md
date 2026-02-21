# Game Modes

BentoBox is a framework — it provides the core tools (island management, protection, teams) but does not create a world by itself. You add one or more **game modes** to define what kind of experience players have.

A game mode is an addon that sets the rules: what the world looks like, how players start, and what the overall goal is. You can run multiple game modes on the same server at the same time.

!!! tip "Not sure which to pick?"
    See the [Game Mode Comparison](../../gamemodes/Comparison.md) page for a side-by-side overview.

---

## Available Game Modes

### BSkyBlock — Classic Skyblock

Players start on a tiny floating island high in the sky, above nothing but clouds and void. The challenge is to survive and grow using only the limited resources they start with.

**Best for:** Servers that want the classic, well-known Skyblock experience. Great for all ages.

---

### AOneBlock — One Block Skyblock

Players start with a single magical block floating in the void. Every time they mine it, it regenerates as a different block or mob. Phases progress as they mine more, gradually unlocking new materials and challenges.

**Best for:** Servers that want a fresh twist on Skyblock with a built-in progression system.

---

### AcidIsland — Survival in Acid

Similar to Skyblock, but the ocean surrounding the islands is filled with acid that damages players. Swimming is dangerous, so players must build carefully and avoid falling in.

**Best for:** Servers that want Skyblock with an extra survival challenge and a unique twist.

---

### CaveBlock — Underground Survival

Instead of a floating island in the sky, players are given a small cave in a solid underground world. They must dig out and expand their space, making the world itself the challenge.

**Best for:** Servers that want an inverted Skyblock feel — underground exploration and mining focused.

---

### SkyGrid — Scattered Block Survival

The world is generated as a vast grid of single blocks spaced apart — one block of dirt here, one block of wood there. Players must travel across the grid to collect resources, with no solid ground to stand on.

**Best for:** Servers that want an extreme survival challenge requiring exploration and precision movement.

---

### Boxed — Confined Space Survival

Players are confined to a small box that travels with them. The box expands as players complete advancements. The challenge is to survive and progress in an ever-growing but still bounded space.

**Best for:** Servers that want an advancement-driven survival mode with a unique mechanic.

---

### Poseidon — Underwater Survival

Players start on or under the ocean surface and must build and survive in an entirely aquatic world. The challenge is adapting standard Minecraft survival to an underwater environment.

**Best for:** Servers that want a visually distinct, water-themed survival experience.

---

### Stranger Realms — Survival with the Upside Down

Players survive in an Overworld while managing an eerie mirror dimension — the Upside Down — that is a dark, dangerous copy of their world. Interactions between the two dimensions create unique challenges.

**Best for:** Servers that want a story-inspired, more complex survival experience with dimensional mechanics.

---

## Installing a Game Mode

Game modes are downloaded as `.jar` files and placed in:
```
plugins/BentoBox/addons/
```

They are **not** placed in the main `plugins/` folder. After placing the file, restart the server and the game mode will create its own config files for you to configure.

See [How to Install BentoBox](../Install-Bentobox.md) for the full setup walkthrough.

## Running Multiple Game Modes

You can run as many game modes as you want simultaneously. Each game mode gets its own separate worlds and its own player data, so a player's BSkyBlock island and their AcidIsland island are completely independent.

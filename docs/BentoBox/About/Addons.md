# Addons

BentoBox on its own doesn't do anything — it's a platform. **Addons** are what bring it to life. There are two kinds:

- **Game Mode addons** — these create the actual game world players play in (Skyblock, CaveBlock, etc.)
- **Feature addons** — these add optional extras on top of any game mode

You choose exactly which addons to install, so you build exactly the server experience you want.

!!! info "Where do addons go?"
    Addons are **not** placed in your server's `plugins/` folder. They go in:
    ```
    plugins/BentoBox/addons/
    ```
    After placing them there, restart the server and they will generate their config files automatically.

---

## Game Mode Addons

These create the world your players actually play in. Install at least one.

| Addon | What it is |
|---|---|
| **BSkyBlock** | Classic Skyblock — floating island in the sky |
| **AOneBlock** | Start from a single magical regenerating block |
| **AcidIsland** | Skyblock where the ocean is acid |
| **CaveBlock** | Survival in a solid underground world |
| **SkyGrid** | Scattered single blocks across the void |
| **Boxed** | A box that grows as you complete advancements |
| **Poseidon** | Underwater survival |
| **StrangerRealms** | Survival with a dangerous mirrored dimension |

See [Game Modes](GameModes.md) for full descriptions, or [compare them](../../gamemodes/Comparison.md) to help pick one.

---

## Feature Addons

These add optional features that work with any game mode. Mix and match what suits your server.

### Essential for most servers

| Addon | What it adds |
|---|---|
| **Level** | Calculates an island score based on blocks placed. Includes a leaderboard so players can compete. |
| **Challenges** | A list of tasks players can complete for rewards. Great for keeping players engaged. |
| **Warps** | Players can place a warp sign on their island so others can teleport there from a central menu. |
| **InvSwitcher** | Keeps each player's inventory, experience, and health separate between different game modes on the same server. Strongly recommended if you run multiple game modes. |

### Quality of life

| Addon | What it adds |
|---|---|
| **IslandFly** | Lets players fly on their own island. |
| **Visit** | Lets players visit each other's islands through a menu, without needing warp signs. |
| **Border** | Shows players a visible border around their island protection area. |
| **Chat** | Adds island-specific chat channels so team members can talk privately. |
| **Bank** | Gives each island a shared bank account. Players pool money into it together. |
| **CheckMeOut** | Lets players submit their island for admin review or community voting. |

### Advanced / competitive

| Addon | What it adds |
|---|---|
| **Biomes** | Lets players change the biome of their island. |
| **Greenhouses** | Players can build glass greenhouse structures that simulate a specific biome inside. |
| **Limits** | Lets admins set caps on how many of each block or mob a player can have on their island. |
| **MagicCobblestoneGenerator** | Cobblestone generators can be configured to produce different blocks (ores, materials) at set rates. |
| **Upgrades** | Players spend resources to upgrade island properties like size, mob spawning, etc. |
| **TopBlock** | A leaderboard based on the highest single block placed on an island. |
| **TwerkingForTrees** | A fun mechanic where players can cause saplings to grow instantly by dancing (sneaking repeatedly). |

### Utility / Admin

| Addon | What it adds |
|---|---|
| **VoidPortals** | Players can travel to the Nether or End by falling into the void. |
| **DimensionalTrees** | Trees grown in specific dimensions produce special drops. |
| **ExtraMobs** | Adds extra mob-related challenges and interactions. |
| **FarmersDance** | Players can cause crops to grow by dancing near them. |
| **ControlPanel** | Provides a GUI control panel for admins to manage BentoBox. |
| **CauldronWitchery** | Players craft special brews using cauldrons for effects and items. |

---

## Finding and Downloading Addons

Official addons are maintained by the BentoBoxWorld team and can be found at:

**[github.com/BentoBoxWorld](https://github.com/BentoBoxWorld)**

Download the `.jar` file from the **Releases** tab of each addon's repository. Development (untested) builds are available from the [CodeMC CI server](https://ci.codemc.io/job/BentoBoxWorld/).

!!! warning "Version compatibility"
    Each addon lists which versions of BentoBox it supports. Always check this before downloading. Using an addon with the wrong version of BentoBox can prevent your server from starting correctly.

---

## Checking What's Installed

In-game, run:
```
/bentobox version
```
This lists BentoBox's version and every addon that is currently loaded, along with their versions. Include this output whenever you report a bug or ask for support.

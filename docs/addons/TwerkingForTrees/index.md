# TwerkingForTrees

**TwerkingForTrees** lets your players grow trees faster by twerking.

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("TwerkingForTrees") }}

!!! info "Compatibility"
    Requires **BentoBox 3.14.0** or newer, **Minecraft 1.21.3 – 1.21.4**, and **Java 21**.

## Installation

1. Place the addon jar in the addons folder of the BentoBox plugin
2. Restart the server
3. Plant trees on your island
4. Twerk, twerk, twerk...
5. Trees grow!

## Trees

Most trees grow from a single twerked sapling. **Dark Oak** and **Pale Oak** are the exception: like vanilla Minecraft they are 2x2-only mega-trees, so you must arrange four saplings in a 2x2 grid and twerk next to them — a single sapling will not grow.

## Config File

```
# TwerkingForTrees configuration file.
#
# How many times the player must twerk before the tree start growing faster.
# If the player has not twerked enough, then the tree will not grow faster.
minimum-twerks: 4
# Hold to twerk. Accessibility feature. Instead of hitting the crouch button continuously, hold it down.
hold-for-twerk: false
# Use sprinting to grow trees instead of twerking.
sprint-to-grow: false
# Range to look for saplings when twerking. A range of 5 will look +/- 5 blocks in all directions around the player
# Making this too big will lag your server.
range: 5
sounds:
  # Toggle on/off the sounds.
  enabled: true
  twerk:
    # Sound that plays when the player twerked enough for the sapling to start growing faster.
    # Available sounds are the following:
    #    https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Sound.html
    sound: block.note_block.bass
    volume: 1.0
    pitch: 2.0
  growing-small-tree:
    # Sound that plays when a small tree (1x1) grows.
    # Available sounds are the following:
    #    https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Sound.html
    sound: block.bubble_column.upwards_ambient
    volume: 1.0
    pitch: 1.0
  growing-big-tree:
    # Sound that plays when a big tree (2x2) grows.
    # Available sounds are the following:
    #    https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Sound.html
    sound: block.bubble_column.upwards_ambient
    volume: 1.0
    pitch: 1.0
effects:
  # Toggle on/off the particle effects.
  enabled: true
  # Effect that plays each time the player twerks.
  # Available effects are the following:
  #    https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Effect.html
  twerk: MOBSPAWNER_FLAMES

```

## Translations

{{ translations("TwerkingForTrees") }}

??? warning "What's new in v1.6.0 — Breaking changes"
    **Released:** 2026-06-01

    A big modernisation release. See the full [Release v1.6.0](https://github.com/BentoBoxWorld/TwerkingForTrees/releases/tag/1.6.0) notes.

    - 🔺 **Requires BentoBox 3.14.0** (Java 21, Paper 1.21.11, Minecraft 1.21.3 – 1.21.4). The addon will not load on older servers.
    - 🌳 Added **Pale Oak** tree support, including its 2x2 mega-tree variant. Like Dark Oak, Pale Oak is a 2x2-only tree — a single sapling will not grow.
    - ⚙️ **Sound configuration format changed.** Sound identifiers in `config.yml` now use the lowercase dotted form (e.g. `block.note_block.bass`). Refresh your `config.yml` if carrying one over from 1.5.2 so twerk and tree-growth sounds keep working.
    - Added new config options: `hold-for-twerk` (accessibility — hold crouch instead of tapping), `sprint-to-grow` (grow trees by sprinting), and `range` (search radius for saplings).
    - Now ships a `Pladdon` and `plugin.yml` for modern, dependency-aware loading on Paper.
    - Fixed Dark Oak saplings being grown from a single sapling, restored per-block island boundary enforcement so logs and leaves can no longer spill past the island edge, and fixed a tree-growth resource leak.
    - Added a JUnit 5 / MockBukkit test suite.

# DimensionalTrees

**DimensionalTrees** is an addon that makes the trees that grow on the Nether/End change to be a tree of that dimension.

Created by [Awakened-Redstone](https://github.com/Awakened-Redstone) and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("DimensionalTrees") }}

## Configuration

The latest `config.yml` can be found [here](https://github.com/BentoBoxWorld/DimensionalTrees/blob/develop/src/main/resources/config.yml).

Each material slot (`logs` / `leaves`) now accepts a **weighted map** of `material: weight` instead of a single string. Weights summing to exactly 100 apply exact probabilities; weights above 100 are scaled proportionally; weights below 100 leave the remainder as AIR. In both cases a warning is logged on load.

```yaml
nether:
  logs:
    gravel: 80
    netherrack: 20
  leaves:
    glowstone: 70
    soul_sand: 30
```

Resolution order when a tree grows: **per-tree override → per-gamemode override → global default**.

??? note "nether.logs / end.logs"
    Global replacement material(s) for tree logs in the Nether / End. Accepts either a single material name (legacy) or a weighted map.

??? note "nether.leaves / end.leaves"
    Global replacement material(s) for tree leaves in the Nether / End.

??? note "nether.per-tree / end.per-tree"
    Optional per-species overrides. Lets you give `oak`, `acacia`, `birch`, `jungle`, `spruce`, and `dark_oak` their own distinct `logs` / `leaves` maps. Missing or invalid entries silently fall back to the global default.

??? note "nether.per-gamemode / end.per-gamemode"
    Optional per-gamemode overrides for servers running multiple BentoBox gamemodes (e.g. BSkyBlock + CaveBlock). Gamemode is resolved at event time via `IWM.getAddon(world)`.

!!! tip "Automatic migration from 1.8.0"
    Existing single-string values (`logs: gravel`) are automatically converted to the weighted-map form (`logs: {gravel: 100}`) on first startup with 1.9.0. A confirmation is logged; no manual editing required.

## Changelog

??? note "What's new in v1.9.0 — Per-tree, per-gamemode, and weighted materials"
    **Released:** 2026-04-14

    - ⚙️ **Per-tree-type overrides** — configure distinct log/leaf replacements for each of the six tree species in the Nether and End (`per-tree.logs`, `per-tree.leaves`).
    - ⚙️ **Per-gamemode overrides** — servers running multiple BentoBox gamemodes can now configure different replacements per gamemode (`per-gamemode.logs`, `per-gamemode.leaves`).
    - ⚙️ 🔺 **Weighted multi-material mixing** — every material slot accepts a `material: weight` map to blend multiple block types.
    - ⚙️ **Automatic config migration** — 1.8.0 single-string values are silently converted to the new weighted-map format on first startup.
    - Updated to Java 21, Paper 1.21.11, and BentoBox 3.14.0. Pladdon support added for standalone-compatible packaging.
    - JUnit 5 + MockBukkit test suite added.
    - Replaced deprecated `Material.matchMaterial` with the modern Registry API.
    - 🔡 Locale files updated to use MiniMessage color codes for error messages.

    [Release v1.9.0](https://github.com/BentoBoxWorld/DimensionalTrees/releases/tag/1.9.0)

## Translations

{{ translations("DimensionalTrees") }}

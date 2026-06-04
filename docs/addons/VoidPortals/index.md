# VoidPortals

**VoidPortals** lets players travel between dimensions by falling into the void. When a player falls into the void in a world where the flag is enabled, they are safely teleported to the matching location in the next dimension — **Overworld → Nether → The End → Overworld** — instead of dying.

Created and maintained by [BONNe](https://github.com/BONNe).

{{ addon_description("VoidPortals", beta=True) }}

!!! info "Compatibility"
    Requires **BentoBox 3.14.0** or newer, **Minecraft 1.21+**, and **Java 21**.

## Installation

1. Place the addon jar in the addons folder of the BentoBox plugin.
2. Restart the server.
3. The "Void world teleports" flag is **disabled by default** — enable it per world in the Game Mode's Admin Settings panel.

## Flags

VoidPortals adds a single world setting flag. Toggle it per world from the Game Mode's Admin Settings panel.

{{ flags_source("VoidPortals", "WORLD_SETTING") }}

## Translations

{{ translations("VoidPortals") }}

??? note "What's new in v1.6.1"
    **Released:** 2026-06-01

    A bug-fix release. See the full [Release v1.6.1](https://github.com/BentoBoxWorld/VoidPortals/releases/tag/1.6.1) notes.

    - Void-fall no longer kills you on arrival. Falling into the void built up downward velocity that carried through the teleport, slamming you into the ground the moment you arrived in the next dimension. Your velocity and fall distance are now reset on arrival, so you land safely.

??? warning "What's new in v1.6.0 — Breaking changes"
    **Released:** 2026-06-01

    First release since 2019 — VoidPortals is fully modernised for the current BentoBox ecosystem. See the full [Release v1.6.0](https://github.com/BentoBoxWorld/VoidPortals/releases/tag/1.6.0) notes.

    - 🔺 **Requires Java 21, Paper 1.21.11 and BentoBox 3.14.0** (was Spigot 1.13.2 / BentoBox 1.5.0). This release will not load on older servers.
    - Now ships a `Pladdon` and `plugin.yml` so the jar loads correctly on modern Paper servers.
    - 🔡 Added 14 new languages and converted every locale to **MiniMessage** formatting. If you customised the locale files, regenerate them or port your edits — legacy `&` colour codes are no longer used.
    - Added a JUnit 5 / MockBukkit test suite, including a regression test ensuring diagonal void-falls still teleport.

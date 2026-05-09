# BSkyBlock

The classic. A tiny island, a tree, a chest, and the void stretching out in every direction. That's all your players get — and somehow, it's never enough. They'll spend hours expanding that island, hunting for resources, completing challenges, and climbing the level leaderboards. Then they'll come back tomorrow and do it again.

**BSkyBlock** is the SkyBlock game mode for BentoBox, and the successor to the legendary **ASkyBlock** that popularised the genre. If you want to run SkyBlock, this is where you start.

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("BSkyBlock") }}

## History
**BSkyBlock** is the evolution of **ASkyBlock** for newer Minecraft server versions.

## Installation

0. Install BentoBox and run it on the server at least once to create its data folders.
1. Place this jar in the addons folder of the BentoBox plugin.
2. Restart the server.
3. The addon will create worlds and a data folder and inside the folder will be a config.yml.
4. Stop the server .
5. Edit the config.yml how you want.
6. Delete any worlds that were created by default if you made changes that would affect them.
7. Restart the server.

## Config.yml

The config.yml is similar to ASkyBlock but *not the same*. Note that distance between islands and protection range are **radius values** so the island size will be twice these values in blocks! Also, the distance between islands will be set automatically to a chunk boundary (a multiple of 16 blocks).

## Permissions

Permissions can be found [here](Permissions).

## Commands

Commands can be found [here](Commands).

## Placeholders

Placeholders can be found [here](Placeholders).

## Changelog

??? warning "What's new in v1.20.0 — requires BentoBox 3.13.0 and Paper 1.21.11"
    **Released:** 2026-04-27

    - 🐛 **Mob spawning fixed.** The chunk generator was not overriding `shouldGenerateMobs()`, which silently suppressed vanilla mob spawning in all BSkyBlock-generated worlds. Mobs now spawn correctly again.
    - 🐛 **Water animals (fish, squid) spawning fixed.** Restores natural fish and squid spawning, broken since the 1.21 platform migration. Fixes [BentoBox #2593](https://github.com/BentoBoxWorld/BentoBox/issues/2593).
    - ⚡ **Modern chunk generation.** The world generator has been migrated from the deprecated `generateChunkData()` + `BiomeGrid` approach to Paper's current `generateNoise()` + `BiomeProvider` API.
    - 🔡 All 17 locale sign files migrated from legacy `&c` color codes to MiniMessage format.
    - Build modernised: JDK 21, JUnit 5 + MockBukkit test stack.

    🔺 **Requires BentoBox 3.13.0 or newer and Paper 1.21.11.** Earlier versions of BentoBox will not load this addon.

    🔡 **Locale note:** Sign text now uses MiniMessage tags (e.g. `<red>…</red>` instead of `&c`). Customised locale files need updating.

    [Release v1.20.0](https://github.com/BentoBoxWorld/BSkyBlock/releases/tag/1.20.0)

## Translations

{{ translations("BSkyBlock") }}

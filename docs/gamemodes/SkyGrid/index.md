# SkyGrid

Every fourth block in every direction is a real block. Everything else is air.

That means gravel floating over the void. Lava pools suspended in nothing. A creeper on a sand block twelve metres above you. Getting anywhere requires planning, precision, and a healthy respect for what happens if you miss a jump.

**SkyGrid** was created by SethBling back in 2012 and became one of the most beloved Minecraft challenge maps ever made. This is the BentoBox version — same chaotic grid, now running as a full multiplayer island experience with all the progression, challenges, and leaderboards players expect.

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("SkyGrid") }}

## Installation

0. Install BentoBox and run it on the server at least once to create its data folders.
1. Place this jar in the addons folder of the BentoBox plugin.
2. Restart the server.
3. The addon will create worlds and a data folder and inside the folder will be a config.yml.
4. Stop the server .
5. Edit the config.yml how you want.
6. Delete any worlds that were created by default if you made changes that would affect them.
7. Restart the server.

## Permissions

Permissions can be found [here](Permissions).

## Commands

Commands can be found [here](Commands).

## Placeholders

Placeholders can be found [here](Placeholders).

## Changelog

??? warning "What's new in v2.2.4 — world generation fix"
    **Released:** 2026-11-05

    Compatibility: BentoBox API 3.3.1 · Minecraft 1.21.x (tested on Paper 26.3) · Java 21.

    - 🔺 **Grid no longer full of stone and grass.** Vanilla terrain was generated underneath the grid and vanilla surface generation replaced blocks with grass. Grid spots now only get blocks from your config. [PR #88](https://github.com/BentoBoxWorld/SkyGrid/pull/88)
    - 🔺 **Chunks no longer repeat.** Every chunk started from the same random sequence, so the same pattern repeated every 16 blocks. Each chunk now gets its own. [PR #88](https://github.com/BentoBoxWorld/SkyGrid/pull/88)
    - **Sugar cane now has water.** It sits in a small sandstone basin so the water stays put. Basin water can freeze in cold biomes. [PR #89](https://github.com/BentoBoxWorld/SkyGrid/pull/89)
    - **Cactus and dead bushes no longer float.** They now stand on sand on top of sandstone. [PR #89](https://github.com/BentoBoxWorld/SkyGrid/pull/89)

    🔺 **Existing worlds:** already-generated chunks don't change, so there will be a visible mismatch where old and new chunks meet. For a consistent grid, delete your SkyGrid worlds and let them regenerate — **this removes every island in those worlds**, so plan it with your players and back up first.

    [Release v2.2.4](https://github.com/BentoBoxWorld/SkyGrid/releases/tag/2.2.4)

## Translations

{{ translations("SkyGrid") }}

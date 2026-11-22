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

## Configuration

SkyGrid's `config.yml` lists the blocks that make up the grid in each world, with a weight for each. The latest file is [here](https://github.com/BentoBoxWorld/SkyGrid/blob/master/src/main/resources/config.yml).

### Spawner mobs

Since SkyGrid 2.3.0 you choose which mobs come out of the grid's spawners. Each world has its own list, in the format `EntityType: weight`:

| World | List |
|---|---|
| Over world | `world.spawners` |
| Nether | `world.nether.spawners` |
| End | `world.end.spawners` |

```yaml
world:
  end:
    spawners:
      ENDERMAN: 45
      ENDERMITE: 54
      SHULKER: 1
```

- A mob is picked in proportion to its weight. In the example, 1 end spawner in 100 is a shulker spawner.
- To stop spawners of one type being made, remove the mob or set its weight to `0`. For example, remove `VILLAGER` and `IRON_GOLEM` from `world.spawners`.
- To have no spawners at all, remove `SPAWNER` from that world's blocks list.
- If a list is empty, SkyGrid uses its built-in list and writes it to the file.
- Mobs that can't be in a spawner, such as `ARROW`, are skipped with a warning in the console.

Changes only affect chunks generated afterwards.

### Grid height and alignment

Grid blocks are placed every 4 blocks. Since 2.3.0, `world.skygrid-height` is rounded to the nearest multiple of 4 (maximum 252), so the centre of each player's area is on a grid layer.

`world.start-x`, `world.start-z` and `world.space-around-players` should also be multiples of 4. SkyGrid logs a warning if they aren't, but doesn't change them, because that would move every area in an existing world.

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

!!! warning "What's new in v2.3.0 — spawner mobs, and players get team and home commands"
    **Released:** 2026-11-22

    Compatibility: BentoBox API 3.3.1 · Minecraft 1.21.x and 26.x · Java 21.

    - ⚙️ **Configurable spawner mobs.** New lists `world.spawners`, `world.nether.spawners` and `world.end.spawners` set which mobs spawners can hold and how common each is. They are added to existing configs with the same odds as before. See [Spawner mobs](#spawner-mobs). [PR #94](https://github.com/BentoBoxWorld/SkyGrid/pull/94)
    - ⚙️ **Grid height lines up with the grid.** `skygrid-height` is rounded to the nearest multiple of 4 (maximum 252). The grid doesn't change, but players' spawn points can move by up to 2 blocks. SkyGrid warns if `start-x`, `start-z` or `space-around-players` aren't multiples of 4. See [Grid height and alignment](#grid-height-and-alignment). [PR #94](https://github.com/BentoBoxWorld/SkyGrid/pull/94)
    - 🔺 **Players can use team and home commands.** 12 player permissions were not declared, so only operators had them: team `invite`, `accept`, `reject`, `kick`, `leave`, `promote` and `setowner`, `info`, `near`, and `homes`, `renamehome` and `deletehome`. They now default to everyone. See [Permissions](Permissions.md). [PR #92](https://github.com/BentoBoxWorld/SkyGrid/pull/92)
    - ⚙️ **New default settings for new installs.** Eight hazard settings are hidden from players (`TNT_DAMAGE`, `BLOCK_EXPLODE_DAMAGE`, `FIRE_BURNING`, `FIRE_IGNITE`, `FIRE_SPREAD`, `LEAF_DECAY`, `ENDERMAN_TELEPORT`, `SHULKER_TELEPORT`), and `PISTON_PUSH` is listed and off. Existing servers keep their `config.yml`; copy the entries into `world.hidden-flags` and `world.flags` if you want them. [PR #93](https://github.com/BentoBoxWorld/SkyGrid/pull/93)

    🔺 **If you kept team or home commands for operators or certain ranks on purpose,** negate the permissions you want to keep restricted in your permissions plugin, for example `skygrid.island.team.invite`.

    [Release v2.3.0](https://github.com/BentoBoxWorld/SkyGrid/releases/tag/2.3.0)

## Translations

{{ translations("SkyGrid") }}

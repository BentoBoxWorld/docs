# Boxed

You start inside a box. A small box. Everything outside it — mobs, blocks, resources — is off limits. To get more space, you have to earn it: complete advancements and your box grows. Every advancement matters. Every new block of territory is a reward you worked for.

**Boxed** is an island game mode with a twist: your world doesn't expand from mining or building, it expands from *doing things*. Craft something new. Explore a structure. Kill a mob. Grow a crop. The whole vanilla advancement tree drives your progression, and the optional custom datapack adds even more to chase.

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("Boxed") }}

## BentoBox Requirements

* Always used the latest BentoBox version (Snapshots can be downloaded here: [https://ci.bentobox.world](https://ci.bentobox.world))
* InvSwitcher - keeps advancements, inventory, etc. separate between worlds on a server.
* Border - shows the box

## How to install

### Quick Start

1. Place Boxed addon into the BentoBox addons folder along with InvSwitcher and Border (use the latest versions!).
2. Restart the server - new worlds will be created. *This will take a long time first time through*
3. Login
4. Type `/boxed` to start.
5. (Optional) Turn off advancement announcements `/gamerule announceAdvancements false` otherwise there is a lot of spam from the server when players get advancements.

* You will start by a tree. The is a chest with some handy items in it. (This is the island blueprint)
* The only area you can operate on is your box that shows as a border.
* To make your box bigger, complete advancements.
* Check your progress with the Advancements screen, (L-key).
* Monsters do not spawn by default outside your box, but your box becomes bigger, and it only takes one block to spawn a mob!
* The box owner can move the box using enderpearls thrown from within the box. Beware! It's a one-way trip. (Optional setting in config.yml)
* The box settings have an option to allow box moving by other ranks (look for the Composter box icon)

## Custom Advancements

The official **BoxedDataPack** adds a set of custom advancements designed specifically for Boxed, giving players more to chase and your server a more complete experience out of the box.

[Download the latest BoxedDataPack release](https://github.com/BentoBoxWorld/BoxedDataPack/releases) and drop the `.zip` into your server's `world/datapacks/` folder (or whichever world Boxed is running in), then run `/reload` or restart.

Prefer to build your own? See the [tutorial video](https://youtu.be/zNzQvIbweQs) for how to create custom advancements that integrate with Boxed's expansion system.

## Keeping world size down

!!! warning "Regionerator is no longer needed"
    Older versions of this guide recommended the third-party [Regionerator](https://github.com/Jikoo/Regionerator) plugin to prune unused chunks. **As of BentoBox 3.15.0 this is built in** — BentoBox now deletes region (`.mca`) files directly, so Regionerator is no longer required and is no longer recommended for Boxed. If you are still running it, you can remove it: it is redundant and, unless its seed-world exemptions are set up correctly, it can delete Boxed's seed worlds and make server startup very slow.

Boxed worlds grow as players expand their boxes and reset, and that disk usage is now reclaimed by BentoBox itself in two ways.

**Automatic housekeeping (on by default).** When a box is reset it is *soft-deleted* — flagged for deletion rather than wiped block-by-block — and a scheduled sweep reaps its region files in the background. The deleted-sweep runs every 24 hours out of the box. The relevant section of BentoBox's `config.yml` is:

```yaml
island:
  deletion:
    housekeeping:
      # Reaps region files for boxes already flagged deleted (e.g. from a reset).
      # On by default.
      deleted-sweep:
        enabled: true
        interval-hours: 24
      # Reaps region files that simply haven't been touched for a long time,
      # regardless of whether the box was reset. Off by default — turn this on
      # for the most aggressive size control.
      age-sweep:
        enabled: false
        interval-days: 30
        min-age-days: 60
```

**Manual purging.** You can also reclaim space on demand from the server console or in-game (see [Commands](Commands)):

* `/boxadmin purge deleted` — immediately reap region files for every box already flagged as deleted.
* `/boxadmin purge <days>` — reap region files for boxes whose owners haven't logged in for `<days>` days and whose region files are at least that old.
* `/boxadmin purge unowned` — flag every unowned box as deletable so the next sweep removes it.

!!! note "Restart after a big purge"
    Region files are deleted from disk immediately, but Paper keeps recently-loaded chunks in an in-memory cache. **Restart the server after a large purge** so that cache is cleared and the freed space is fully released. Purge-protected boxes, spawn islands, and (if the Level addon is installed) boxes above the configured purge level are always skipped. As always, **back up your world folder before purging.**

The old `keep-previous-island-on-reset` setting no longer exists — boxes are always soft-deleted on reset and cleaned up by housekeeping, so there is nothing to configure for Regionerator to "take over".


## Advanced Config

### config.yml
The config is very similar to BSkyBlock, AcidIsland, etc.

Each player will have a land of their own to explore up to the limit of the island distance value. The default is 400, so the land will be 800 x 800 blocks. The land is semi-random, but each player will get roughly the same layout (see the biomes config). Structures such as villages, broken nether gates, shipwrecks, etc. are random and so some players may get them, others not. In a future version, switching off structures will be a config option. Strongholds are switched off and do not exist. Each player's land is surrounded by seas of different temperatures. If the border is not solid, then players can theoretically explore other lands.

*World Seed*
The world seed is what it is used to generate the lands. I recommend keeping this value. If you change it the land may be very different.

### Blueprint

There is one blueprint "island" that is used to generate the tree, chest and blocks below down to y = 5. The default height of the surface is about y = 65, so the blueprint has to be about 60 blocks tall. If you make any good blueprints, please share them!

### advancements.yml
This file contains all the advancements and how much your box should grow if you get one. The file can contain custom advancements if you have them.

There are two settings at the top - the first `default-root-increase` you probably don't need to change. This sets the score of any root advancement to 0. In other words, players will not get box expansion just for seeing the new advancement tab.

The second setting `unknown-advancement-increase` gives any unknown advancements, i.e., ones not listed in this file, a default value. This is the default value used should you add custom advancements via a data pack and it frees you up from having to list every new advancement in this file.

Example:

```
# Lists how many blocks the box will increase when advancement occurs
settings:
  default-root-increase: 0
  unknown-advancement-increase: 1
advancements:
  'minecraft:adventure/adventuring_time': 1
  'minecraft:adventure/arbalistic': 1
  'minecraft:adventure/bullseye': 1
...
```
  
### biomes.yml
The player's land has biomes and they are defined here. It's not possible to define where the biomes are right now, only what affect they have on the terrain.

* height: the default height is 8. Lower numbers will produce lower land, higher higher land.
* scale: this is how smooth the land will be. Smaller numbers are more jagged, larger numbers are flatter.

Setting ocean biomes to higher height numbers will result in the ocean floor being above the sea level and creating land.

A lot of these numbers are rough guesses right now and if you come up with better values, please share them!


## Permissions

Permissions can be found [here](Permissions).

## Commands

Commands can be found [here](Commands).

## Placeholders

Placeholders can be found [here](Placeholders).

## Changelog

??? note "What's new in v3.4.0"
    **Released:** 2026-05-30

    - **Trial Chambers support.** Boxed now captures and restores Trial Spawner state — including both the normal *and* ominous configurations — when structures are pulled from the seed world into a player's box, and recognises `trial_chambers` as a tracked structure for advancement-driven box growth.
    - 🐛 **No more cross-game-mode progress loss.** Boxed no longer clears a player's advancements and statistics when an island is reset in a *different*, non-Boxed game mode.
    - 🐛 Pending structure pastes are now cancelled when an island is deleted, preventing structures being placed into a box that no longer exists.
    - 🐛 Ominous trial spawners now restore the correct configuration rather than always applying the normal one.
    - Modernised build & test stack: Paper 1.21.11, BentoBox API 3.13.0, JUnit 5 + Mockito + MockBukkit.

    !!! note
        Trial Chambers are captured from the seed world when a box is generated, so boxes created *before* 3.4.0 will not retroactively gain them. New boxes (and newly expanded regions) will include them.

    [Release v3.4.0](https://github.com/BentoBoxWorld/Boxed/releases/tag/3.4.0)

## Translations

{{ translations("Boxed") }}

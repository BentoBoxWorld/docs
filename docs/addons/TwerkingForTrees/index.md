# TwerkingForTrees Addon
[![Discord](https://img.shields.io/discord/272499714048524288.svg?logo=discord)](https://discord.bentobox.world)
[![Build Status](https://ci.codemc.org/buildStatus/icon?job=BentoBoxWorld/TwerkingForTrees)](https://ci.codemc.org/job/BentoBoxWorld/job/TwerkingForTrees/)

This is Addon that enables players to grow trees faster by twerking. If you like this or want more features, please [sponsor](https://github.com/sponsors/tastybento)!

## How to use

1. Place the addon jar in the addons folder of the BentoBox plugin
2. Restart the server
3. Plant trees on your island
4. Twerk, twerk, twerk...
5. Trees grow!

## Compatibility

- [x] BentoBox - 1.7.0 version
- [x] BSkyBlock - 1.7.0 version
- [x] AcidIsland - 1.7.0 version
- [x] SkyGrid - 1.7.0 version
- [x] CaveBlock - 1.7.0 version

## Config File

```
# TwerkingForTrees configuration file.
#
# How many times the player must twerk before the tree start growing faster.
# If the player has not twerked enough, then the tree will not grow faster.
minimum-twerks: 4
sounds:
  # Toggle on/off the sounds.
  enabled: true
  twerk:
    # Sound that plays when the player twerked enough for the sapling to start growing faster.
    # Available sounds are the following:
    #    https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Sound.html
    sound: BLOCK_NOTE_BLOCK_BASS
    volume: 1.0
    pitch: 2.0
  growing-small-tree:
    # Sound that plays when a small tree (1x1) grows.
    # Available sounds are the following:
    #    https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Sound.html
    sound: BLOCK_BUBBLE_COLUMN_UPWARDS_AMBIENT
    volume: 1.0
    pitch: 1.0
  growing-big-tree:
    # Sound that plays when a big tree (2x2) grows.
    # Available sounds are the following:
    #    https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Sound.html
    sound: BLOCK_BUBBLE_COLUMN_UPWARDS_AMBIENT
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

## Bugs or Feature Requests

Report bugs or request features on the [TwerkingForTrees issue tracker](https://github.com/BentoBoxWorld/TwerkingForTrees/issues).
# TwerkingForTrees

**TwerkingForTrees** lets your players grow trees faster by twerking.

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("TwerkingForTrees") }}

## Installation

1. Place the addon jar in the addons folder of the BentoBox plugin
2. Restart the server
3. Plant trees on your island
4. Twerk, twerk, twerk...
5. Trees grow!

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

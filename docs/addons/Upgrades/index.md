# Upgrades

**Upgrades** allows you to upgrade your island size, Entities/Blocks limits at the cost of money and island level.

This addon was created to add a progression curve and a use of money for the island.

Created and maintained by [Ikkino](https://github.com/Guillaume-Lebegue)

{{ addon_description("Upgrades", true) }}

## Installation

1. Place the Upgrades addon jar in the addons folder of the BentoBox plugin
2. Restart the server
3. The addon will create a data folder and inside the folder will be a config.yml
4. Edit the config.yml how you want.
5. Restart the server if you make a change

## Commands

!!! tip
    `[player_command]` is a command that differs depending on the gamemode you are running.
    The Gamemodes' `config.yml` file contains options that allows you to modify this value.
    As an example, on BSkyBlock, the default `[player_command]` is `island`.

There is a user command to open a GUI with the upgrades.

`/[Player command] upgrade`

## Setup - Config.yml

The config.yml has the following sections:

* range-upgrade
* block-limits-upgrade
* entity-limits-upgrade
* command-upgrade
* gamemodes
* entity-icon
* command-icon

!!! tip
    All `upgrade`, `island-min-level` and `vault-cost` fields are mathematical expression. So:

    * +,-,*,/,^,(,) can be used
    * sqrt(), sin(), cos(), tan() can be used
    * `[level]` is replaced by the actual level for this upgrade
    * `[islandLevel]` is replaced by the island level from level addon **(Can be 0)**
    * `[numberPlayer]` is replaced by the number of players in the team


### General

One upgrade is divided by "tier" that can be named at will

Exemple:
```yml
tier1:
  max-level: 5
  upgrade: "5"
  island-min-level: "2"
  vault-cost: "[level]*100"
  permission-level: 1
```

* `max-level` is the maximum level of this tier.
* `upgrade` is how much is given at each level.
* `island-min-level` is the minimum island level needed to buy this upgrade. It is given by [Level Addon](/addons/Level)
* `vault-cost` is the cost to buy this upgrade **(>= 0)**
* `permission-level` is the level of permission needed to buy this upgrade (cf. Permission)


### Range Upgrade

This upgrade increases the protection size of the island.

The size increase is given in the `upgrade` field

Exemple:
```yaml
range-upgrade:
  tier1:
    max-level: 5
    upgrade: "5"
    island-min-level: "2"
    vault-cost: "[level]*100"
  tier2:
    max-level: 10
    upgrade: "3"
    island-min-level: "4"
    vault-cost: "[level]*[numberPlayer]*200"
```

!!! warning "Max Range"
    You should always check that, even at the maximum upgrade, the protection size never exceeds the size between island.

### Block Limits Upgrade

This upgrade increase the limits of blocks set in the [Limits Addon](/addons/Limits)

The number to add to the limits is given by the `upgrade` field.

Exemple:
```yaml
block-limits-upgrade:
  HOPPER:
    tier1:
      max-level: 2
      upgrade: "1"
      island-min-level: "2"
      vault-cost: "[level]*100"
    tier2:
      max-level: 5
      upgrade: "1"
      island-min-level: "4"
      vault-cost: "([level]-2)*[numberPlayer]*700"
      permission-level: 1
```

!!! tip "Blocks"
    A list of blocks can be found [here](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)


### Entity Limits Upgrade

This upgrade increase the limits of entities set in the [Limits Addon](/addons/Limits)

All entities need to have a corresponding icon (CF: [entity-icon](#entity-icon))

The number to add to the limits is given by the `upgrade` field.

Exemple:
```yaml
entity-limits-upgrade:
  CHICKEN:
    tier1:
      max-level: 2
      upgrade: "1"
      island-min-level: "2"
      vault-cost: "[level]*100"
    tier2:
      max-level: 5
      upgrade: "1"
      island-min-level: "4"
      vault-cost: "([level]-2)*[numberPlayer]*700"
      permission-level: 3
```

!!! tip "Entities"
    A list of entities can be found [here](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/entity/EntityType.html)

### Command Upgrade

This upgrade runs given command on each upgrade

All command upgrade needs to have a corresponding icon (CF: [command-icon](#command-icon))

In the config:

* The name of the section is the real name of the upgrade
* The `name` field is only the display name. Not used in permission.
* The `console` field specify if the command should be launched by the console or by the player
* The `command` field is a list containing all the commands to run. They are launched in the list order

!!! tip "Command Field"
    In the command field:

    * `[player]` is replaced by the name of the player who bought the upgrade
    * `[level]` is replaced with the level of the upgrade

Exemple:
```yaml
command-upgrade:
  lambda-upgrade:
    name: "Lambda upgrade"
    tier1:
      max-level: 1
      island-min-level: "2"
      vault-cost: "[level]*100"
      console: true
      command:
        - "say [player] has upgrade his lambda to level [level]"
    tier2:
      max-level: 2
      island-min-level: "2"
      vault-cost: "[level]*200"
      console: true
      command: 
        - "say [player] has upgrade his lambda to level [level]"
        - "say [player] has reached the max level"
```

### Gamemode


It is possible to set differences in upgrade between each gamemode.

Exemple:
```yaml
gamemodes:
  BSkyBlock:

    range-upgrade:
      tier3:
        max-level: 15
        upgrade: "5"
        island-min-level: "6"
        vault-cost: "[level]*[numberPlayer]*500"

    block-limits-upgrade:
      HOPPER:
        tier1:
          max-level: 2
          upgrade: "1"
          island-min-level: "2"
          vault-cost: "[level]*200"
```

### Entity Icon

This section is made to link entities to icons.

Here the syntax:

`ENTITY: MATERIAL`

Exemple:
```yaml
entity-icon:
  CHICKEN: CHICKEN_SPAWN_EGG
```

!!! tip "Entities"
    A list of entities can be found [here](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/entity/EntityType.html)

!!! tip "Material"
    A list of materials can be found [here](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)

### Command Icon

This section is made to link command upgrade to icon.

Here the syntax:

`NAME: MATERIAL`

`NAME` being the real name of the command upgrade (!= display name)

Exemple:
```yaml
command-icon:
  lambda-upgrade: GRASS
```

!!! tip "Material"
    A list of materials can be found [here](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)

## Permissions

There can be permission for buying an upgrade.

To do so, a `permission-level` superior to 0 should be added to the upgrade. To buy the upgrade, the player need to have a level superior or equal to this level. By default, a player has a level of 0 everywhere.

Here is the permission:

`[GAMEMODE].upgrades.[UPGRADE].[LEVEL]`

Where:

* `[GAMEMODE]` is the name of the gamemode where this permission should be set
* `[UPGRADE]` is the name of the upgrade (CF: [Name Upgrades](#name-upgrades))
* `[LEVEL]` is the level to give to the player

Exemple:

`bskyblock.upgrades.range-upgrade.2`

!!! warning
    Permission is in lowercase

!!! tip
    Because permission is created at runtime, it won't appear in a list of permissions

### Name Upgrades

**Range Upgrade**:

`rangeupgrade` | Exemple: `bskyblock.upgrades.range-upgrade.1`

**Block Limits Upgrade**:

`limitsupgrade-[BLOCK]` | Exemple: `bskyblock.upgrades.limitsupgrade-hopper.8`

**Entity Limits Upgrade**:

`limitsupgrade-[ENTITY]` | Exemple: `bskyblock.upgrades.limitsupgrade-chicken-hopper.4`

**Command Upgrade**:

`command-[NAME]` | Exemple: `bskyblock.upgrades.command-lambda-upgrade.6`

`NAME` being the real name of the command upgrade (!= display name)

# Biomes

**Biomes** lets your players **change the biome** on their island.

Created and maintained by [BONNe](https://github.com/BONNe).

!!! warning
    **Biomes** is currently in **Beta**.  
    Keep in mind that **you are more likely to encounter bugs** and **some features might not be stable**.

!!! info "Useful links"
    - [GitHub repository](https://github.com/BentoBoxWorld/Biomes) ([Releases](https://github.com/BentoBoxWorld/Biomes/releases))
    - [Issue tracker](https://github.com/BentoBoxWorld/Biomes/issues)
    - [Development builds](https://ci.codemc.org/job/BentoBoxWorld/job/Biomes) ([Latest stable build](https://ci.codemc.io/job/BentoBoxWorld/job/Biomes/lastStableBuild/))

## Installation

1. Put the addon jar in the `plugins/BentoBox/addons` folder.
2. Start and stop the server to let Biomes generate its configuration files.
3. Edit the [`config.yml`](#configyml) and [`biomes.yml`](#biomesyml) files (you can find them in the `plugins/BentoBox/addons/Biomes` folder).
4. Restart the server.
5. Import the biomes into the gamemode.

## Configuration

### config.yml

After addon is successful installed, it will create config.yml file. Every option in this file comes with comments about them. Please check file for more information.
Most options are also editable admin via commands.

### biomes.yml

!!! warning
    Unlike usual configuration files, the changes you make to the `biomes.yml` file are not automatically taken into account when starting the server.  
    You must import manually the changes you made and eventually override them if you already imported a previous configuration.

This file contains all necessary information about default biomes.
If you change values in biomes.yml, then to apply them, you must run **/[admin_command] biomes import**.

If you want to force an overwrite of biomes via an import, add the **overwrite** option to the end of the import command.
Note that you must import biomes into both BSkyBlock and AcidIsland separately.

!!! info "Useful resources about biomes"
    - [Comprehensive list of available biomes on Spigot](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/block/Biome.html)
    - ["Biome" page on the official Minecraft wiki](https://minecraft.gamepedia.com/Biome)

## Commands

!!! tip
    `[player_command]` and `[admin_command]` are commands that differ depending on the gamemode you are running.
    The Gamemodes' `config.yml` file contains options that allows you to modify these values.
    As an example, on BSkyBlock, the default `[player_command]` is `island`, and the default `[admin_command]` is `bsbadmin`.

=== "Player commands"
    - `/[player_command] biomes`: This method opens GUI that allows to change biome on User island.
    - `/[player_command] biomes help`: Show help for all the commands
    - `/[player_command] biomes info <biome>`: This command returns information about given biome, like cost and necessary level.
    - `/[player_command] biomes set <biome> [<type>] [<size>]`: This command allows to change biome on island without opening GUI. If prarameters < type> and < size> are not provided, command uses default values from addon config.

    !!! info
        - `<biome>` may not be the actual Minecraft biome name. It is defined by the admin.
        - `<type>` is one of the three biome change types. It offers to change biome on whole island (`ISLAND`), in current chunk(s) (`CHUNK`) or by distance around player (`RANGE`).
        - Currently, the biome is changed on the entire y axis. This behaviour might change in the future as Minecraft 1.16 brings support for 3D biomes.

=== "Admin commands"
    - `/[admin_command] biomes`: opens the Admin Biomes GUI.
    - `/[admin_command] biomes help`: displays the help for all the Biomes-related admin commands.
    - `/[admin_command] biomes import [overwrite]`: imports biomes from the `biomes.yml` configuration file.
    - `/[admin_command] biomes add <biome>`: adds a new biome that can be edited via GUI or `biomes edit` command. Biome will not be deployed. To do it, you should enable it in GUI or via `biomes edit <biome> deployed true` command.
    - `/[admin_command] biomes set <player> <biome> [<type>] [<size>]`: works the same as user biome set command, but it is necessary to provide also player, which island biome will be updated.
    - `/[admin_command] biomes edit <biome> <property> <new_value>`: edits provided biome property to new value.
    - `/[admin_command] biomes settings <property> <new_value>`: edits current addon settings via command.

## Permissions

!!! tip
    `[gamemode]` is a prefix that differs depending on the gamemode you are running.
    The prefix is the lowercased name of the gamemode, i.e. if you are using BSkyBlock, the prefix is `bskyblock`.
    Similarly, if you are using AcidIsland, the prefix is `acidisland`.

??? question "Something is missing?"
    You can find the comprehensive list of permissions in the [addon.yml](https://github.com/BentoBoxWorld/Biomes/blob/develop/src/main/resources/addon.yml) file of this addon.  
    If something is indeed missing from the list below, please let us know!

=== "Player permissions"
    - `[gamemode].biomes` (default: `true`): player can use biomes command that opens GUI.
    - `[gamemode].biomes.info` (default: `true`): player can use biomes info command.
    - `[gamemode].biomes.set` (default: `true`): player can use biomes set command.

=== "Admin permissions"
    - `[gamemode].admin.biomes` (default: `op`): player can use admin biomes command that opens GUI.
    - `[gamemode].admin.biomes.add` (default: `op`): player can use admin biomes add command that adds new biome.
    - `[gamemode].admin.biomes.edit` (default: `op`): player can use admin biomes edit command that edits existing biomes parameters.
    - `[gamemode].admin.biomes.set` (default: `op`): player can use admin biomes set command that allows to change other player biomes.
    - `[gamemode].admin.biomes.import` (default: `op`): player can use admin biomes import command allows to import biomes in world.
    - `[gamemode].admin.biomes.settings` (default: `op`): player can use admin biomes settings command that allows to change addon settings.

## Translations

{{ translations(2894, ["zh-CN", "zh-TW", "cs", "fr", "de", "lv", "es"]) }}

## API

### Addon Request Handlers

=== "biome-data"
    !!! summary "Description"
        Returns a `Map<String, Object>` containing all the information about the requested biome.

    !!! question "Input"
        - `biomeId`: String - the unique ID of the requested biome.

    !!! success "Output"
        The output is a `Map<String, Object>` with the following keys:

        - `uniqueId`: String - the unique ID of the requested biome.
        - `world`: String - the name of the world where the biome is available.
        - `biome`: String - the name of the corresponding Minecraft biome.
        - `name`: String - the display name for the biome.
        - `deployed`: Boolean - `true` if the biome is deployed, `false` otherwise.
        - `description`: List&lt;String&gt; - the description for the biome.
        - `icon`: ItemStack - the item that represents the biome in GUIs.
        - `order`: Integer - the order number for the given biome.
        - `cost`: Integer - the cost to use the biome.
        - `level`: Long - the minimum Island Level required in order to use the biome.
        - `permissions`: Set&lt;String&gt; - the list of permissions required in order to use the biome.

    !!! failure
        This handler will return an empty map if the `biomeId` has not been provided or if the `biomeId` could not be found in the database.

    !!! example "Code example"
        ```java
        public Map<String, Object> getBiomeData(String biomeId) {
            return (Map<String, Object>) new AddonRequestBuilder()
                .addon("Biomes")
                .label("biome-data")
                .addMetadata("biomeId", biomeId)
                .request();
        }
        ```

=== "biomes-list"
    !!! summary "Description"
        Returns a list of all biomes' uniqueIds that are defined in a given world.

    !!! question "Input"
        - `world-name`: String - the name of the world.

    !!! success "Output"
        The output is a `List<String>` containing the list of the uniqueIds of the biomes that are defined for the specified world.

    !!! failure
        This handler will return an empty list if the `world-name` has not been provided or if the `world-name` does not exist or is not a gamemode world.

    !!! example "Code example"
        ```java
        public List<String> getBiomesList(String worldName) {
            return (List<String>) new AddonRequestBuilder()
                .addon("Biomes")
                .label("biomes-list")
                .addMetadata("world-name", worldName)
                .request();
        }
        ```

=== "biome-request-change"
    !!! summary "Description"
        Requests a biome change with the provided parameters.

    !!! question "Input"
        - Mandatory parameters:
            - `player`: UUID - the UUID of the targetted player.
            - `world-name`: String - the name of the world where the biome will be changed.
            - `biomeId`: String - the uniqueId of the biome.
        - Optional parameters:
            - `updateMode`: String - the mode to use when changing the biome.
                                     Can be either ISLAND, RANGE or CHUNK.
                                     (Default: config)
            - `range`: Integer - the range within which the biome will be changed.
                                 (Default: config)
            - `checkRequirements`: Boolean - if `true`, the player will have to fulfill all the requirements for the specified biome.
                                   (Default: true)
            - `withdraw`: Boolean - if `true`, the money will be withdrawn from the player's bank account.
                          (Default: true)

    !!! success "Output"
        The output is a `Map<String, Object>` with the following keys:

        - `status`: Boolean - `true` if the biome was changed successfully, `false` otherwise.
        - `reason`: String - message explaining what happened (whether the change was successful or not).

    !!! failure
        This handler will return `false` as its status with an appropriate reason if it failed.

    !!! example "Code example"
        ```java
        public Map<String, Object> requestBiomeChange(UUID player, String worldName, String biomeId, String mode, int range, boolean requirements, boolean withdraw) {
            return (Map<String, Object>) new AddonRequestBuilder()
                .addon("Biomes")
                .label("biome-request-change")
                .addMetadata("player", player)
                .addMetadata("world-name", worldName)
                .addMetadata("biomeId", biomeId)
                .addMetadata("updateMode", mode)
                .addMetadata("range", range)
                .addMetadata("checkRequirements", requirements)
                .addMetadata("withdraw", withdraw)
                .request();
        }
        ```

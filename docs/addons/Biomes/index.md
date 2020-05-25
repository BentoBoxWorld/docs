# Biomes

**Biomes** lets your players **change the biome** on their island.

Created and maintained by [BONNe](https://github.com/BONNe).

!!! info "Useful links"
    - [GitHub repository](https://github.com/BentoBoxWorld/Biomes) ([Releases](https://github.com/BentoBoxWorld/Biomes/releases))
    - [Issue tracker](https://github.com/BentoBoxWorld/Biomes/issues)
    - [CI](https://ci.codemc.org/job/BentoBoxWorld/job/Biomes) ([Latest stable build](https://ci.codemc.io/job/BentoBoxWorld/job/Biomes/lastStableBuild/))

!!! warning
    The Biomes addon is currently in **Beta**.  
    Keep in mind that **you are more likely to encounter bugs** and **some features might not be stable**.  

## Installation

1. Put the addon jar in the `plugins/BentoBox/addons` folder.
2. Restart the server.
3. The addon will create a data folder and inside the folder will be a `config.yml` and an example `biomes.yml`
4. Edit the `config.yml` and `biomes.yml` files how you want. The `biomes.yml` is for importing only.
5. Restart the server.

## Configuration

### config.yml

After addon is successful installed, it will create config.yml file. Every option in this file comes with comments about them. Please check file for more information.
Most options are also editable admin via commands.

### biomes.yml

This file contains all necessary information about default biomes. 
If you change values in biomes.yml, then to apply them, you must run **/bsb biomes import** or **/acid biomes import**.

If you want to force an overwrite of biomes via an import, add the **overwrite** option to the end of the import command.
Note that you must import biomes into both BSkyBlock and AcidIsland separately.

## Commands

!!! tip
    `[user_command]` and `[admin_command]` are prefixes that differs depending on the gamemode you are running. Gamemodes config section contains option to modify these values.
    F.e. in BSkyBlock default `[user_command]` is `island` and default `[admin_command]` is `bsbadmin`. 

=== "Player commands"
    - `/[user_command] biomes`: This method opens GUI that allows to change biome on User island.
    - `/[user_command] biomes help`: Show help for all the commands
    - `/[user_command] biomes info <biome>`: This command returns information about given biome, like cost and necessary level.
    - `/[user_command] biomes set <biome> [<type>] [<size>]`: This command allows to change biome on island without opening GUI. If prarameters < type> and < size> are not provided, command uses default values from addon config.

    !!! info
        - `<biome>` may not be equal Minecraft biome name. It is defined by admin.
        - `<type>` is one of 3 biome chaning types. It offers to change biome on whole island (`ISLAND`), in current chunk(-s) (`CHUNK`) or by distance around player (`RANGE`).
        - Currently biome is changed in whole height.

=== "Admin commands"
    - `/[admin_command] biomes`: To open Admin GUI. 
    - `/[admin_command] biomes help` : Show help for all the commands
    - `/[admin_command] biomes import [overwrite]`: import biomes from biomes.yml
    - `/[admin_command] biomes add <biome>`: add a new biome what can be edited via GUI or `biomes edit` command. Biome will not be deployed. To do it, you should enable it in GUI or via `biomes edit <biome> deployed true` command.
    - `/[admin_command] biomes set <player> <biome> [<type>] [<size>]`: This command works the same as user biome set command, but it is necessary to provide also player, which island biome will be updated.
    - `/[admin_command] biomes edit <biome> <property> <new_value>`: This command allows to edit provided biome property to new value. 
    - `/[admin_command] biomes settings <property> <new_value>`: This command allows to edit current addon settings via command. 

## Permissions

!!! tip
    `[gamemode]` is a prefix that differs depending on the gamemode you are running.
    The prefix is the lowercased name of the gamemode, i.e. if you are using BSkyBlock, the prefix is `bskyblock`.
    Similarly, if you are using AcidIsland, the prefix is `acidisland`.

??? question "Something is missing?"
    You can find the comprehensive list of permissions in the [addon.yml](https://github.com/BentoBoxWorld/Biomes/blob/develop/src/main/resources/addon.yml) file of this addon.

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

As most of BentoBox projects, Biomes Addon is translatable in any language. Everyone can contribute, and translate some parts of the addon in their language via [GitLocalize](https://gitlocalize.com/repo/2894).
If your language is not in the list, please contact to developers via Discord and it will be added there.

| Available | Language | Language code | Progress |
| --- | ---------- | --- | ----------- |
| ✅ | English (United States) | `en-US` | 100% (Default) |
| ❌ | [Chinese (China)](https://gitlocalize.com/repo/2894/zh-CN/src/main/resources/locales) | `zh-CN` | ![gitlocalized](https://gitlocalize.com/repo/2894/zh-CN//badge.svg) |
| ❌ | [Chinese (Taiwan)](https://gitlocalize.com/repo/2894/zh-TW/src/main/resources/locales) | `zh-TW` | ![gitlocalized](https://gitlocalize.com/repo/2894/zh-TW//badge.svg) |
| ✅ | [Czech](https://gitlocalize.com/repo/2894/cs/src/main/resources/locales) | `cs` | ![gitlocalized](https://gitlocalize.com/repo/2894/cs/badge.svg) |
| ✅ | [French](https://gitlocalize.com/repo/2894/fr/src/main/resources/locales) | `fr` | ![gitlocalized](https://gitlocalize.com/repo/2894/fr/badge.svg) |
| ✅ | [German](https://gitlocalize.com/repo/2894/de/src/main/resources/locales) | `de` | ![gitlocalized](https://gitlocalize.com/repo/2894/de/badge.svg) |
| ❌ | [Hungarian](https://gitlocalize.com/repo/2894/hu/src/main/resources/locales) | `hu` | ![gitlocalized](https://gitlocalize.com/repo/2894/hu/badge.svg) |
| ❌ | [Indonesian](https://gitlocalize.com/repo/2894/id/src/main/resources/locales) | `id` | ![gitlocalized](https://gitlocalize.com/repo/2894/id/badge.svg) |
| ❌ | [Italian](https://gitlocalize.com/repo/2894/it/src/main/resources/locales) | `it` | ![gitlocalized](https://gitlocalize.com/repo/2894/it/badge.svg) |
| ❌ | [Japanese](https://gitlocalize.com/repo/2894/ja/src/main/resources/locales) | `ja` | ![gitlocalized](https://gitlocalize.com/repo/2894/ja/badge.svg) |
| ❌ | [Korean](https://gitlocalize.com/repo/2894/ko/src/main/resources/locales) | `ko` | ![gitlocalized](https://gitlocalize.com/repo/2894/ko/badge.svg) |
| ✅ | [Latvian](https://gitlocalize.com/repo/2894/lv/src/main/resources/locales) | `lv` | ![gitlocalized](https://gitlocalize.com/repo/2894/lv/badge.svg) |
| ❌ | [Polish](https://gitlocalize.com/repo/2894/pl/src/main/resources/locales) | `pl` | ![gitlocalized](https://gitlocalize.com/repo/2894/pl/badge.svg) |
| ❌ | [Portuguese](https://gitlocalize.com/repo/2894/pt/src/main/resources/locales) | `pt` | ![gitlocalized](https://gitlocalize.com/repo/2894/pt/badge.svg) |
| ❌ | [Romanian](https://gitlocalize.com/repo/2894/ro/src/main/resources/locales) | `ro` | ![gitlocalized](https://gitlocalize.com/repo/2894/ro/badge.svg) |
| ❌ | [Russian](https://gitlocalize.com/repo/2894/ru/src/main/resources/locales) | `ru` | ![gitlocalized](https://gitlocalize.com/repo/2894/ru/badge.svg) |
| ✅ | [Spanish](https://gitlocalize.com/repo/2894/es/src/main/resources/locales) | `es` | ![gitlocalized](https://gitlocalize.com/repo/2894/es/badge.svg) |
| ❌ | [Turkish](https://gitlocalize.com/repo/2894/tr/src/main/resources/locales) | `tr` | ![gitlocalized](https://gitlocalize.com/repo/2894/tr/badge.svg) |
| ❌ | [Vietnamese](https://gitlocalize.com/repo/2894/vi/src/main/resources/locales) | `vi` | ![gitlocalized](https://gitlocalize.com/repo/2894/vi/badge.svg) |

All guidelines are described [here](../../BentoBox/Translate-BentoBox-and-addons).

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

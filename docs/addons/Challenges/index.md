# Challenges

**Challenges** lets your players **complete various customizable challenges and receive rewards**!

Created and maintained by [BONNe](https://github.com/BONNe).

!!! warning
    0.8.0 stores data in a different format that in 0.7.5 and below.
    You will need to migrate data with `/[gamemode_admin] challenges migrate` if you are using older versions.

{{ addon_useful_links("Challenges") }}

## Installation

1. Place the addon jar in the addons folder of the BentoBox plugin
2. Restart the server
3. Run the admin challenges command, e.g., `/bsbadmin challenges` to configure the addon

## Configuration

By default, the challenges addon comes without any challenge or levels. On first runtime only the Admin GUI will be accessible.
Admins can create their own challenges or load a set of default challenges. Default challenges contains 5 levels and 57 challenges.
There also exist a Web Library, where admins can download public challenges. It is accessible via the Admin GUI by clicking on the Web icon.

## Commands

!!! tip
    `[player_command]` and `[admin_command]` are commands that differ depending on the gamemode you are running.
    The Gamemodes' `config.yml` file contains options that allows you to modify these values.
    As an example, on BSkyBlock, the default `[player_command]` is `island`, and the default `[admin_command]` is `bsbadmin`.

=== "Player commands"
    - `/challenges`: Access Player Challenges GUI. Contains either Challenges in current world or list of worlds where are Challenges enabled. This must be enabled in configuration.
    - `/[player_command] challenges [challenge] [number]`: Access BSkyBlock Player Challenges GUI. If challenge name is provided, than this method will complete that challenge once. If number is provided, than it will complete challenge from 0-number times.

=== "Admin commands"
    - `/challengesadmin`: Access Admin Challenges GUI. Contains list of worlds where Challenges are enabled. This must be enabled in configuration.
    - `/[admin_command] challenges`: Access BSkyBlock Admin Challenges GUI
    - `/[admin_command] challenges reload [hard]`: Ability to reload Challengs addon configuration. This method clears also cache data. Parameter hard allows to reset database connection.
    - `/[admin_command] challenges import [overwrite]`: Ability to import ASkyBlock challenges. Requires challenges.yml file in ./plugins/BentoBox/addons/Challenges/ folder. Parameter overwrite allows to overwrite existing challenges.
    - `/[admin_command] challenges defaults import`: Ability to import Default challenges. This method will not work, if in current world already exist challenges or levels.
    - `/[admin_command] challenges defaults generate`: Ability to export existing challenges. This method will generate defaults.json file in ./plugins/BentoBox/addons/Challenges/ folder.


## Permissions

!!! tip
    `[gamemode]` is a prefix that differs depending on the gamemode you are running.
    The prefix is the lowercased name of the gamemode, i.e. if you are using BSkyBlock, the prefix is `bskyblock`.
    Similarly, if you are using AcidIsland, the prefix is `acidisland`.

??? question "Something is missing?"
    You can find the comprehensive list of permissions in the [addon.yml](https://github.com/BentoBoxWorld/Challenges/blob/develop/src/main/resources/addon.yml) file of this addon.  
    If something is indeed missing from the list below, please let us know!

Permissions can be found [here](Permissions).

=== "Player permissions"

=== "Admin permissions"

## Translations

!!! info "Translations for challenges"
    The translations do not cover the challenges.
    Each challenge has its own "display name" and "description" which are not localized to keep the configuration process as simple as possible for the end user.  
    You can however find or provide translations for various challenges on our [online Challenges Library](https://github.com/BentoBoxWorld/weblink/tree/master/challenges/library) on GitHub.

{{ translations(2896, ["cs", "de", "es", "fr", "ja", "lv", "ru", "zh-CN", "zh-TW"]) }}

## API

### Addon Request Handlers

=== "challenge-list"

=== "challenge-data"

=== "level-list"

=== "level-data"

=== "completed-challenges"

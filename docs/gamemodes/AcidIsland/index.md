# AcidIsland

**AcidIsland** is a Survival gamemode where players have to survive on an island surrounded by a sea of acid.

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("AcidIsland") }}

## The Story
You're on an island, in a sea of acid! If you like Skyblock, try AcidIsland for a new challenge!

This is a variation of SkyBlock. Instead of falling, you must contend with acid water when expanding your island and players can boat to each other's islands.

## Installation

0. Install BentoBox and run it on the server at least once to create its data folders.
1. Place this jar in the addons folder of the BentoBox plugin.
2. Restart the server.
3. The addon will create worlds and a data folder and inside the folder will be a config.yml.
4. Stop the server.
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

??? warning "What's new in v1.21.0 — BentoBox 3.14.0 required, locale migration"
    **Released:** 2026-04-12

    - **Cherry Grove Sanctuary starter island.** A new starter island blueprint themed around the Cherry Grove biome is included for Minecraft 1.21+ servers. To activate it, delete `BentoBox/addons/AcidIsland/blueprints/` so blueprints regenerate on the next startup.
    - 🔺 **BentoBox API 3.14.0 is now required.** Update BentoBox before installing this release.
    - 🔡 **All 24 locale files migrated from `&` codes to MiniMessage.** Delete `BentoBox/locales/AcidIsland/` and restart to regenerate. Any remaining `&` codes in custom files will render as plain text.
    - Bug fix: NullPointerException in the EssentialsX god mode check when EssentialsX fails to load at startup.
    - Several pre-existing locale bugs fixed during migration.

    [Release v1.21.0](https://github.com/BentoBoxWorld/AcidIsland/releases/tag/1.21.0)

## Translations

{{ translations("AcidIsland") }}

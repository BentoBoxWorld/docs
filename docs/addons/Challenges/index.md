# Challenges Addon
[![Discord](https://img.shields.io/discord/272499714048524288.svg?logo=discord)](https://discord.bentobox.world)
[![Build Status](https://ci.codemc.org/buildStatus/icon?job=BentoBoxWorld/Challenges)](https://ci.codemc.org/job/BentoBoxWorld/job/Challenges/)

Add-on for BentoBox to provide challenges for any BentoBox GameMode. 

## Where to find

Latest official release can be downloaded from [Release tab](https://github.com/BentoBoxWorld/Challenges/releases)

Latest development builds are available on the [Jenkins Server](https://ci.codemc.org/job/BentoBoxWorld/job/Challenges/lastStableBuild/).

Be aware that 0.8.0 stores data differently than in 0.7.5 and below. It will be necessary to migrate data via command `/[gamemode_admin] challenges migrate` if you are using older versions.

## Feature requests and bug reports

If you like this addon but something is missing or is not working as you want, you can always submit an [Issue request](https://github.com/BentoBoxWorld/Challenges/issues) or get a support in Discord [BentoBox ![icon](https://avatars2.githubusercontent.com/u/41555324?s=15&v=4)](https://discord.bentobox.world)

## Translations

As most of BentoBox projects, Challenges Addon is translatable in any language. Everyone can contribute, and translate some parts of the addon in their language via [GitLocalize](https://gitlocalize.com/repo/2896).

If your language is not in the list, please contact to developers via Discord and it will be added.
Default challenges come only in English but the addon provides a library of challenges where everyone can share their challenges with their translations.

Please see [this page](Translate-Challenges) for status.


## How to use

1. Place the addon jar in the addons folder of the BentoBox plugin
2. Restart the server
3. Run the admin challenges command, e.g., `/bsbadmin challenges` to configure the addon

### Setup

By default, the challenges addon comes without any challenge or levels. On first runtime only the Admin GUI will be accessible. 
Admins can create their own challenges or load a set of default challenges. Default challenges contains 5 levels and 57 challenges.
There also exist a Web Library, where admins can download public challenges. It is accessible via the Admin GUI by clicking on the Web icon.

## Permissions

Permissions can be found [here](Permissions).

## Commands

Commands can be found [here](Commands).

## Placeholders

Placeholders can be found [here](Placeholders).

## Compatibility

- ✅ BentoBox
- ✅ BSkyBlock
- ✅ AcidIsland
- ✅ SkyGrid 
- ✅ CaveBlock

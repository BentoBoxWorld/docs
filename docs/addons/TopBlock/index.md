# TopBlock

Add-on for BentoBox that produces a Top Ten ranking for magic-block game modes. Ranks are determined by how many magic blocks have been mined - the count.

TopBlock supports [**AOneBlock**](../../gamemodes/AOneBlock/index.md) and [**ChunkBlock**](../../gamemodes/ChunkBlock/index.md). You can install either one or both — when both are present, each game mode gets its own completely separate top ten, its own `topblock` command, and its own set of placeholders. A player's standing in AOneBlock has no effect on their standing in ChunkBlock.

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("TopBlock") }}

## Installation

1. Place the top block addon jar in the addons folder of the BentoBox plugin
2. Restart the server
3. The addon will create a data folder and inside the folder will be a config.yml
4. Edit the config.yml how you want.
5. Restart the server if you make a change

!!! note "TopBlock is not standalone"
    TopBlock requires **at least one** of [AOneBlock](../../gamemodes/AOneBlock/index.md) or [ChunkBlock](../../gamemodes/ChunkBlock/index.md) to be installed alongside it. If neither is found, TopBlock logs an error and disables itself. It hooks whichever of the two it finds at startup, so installing or removing a game mode later only takes effect after a restart.

## Configuration

TopBlock addon has 2 general configuration things:

- config.yml file contains default addon configuration files.
- /panels/ contains files that manages player GUI's

### config.yml

Config file contains main functions for the addon. 

The latest config.yml can be found [here](https://github.com/BentoBoxWorld/TopBlock/blob/develop/src/main/resources/config.yml).

This section defines a number of overall settings for the add-on. These settings are global — they apply to every game mode TopBlock has hooked. There is no per-game-mode configuration.

??? note "refresh-time"
    How often the Top Ten should be refreshed in minutes. Minimum is 1 minute, default is 5.
    Each refresh requires reading every island of every hooked game mode from the database, so this should not be done too often. If you run both AOneBlock and ChunkBlock, each refresh reads both sets of islands, so consider leaving this at the default or raising it.

    Default: `5`

??? note "shorthand"
    Allows to show shorter island level numbers.

    Shows large level values rounded down, e.g., 10,345 -> 10k

    Default: `false`

### Customizable GUI's

BentoBox 1.17 API introduced a function that allows to implement customizable GUI's. We tried to be as simple as possible for customization, however, some features requires explanation.
You can find more information how BentoBox custom GUI's works here: [Custom GUI's](/en/latest/Tutorials/generic/Customizable-GUI/)

??? question "How can I customize GUI's"
     Addon will create a new directory under `/plugins/bentobox/addons/topblock` with a name `panels`

    Currently you can customize GUI's:

    - Top panel: `top_panel` - allows to see top 10 islands.

??? question "What does `TOP` button type?"
    This button is available in top_panel. It shows island at the top X by island top.
    
    The `icon` by default will be `PLAYER_HEAD` with a proper player skin. Enabling it will replace it with specified material.

    `index` in the data field allows to specify which place of Top 10 should be showed in current spot.

    Top panel has 2 implemented actions which funstion requires extra addon:
    
    - `warp` - requires Warps addon. Will be shown only if warp sign exists on players island.
    - `visit` - requires Visit addon. Will be shown only if visiting is allowed on players island.

    Fallback allows to change background icon, when there are no player in top spot.

    Example:
    ```yaml
        #icon: PLAYER_HEAD
        title: topblock.gui.buttons.island.name
        description: topblock.gui.buttons.island.description
        data:
          type: TOP
          index: 1
        actions:
          warp:
            click-type: LEFT
            tooltip: topblock.gui.tips.click-to-warp
          visit:
            click-type: RIGHT
            tooltip: topblock.gui.tips.right-click-to-visit
        fallback:
          icon: LIME_STAINED_GLASS_PANE
          title: topblock.gui.buttons.island.empty
    ```

??? question "What does `VIEW` button type?"
    This button is available in top_panel. It shows viewer island topblock value.

    The `icon` by default will be `PLAYER_HEAD` with a proper player skin. Enabling it will replace it with specified material.
    
    The action `view` allows to see detailed menu of players island.

    Example:
    ```yaml
        #icon: PLAYER_HEAD
        title: topblock.gui.buttons.island.name
        description: topblock.gui.buttons.island.description
        data:
          type: VIEW
        actions:
          view:
            click-type: unknown
            tooltip: topblock.gui.tips.click-to-view
    ```

## Commands

!!! tip
    `[player_command]` and `[admin_command]` are commands that differ depending on the gamemode you are running.
    The Gamemodes' `config.yml` file contains options that allows you to modify these values.
    As an example, on BSkyBlock, the default `[player_command]` is `island`, and the default `[admin_command]` is `bsbadmin`.

=== "Player commands"
    - `/[player_command] topblock`: access to the top panel. Requires the `island.topblock` permission for that game mode (`aoneblock.island.topblock` or `chunkblock.island.topblock`).

TopBlock registers the `topblock` subcommand on **each** game mode it hooks, so with both installed you get `/ob topblock` for AOneBlock and the equivalent under ChunkBlock's player command. Each opens the panel for the game mode whose world you ran it in — the two leaderboards are entirely separate.

## Permissions

=== "Player permissions"
    - `aoneblock.island.topblock` - (default: `true`) - Allows player to use the `/[player_command] topblock` command in AOneBlock.
    - `aoneblock.intopten` - (default: `true`) - Controls whether the player's island appears in the AOneBlock top ten. Remove from an admin or tester to exclude them from the leaderboard.
    - `chunkblock.island.topblock` - (default: `true`) - Allows player to use the `/[player_command] topblock` command in ChunkBlock.
    - `chunkblock.intopten` - (default: `true`) - Controls whether the player's island appears in the ChunkBlock top ten.

??? question "How do I hide a player from the leaderboard?"
    Remove (or negate) the `intopten` permission for the game mode you want to hide them from — `aoneblock.intopten` or `chunkblock.intopten`. Because the prefix is per game mode, you can hide someone from one leaderboard while leaving them visible in the other.

    Two things to be aware of:

    - The permission is only checked while the island **owner is online**. Offline owners are always included, because Bukkit cannot reliably evaluate permissions for a player who is not logged in. So remove the permission from the account that actually logs in, not from an alt.
    - Only the **island owner's** permission is checked. Team members' permissions make no difference.

    The change takes effect at the next refresh, so allow up to `refresh-time` minutes for the island to drop off the list.

??? question "Something is missing?"
    You can find the comprehensive list of permissions in the [addon.yml](https://github.com/BentoBoxWorld/TopBlock/blob/develop/src/main/resources/addon.yml) file of this addon.  
    If something is indeed missing from the list below, please let us know!


## Placeholders

Placeholders are registered separately for each game mode TopBlock has hooked, using that game mode's own prefix. The `chunkblock_` set only exists if ChunkBlock is installed, and reports ChunkBlock's own ranking — the two never mix.

{{ placeholders_source(source="TopBlock") }}

## FAQ

??? question "Can you add a feature X?"
    Please add it to the list [here](https://github.com/BentoBoxWorld/TopBlock/issues).

## Changelog

??? note "What's new in v2.1.0 — ChunkBlock support"
    **Released:** 2026-08-07

    TopBlock is no longer AOneBlock-only. It now supports **ChunkBlock** as well, and either game mode — or both together — can be installed.

    - ✨ **ChunkBlock support.** TopBlock hooks whichever of AOneBlock and ChunkBlock it finds at startup. With both installed, each keeps a completely separate top ten, `topblock` command, and placeholder set.
    - ✨ **New placeholders** — the full `%chunkblock_island_*_top_<number>%` set, mirroring the existing `aoneblock_` ones and reporting ChunkBlock's own ranking.
    - ✨ **New permissions** — `chunkblock.island.topblock` and `chunkblock.intopten`, both default `true`, mirroring the AOneBlock equivalents. Because the prefix is per game mode, you can hide a player from one leaderboard while leaving them visible in the other.
    - 🔺 **AOneBlock is now a soft dependency.** TopBlock previously refused to load without AOneBlock; it now only disables itself if *neither* supported game mode is present. Existing AOneBlock-only setups are unaffected and need no changes.

    ℹ️ This is a drop-in update for AOneBlock servers — no config, panel, or locale changes are required.

    [Release v2.1.0](https://github.com/BentoBoxWorld/TopBlock/releases/tag/2.1.0)

??? warning "What's new in v2.0.0 — platform upgrade required"
    **Released:** 2026-04-26

    - 🐛 **Top Ten panel fixed.** A long-standing bug caused the top ten panel to show only empty green placeholders. The event handler was `private`, causing Bukkit to silently skip it. Now fixed — the panel renders player heads and stats correctly.
    - ✨ **`aoneblock.intopten` permission.** Admins and testers can be excluded from the top ten by removing this permission (granted to all players by default).
    - 🔡 **22 new locales** — cs, de, es, fr, hr, hu, id, it, ja, ko, lv, nl, pl, pt, pt-BR, ro, ru, tr, uk, vi, zh-CN, zh-HK.
    - 🔺 Now requires **Paper 1.21.x**, **Java 21**, **BentoBox 3.14.0+**, and **AOneBlock 1.18.0+**. Spigot is no longer supported.

    🔺 **Delete `addons/TopBlock/panels/top_panel.yml`** before restarting so the updated panel template is extracted. Re-apply any custom layout changes after.

    🔡 Run `/bentobox reload` after updating so BentoBox merges new locale keys into your existing locale files.

    [Release v2.0.0](https://github.com/BentoBoxWorld/TopBlock/releases/tag/2.0.0)

## Translations

{{ translations("TopBlock") }}

## API

### Maven Dependency
TopBlock provides an API for other plugins.

!!! note
    Add the TopBlock dependency to your Maven POM.xml:

    ```xml
        <repositories>
            <repository>
                <id>codemc-repo</id>
                <url>https://repo.codemc.io/repository/bentoboxworld/</url>
            </repository>
        </repositories>
        
        <dependencies>
            <dependency>
                <groupId>world.bentobox</groupId>
                <artifactId>topblock</artifactId>
                <version>1.0.1</version>
                <scope>provided</scope>
            </dependency>
        </dependencies>
    ```

The JavaDocs for TopBlock can be found [here](https://ci.codemc.io/job/BentoBoxWorld/job/TopBlock/ws/target/apidocs/index.html).
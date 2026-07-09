# Admin Tools

BentoBox gives server admins a range of tools to manage the game, investigate problems, and keep things running smoothly — all without needing to edit files manually.

## The Management Panel

The main admin hub is the **Management Panel**, opened with:
```
/bentobox manage
```
(or its alias `/bbox manage`)

From here you can see all running game modes, active islands, and basic server health at a glance.

## The `/bentobox` Command

All top-level BentoBox administration goes through `/bentobox` (alias `/bbox`):

| Command | What it does |
|---|---|
| `/bentobox version` | Shows BentoBox version and all loaded addons. **Always include this when reporting bugs.** |
| `/bentobox manage` | Opens the Management Panel GUI |
| `/bentobox reload` | Reloads BentoBox config files and locales without a full server restart |
| `/bentobox catalog` | Opens the addon catalogue |
| `/bentobox perms` | Shows effective permissions for BentoBox and all addons |
| `/bentobox rank` | Lists, adds, or removes custom ranks |

## Per-Game-Mode Admin Commands

Each game mode has its own admin command. For BSkyBlock it's `/bsb`, for AcidIsland it's `/acid admin`, and so on. These give you controls specific to that game mode:

| Command | What it does |
|---|---|
| `/[admin] info <player>` | Shows full details of a player's island |
| `/[admin] delete <player>` | Deletes a player's island |
| `/[admin] delete` | *(3.19.0)* With no player argument, soft-deletes the island you are **standing on** after confirmation (refused if it still has a team) |
| `/[admin] undelete` | *(3.19.0)* Clears the pending-deletion status of the island you are **standing on**, leaving it unowned, before its region files are purged |
| `/[admin] register <player>` | Registers an unowned island to a player. On an island pending deletion this now shows a confirmation prompt and cancels the deletion instead of refusing |
| `/[admin] setrange <player> <range>` | Changes a player's island protection range |
| `/[admin] range removebonus <player> [id]` | Removes all bonus protection ranges from a single island, or just those for a given id |
| `/[admin] range purgebonus <id>` | Removes a bonus range id from **every** island in the world — ideal after uninstalling an addon that granted bonus ranges. The scan runs asynchronously so it won't freeze large servers |
| `/[admin] settings` | Opens the world settings panel for admins |
| `/[admin] settings <player>` | Opens the island settings panel for a specific player |
| `/[admin] why <player>` | Starts tracking why a player can or cannot do something (see below) |
| `/[admin] reload` | Reloads the game mode's config |
| `/[admin] blueprint` | Opens the Blueprint Manager GUI |

The exact admin command prefix depends on the game mode's configuration. Check the game mode's documentation for its specific command.

## The "Why" Diagnostic Tool

One of the most useful admin tools is the `why` command. If a player reports that they can't do something on their island (or that they *can* do something they shouldn't), run:

```
/[admin_command] why <player>
```

After that, the server console will log the reason for every action that player takes — whether it was allowed or blocked, and which protection flag caused it. This makes it easy to diagnose misconfigured permissions without guessing.

To stop tracking, run the command again.

## Admin Settings Panel

The admin settings panel (opened with `/[admin] settings`) controls world-wide defaults — settings that apply everywhere in the game mode's world, not just on one island. This includes:

- Default protection flags for new islands
- World-wide restrictions (e.g. creeper explosion damage, piston behaviour)
- Visibility settings for the player settings panel (hide flags you don't want players to change)

See [Protection](Protections.md) for a full explanation of the flag system.

## Permissions-Based Control

BentoBox is heavily permission-based. Almost everything — from how many homes a player can have, to whether they can fly, to the size of their island — can be controlled by giving or withholding permissions through your permissions plugin (e.g. LuckPerms).

!!! tip
    Run `/bentobox perms` in the console to see a list of all permissions registered by BentoBox and its addons in YAML format. This is useful for configuring your permissions plugin.

## Database Management

BentoBox supports several database backends for storing island and player data:

- **JSON (flat file)** — the default; easy to set up, no extra software needed
- **MySQL** (5.7+)
- **MariaDB** (10.2.3+)
- **MongoDB** (3.6+)
- **SQLite** (3.28+)
- **PostgreSQL**

The database type is set in BentoBox's `config.yml`. To migrate from one database type to another without losing data, use:
```
/bentobox migrate
```

!!! warning
    Always take a full backup before migrating databases.

## Reloading Without Restarting

After changing a config file, you can apply it without fully restarting the server:
```
/bentobox reload
```
This reloads BentoBox and all addons, including locales. Note that some changes (like world generation settings) always require a full restart to take effect.

## Changelog

!!! warning "What's new in v3.19.0 — bed/anchor respawns now honored"
    **Released:** 2026-07-08

    Compatibility: Paper Minecraft 1.21.5 – 26.2, Java 25+.

    - 🔡 **New `FISHING` protection flag.** Stops players fishing into protected areas from outside the island (the flag checks the hook's location). Defaults to visitor rank, so nothing changes until you raise it.
    - 🔺 **Bed & respawn-anchor spawns are now honored.** Dying on an island now respawns you at your bed or charged respawn anchor when it's on an island you're a member of. Controlled by the new `BED_ANCHOR_RESPAWN` world setting (**enabled by default**); economy-sensitive servers that want the old "always respawn at island home" behaviour should disable it.
    - 🐛 **End exit portal no longer dumps you at world spawn.** Jumping through the end exit portal now routes you to your safe island home on multi-gamemode servers.
    - 🐛 **Item frames and paintings survive blueprints.** Frames keep their facing and contents, and paintings restore their artwork, instead of popping off or facing the wrong way.
    - 🔡 **Recover islands pending deletion.** New `/[admin] undelete`, a stand-on `/[admin] delete` (no player argument), and a confirmation prompt on `/[admin] register` can now rescue soft-deleted islands before their region files are purged (see the Per-Game-Mode Admin Commands table above).
    - ⚙️ **BlueMap island layer survives reloads.** Owner pins and area boxes no longer vanish after `/bluemap reload`. A new `bluemap` section in `config.yml` adds `island-markers` and `island-areas` toggles (both default `true`), mirroring the Dynmap toggles, plus marker customization.
    - ⚙️ **Configurable team panel button icons + member/prospect text.** The STATUS, RANK-filter and INVITE buttons in the team panel now honour the `icon:` set in `team_panel.yml`, and the member/prospect button name and description are now driven by locale keys. Defaults reproduce the previous appearance exactly.
    - ⚡ **Settings-GUI click spam no longer spikes MSPT.** Spam-clicking `/is settings` dropped from ~30–40 MSPT to negligible via in-place panel refresh and a translation cache.

    [Release v3.19.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.19.0)

??? warning "What's new in v3.18.0 — Minecraft 26.2 support requires Java 25 (server)"
    **Released:** 2026-06-27

    - 🔺 **Minecraft 26.2 support + Java 25.** BentoBox now runs on the Minecraft 26.x line (26.2 supported at runtime) and the build has migrated to the Java 25 toolchain. **Your server must run on a Java 25-capable Paper build for the 26.x line.** Already-built addon jars keep working unchanged — only addon *developers* recompiling against this release need to move their own build to Java 25. Compatibility: Paper Minecraft 1.21.5 – 26.2, Java 25+.
    - ⚙️ **Dynmap island marker / area toggles.** A new `dynmap` section in `config.yml` adds `island-markers` (the house icon at the centre of every island) and `island-areas` (the protected-area border box) switches. Both default to `true`, preserving existing behaviour; set either to `false` and run `/bbox reload` to hide those overlays on servers where dense islands flood the map.
    - **Admin range bonus management.** New `/[admin] range removebonus` and `/[admin] range purgebonus` commands clear bonus protection ranges from one island or every island — ideal after uninstalling an addon that granted them (see the Per-Game-Mode Admin Commands table above).
    - 🐛 `/is team setowner` is no longer blocked by the island limit when transferring to an existing team member.
    - 🐛 The Vault hook now retries after addons enable, fixing economy integration that depended on load order.

    [Release v3.18.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.18.0)

??? note "What's new in v3.18.1"
    **Released:** 2026-07-01

    Maintenance release.

    - 🐛 **Multi-line lore & names keep their colour.** Text after the first line of a GUI tooltip no longer falls back to the default purple — the serializer now re-emits the active colour (and decorations) after each newline, fixing tooltips across all addons.

    [Release v3.18.1](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.18.1)

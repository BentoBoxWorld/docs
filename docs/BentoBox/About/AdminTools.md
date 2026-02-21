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
| `/[admin] setrange <player> <range>` | Changes a player's island protection range |
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

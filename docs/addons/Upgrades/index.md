# Upgrades

**Upgrades** gives players a progression curve by letting them purchase island upgrades — expanded protection range, higher block/entity limits, custom commands, spawner boosts, and crop growth boosts — using money, items, permissions, or island level.

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("Upgrades", true) }}

!!! warning "Version 1.0.0 is a complete rewrite"
    Upgrades 1.0.0 replaced the old config-file-based system with a fully **database-driven architecture**. Upgrade definitions, tiers, prices, and rewards are now stored in BentoBox's database and managed entirely in-game. **The old `config.yml` is no longer used** — remove it before installing 1.0.0 if you are upgrading from 0.x.

## Installation

1. Place the Upgrades addon jar in the addons folder of the BentoBox plugin.
2. Restart the server.
3. On first run, 8 example upgrades are seeded automatically so you can get started right away.
4. Use `/[admin_command] upgrades` to customise or create upgrades in-game.

## How It Works

Upgrades, their tiers, prices, and rewards are stored in BentoBox's database (YAML, JSON, MySQL, MongoDB, etc.). There is no large config file to edit. All upgrade data is loaded, cached, and saved automatically by the addon.

On first install the seeder creates 8 example upgrades. Once you delete an example upgrade it will not be re-seeded on the next restart. To re-trigger seeding, delete the `.seeded-gamemodes` marker file from the addon data folder.

## Commands

!!! tip
    `[player_command]` and `[admin_command]` are commands that differ depending on the gamemode you are running.

=== "Player commands"
    - `/[player_command] upgrade`: opens the upgrade purchase panel.

=== "Admin commands"
    - `/[admin_command] upgrades`: opens the admin GUI to create, edit, and delete upgrades and their tiers.

## Price Types

Each upgrade tier can require any combination of the following prices (all must be met to purchase):

| Type | Description |
|---|---|
| **Money** | Vault economy cost |
| **Items** | Specific items must be in the player's inventory |
| **Permissions** | Player must hold a specific permission node |
| **Island Level** | Minimum island level (requires Level addon) |

## Reward Types

Each upgrade tier can grant any combination of the following rewards:

| Type | Description |
|---|---|
| **Range** | Increases the island protection range |
| **Block Limits** | Raises a block type's limit (requires Limits addon) |
| **Entity Limits** | Raises an entity type's limit (requires Limits addon) |
| **Entity Group Limits** | Raises an entity group's limit (requires Limits addon) |
| **Commands** | Runs console or player commands on purchase |
| **Spawner Boost** | Multiplies spawner spawn rates |
| **Crop Growth Boost** | Multiplies crop growth speed |

## Level Formula Variables

In price formulas, the following variables are available:

- `[level]` — the current upgrade level being purchased
- `[islandLevel]` — the island's current level (from Level addon; may be 0)
- `[numberPlayer]` — the number of players on the island team

## Permissions

Permissions are granted automatically by the addon based on upgrade configuration. Check the [addon.yml](https://github.com/BentoBoxWorld/Upgrades/blob/develop/src/main/resources/addon.yml) for the current permission list.

## API

The `UpgradeAPI` class is exposed for other addons to query and modify upgrade data programmatically. See the JavaDocs linked from the addon description above.

## Changelog

??? warning "What's new in v1.0.0 — complete rewrite, action required"
    **Released:** 2026-04-12

    - **Database-driven upgrade system.** All upgrades, tiers, prices, and rewards are now stored in BentoBox's database — no config file editing required.
    - **New admin GUI.** `/[admin_command] upgrades` opens a full in-game admin interface to create and edit upgrades via GUI and chat-input.
    - **New reward types:** Spawner Boost (multiplies spawner rates) and Crop Growth Boost (multiplies crop growth speed).
    - **Templated player panel.** The player upgrade panel is now a BentoBox `TemplatedPanel` — fully customisable via `panels/upgrades_panel.yml`.
    - **Full `UpgradeAPI`** for programmatic access from other addons.
    - 8 example upgrades seeded automatically on first install.
    - Compatibility fixes for Limits addon 1.28.

    🔺 **Not backwards-compatible with 0.x.** Remove your old `config.yml` and any existing upgrade data before installing. There is no automatic migration.

    [Release v1.0.0](https://github.com/BentoBoxWorld/Upgrades/releases/tag/1.0.0)

??? note "What's new in v1.0.1"
    **Released:** 2026-04-12

    - **Seeder fix.** Example upgrades no longer regenerate on every restart after being deleted. The seeder now tracks which game modes have been seeded in a persistent `.seeded-gamemodes` marker file.

    [Release v1.0.1](https://github.com/BentoBoxWorld/Upgrades/releases/tag/1.0.1)

## Translations

{{ translations("Upgrades") }}

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

## Tiers and Levels

Each upgrade is made up of one or more **tiers**. A tier covers a range of levels — for example, a tier might cover levels 0 to 4, meaning any player whose upgrade level falls in that range is affected by that tier's rewards.

- When a player purchases an upgrade their level increases by 1.
- The rewards applied are always those of the tier whose range contains the player's current level. Moving into a new tier's range immediately switches to that tier's rewards.
- A tier can require **multiple prices** (all must be paid) and grant **multiple rewards** (all are applied).
- Price and reward formulas can use variables (see [Formula Variables](#formula-variables)) to scale automatically with level, island level, or team size.

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

| Type | Description | Applied |
|---|---|---|
| **Range** | Increases the island protection range | At purchase |
| **Block Limits** | Raises a block type's per-island limit (requires Limits addon) | At purchase |
| **Entity Limits** | Raises an entity type's limit (requires Limits addon) | At purchase |
| **Entity Group Limits** | Raises an entity group's limit (requires Limits addon) | At purchase |
| **Commands** | Runs console or player commands | At purchase |
| **Spawner Boost** | Adds extra mob spawns to every spawner event on the island | Passive — always on |
| **Crop Growth Boost** | Adds extra growth ticks to every natural crop growth event on the island | Passive — always on |

### Commands

The Commands reward runs one or more commands when a player purchases the upgrade.

- **Console mode**: commands run as the server console (use this for `/give`, rank-up commands, or anything requiring elevated permissions).
- **Player mode**: commands run as the purchasing player (limited to their own permissions).

The following placeholders are available in command strings:

- `[player]` — the name of the player who purchased the upgrade
- `[owner]` — the island owner's name

### Spawner Boost

Spawner Boost is a **passive, always-on** effect. It does not do anything at purchase time; it takes effect immediately and stays active as long as the island holds that upgrade level.

Every time a spawner on the island fires, the addon totals the island's Spawner Boost value across all active upgrade tiers and spawns that many additional mobs of the same type at the same location.

The formula value is a **bonus multiplier**:

| Formula value | Effect per spawner event |
|---|---|
| `0.5` | 50% chance of 1 extra mob |
| `1.0` | Always 1 extra mob |
| `1.5` | Always 1 extra mob + 50% chance of a second |
| `2.0` | Always 2 extra mobs |

Bonuses from multiple upgrades that include a Spawner Boost reward are **added together**. The boost works for all spawner types.

### Crop Growth Boost

Crop Growth Boost is also a **passive, always-on** effect. When a crop grows naturally, the addon applies additional bone-meal growth ticks equal to the bonus value — making crops grow faster the higher a player's upgrade level.

The formula value works the same way as Spawner Boost:

| Formula value | Effect per natural growth event |
|---|---|
| `0.5` | 50% chance of 1 extra growth tick |
| `1.0` | Always 1 extra tick |
| `2.0` | Always 2 extra ticks |

Bonuses from multiple upgrades stack. Supported crops: **Wheat, Carrots, Potatoes, Beetroots, Nether Wart, Sweet Berry Bush, Torchflower, Pitcher Plant**.

## Formula Variables

Formula fields in both prices and rewards support the following variables:

- `[level]` — the current upgrade level being purchased (or active)
- `[islandLevel]` — the island's current level (from Level addon; may be 0 if Level is not installed)
- `[numberPlayer]` — the number of players on the island team

These let you write formulas that scale automatically, e.g. a money cost of `500 * [level]` or a spawner bonus of `0.1 * [level]`.

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

??? note "What's new in v1.0.2"
    **Released:** 2026-04-14

    Two data-persistence bugs fixed that caused upgrade data to be lost on server restart:

    - **Admin upgrade definitions now saved** — Changes made through the admin GUI (names, descriptions, icons, price/reward formulas, tier counts, deletions) are now written to the database immediately instead of being discarded on restart.
    - **Player purchase levels now saved** — When a player buys an upgrade, the new level is written to the database immediately. Islands no longer revert to pre-purchase levels after a restart.

    [Release v1.0.2](https://github.com/BentoBoxWorld/Upgrades/releases/tag/1.0.2)

## Translations

{{ translations("Upgrades") }}

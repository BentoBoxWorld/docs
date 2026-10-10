# IslandStats

**IslandStats** keeps statistics for each island rather than for each player. It starts with mob deaths: how many of each mob has died on an island, and how many of those a player killed. It works with every game mode.

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("IslandStats") }}

## Installation

1. Place the IslandStats addon jar in the addons folder of the BentoBox plugin.
2. Restart the server.
3. The addon will create a data folder and inside the folder will be a config.yml.
4. Edit the config.yml how you want.
5. Restart the server if you make a change.

IslandStats requires BentoBox 3.23.0 or later, Minecraft 26.2 or later and Java 25.

!!! warning "Counting starts when the addon is installed"
    IslandStats does not read old player statistics, so every island starts at zero.

## Statistics

The addon keeps two counts for each mob type:

| Stat | Counts |
|---|---|
| `KILL_ENTITY` | Mobs killed by a player on the island. Same meaning as the vanilla `KILL_ENTITY` player statistic. |
| `ENTITY_DEATH` | Mobs that died on the island from any cause: players, mob farms, fall damage, lava. |

A death counts for the island whose protected area it happened in. Players and armor stands are not counted. Kills by visitors count toward `KILL_ENTITY` unless `count-visitor-kills` is turned off. Every death on the island always counts toward `ENTITY_DEATH`.

The addon doesn't use vanilla player statistics, because they only record kills where a player gets the credit and they don't record where the mob was. That would miss mob farms and credit the killer's island rather than the island the mob died on.

### Stats dialog

`/[player_command] stats` opens a dialog:

- The summary page shows a total for each stat, with a button to open it.
- Each stat page lists mobs from most to fewest, with Previous, Next, Back and Close buttons.
- Mob names are sent as translatable text, so each player sees them in their own client language.

### Storage

Stats are stored through the BentoBox database API, so they go into whatever database BentoBox is set up to use. There is one record per island. With the JSON database these are in `plugins/BentoBox/database/IslandStatsData/`. Counting happens in memory, and changed islands are saved on a timer (`save-interval`) and when the server stops. When an island is deleted or reset, its stats are deleted too.

## Configuration

The latest `config.yml` can be found [here](https://github.com/BentoBoxWorld/IslandStats/blob/develop/src/main/resources/config.yml).

??? note "disabled-gamemodes"
    Game modes listed here are ignored by IslandStats.

    Default: `[]`

    ```yaml
    disabled-gamemodes:
      - BSkyBlock
    ```

??? note "count-visitor-kills"
    Count mobs killed on an island by players who are not members of it, such as visitors or coops. This only affects the 'killed by players' stat. Every mob death on the island is always counted in the 'all mob deaths' stat.

    Default: `true`

??? note "ignored-entities"
    Entity types that are never counted. Use the Bukkit entity type names. Armor stands are living entities to the server, so they are ignored by default.

    Default: `ARMOR_STAND`

??? note "save-interval"
    How often, in minutes, changed stats are written to the database. Stats are counted in memory and always saved when the server stops. Minimum 1.

    Default: `5`

??? note "dialog.page-size"
    How many mob lines to show on each page of the stats dialog. Range 1 to 50.

    Default: `15`

## Commands

!!! tip
    `[player_command]` and `[admin_command]` are commands that differ depending on the gamemode you are running.
    The Gamemodes' `config.yml` file contains options that allows you to modify these values.
    As an example, on BSkyBlock, the default `[player_command]` is `island`, and the default `[admin_command]` is `bsbadmin`.

=== "Player commands"
    - `/[player_command] stats`: opens your island's stats dialog.

=== "Admin commands"
    - `/[admin_command] stats <player>`: shows that player's island stats. A player sees the dialog, and the console gets the stats as chat lines.
    - `/[admin_command] stats <player> reset`: erases the island's stats after asking for confirmation.

!!! warning "Use the command for the world you're in"
    `/[player_command] stats` only works in that game mode's world. For example, in the OneBlock world use the OneBlock command, not `/is`, so players who have islands in several game modes see the right one.

## Permissions

!!! tip
    `[gamemode]` is a prefix that differs depending on the gamemode you are running.

| Permission | Default | What it allows |
|---|---|---|
| `[gamemode].island.stats` | true | `/[player_command] stats`, which opens your island's stats |
| `[gamemode].admin.stats` | op | `/[admin_command] stats <player> [reset]` |

## Placeholders

{{ placeholders_source("IslandStats") }}

`<entity>` is the lower case mob type, such as `zombie` or `iron_golem`. With PlaceholderAPI the placeholders look like `%IslandStats_bskyblock_island_kill_entity_zombie%`.

## For addon developers

Other addons can read counts through the manager:

```java
IslandStats stats = (IslandStats) BentoBox.getInstance().getAddonsManager().getAddonByName("IslandStats").orElseThrow();
long zombies = stats.getManager().getCount(island, IslandStat.KILL_ENTITY, EntityType.ZOMBIE);
long allDeaths = stats.getManager().getTotal(island, IslandStat.ENTITY_DEATH);
```

??? note "What's new in v1.0.0 — first release"
    **Released:** 2026-10-04

    First release. Compatibility: BentoBox API 3.23.0 · Minecraft 26.2 and later · Java 25. [Release 1.0.0](https://github.com/BentoBoxWorld/IslandStats/releases/tag/1.0.0)

    - Mob kill and death counts per island (`KILL_ENTITY` and `ENTITY_DEATH`).
    - Stats dialog with `/[player_command] stats`, and an admin view and reset with `/[admin_command] stats <player> [reset]`.
    - Placeholders for island totals, per-mob counts and the island the player is standing on.
    - 🔡 Only the `en-US` locale ships in this release. Translations are welcome.

## Translations

{{ translations("IslandStats") }}

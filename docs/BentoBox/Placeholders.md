# Placeholders

Placeholders let other plugins show BentoBox information: a player's island name or level on a scoreboard, their rank in chat, the number of islands in a hologram, and so on.

## Setting up

1. Install [PlaceholderAPI](https://www.spigotmc.org/resources/placeholderapi.6245/).
2. Restart the server.

That's all. BentoBox registers its placeholders with PlaceholderAPI itself; there's no expansion to download with `/papi ecloud`.

Then use the placeholders in any plugin that supports PlaceholderAPI (scoreboards, tab lists, chat, holograms…).

## How placeholders are named

Each game mode registers its own copy of every placeholder, starting with the game mode's name in lower case:

```
%bskyblock_island_name%
%aoneblock_island_members_count%
%acidisland_rank%
```

The tables below write this prefix as `[gamemode]`. Placeholders from addons start with the addon's name and then the game mode, for example `%Level_bskyblock_island_level%`; they're listed on each [addon's page](../addons/Level/index.md#placeholders).

There are two kinds:

- `[gamemode]_island_...` is about **the player's own island** in that game mode.
- `[gamemode]_visited_island_...` is about **the island the player is standing on**, which may be someone else's.

## Finding a placeholder in game

| Command | What it does |
|---|---|
| `/bentobox placeholders` | Opens a menu to browse every placeholder from BentoBox and the addons, and turn individual placeholders on or off |
| `/bentobox dump-placeholders` | Writes every registered placeholder to `plugins/BentoBox/placeholder-dump.md` |
| `/papi parse me %bskyblock_island_name%` | Shows what a placeholder returns for you (a PlaceholderAPI command) |

## BentoBox placeholders

These are registered for every game mode.

{{ placeholders_source("BentoBox") }}

### Numbered placeholders

Placeholders ending in `_<n>` are registered once for each number:

- `island_member_name_<n>`, `island_member_rank_<n>` and `island_banned_name_<n>` (and their `visited_island_` versions) go from 1 to 50, for listing a team or ban list one line at a time, for example `%bskyblock_island_member_name_1%`.
- `island_name_<n>` and `island_memberlist_<n>` go from 1 to the number of islands a player can own (`concurrent-islands`). See [Multiple Islands](ConcurrentIslands.md).

### Flag placeholders

Every protection flag, island setting and world setting has a placeholder: `flag_` followed by the flag's ID in lower case.

| Flag type | Returns |
|---|---|
| Protection flag | The lowest rank allowed on the player's island, for example `Member` |
| Island setting | `true` or `false` for the player's island |
| World setting | `true` or `false` for the game mode's world |

```
%bskyblock_flag_break_blocks%    → Member
%bskyblock_flag_pvp_overworld%   → false
```

Flag IDs are listed in [Flags](Flags.md). Flags added by addons get placeholders automatically.

## Game mode pages

Each game mode's page lists these placeholders with its own prefix filled in, together with the game mode's own placeholders:

[AcidIsland](../gamemodes/AcidIsland/Placeholders.md) · [AOneBlock](../gamemodes/AOneBlock/Placeholders.md) · [Boxed](../gamemodes/Boxed/Placeholders.md) · [BSkyBlock](../gamemodes/BSkyBlock/Placeholders.md) · [CaveBlock](../gamemodes/CaveBlock/Placeholders.md) · [ChunkBlock](../gamemodes/ChunkBlock/Placeholders.md) · [Poseidon](../gamemodes/Poseidon/Placeholders.md) · [SkyGrid](../gamemodes/SkyGrid/Placeholders.md) · [TradeWinds](../gamemodes/TradeWinds/Placeholders.md)

## Troubleshooting

**A placeholder shows as text (`%bskyblock_island_name%`) instead of a value.**
Check that PlaceholderAPI is installed, that the plugin showing it supports PlaceholderAPI, and that the placeholder isn't turned off in `/bentobox placeholders`. Some chat plugins need an extra setting or plugin to parse placeholders in chat messages. Test with `/papi parse me <placeholder>`.

**A placeholder is empty.**
The player has no island in that game mode, or for `visited_island_` placeholders, isn't standing on an island.

**A placeholder from an addon doesn't exist.**
Check the addon is installed and enabled for that game mode. Addon placeholders start with the addon name, then the game mode: `%Level_bskyblock_island_level%`. Also check it hasn't been turned off in `/bentobox placeholders`.

**I need a placeholder that doesn't exist.**
[Request one](https://github.com/BentoBoxWorld/BentoBox/issues/new?labels=Status%3A+Pending%2C+Type%3A+Enhancement&template=placeholder_request.md&title=Placeholder%3A+) on GitHub.

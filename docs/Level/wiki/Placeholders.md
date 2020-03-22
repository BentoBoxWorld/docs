# Introduction

Please read the [Placeholders page](/BentoBox/wiki/Placeholders).

# Placeholders

## Generic placeholders

These placeholders are available in all currently available gamemodes ([BSkyBlock](/BSkyBlock/wiki/Placeholders), [AcidIsland](/AcidIsland/wiki/Placeholders), [CaveBlock](/CaveBlock/wiki/Placeholders), [SkyGrid](/SkyGrid/wiki/Placeholders)).

**List of available placeholders as of Level 1.9.0.**

| Placeholder | Description | Level Version |
|-------------------------------------------------------|--------------------------------------------------------------------------------|-----------|
| `%Level_[gamemode]_island_level%` | Island level of the player's island | 1.9.0 |
| `%Level_[gamemode]_visited_island_level%` | Island level of the island the player is standing on | 1.9.0 |
| `%Level_[gamemode]_top_value_#RANK#%` | Island level of the `#RANK#`-th island in the Top 10 | 1.9.0 |
| `%Level_[gamemode]_top_name_#RANK#%` | Island owner's name of the `#RANK#`-th island in the Top 10 | 1.9.0 |

*Note*: `#RANK#` is a number between 1 and 10.

## Usage examples
### Displaying Top 10 in BSkyBlock
1. `%Level_bskyblock_top_name_1% with island level: %Level_bskyblock_top_value_1%`
2. `%Level_bskyblock_top_name_2% with island level: %Level_bskyblock_top_value_2%`
3. `%Level_bskyblock_top_name_3% with island level: %Level_bskyblock_top_value_3%`
4. `%Level_bskyblock_top_name_4% with island level: %Level_bskyblock_top_value_4%`
5. `%Level_bskyblock_top_name_5% with island level: %Level_bskyblock_top_value_5%`
6. `%Level_bskyblock_top_name_6% with island level: %Level_bskyblock_top_value_6%`
7. `%Level_bskyblock_top_name_7% with island level: %Level_bskyblock_top_value_7%`
8. `%Level_bskyblock_top_name_8% with island level: %Level_bskyblock_top_value_8%`
9. `%Level_bskyblock_top_name_9% with island level: %Level_bskyblock_top_value_9%`
10. `%Level_bskyblock_top_name_10% with island level: %Level_bskyblock_top_value_10%`

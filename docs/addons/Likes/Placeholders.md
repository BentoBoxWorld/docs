# Likes Placeholders

Please read the main [Placeholders page](/BentoBox/Placeholders).

## How to suggest a new placeholder?

If you think a placeholder for LikesAddon should be added, then please submit us a [placeholder request](https://github.com/BentoBoxWorld/Likes/issues/new?assignees=&labels=Status%3A+Pending%2C+Type%3A+Enhancement&template=placeholder_request.md&title=Placeholder%3A+).

# Placeholders

## Generic placeholders

These placeholders are available in all currently available gamemodes ([BSkyBlock](/BSkyBlock/Placeholders), [AcidIsland](/AcidIsland/Placeholders), [CaveBlock](/CaveBlock/Placeholders), [SkyGrid](/SkyGrid/Placeholders)).

## LikesAddon placeholders for gamemode addons

**Available player placeholders in 1.7.0.**

| Placeholder | Description | Version |
|-------------------------------------------------------|--------------------------------------------------------------------------------|-----------|
| `%[gamemode]_likes_addon_island_likes_count%` | Count of likes that are set to player island | 1.7.0 |
| `%[gamemode]_likes_addon_island_likes_place%` | Island place by likes count | 1.7.0 |
| `%[gamemode]_likes_addon_island_dislikes_count%` | Count of dislikes that are set to player island | 1.7.0 |
| `%[gamemode]_likes_addon_island_dislikes_place%` | Island place by dislikes count | 1.7.0 |
| `%[gamemode]_likes_addon_island_rank_count%` | Rank number (likes - dislikes) that are set to player island | 1.7.0 |
| `%[gamemode]_likes_addon_island_rank_place%` | Island place by rank | 1.7.0 |


**Available top placeholders in 1.7.0.**

In all placeholders below X must be replaced to integer from 1 to 10. Returned value can be empty.

| Placeholder | Description | Version |
|-------------------------------------------------------|--------------------------------------------------------------------------------|-----------|
| `%[gamemode]_likes_addon_top_likes_owner_name_X%` | Island owner name who are in place X by likes | 1.7.0 |
| `%[gamemode]_likes_addon_top_likes_island_name_X%` | Island name which are in place X by likes | 1.7.0 |
| `%[gamemode]_likes_addon_top_likes_count_X%` | Count of likes for island that are in place X by likes | 1.7.0 |
| `%[gamemode]_likes_addon_top_dislikes_owner_name_X%` | Island owner name who are in place X by dislikes | 1.7.0 |
| `%[gamemode]_likes_addon_top_dislikes_island_name_X%` | Island name which are in place X by dislikes | 1.7.0 |
| `%[gamemode]_likes_addon_top_dislikes_count_X%` | Count of dislikes for island that are in place X by dislikes | 1.7.0 |
| `%[gamemode]_likes_addon_top_rank_owner_name_X%` | Island owner name who are in place X by rank | 1.7.0 |
| `%[gamemode]_likes_addon_top_rank_island_name_X%` | Island name which are in place X by rank | 1.7.0 |
| `%[gamemode]_likes_addon_top_rank_count_X%` | Rank value for island that are in place X by rank | 1.7.0 |

## Usage examples
### Displaying Top 10 by like count in BSkyBlock
1. `%bskyblock_likes_addon_top_likes_owner_name_1% with island likes: %bskyblock_likes_addon_top_likes_count_1%`
2. `%bskyblock_likes_addon_top_likes_owner_name_2% with island likes: %bskyblock_likes_addon_top_likes_count_2%`
3. `%bskyblock_likes_addon_top_likes_owner_name_3% with island likes: %bskyblock_likes_addon_top_likes_count_3%`
4. `%bskyblock_likes_addon_top_likes_owner_name_4% with island likes: %bskyblock_likes_addon_top_likes_count_4%`
5. `%bskyblock_likes_addon_top_likes_owner_name_5% with island likes: %bskyblock_likes_addon_top_likes_count_5%`
6. `%bskyblock_likes_addon_top_likes_owner_name_6% with island likes: %bskyblock_likes_addon_top_likes_count_6%`
7. `%bskyblock_likes_addon_top_likes_owner_name_7% with island likes: %bskyblock_likes_addon_top_likes_count_7%`
8. `%bskyblock_likes_addon_top_likes_owner_name_8% with island likes: %bskyblock_likes_addon_top_likes_count_8%`
9. `%bskyblock_likes_addon_top_likes_owner_name_9% with island likes: %bskyblock_likes_addon_top_likes_count_9%`
10. `%bskyblock_likes_addon_top_likes_owner_name_10% with island likes: %bskyblock_likes_addon_top_likes_count_10%`
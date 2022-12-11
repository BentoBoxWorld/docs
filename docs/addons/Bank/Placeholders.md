# Introduction

Please read the [Placeholders page](../../../BentoBox/Placeholders).

# Placeholders

## Generic placeholders

These placeholders are available in all currently available gamemodes ([BSkyBlock](../../../gamemodes/BSkyBlock/Placeholders), [AcidIsland](../../../gamemodes/AcidIsland/Placeholders), [CaveBlock](../../../gamemodes/CaveBlock/Placeholders), [SkyGrid](../../../gamemodes/SkyGrid/Placeholders), [AOneBlock](../../../gamemodes/AOneBlock/Placeholders)).

**List of available placeholders**

| Placeholder | Description | Bank Version |
|-------------------------------------------------------|--------------------------------------------------------------------------------|-----------|
| `%Bank_[gamemode]_island_balance%` | Island balance of the player's island formatted by Vault | 1.1.0 |
| `%Bank_[gamemode]_visited_island_balance%` | Island balance of the island the player is standing on formatted by Vault| 1.1.0 |
| `%Bank_[gamemode]_island_balance_number%` | Island balance of the player's island - no formatting. Raw value.| 1.4.0 |
| `%Bank_[gamemode]_visited_island_balance_number%` | Island balance of the island the player is standing on - no formatting. Raw value.| 1.4.0 |
| `%Bank_[gamemode]_island_balance_formatted%` | Formatted island balance of the player's island, e.g. 1.5M | 1.1.1 |
| `%Bank_[gamemode]_visited_island_balance_formatted%` | Formatted island balance of the island the player is standing on. e.g. 1.2k | 1.1.0 |
| `%Bank_[gamemode]_top_value_#RANK#%` | Island balance of the `#RANK#`-th island on the leader board | 1.1.0 |
| `%Bank_[gamemode]_top_name_#RANK#%` | Island owner's name of the `#RANK#`-th island on the leader board | 1.1.0 |

*Note*: `#RANK#` is a number between 1 and the `number-of-ranks` setting in Bank's config.yml.

## Usage examples
### Displaying the fist 10 in BSkyBlock
1. `%Bank_bskyblock_top_name_1% with island balance: %Bank_bskyblock_top_value_1%`
2. `%Bank_bskyblock_top_name_2% with island balance: %Bank_bskyblock_top_value_2%`
3. `%Bank_bskyblock_top_name_3% with island balance: %Bank_bskyblock_top_value_3%`
4. `%Bank_bskyblock_top_name_4% with island balance: %Bank_bskyblock_top_value_4%`
5. `%Bank_bskyblock_top_name_5% with island balance: %Bank_bskyblock_top_value_5%`
6. `%Bank_bskyblock_top_name_6% with island balance: %Bank_bskyblock_top_value_6%`
7. `%Bank_bskyblock_top_name_7% with island balance: %Bank_bskyblock_top_value_7%`
8. `%Bank_bskyblock_top_name_8% with island balance: %Bank_bskyblock_top_value_8%`
9. `%Bank_bskyblock_top_name_9% with island balance: %Bank_bskyblock_top_value_9%`
10. `%Bank_bskyblock_top_name_10% with island balance: %Bank_bskyblock_top_value_10%`

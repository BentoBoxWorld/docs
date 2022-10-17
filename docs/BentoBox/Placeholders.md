Placeholders allow you to display data from any BentoBox's addons or gamemodes in other plugins. And the opposite is true as well!

## How to use placeholders?

### Download the placeholder API you need.

BentoBox uses [**PlaceholderAPI**](https://www.spigotmc.org/resources/placeholderapi.6245/) for placeholders.

### Launch the server and you're ready to go!

Regardless of the placeholder API you're using, just start the server. There are **no expansions to download**: BentoBox handles everything!

## How to display a placeholder in the chat?

If you're using **EssentialsChat** and **PlaceholderAPI**, you **must** install [**ChatInjector**](https://www.spigotmc.org/resources/chatinjector-1-13.81201/) in order for the placeholders to show up in the chat. However, please note it has been reported that ChatInjector might cause issues.

We recommend you to use an alternative chat plugin which supports PlaceholderAPI, such as [**ChatControl**](https://www.spigotmc.org/resources/chatcontrol%E2%84%A2-the-ultimate-chat-plugin-500-000-downloads-1-2-5-1-14-4.271/).

## How to display a placeholder in a scoreboard?

If you're using a scoreboard plugin that natively does not support **PlaceholderAPI**, but supports **MVdWPlaceholderAPI** (like **Featherboard**), you still can use BentoBox placeholders, however, you need to add **{placeholderapi_[text]}**, and replace *[text]* with a placeholder without *%* chars, like *{placeholderapi_bskyblock_island_name}*.

## How to suggest a new placeholder?

If you think a placeholder for BentoBox or another default placeholder for gamemodes should be added, then please submit a [placeholder request](https://github.com/BentoBoxWorld/BentoBox/issues/new?assignees=&labels=Status%3A+Pending%2C+Type%3A+Enhancement&template=placeholder_request.md&title=Placeholder%3A+).

## Default placeholders for gamemode addons

All gamemode addons get some default placeholders automatically registered to them.

**Available default placeholders**

| Placeholder | Description | Version |
|-------------------------------------------------------|--------------------------------------------------------------------------------|-----------|
| %[gamemode]_world_friendly_name% | Name of the gamemode's world | 1.4.0 |
| %[gamemode]_world_islands% | Number of islands in this gamemode's world | 1.5.0 |
| %[gamemode]_island_distance% | Half the distance between islands' centers of the gamemode's world | 1.4.0 |
| %[gamemode]_island_distance_diameter% | Distance between islands of the gamemode's world | 1.5.0 |
| %[gamemode]_island_protection_range% | Radius of the island's protection range | 1.4.0 |
| %[gamemode]_island_protection_range_diameter% | Diameter of the island's protection range | 1.5.0 |
| %[gamemode]_island_owner% | Name of the island's owner | 1.4.0 |
| %[gamemode]_island_creation_date% | Creation date of the island | 1.4.0 |
| %[gamemode]_island_name% | Name of the island | 1.4.0 |
| %[gamemode]_island_center% | Coordinates of the island's center | 1.5.0 |
| %[gamemode]_island_center_x% | X coordinate of the island's center | 1.5.0 |
| %[gamemode]_island_center_y% | Y coordinate of the island's center | 1.5.0 |
| %[gamemode]_island_center_z% | Z coordinate of the island's center | 1.5.0 |
| %[gamemode]_island_members_max% | Maximum number of members there can be on the island | 1.5.0 |
| %[gamemode]_island_members_count% | Number of members, subowners and owner there are on the island | 1.5.0 |
| %[gamemode]_island_members_list% | Comma separated list of player names that are at least MEMBER on the island | 1.13.0 |
| %[gamemode]_island_trustees_count% | Number of players trusted to the island | 1.5.0 |
| %[gamemode]_island_coops_count% | Number of players cooped to the island | 1.5.0 |
| %[gamemode]_island_visitors_count% | Number of players currently visiting the island | 1.5.0 |
| %[gamemode]_island_bans_count% | Number of players banned from the island | 1.5.0 |
| %[gamemode]_island_uuid% | The unique ID of the island as used in the database | 1.15.4 |
| %[gamemode]_visited_island_protection_range% | Radius of the protection range of the island the player is standing on | 1.5.2 |
| %[gamemode]_visited_island_protection_range_diameter% | Diameter of the protection range of the island the player is standing on | 1.5.2 |
| %[gamemode]_visited_island_owner% | Name of the owner of the island the player is standing on | 1.5.2 |
| %[gamemode]_visited_island_creation_date% | Creation date of the island the player is standing on | 1.5.2 |
| %[gamemode]_visited_island_name% | Name of the island the player is standing on | 1.5.2 |
| %[gamemode]_visited_island_center% | Coordinates of the center of the island the player is standing on | 1.5.2 |
| %[gamemode]_visited_island_center_x% | X coordinate of the center of the island the player is standing on | 1.5.2 |
| %[gamemode]_visited_island_center_y% | Y coordinate of the center of the island the player is standing on | 1.5.2 |
| %[gamemode]_visited_island_center_z% | Z coordinate of the center of the island the player is standing on | 1.5.2 |
| %[gamemode]_visited_island_members_max% | Maximum number of members there can be on the island the player is standing on | 1.5.2 |
| %[gamemode]_visited_island_members_count% | Number of members, subowners and owner there are on the island | 1.5.2 |
| %[gamemode]_visited_island_members_list% | Comma separated list of player names that are at least MEMBER on the island the player is standing on | 1.13.0 |
| %[gamemode]_visited_island_trustees_count% | Number of players trusted on the island the player is standing on | 1.5.2 |
| %[gamemode]_visited_island_coops_count% | Number of players cooped to the island the player is standing on | 1.5.2 |
| %[gamemode]_visited_island_visitors_count% | Number of players currently visiting the island the player is standing on | 1.5.2 |
| %[gamemode]_visited_island_bans_count% | Number of players banned from the island the player is standing on | 1.5.2 |
| %[gamemode]_visited_island_uuid% | The unique ID of the island the player is standing on | 1.15.4 |
| %[gamemode]_has_island% | Whether the player has an island or not | 1.5.0 |
| %[gamemode]_rank% | Rank the player has on his island | 1.5.0 |
| %[gamemode]_resets% | Number of times the player has reset his island | 1.5.0 |
| %[gamemode]_resets_left% | Number of times the player can reset his island | 1.5.0 |
| %[gamemode]_deaths% | Number of times the player died | 1.12.0 |
| %[gamemode]_on_island% | Whether the player is on an island he is part of or not | 1.13.0 |

## See also
Gamemodes and Addons can also bring their own placeholders. We highly recommend that you look up the following pages, which are likely more adapted to your needs.

- Gamemodes
    - [AcidIsland](../../gamemodes/AcidIsland/Placeholders)
    - [AOneBlock](../../gamemodes/AOneBlock/Placeholders)
    - [Boxed](../../gamemodes/Boxed/Placeholders)
    - [BSkyBlock](../../gamemodes/BSkyBlock/Placeholders)
    - [CaveBlock](../../gamemodes/CaveBlock/Placeholders)
    - [SkyGrid](../../gamemodes/SkyGrid/Placeholders)
- Addons
    - [Bank](../../addons/Bank/#placeholders)
    - [Challenges](../../addons/Challenges/#placeholders)
    - [Level](../../addons/Level/#placeholders)
    - [Likes](../../addons/Likes/#placeholders)
    - [Limits](../../addons/Limits/#placeholders)
    - [MagicCobblestoneGenerator](../../addons/MagicCobblestoneGenerator/#placeholders)

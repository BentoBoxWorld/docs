# Glossary

New to BentoBox? This page explains the key terms used throughout the documentation.

---

## Addon
A file (`.jar`) that extends BentoBox with new features. Addons go in `plugins/BentoBox/addons/` — **not** in your server's `plugins/` folder. There are two types: [game mode addons](#game-mode) and [feature addons](#feature-addon). See [Addons](BentoBox/About/Addons.md).

## Admin Command
Each game mode has an admin-only command for managing islands, settings, and players. For BSkyBlock it is `/bsb`, for AcidIsland it is `/acid admin`, etc. The exact command is listed in each game mode's documentation.

## Blueprint
A saved template of a built island used when a player creates a new island. BentoBox comes with default blueprints but admins can create their own in-game. Blueprints are stored in `plugins/BentoBox/blueprints/`. See [Blueprints](BentoBox/About/BlueprintsSummary.md).

## Blueprint Bundle
A named set of blueprints (one each for the Overworld, Nether, and End) grouped together. When a player creates a new island, they may be presented with a choice of bundles. Each bundle can have its own icon, description, and permission requirement.

## Coop
A temporary island rank given to players who are not full team members. A coop player's access expires when the team member who granted it logs off. See [Teams](BentoBox/About/Teams.md).

## Feature Addon
An addon that adds extra functionality (challenges, fly, warps, etc.) on top of a game mode. Feature addons are optional. See [Addons](BentoBox/About/Addons.md).

## Flag
A single protection or settings toggle that controls what is or isn't allowed on an island or in the game world. Flags are managed through the in-game settings GUI. Examples: whether visitors can break blocks, whether creepers can explode, whether leaf blocks decay. See [Protection](BentoBox/About/Protections.md).

## Game Mode
An addon that defines the type of game world players play in — the world type, how islands are generated, and the overall challenge. Examples: BSkyBlock, AcidIsland, AOneBlock. You must install at least one game mode for BentoBox to do anything. See [Game Modes](BentoBox/About/GameModes.md).

## Island
The protected area of the game world that belongs to a player or team. Each player gets one island per game mode. Islands are created automatically when a player runs the main command for the first time. See [Island Management](BentoBox/About/IslandManagement.md).

## Island Distance
The gap between the centres of adjacent islands in the world grid. Set once in the game mode's `config.yml` and **cannot be changed** once islands exist. The protection range can never exceed half this value. See the [FAQ](FAQ.md#how-do-i-change-the-island-distance).

## Locale
A language file that contains all the in-game text for BentoBox or an addon in a specific language. Locale files live in `plugins/BentoBox/locales/`. See [Multilingual Support](BentoBox/About/Multilingual.md).

## Owner
The player who created an island or has had ownership transferred to them. There is always exactly one owner per island. Owners have full control over their island settings and team.

## Placeholder
A short code like `%bskyblock_island_name%` that other plugins can use to display BentoBox data — for example in chat, scoreboards, or holograms. BentoBox uses PlaceholderAPI. See [Placeholders](BentoBox/Placeholders.md).

## Player Command
The main command players use to interact with a game mode. For BSkyBlock it is `/island` (or `/is`), for AOneBlock it is `/oneblock` (or `/ob`), etc. The exact command is listed in each game mode's documentation.

## Protection Range
The radius of the area around an island centre that is protected. No other player can build, break, or interact in this area without permission. Always smaller than or equal to half the [island distance](#island-distance). Can be expanded by admin command or player permission.

## Rank
A trust level assigned to players in relation to a specific island. From lowest to highest: **Banned**, **Visitor**, **Coop**, **Trusted**, **Member**, **Sub-Owner**, **Owner**. Ranks control what actions a player can take on an island. See [Teams](BentoBox/About/Teams.md).

## Reset
When a player deletes their own island and starts fresh with a new one. The number of times a player can reset is configurable. See [Island Management](BentoBox/About/IslandManagement.md#resetting-an-island).

## Sub-Owner
An island rank below Owner but above Member. Sub-owners have almost all the same permissions as the owner. Multiple sub-owners can exist on one island.

## Trusted
A permanent guest rank for players who are not full team members. Unlike [coop](#coop), trusted status does not expire when the granting player logs off. See [Teams](BentoBox/About/Teams.md).

## Visitor
The default rank for any player who is on an island they do not own or belong to. What visitors can do is controlled by the island owner through the settings GUI.

## World Settings
Protection and behaviour settings that apply to the entire game mode world, not just individual islands. Only admins can change these. Accessed via `/[admin_command] settings`. See [Protection](BentoBox/About/Protections.md).

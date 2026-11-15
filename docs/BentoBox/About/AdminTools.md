# Admin Tools

BentoBox has in-game tools for looking up islands, finding out why something is blocked, and managing the server, so you rarely need to edit data files by hand. This page covers the tools you'll use most; every command is in the [Commands reference](../Commands.md).

!!! info "Commands on this page"
    Game mode admin commands are shown as `/bsbadmin` (BSkyBlock). Use your game mode's admin command instead, for example `/oba` (AOneBlock), `/acid` (AcidIsland) or `/cbadmin` (CaveBlock). They're operator-only by default; see [Permissions & VIP Perks](../Permissions-Guide.md#staff-permissions) for giving them to staff.

## Look up an island

| I want to… | Command |
|---|---|
| See everything about a player's island: owner, team, range, homes, resets, deaths, bans | `/bsbadmin info <player>` |
| See the island I'm standing on | `/bsbadmin info` |
| See one of several islands a player has | `/bsbadmin info <player> <island name>` |
| Go to a player's island (or its Nether/End island) | `/bsbadmin tp <player>`, `tpnether`, `tpend` |
| Send a player to someone else's island | `/bsbadmin tpuser <player> <island owner>` |
| See a player's rank on an island | `/bsbadmin getrank <player>` |
| Show the island's protected area in game | `/bsbadmin range display` |

## Find out why something is blocked

When a player says they can't do something (or can do something they shouldn't), turn on the **why** tool:

```
/bsbadmin why <player>
```

Then ask the player to try again. The console logs every protection check for that player: what they tried, where, whether it was allowed, and which flag or rank decided it. Run the same command again to turn it off. The player must be online.

Most problems turn out to be a flag set for a different rank than expected, or the player being on someone else's island. See [Protection, Flags & Ranks](../Island-Protection,-Flags-&-Ranks.md).

## Act as a normal player

Operators and moderators with bypass permissions ignore island protection, which makes testing confusing. **`/bsbadmin switch`** turns your bypass off so you're protected against like a normal player; run it again to turn it back on. Operator status itself isn't affected. See [Bypass the protection](../Island-Protection,-Flags-&-Ranks.md#bypass-the-protection).

## Fix an island

| I want to… | Command | More |
|---|---|---|
| Change a player's rank on an island | `/bsbadmin setrank <player> <rank>` | [Teams & Ranks](Teams.md) |
| Add or remove team members, change the owner | `/bsbadmin team add`, `team kick`, `team setowner` | [Teams & Ranks](Teams.md#common-admin-tasks) |
| Change an island's settings | `/bsbadmin settings <player>` | [Protection, Flags & Ranks](../Island-Protection,-Flags-&-Ranks.md) |
| Make an island bigger or smaller | `/bsbadmin range set <player> <range>` | [Islands](IslandManagement.md#island-size-protection-range) |
| Reset a player's home, or delete their homes | `/bsbadmin resethome <player>`, `deletehomes <player>` | [Islands](IslandManagement.md#homes) |
| Clear an island's name | stand on it, `/bsbadmin resetname` | [Islands](IslandManagement.md#island-names) |
| Give a player resets back | `/bsbadmin resets reset <player>` | [Islands](IslandManagement.md#resetting-islands) |
| Delete, undelete or reassign an island | `/bsbadmin delete`, `undelete`, `register` | [Islands](IslandManagement.md#deleting-islands) |
| Move the centre of an island's protected area | stand there, `/bsbadmin setprotectionlocation` | |
| Reset every island's settings to the config defaults | `/bsbadmin resetflags` | |
| Make an island the game mode's spawn | stand on it, `/bsbadmin setspawn` | |

## World settings

**`/bsbadmin settings`** opens the admin settings menu for the game mode's world: world settings (such as creeper damage or visitor keep-inventory), the protection rules outside islands, the defaults for new islands, and which island settings players can see. See [Admin Settings Panel](../Island-Protection,-Flags-&-Ranks.md#admin-settings-panel).

## Managing BentoBox

| Command | What it does |
|---|---|
| `/bentobox version` | BentoBox, game mode and addon versions, server version and database. **Include this when you ask for help or report a bug.** |
| `/bentobox manage` | The Management Panel: tabs for your game modes, addons and hooks (other plugins BentoBox works with), plus the addon catalog |
| `/bentobox catalog` | Browse the game modes and addons you can download |
| `/bentobox reload` | Reload BentoBox's and the addons' settings, language files and menu templates |
| `/bsbadmin reload` | Reload one game mode's settings |
| `/bentobox perms` | Print every command permission and its default (console) |
| `/bentobox locale` | Check the language files for missing translations |
| `/bentobox placeholders` | Browse placeholders and turn them on or off. See [Placeholders](../Placeholders.md) |

Some settings, like world generation and `distance-between-islands`, only take effect after a full restart.

## Database

BentoBox stores islands and players in a database set in BentoBox's `config.yml`. The default is **JSON** files in the BentoBox folder, which needs no setup. For larger servers, or several servers sharing data, you can use **MySQL** (5.7+), **MariaDB** (10.2.3+), **PostgreSQL** (9.4+), **SQLite** (3.28+) or **MongoDB** (3.6+).

To change database type without losing data, see [Changing Database](../Database-transition.md). Always back up first.

## See also

- [Commands reference](../Commands.md)
- [Permissions & VIP Perks](../Permissions-Guide.md)
- [BentoBox Release Notes](../Release-Notes.md)

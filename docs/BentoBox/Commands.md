# Commands

Every command in BentoBox and its game modes, generated from the BentoBox source. For how to use them, see the [Admin Guides](About/Teams.md) and the [Player Guide](Player-Guide.md).

## How game mode commands are named

Each game mode has its own player and admin command. The tables below write them as `/[player_command]` and `/[admin_command]`. Permissions start with the game mode's prefix, written `[gamemode].`:

| Game mode | `[player_command]` | `[admin_command]` | `[gamemode]` |
|---|---|---|---|
| BSkyBlock | `/island`, `/is` | `/bsbadmin`, `/bsb` | `bskyblock` |
| AOneBlock | `/ob`, `/oneblock` | `/oba`, `/obadmin` | `aoneblock` |
| AcidIsland | `/ai` | `/acid` | `acidisland` |
| CaveBlock | `/cave`, `/cb` | `/cbadmin`, `/cba` | `caveblock` |

Other game modes list theirs on their own page. All labels can be changed in the game mode's `config.yml`.

Typing a command with no subcommand runs a default: for players, `/[player_command]` creates an island or teleports home (see [Islands](About/IslandManagement.md#creating-islands)); `/[admin_command]` and `help` list the commands the player can use.

Addons add their own subcommands to these, for example `/island level` or `/island challenges`. See each [addon's page](../addons/Bank/index.md).

## BentoBox commands

The `/bentobox` command (alias `/bbox`) manages BentoBox itself.

| Command | Description | Permission |
|---|---|---|
| `/bentobox about` | Copyright and license information | `bentobox.about` |
| `/bentobox version` | BentoBox, addon and server versions. Include this when you ask for help | `bentobox.version` |
| `/bentobox reload` | Reload BentoBox and all addons, settings, locales and menu templates | `bentobox.admin.reload` |
| `/bentobox reload locales` | Reload only the locale files | `bentobox.admin.reload` |
| `/bentobox manage` | Open the Management Panel | `bentobox.admin.manage` |
| `/bentobox catalog` | Open the catalog of game modes and addons | `bentobox.admin.catalog` |
| `/bentobox locale` | Check the locale files for missing translations | `bentobox.admin.locale` |
| `/bentobox migrate` | Move data from one database type to another. See [Changing Database](Database-transition.md) | `bentobox.admin.migrate` |
| `/bentobox perms` | Print every command permission and its default (console only) | `bentobox.admin.perms` |
| `/bentobox rank [list \| add \| remove] [rank reference] [rank value]` | List, add or remove island ranks. See [Teams & Ranks](About/Teams.md#custom-ranks) | `bentobox.admin.rank` |
| `/bentobox placeholders` | Open the placeholder browser | `bentobox.admin.placeholders` |
| `/bentobox dump-placeholders` | Write every registered placeholder to a markdown file | `bentobox.admin.dump-placeholders` |

## Player commands

| Command | Description | Permission |
|---|---|---|
| `/[player_command] ban <player>` | Ban a player from your island | `[gamemode].island.ban` |
| `/[player_command] banlist` | List banned players | `[gamemode].island.ban` |
| `/[player_command] create <blueprint>` | Create an island, using optional blueprint (requires permission) | `[gamemode].island.create` |
| `/[player_command] deletehome [home name]` | Delete a home location | `[gamemode].island.deletehome` |
| `/[player_command] expel <player>` | Expel a player from your island | `[gamemode].island.expel` |
| `/[player_command] go [home name]` | Teleport you to your island | `[gamemode].island.home` |
| `/[player_command] homes` | List your homes | `[gamemode].island.homes` |
| `/[player_command] info <player>` | Display info about your island or the player's island | `[gamemode].island.info` |
| `/[player_command] language [language]` | Select language | `[gamemode].island.language` |
| `/[player_command] lock` | Lock or unlock your island | `[gamemode].island.lock` |
| `/[player_command] near` | Show the name of neighboring islands around you | `[gamemode].island.near` |
| `/[player_command] renamehome [home name]` | Rename a home location | `[gamemode].island.renamehome` |
| `/[player_command] reset <blueprint>` | Restart your island and remove the old one | `[gamemode].island.reset` |
| `/[player_command] resetname` | Reset your island name | `[gamemode].island.name` |
| `/[player_command] sethome` | Set your home teleport point | `[gamemode].island.sethome` |
| `/[player_command] setname <name>` | Set a name for your island | `[gamemode].island.name` |
| `/[player_command] settings` | Display island settings | `[gamemode].island.settings` |
| `/[player_command] spawn` | Teleport you to the spawn | `[gamemode].island.spawn` |
| `/[player_command] team` | Manage your team | `[gamemode].island.team` |
| `/[player_command] team accept` | Accept an invitation | `[gamemode].island.team.accept` |
| `/[player_command] team coop <player>` | Make a player coop rank on your island | `[gamemode].island.team.coop` |
| `/[player_command] team demote <player>` | Move a player down one rank (never below Member) | `[gamemode].island.team.promote` |
| `/[player_command] team invite <player>` | Invite a player to join your island | `[gamemode].island.team.invite` |
| `/[player_command] team kick <player>` | Remove a member from your island | `[gamemode].island.team.kick` |
| `/[player_command] team leave` | Leave your island | `[gamemode].island.team.leave` |
| `/[player_command] team promote <player>` | Promote a player on your island up a rank | `[gamemode].island.team.promote` |
| `/[player_command] team reject` | Reject an invitation | `[gamemode].island.team.reject` |
| `/[player_command] team setowner <player>` | Transfer your island ownership to a member | `[gamemode].island.team.setowner` |
| `/[player_command] team trust <player>` | Give a player trusted rank on your island | `[gamemode].island.team.trust` |
| `/[player_command] team uncoop <player>` | Remove a coop rank from player | `[gamemode].island.team.coop` |
| `/[player_command] team uninvite <player>` | Withdraw a pending team, trust or coop invite (BentoBox 3.24.0+) | `[gamemode].island.team.invite` |
| `/[player_command] team untrust <player>` | Remove trusted player rank from player | `[gamemode].island.team.trust` |
| `/[player_command] unban <player>` | Unban a player from your island | `[gamemode].island.ban` |

## Admin commands

Admin commands are for operators by default. Commands with a `mod.` permission are meant for moderators who aren't full admins; see [Permissions & VIP Perks](Permissions-Guide.md#staff-permissions).

| Command | Description | Permission |
|---|---|---|
| `/[admin_command] blueprint <load/copy/paste/pos1/pos2/save>` | Manipulate blueprints | `[gamemode].admin.blueprint` |
| `/[admin_command] blueprint copy [air] [biome] [nowater]` | Copy the clipboard set by pos1 and pos2 and optionally the air, biome, and water blocks | `[gamemode].admin.blueprint.copy` |
| `/[admin_command] blueprint delete <name>` | Delete the blueprint | `[gamemode].admin.blueprint.delete` |
| `/[admin_command] blueprint list` | List available blueprints | `[gamemode].admin.blueprint.list` |
| `/[admin_command] blueprint load <name>` | Load blueprint into the clipboard | `[gamemode].admin.blueprint.load` |
| `/[admin_command] blueprint origin` | Set the blueprint's origin to your position | `[gamemode].admin.blueprint.origin` |
| `/[admin_command] blueprint paste` | Paste the clipboard to your location | `[gamemode].admin.blueprint.paste` |
| `/[admin_command] blueprint pos1` | Set 1st corner of cuboid clipboard | `[gamemode].admin.blueprint.pos1` |
| `/[admin_command] blueprint pos2` | Set 2nd corner of cuboid clipboard | `[gamemode].admin.blueprint.pos2` |
| `/[admin_command] blueprint rename <blueprint name> <new name>` | Rename a blueprint | `[gamemode].admin.blueprint.rename` |
| `/[admin_command] blueprint save <blueprint name>` | Save the copied clipboard | `[gamemode].admin.blueprint.save` |
| `/[admin_command] blueprint sink` | Set this blueprint to sink to the ocean floor when pasted | `[gamemode].admin.blueprint.sink` |
| `/[admin_command] deaths` | Edit deaths of players | `[gamemode].admin.deaths` |
| `/[admin_command] deaths add <player> <deaths>` | Adds deaths to the player | `[gamemode].admin.deaths.add` |
| `/[admin_command] deaths remove <player> <deaths>` | Removes deaths to the player | `[gamemode].admin.deaths.remove` |
| `/[admin_command] deaths reset <player>` | Resets deaths of the player | `[gamemode].admin.deaths.reset` |
| `/[admin_command] deaths set <player> <deaths>` | Sets deaths of the player | `[gamemode].admin.deaths.set` |
| `/[admin_command] delete [player]` | Deletes a player's island, or the island you are standing on if no player is given | `[gamemode].admin.delete` |
| `/[admin_command] deletehomes <player>` | Deletes all named homes from an island | `[gamemode].mod.deletehomes` |
| `/[admin_command] getrank <player> [island owner]` | Get a player's rank on their island or the island of the owner | `[gamemode].admin.getrank` |
| `/[admin_command] info <player> [island name]` | Get info on where you are or player's island | `[gamemode].mod.info` |
| `/[admin_command] maxhomes <number / player> <number> [island name]` | Change the number of homes allowed on this island or player's island | `[gamemode].mod.maxhomes` |
| `/[admin_command] purge [days]` | Delete region files for islands untouched for more than [days] days (frees disk) | `[gamemode].admin.purge` |
| `/[admin_command] purge age-regions [days]` | Debug/test: rewrite region file timestamps so they become purgable | `[gamemode].admin.purge.age-regions` |
| `/[admin_command] purge deleted` | Purge region files for any island already flagged as deleted | `[gamemode].admin.purge.deleted` |
| `/[admin_command] purge protect` | Toggle island purge protection | `[gamemode].admin.purge.protect` |
| `/[admin_command] purge unowned` | Flag unowned islands as deletable so they can be reaped | `[gamemode].admin.purge.unowned` |
| `/[admin_command] range` | Admin island range command | `[gamemode].admin.range` |
| `/[admin_command] range add <player> <range> [island location]` | Increases the island protected range | `[gamemode].admin.range.add` |
| `/[admin_command] range display` | Show/hide island range indicators | `[gamemode].admin.range.display` |
| `/[admin_command] range purgebonus <id>` | Removes a bonus range id from every island (e.g. after removing the addon that added it) | `[gamemode].admin.range.purgebonus` |
| `/[admin_command] range remove <player> <range> [island location]` | Decreases the island protected range | `[gamemode].admin.range.remove` |
| `/[admin_command] range removebonus <player> [id]` | Removes bonus ranges from the island (all, or one by id) | `[gamemode].admin.range.removebonus` |
| `/[admin_command] range reset <player>` | Resets the island protected range to the world default | `[gamemode].admin.range.reset` |
| `/[admin_command] range set <player> <range> [island location]` | Sets the island protected range | `[gamemode].admin.range.set` |
| `/[admin_command] register <player>` | Register player to unowned island you are on | `[gamemode].admin.register` |
| `/[admin_command] reload` | Reload | `[gamemode].admin.reload` |
| `/[admin_command] resetflags [flag]` | Reset all islands to default flag settings in config.yml | `[gamemode].admin.resetflags` |
| `/[admin_command] resethome <player> [island name]` | Reset the player's home to default | `[gamemode].mod.resethome` |
| `/[admin_command] resetname` | Reset player island name | `[gamemode].mod.resetname` |
| `/[admin_command] resets` | Edit player reset values | `[gamemode].admin.resets` |
| `/[admin_command] resets add <player> <resets>` | Adds this player's island reset count | `[gamemode].admin.resets.add` |
| `/[admin_command] resets remove <player> <resets>` | Reduces the player's island reset count | `[gamemode].admin.resets.remove` |
| `/[admin_command] resets reset <player>` | Sets the player's island reset count to 0 | `[gamemode].admin.resets.remove` |
| `/[admin_command] resets set <player> <resets>` | Sets how many times this player has reset his island | `[gamemode].admin.resets.set` |
| `/[admin_command] setprotectionlocation [x y z coords]` | Set current location or [x y z] as center of island's protection area | `[gamemode].admin.setprotectionlocation` |
| `/[admin_command] setrank <player> <rank> [island owner \| x,y,z]` | Promote or demote a player to a rank on their team island, or on the island named by its owner or x,y,z centre | `[gamemode].admin.setrank` |
| `/[admin_command] setspawn` | Set an island as spawn for this gamemode | `[gamemode].admin.setspawn` |
| `/[admin_command] setspawnpoint` | Set current location as spawn point for this island | `[gamemode].admin.setspawnpoint` |
| `/[admin_command] settings [player]/[world flag]/spawn-island [flag/active/disable] [rank/active/disable]` | Open settings GUI or set settings | `[gamemode].admin.settings` |
| `/[admin_command] switch` | Switch on/off protection bypass | `[gamemode].mod.switch` |
| `/[admin_command] team` | Manage teams | `[gamemode].mod.team` |
| `/[admin_command] team add <owner> <player>` | Add player to owner's team | `[gamemode].mod.team.add` |
| `/[admin_command] team disband <owner>` | Disband owner's team | `[gamemode].mod.team.disband` |
| `/[admin_command] team disbandall` | Strip every member and sub-owner from every island in this world | `[gamemode].mod.team.disbandall` |
| `/[admin_command] team kick <team player> [x,y,z]` | Kick a player from a team | `[gamemode].mod.team.kick` |
| `/[admin_command] team maxsize <player> <size>` | Set the max team size for a player's island (use 0 to reset to world default) | `[gamemode].mod.team.maxsize` |
| `/[admin_command] team setowner <player> [island owner]` | Transfers island ownership to the player. Name the current island owner to run it from the console | `[gamemode].mod.team.setowner` |
| `/[admin_command] tp <player> [player's island]` | Teleport to a player's island | `[gamemode].admin.tp` |
| `/[admin_command] tpend <player> [player's island]` | Teleport to a player's island in the End | `[gamemode].admin.tp` |
| `/[admin_command] tpnether <player> [player's island]` | Teleport to a player's island in the Nether | `[gamemode].admin.tp` |
| `/[admin_command] tpuser <teleporting player> <island's player> [player's island]` | Teleport a player to another player's island | `[gamemode].admin.tpuser` |
| `/[admin_command] tpuserend <teleporting player> <island's player> [player's island]` | Teleport a player to another player's island in the End | `[gamemode].admin.tpuser` |
| `/[admin_command] tpusernether <teleporting player> <island's player> [player's island]` | Teleport a player to another player's island in the Nether | `[gamemode].admin.tpuser` |
| `/[admin_command] undelete` | Remove the pending deletion status from the unowned island you are on | `[gamemode].admin.undelete` |
| `/[admin_command] unregister <owner> [x,y,z]` | Unregister owner from island, but keep island blocks | `[gamemode].admin.unregister` |
| `/[admin_command] version` | Display BentoBox and addons versions | `[gamemode].admin.version` |
| `/[admin_command] why <player>` | Toggle console protection debug reporting | `[gamemode].admin.why` |

`/[admin_command] add`, `disband`, `kick` and `setowner` also work without `team` (for example `/bsbadmin kick <player>`), for compatibility with older versions.

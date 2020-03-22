This is a planning Wiki (for now). It lists the various plans and ideas around BSkyBlock.

# Concept
BSkyblock is a Skyblock plugin for Bukkit servers. It will aim to provide the same overall functionality as ASkyBlock, its predecessor. It also has the ability to implement the AcidIsland mode.

BSkyBlock will have a core set of functionality with optional additions made available for server admins to select to add to its functionality. These will be called "add-ons" and will function the same as additional plugins, except they will be located in a dedicated folder.

# Core functionality
BSkyBlock Core will offer:

- World generation (Island world, Island Nether, Island End; Standard Nether and End; no Nether or End options)
- Island spawn creation and management
- Command handling
- Island protection (includes ban, lock and changes to protection sizes)
- Island settings GUI
- Creation, deletion and reseting of of islands (pasting schematics, etc.)
- Storage of island and player data in a database and backups (YAML or MySQL)
- Plugin configuration (config.yml management, and unlike ASkyBlock, most of the changes will automatically be applied)
- Localization system (languages)
- Firing events, e.g. new island event
- Management of island teams, coop and trusting (sizes, adds, removals, changes, permissions, etc.) 
- Anti-abuse - (cool downs, etc.) 
- Island cleanup (purging)
- Chat placeholders
- GUI panels
- Add-ons / Extended API

# Add-on's
This functionality will be put into add-ons and will not be in the core plugin:

- Island levels and Top Ten - /island level, /island topten
- Challenges - /challenge - Shows the GUI for challenges available to the player.
- Biomes - /island biomes - open the biomes GUI
- Minishop - /island ms or minishop - Opens the mini-shop where players can buy stuff. Disabled if there is no economy.
- Team chat - /island teamchat - enables teams to chat among themselves without bothering others. Must be enabled in config.yml and player must be in a team to see the command. Chats can be spied on by admins.
- Magic cobble genenerators
- Temporary island permissions
- Island Fly
- Running commands when events happen (start commands, reset commands, etc.)
- Invincible visitors
- AcidIsland game mode (acid burn, acid rain, procedural creation of starter island)
- Entity Limiting (spawn limiting, breeding limits, etc)
- Island stats for admins
- Lag reduction options, (e.g. red stone disabling)
- Welcome warp signs, /is warps, /is warp <name>
- Island visual borders
- Island / Team Chats, /is teamchat, /is islandchat

## Core User Commands
### The /island, /is or /bsb command

/island - generates a new island, opens the GUI or teleports the player to their island, home location or the team island

The command /island by itself can perform the following
- Generates default island if the player does not have one
- Shows the new island selection GUI if the player does not have an island
- Shows Control Panel GUI
- Teleports player to their island home location

- help - shows help text
- go - teleport to your island
- go <number> - teleport to a numbered island home (use /island sethome <number> to set)
- cp - shows a GUI with useful commands so players do not have to type
- expel - Removes a visitor from your island
- reset - restarts an island. There is a cool down timer and a max limit on this so that players do not abuse it
- lang - allows player to chose their UI language
- lock - locks an island so none can enter or teleport into
- settings - lists the game settings in a read-only panel
- sethome - sets your island home
- sethome <number> - sets a numbered home point, up to the max the server allows
- spawn - teleport to the island-world spawn, if it exists (set via admin command setspawn)

### Team-related Commands
- invite - Invite a player to join your team. You can only invite one person at a time. Only the leader can invite.
- accept or reject - Accepts or rejects an invite. If a player has an island already and accepts, the island will be deleted.
- invites - Lists any invites you have pending
- team - lists info on the team
- leave - leave the team. You will need to type it twice to leave.
- kick or remove <name> - only available for the team leader - removes a team member. They are not physically moved. They just are no longer on the team.
- makeleader <name> - Transfers ownership to a team member. Can only be issued by the leader.

### Trust Commands - enables players to help others without having to join their team
- trust <player> - Gives a player full access to your island. Notifies other team members and the leader when this happens. Use it wisely.
- untrust <player> - Removes trust from player.
- trust - lists players you trust.
- expel <player> - Removes trust status. Also ejects player from your island.

## Admin Commands
Access via /bsadmin command:

### Console And Game Available Commands
- reload - reloads all the configuration files. Use this if you have edited the .yml files.
- delete <player> - deletes a player's island. 100% permanent, no undo - *warning*
- purge [TimeInDays] - *warning* very dangerous command. Will remove all old/unused islands where the player has not logged in for X number of days. Strongly recommend you back up the world first and run when no players are online.
- info <player> - Displays info on a player and their island
- unregister <player> - Removes a player from an island without deleting the island blocks
- clearreset <player> - Clears the reset limit for a player
- clearresetall - Resets every player in the game to the value in config.yml. Use if you change the config.yml value.
- setrange <leader> <range> - Sets the protection range of the leader's island up to a maximum of the island distance.

### Team Editing Commands
- team info <player> - lists info on the player's team
- team add <player1> <player2> - adds player1 to player2's team. If player1 has an island, the island will become unowned.
- team kick <player> - removes player from the team.
- team makeleader <player> - makes the player the team leader. The old leader will become a team member.
- team delete <player> - kicks all the players from the team player is in. The leader remains as the island owner.

Note that you do not have to specify the team leader in these commands. It is inferred.

### In-game admin commands
- register <player> - Registers the closest island to <player>. To use, go to an island and execute the command.
- setspawn - Sets the spawn point for the world. The spawn area has special rules and protections.
- tp <player>, tpnether <player>, tpend <player> - Teleports to a player's island
- unregister - Removes any player registration for the island you are standing on.
- deleteisland confirm - Deletes the island you are standing on. Note that you must type the full command.
- info - Provides info on the island that you are standing on.
- setrange - Sets the range of the island you are on. If the area is spawn, the range can be greater than the island range.
- reserve <player> - Reserves the spot you are in for this player's next island. Lasts until server restart.

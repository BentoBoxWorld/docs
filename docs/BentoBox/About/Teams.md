# Teams

BentoBox manages teams for game modes. Teams enable players to group together on one island. Teams have one owner, or leader, and at least one team member. 

## Team GUI

When players issue the `team` command it brings up a GUI that enables them to see their team, invite other players, search for players, and manage the team. The commands can also be used, but players often like the GUI.

## Team commands
This is a list of team commands available to players. The command is used after the main player command, for example `/island team` for BSkyBlock. 
<table width="100%" align="center">
<tr>
<td align='left'><b>Command</b></td>
<td align='left'><b>Description</b></td>
<td align='left'><b>Permission</b></td>
</tr>
<tr>
<td align='left'><b> team</b></td>
<td align='left'>manage your team</td>
<td align='left'>[gamemode].island.team</td>
</tr>
<tr>
<td align='left'><b> team accept</b></td>
<td align='left'>accept an invitation</td>
<td align='left'>[gamemode].island.team</td>
</tr>
<tr>
<td align='left'><b> team coop <player></b></td>
<td align='left'>make a player coop rank on your island</td>
<td align='left'>[gamemode].island.team.coop</td>
</tr>
<tr>
<td align='left'><b> team demote <player></b></td>
<td align='left'>demote a player on your island down a rank</td>
<td align='left'>[gamemode].island.team</td>
</tr>
<tr>
<td align='left'><b> team leave</b></td>
<td align='left'>leave your island</td>
<td align='left'>[gamemode].island.team</td>
</tr>
<tr>
<td align='left'><b> team invite</b></td>
<td align='left'>invite a player to join your island</td>
<td align='left'>[gamemode].island.team</td>
</tr>
<tr>
<td align='left'><b> team kick <player></b></td>
<td align='left'>remove a member from your island</td>
<td align='left'>[gamemode].island.expel</td>
</tr>
<tr>
<td align='left'><b> team promote <player></b></td>
<td align='left'>promote a player on your island up a rank</td>
<td align='left'>[gamemode].island.team</td>
</tr>
<tr>
<td align='left'><b> team reject</b></td>
<td align='left'>reject an invitation</td>
<td align='left'>[gamemode].island.team</td>
</tr>
<tr>
<td align='left'><b> team setowner <player></b></td>
<td align='left'>transfer your island ownership to a member</td>
<td align='left'>[gamemode].island.team</td>
</tr>
<tr>
<td align='left'><b> team trust <player></b></td>
<td align='left'>give a player trusted rank on your island</td>
<td align='left'>[gamemode].island.team.trust</td>
</tr>
</table>

## The Main Team Command
The main team command is `team`. To issue this command you must have an island. If run by itself, it will provide the following information to the player:

 - If the player is the owner, it will tell them how many players they can invite onto their team.
 - It will show all the members of the team. This includes info on the player's ranks, online/offline status, and when they were last seen online. 

## Team Sizes
Teams can be any size and the maximum size can be set globally on a gamemode-basis or determine by a numbered permission given to the team owner. The default max team size is 4. The maximum number of coop and trusted members is also set to 4.

### Team Size Permissions

* Team Size: The permission for team size is `[gamemode].team.maxsize.X` where X is a number.
* Coop Size: `[gamemode].team.coopsize.X` where X is a number
* Trust Size: `[gamemode].team.trustsize.X` where X is a number

## Team Member Ranks
BentoBox has the following team ranks built-in:

* Owner - this is the owner of the island. There can be only one owner.
* Sub-Owner - this is a member rank that has almost the same permissions as the owner. There can be multiple sub-owners.
* Member - this is the default member rank.

### Non-team member ranks
Islands have other ranks that are related to teams but are not team members:

* Trusted - this is a non-team member who has permanent permissions on the island, i.e., they have them until they are untrusted by a team member.
* Coop - this is a non-team member who has temporary permissions on the island and these permissions will cease if the team member who gave them logs off, or if they are uncoop-ed.
* Visitor - this is the default rank for any players who visit the island
* Banned - these players have been banned by a team member and cannot enter the island

### Configurable Rank Commands
The owner of the island is able to grant access to team management commands to lower ranks via the Command Ranks menu in the in-game settings menu. This enables the owner to allow other members to invite other members, for example. 

### Promotion and Demotion
Team members can be promoted or demoted by the island owner or an island member who has the rank required to use these commands.

A player cannot demote or promote themselves.

Currently, the only promotion or demotion possible is between the ranks of Member and Sub-Owner. In the future, additional ranks or custom ranks may be possible.

## Joining Teams
### Inviting
Players can be invited to join a team using the `team invite` command. To invite players to join a team, the inviter must be an island owner or have sufficient rank to use the command (see [Configurable Rank Command](#configurable-rank-commands)). Players are invited by name and must be online. Invites can only be made to players who are not already on a team. If a player wants to switch teams, they must leave their current team before they can be invited.
Invited players cannot be invited again until they reject the invite.
Invited players can only have **one** active invite at a time. This includes team, coop and trusted invites. If a player receives a new valid invite while another is pending, the old one is replaced by the new invite.
If the island team size is already at the maximum, the invite command will tell the user that the island is full.

#### Cooldown
Invites can be abused by players, so BentoBox prevents the same player being invited to an island in the cool down period. The cool down is imposed on the island as a whole, so it is not possible for various members of the island to spam another player with invites. The default cool down times for the various invites are:

* Team member - 60 minutes
* Coop invite - 5 minutes
* Trusted invite - 5 minutes
See the game mode's `config.yml` to change.

### Checking invites
A player can check who has invited them by using the `invite` command with no arguments. This will show any current team, coop or trusted invites. 

### Accepting an invite
A player accepts an invite by issuing the `team invite accept` command. 

#### Confirmation
The admin can decide whether confirmation is required or not for this command. The default is to require it for team membership but not require it for coop or trusted status. This is because team members lose their island if they join another one. If confirmation is required, the player will receive a warning that if they have an island then it will be lost. Once the player accepts the invite a second time, they will become a team member and teleport to the team island. 

There is a small chance that the inviter loses the rank required to invite players before the player accepts the invite. In this case, the acceptance will not process and the user will be told that the invite is no longer valid.

!!! tip "Confirmation time"
    The default time players have to confirm a command is 10 seconds. If your players need more time, increase this value in BentoBox's `config.yml`. Players can also press the up arrow to recall the previous command rather than retyping it.

#### What happens when a player accepts

When a player accepts a team invite, BentoBox automatically:

- Removes them as owner of their previous island (if they had one) and begins deleting it
- Clears the player based on the game mode's config settings (ender chest, inventory, money, health, hunger, experience)
- Adds them as a member of the new island and teleports them to its home point

!!! warning "Inventory cleanup"
    By default, BentoBox does **not** clear a player's inventory when they join a team, to avoid accidents during initial setup. However, **admins should enable this in the game mode's `config.yml`** to prevent players from carrying items from their old island to the new one. Check the config for the `on-join` cleanup settings.

### Rejecting an invite
A player rejects an invite by issuing the `team invite reject` command.

A player must have a valid invite to reject otherwise they just receive an error. Once rejected, the inviter is notified.

## Changing Team Ownership

Owners can make another team member an owner using the `team setowner` command with the new owner's name as the parameter. Once ownership transfers, the previous owner becomes a Sub-Owner.

Owners must select a new owner before they can leave a team.

## Kicking A Player
Sometimes a team member needs to be forced out of a team. This is done using the `team kick` command. The owner can always kick players and the owner can allow lower-ranked team members to kick too via the Command Ranks menu in island settings. The team member does not have to be online to be kicked.

The command by default requires confirmation. This can be configured in BentoBox's `config.yml`.

When a player is kicked, BentoBox removes them from the island, runs any configured on-leave commands, cleans up their inventory/ender chest/money based on the game mode config, and notifies both parties. An invite cooldown is applied to prevent the exploit of repeatedly kicking and re-inviting players.

## Leaving a Team
A player can voluntarily leave a team using the `team leave` command. The command requires confirmation by default, but this can be switched off in the BentoBox's config. When leaving a team voluntarily, a player may use up one of their allowed island resets. This is set in the GameMode's config and the default is not to lose a reset. If the player will lose a reset, then they will be warned about it if the leave command has a confirmation requirements. **Note:** is it possible for a player to use up all their resets by leaving a team and therefore not be able to make a new island of their own. That is something admins will have to consider.

When a player leaves the island, the sequence and process is the same as when a player is kicked, except that the player may lose a reset.


## Trusting and Cooping Other Players
Sometimes players want to help out on other islands without having to join the team as a full member. This can be done by trusting a player or cooping an online player:

 - `team trust <player>`: the player becomes a permanent member of the island at a rank below Member
 - `team coop <player>`: the player becomes a temporary member of the island at a rank below Trusted

Island owners can trust or coops players and also enable lower-ranked players to use these commands via the Command Ranks page in the island settings.

These commands actually send an invite to the player that they can accept or reject, just like the team join command. If the invite is rejected, it will not be possible to send another invite for a cool down period, which is set to 5 minutes by default. This protects players from invite-spam.

If a player already has an invite pending from someone else or for a different rank, then that invite will be replaced by this one.

Once accepted, the player will receive the rank given for the new island. The inviter is notified of the acceptance.

Coop players hold their rank until the player who invited them logs out, or until the server shuts down, whichever occurs first.

### Untrusting or uncooping players
Island owners, or players with a high enough rank, can issue the `team untrust` or `team uncoop` commands to remove players from the island with these ranks. The removed player reverts to Visitor status.


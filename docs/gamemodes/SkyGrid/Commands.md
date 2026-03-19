# SkyGrid Commands

<h1><b>SkyGrid Admin Commands </b>(Alias: /sga)</h2>
<table width="100%" align="center">
<tr>
<td align='left'><b>Command</b></td>
<td align='left'><b>Description</b></td>
<td align='left'><b>Permission</b></td>
</tr>
<tr>
<td align='left'><b>/sgadmin</b></td>
<td align='left'>displays all SkyGrid admin commands</td>
<td align='left'>skygrid.admin</td>
</tr>
<tr>
<td align='left'><b>/sgadmin deaths</b></td>
<td align='left'>edit deaths of players</td>
<td align='left'>skygrid.admin.deaths</td>
</tr>
<tr>
<td align='left'><b>/sgadmin delete</b></td>
<td align='left'>deletes a player and regenerates their area</td>
<td align='left'>skygrid.admin.delete</td>
</tr>
<tr>
<td align='left'><b>/sgadmin getrank <player></b></td>
<td align='left'>get a player's rank on their area</td>
<td align='left'>skygrid.admin.getrank</td>
</tr>
<tr>
<td align='left'><b>/sgadmin info <player></b></td>
<td align='left'>get info on where you are or player's area</td>
<td align='left'>skygrid.mod.info</td>
</tr>
<tr>
<td align='left'><b>/sgadmin kick <player></b></td>
<td align='left'>kick a player from a team</td>
<td align='left'>skygrid.mod.team</td>
</tr>
<tr>
<td align='left'><b>/sgadmin range</b></td>
<td align='left'>Admin area range command</td>
<td align='left'>skygrid.admin.setrange</td>
</tr>
<tr>
<td align='left'><b>/sgadmin register <player></b></td>
<td align='left'>register player to unowned area you are on</td>
<td align='left'>skygrid.admin.register</td>
</tr>
<tr>
<td align='left'><b>/sgadmin reload</b></td>
<td align='left'>reload the plugin</td>
<td align='left'>skygrid.admin.reload</td>
</tr>
<tr>
<td align='left'><b>/sgadmin resetflags</b></td>
<td align='left'>reset all areas to default flag settings in config.yml</td>
<td align='left'>skygrid.admin.settingsreset</td>
</tr>
<tr>
<td align='left'><b>/sgadmin bp</b></td>
<td align='left'>manipulate blueprints</td>
<td align='left'>skygrid.admin.blueprint</td>
</tr>
<tr>
<td align='left'><b>/sgadmin bp copy [air]</b></td>
<td align='left'>copy the clipboard set by pos1 and pos2 and optionally the air blocks</td>
<td align='left'>skygrid.admin.blueprint</td>
</tr>
<tr>
<td align='left'><b>/sgadmin bp load <bp name></b></td>
<td align='left'>load blueprint into the clipboard</td>
<td align='left'>skygrid.admin.blueprint</td>
</tr>
<tr>
<td align='left'><b>/sgadmin bp origin</b></td>
<td align='left'>set the blueprint's origin to your position</td>
<td align='left'>skygrid.admin.blueprint</td>
</tr>
<tr>
<td align='left'><b>/sgadmin bp paste</b></td>
<td align='left'>paste the clipboard to your location</td>
<td align='left'>skygrid.admin.blueprint</td>
</tr>
<tr>
<td align='left'><b>/sgadmin bp pos1</b></td>
<td align='left'>set 1st corner of cuboid clipboard</td>
<td align='left'>skygrid.admin.blueprint</td>
</tr>
<tr>
<td align='left'><b>/sgadmin bp pos2</b></td>
<td align='left'>set 2nd corner of cuboid clipboard</td>
<td align='left'>skygrid.admin.blueprint</td>
</tr>
<tr>
<td align='left'><b>/sgadmin bp save <bp name></b></td>
<td align='left'>save the copied clipboard</td>
<td align='left'>skygrid.admin.blueprint</td>
</tr>
<tr>
<td align='left'><b>/sgadmin setowner <player></b></td>
<td align='left'>transfers area ownership to the player</td>
<td align='left'>skygrid.mod.team</td>
</tr>
<tr>
<td align='left'><b>/sgadmin setrank <player> <rank></b></td>
<td align='left'>set a player's rank on their area</td>
<td align='left'>skygrid.admin.setrank</td>
</tr>
<tr>
<td align='left'><b>/sgadmin setspawn</b></td>
<td align='left'>set an area as spawn for this gamemode</td>
<td align='left'>skygrid.admin.setspawn</td>
</tr>
<tr>
<td align='left'><b>/sgadmin tp <player></b></td>
<td align='left'>teleport to a player's area</td>
<td align='left'>skygrid.mod.tp</td>
</tr>
<tr>
<td align='left'><b>/sgadmin tpend <player></b></td>
<td align='left'>teleport to a player's end area</td>
<td align='left'>skygrid.mod.tp</td>
</tr>
<tr>
<td align='left'><b>/sgadmin tpnether <player></b></td>
<td align='left'>teleport to a player's nether area</td>
<td align='left'>skygrid.mod.tp</td>
</tr>
<tr>
<td align='left'><b>/sgadmin unregister <owner></b></td>
<td align='left'>unregister owner from area, but keep area blocks</td>
<td align='left'>skygrid.admin.unregister</td>
</tr>
<tr>
<td align='left'><b>/sgadmin version</b></td>
<td align='left'>display BentoBox and addons versions</td>
<td align='left'>skygrid.admin.version</td>
</tr>
<tr>
<td align='left'><b>/sgadmin why <player></b></td>
<td align='left'>toggle console protection debug reporting</td>
<td align='left'>skygrid.admin.why</td>
</tr>
</table>

<h1><b>SkyGrid Player Commands </b>(Alias: /sg)</h2>
<table width="100%" align="center">
<tr>
<td align='left'><b>Command</b></td>
<td align='left'><b>Description</b></td>
<td align='left'><b>Permission</b></td>
</tr>
<tr>
<td align='left'><b>/skygrid</b></td>
<td align='left'>The main player command</td>
<td align='left'>skygrid.island</td>
</tr>
<tr>
<td align='left'><b>/skygrid ban <player></b></td>
<td align='left'>ban a player from your area</td>
<td align='left'>skygrid.island.ban</td>
</tr>
<tr>
<td align='left'><b>/skygrid banlist</b></td>
<td align='left'>list banned players</td>
<td align='left'>skygrid.island.ban</td>
</tr>
<tr>
<td align='left'><b>/skygrid create</b></td>
<td align='left'>create a new area</td>
<td align='left'>skygrid.island.create</td>
</tr>
<tr>
<td align='left'><b>/skygrid expel <player></b></td>
<td align='left'>expel a player from your area</td>
<td align='left'>skygrid.island.expel</td>
</tr>
<tr>
<td align='left'><b>/skygrid go</b></td>
<td align='left'>teleport to your area home</td>
<td align='left'>skygrid.island.home</td>
</tr>
<tr>
<td align='left'><b>/skygrid info <player></b></td>
<td align='left'>display info about your area or a player's area</td>
<td align='left'>skygrid.island.info</td>
</tr>
<tr>
<td align='left'><b>/skygrid language</b></td>
<td align='left'>select language</td>
<td align='left'>skygrid.island.language</td>
</tr>
<tr>
<td align='left'><b>/skygrid reset</b></td>
<td align='left'>restart your area and remove the old one</td>
<td align='left'>skygrid.island.reset</td>
</tr>
<tr>
<td align='left'><b>/skygrid sethome</b></td>
<td align='left'>set your home teleport point</td>
<td align='left'>skygrid.island.sethome</td>
</tr>
<tr>
<td align='left'><b>/skygrid setname <name></b></td>
<td align='left'>set a name for your area</td>
<td align='left'>skygrid.island.name</td>
</tr>
<tr>
<td align='left'><b>/skygrid settings</b></td>
<td align='left'>display area settings</td>
<td align='left'>skygrid.island.settings</td>
</tr>
<tr>
<td align='left'><b>/skygrid spawn</b></td>
<td align='left'>teleport to the spawn</td>
<td align='left'>skygrid.island.spawn</td>
</tr>
<tr>
<td align='left'><b>/skygrid resetname</b></td>
<td align='left'>reset your area name</td>
<td align='left'>skygrid.mod.resetname</td>
</tr>
<tr>
<td align='left'><b>/skygrid unban <player></b></td>
<td align='left'>unban a player from your area</td>
<td align='left'>skygrid.island.ban</td>
</tr>
<tr>
<td align='left'><b>/skygrid team</b></td>
<td align='left'>manage your team</td>
<td align='left'>skygrid.island.team</td>
</tr>
<tr>
<td align='left'><b>/skygrid team accept</b></td>
<td align='left'>accept an invitation</td>
<td align='left'>skygrid.island.team</td>
</tr>
<tr>
<td align='left'><b>/skygrid team coop <player></b></td>
<td align='left'>make a player coop rank on your area</td>
<td align='left'>skygrid.island.team.coop</td>
</tr>
<tr>
<td align='left'><b>/skygrid team demote <player></b></td>
<td align='left'>demote a player on your area down a rank</td>
<td align='left'>skygrid.island.team</td>
</tr>
<tr>
<td align='left'><b>/skygrid team invite <player></b></td>
<td align='left'>invite a player to join your area</td>
<td align='left'>skygrid.island.team</td>
</tr>
<tr>
<td align='left'><b>/skygrid team kick <player></b></td>
<td align='left'>remove a member from your area</td>
<td align='left'>skygrid.island.team</td>
</tr>
<tr>
<td align='left'><b>/skygrid team leave</b></td>
<td align='left'>leave your area</td>
<td align='left'>skygrid.island.team</td>
</tr>
<tr>
<td align='left'><b>/skygrid team promote <player></b></td>
<td align='left'>promote a player on your area up a rank</td>
<td align='left'>skygrid.island.team</td>
</tr>
<tr>
<td align='left'><b>/skygrid team reject</b></td>
<td align='left'>reject an invitation</td>
<td align='left'>skygrid.island.team</td>
</tr>
<tr>
<td align='left'><b>/skygrid team setowner <player></b></td>
<td align='left'>transfer your area ownership to a member</td>
<td align='left'>skygrid.island.team</td>
</tr>
<tr>
<td align='left'><b>/skygrid team trust <player></b></td>
<td align='left'>give a player trusted rank on your area</td>
<td align='left'>skygrid.island.team.trust</td>
</tr>
<tr>
<td align='left'><b>/skygrid team uncoop <player></b></td>
<td align='left'>remove a coop rank from player</td>
<td align='left'>skygrid.island.team.coop</td>
</tr>
<tr>
<td align='left'><b>/skygrid team untrust <player></b></td>
<td align='left'>remove trusted player rank from player</td>
<td align='left'>skygrid.island.team.trust</td>
</tr>
</table>

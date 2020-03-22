<h2><b>Challenges Commands</b></h2>
Commands for Challenges are formatted by the command being the Addon or the Addon Alias as the command followed by the "challenges" mode to use.

<h4><b>Challenges Commands</b></h4>
<table align='center'>
<tr>
<td align='left'><b>Command</b></td>
<td align='left'><b>Enable For</b></td>
<td align='left'><b>Description</b></td>
<td align='left'><b>Permission</b></td>
</tr>
<tr>
<td align='left' nowrap=nowrap><b>/challenges</b></td>
<td align='left' nowrap=nowrap>true</td>
<td align='left' nowrap=nowrap>Access Player Challenges GUI.
Contains either Challenges in current world or list of worlds
where are Challenges enabled. 
This must be enabled in configuration.</td>
<td align='left' nowrap=nowrap>addon.challenges</td>
</tr>
<tr>
<td align='left' nowrap=nowrap><b>/challengesadmin</b></td>
<td align='left' nowrap=nowrap>op</td>
<td align='left' nowrap=nowrap>Access Admin Challenges GUI. Contains 
list of worlds where Challenges are enabled. 
This must be enabled in configuration.</td>
<td align='left' nowrap=nowrap>addon.admin.challenges</td>
</tr>
</table>

<h4><b>BSkyBlock Commands</b></h4>
<table align='center'>
<tr>
<td align='left'><b>Command</b></td>
<td align='left'><b>Enable For</b></td>
<td align='left'><b>Description</b></td>
<td align='left'><b>Permission</b></td>
</tr>
<tr>
<td align='left' nowrap=nowrap><b>/island challenges [challenge] [number]</b></td>
<td align='left' nowrap=nowrap>true</td>
<td align='left' nowrap=nowrap>Access BSkyBlock Player Challenges GUI.
If challenge name is provided, than
this method will complete that challenge
once.
If number is provided, than it will complete
challenge from 0-number times.
</td>
<td align='left' nowrap=nowrap>bskyblock.challenges</td>
</tr>
<tr>
<td align='left' nowrap=nowrap><b>/bsbadmin challenges</b></td>
<td align='left' nowrap=nowrap>op</td>
<td align='left' nowrap=nowrap>Access BSkyBlock Admin Challenges GUI</td>
<td align='left' nowrap=nowrap>bskyblock.admin.challenges</td>
</tr>
<tr>
<td align='left' nowrap=nowrap><b>/bsbadmin challenges reload [hard]</b></td>
<td align='left' nowrap=nowrap>op</td>
<td align='left' nowrap=nowrap>Ability to reload Challengs addon configuration.
This method clears also cache data.
Parameter <code>hard</code> allows to reset database connection.
</td>
<td align='left' nowrap=nowrap>bskyblock.admin.challenges</td>
</tr>
<tr>
<td align='left' nowrap=nowrap><b>/bsbadmin challenges import [overwrite]</b></td>
<td align='left' nowrap=nowrap>op</td>
<td align='left' nowrap=nowrap>Ability to import ASkyBlock challenges.
Requires <code>challenges.yml</code> file in 
<code>./plugins/BentoBox/addons/Challenges/</code> folder.
Parameter <code>overwrite</code> allows to overwrite 
existing challenges.
</td>
<td align='left' nowrap=nowrap>bskyblock.admin.challenges</td>
</tr>
<tr>
<td align='left' nowrap=nowrap><b>/bsbadmin challenges defaults import</b></td>
<td align='left' nowrap=nowrap>op</td>
<td align='left' nowrap=nowrap>Ability to import Default challenges.
This method will not work, if in 
current world already exist challenges 
or levels.
</td>
<td align='left' nowrap=nowrap>bskyblock.admin.challenges</td>
</tr>
<tr>
<td align='left' nowrap=nowrap><b>/bsbadmin challenges defaults generate</b></td>
<td align='left' nowrap=nowrap>op</td>
<td align='left' nowrap=nowrap>Ability to export existing challenges.
This method will generate <code>defaults.json</code> 
file in <code>./plugins/BentoBox/addons/Challenges/</code> folder.
</td>
<td align='left' nowrap=nowrap>bskyblock.admin.challenges</td>
</tr>
</table>

<h4><b>AcidIsland Commands</b></h4>
<table align='center'>
<tr>
<td align='left'><b>Command</b></td>
<td align='left'><b>Enable For</b></td>
<td align='left'><b>Description</b></td>
<td align='left'><b>Permission</b></td>
</tr>
<tr>
<td align='left' nowrap=nowrap><b>/ai challenges [challenge] [number]</b></td>
<td align='left' nowrap=nowrap>true</td>
<td align='left' nowrap=nowrap>Access AcidIsland Player Challenges GUI.
If challenge name is provided, than
this method will complete that challenge
once.
If number is provided, than it will complete
challenge from 0-number times.
</td>
<td align='left' nowrap=nowrap>acidisland.challenges</td>
</tr>
<tr>
<td align='left' nowrap=nowrap><b>/acid challenges</b></td>
<td align='left' nowrap=nowrap>op</td>
<td align='left' nowrap=nowrap>Access AcidIsland Admin Challenges GUI</td>
<td align='left' nowrap=nowrap>acidisland.admin.challenges</td>
</tr>
<tr>
<td align='left' nowrap=nowrap><b>/acid challenges reload [hard]</b></td>
<td align='left' nowrap=nowrap>op</td>
<td align='left' nowrap=nowrap>Ability to reload Challengs addon configuration.
This method clears also cache data.
Parameter <code>hard</code> allows to reset database connection.
</td>
<td align='left' nowrap=nowrap>acidisland.admin.challenges</td>
</tr>
<tr>
<td align='left' nowrap=nowrap><b>/acid challenges import [overwrite]</b></td>
<td align='left' nowrap=nowrap>op</td>
<td align='left' nowrap=nowrap>Ability to import ASkyBlock challenges.
Requires <code>challenges.yml</code> file in 
<code>./plugins/BentoBox/addons/Challenges/</code> folder.
Parameter <code>overwrite</code> allows to overwrite 
existing challenges.
</td>
<td align='left' nowrap=nowrap>acidisland.admin.challenges</td>
</tr>
<tr>
<td align='left' nowrap=nowrap><b>/acid challenges defaults import</b></td>
<td align='left' nowrap=nowrap>op</td>
<td align='left' nowrap=nowrap>Ability to import Default challenges.
This method will not work, if in 
current world already exist challenges 
or levels.
</td>
<td align='left' nowrap=nowrap>acidisland.admin.challenges</td>
</tr>
<tr>
<td align='left' nowrap=nowrap><b>/acid challenges defaults generate</b></td>
<td align='left' nowrap=nowrap>op</td>
<td align='left' nowrap=nowrap>Ability to export existing challenges.
This method will generate <code>defaults.json</code> 
file in <code>./plugins/BentoBox/addons/Challenges/</code> folder.
</td>
<td align='left' nowrap=nowrap>acidisland.admin.challenges</td>
</tr>
</table>

<h4><b>CaveBlock Commands</b></h4>
<table align='center'>
<tr>
<td align='left'><b>Command</b></td>
<td align='left'><b>Enable For</b></td>
<td align='left'><b>Description</b></td>
<td align='left'><b>Permission</b></td>
</tr>
<tr>
<td align='left' nowrap=nowrap><b>/cave challenges [challenge] [number]</b></td>
<td align='left' nowrap=nowrap>true</td>
<td align='left' nowrap=nowrap>Access CaveBlock Player Challenges GUI.
If challenge name is provided, than
this method will complete that challenge
once.
If number is provided, than it will complete
challenge from 0-number times.
</td>
<td align='left' nowrap=nowrap>caveblock.challenges</td>
</tr>
<tr>
<td align='left' nowrap=nowrap><b>/cbadmin challenges</b></td>
<td align='left' nowrap=nowrap>op</td>
<td align='left' nowrap=nowrap>Access CaveBlock Admin Challenges GUI</td>
<td align='left' nowrap=nowrap>caveblock.admin.challenges</td>
</tr>
<tr>
<td align='left' nowrap=nowrap><b>/cbadmin challenges reload [hard]</b></td>
<td align='left' nowrap=nowrap>op</td>
<td align='left' nowrap=nowrap>Ability to reload Challengs addon configuration.
This method clears also cache data.
Parameter <code>hard</code> allows to reset database connection.
</td>
<td align='left' nowrap=nowrap>caveblock.admin.challenges</td>
</tr>
<tr>
<td align='left' nowrap=nowrap><b>/cbadmin challenges import [overwrite]</b></td>
<td align='left' nowrap=nowrap>op</td>
<td align='left' nowrap=nowrap>Ability to import ASkyBlock challenges.
Requires <code>challenges.yml</code> file in 
<code>./plugins/BentoBox/addons/Challenges/</code> folder.
Parameter <code>overwrite</code> allows to overwrite 
existing challenges.
</td>
<td align='left' nowrap=nowrap>caveblock.admin.challenges</td>
</tr>
<tr>
<td align='left' nowrap=nowrap><b>/cbadmin challenges defaults import</b></td>
<td align='left' nowrap=nowrap>op</td>
<td align='left' nowrap=nowrap>Ability to import Default challenges.
This method will not work, if in 
current world already exist challenges 
or levels.
</td>
<td align='left' nowrap=nowrap>caveblock.admin.challenges</td>
</tr>
<tr>
<td align='left' nowrap=nowrap><b>/cbadmin challenges defaults generate</b></td>
<td align='left' nowrap=nowrap>op</td>
<td align='left' nowrap=nowrap>Ability to export existing challenges.
This method will generate <code>defaults.json</code> 
file in <code>./plugins/BentoBox/addons/Challenges/</code> folder.
</td>
<td align='left' nowrap=nowrap>caveblock.admin.challenges</td>
</tr>
</table>

<h4><b>SkyGrid Commands</b></h4>
<table align='center'>
<tr>
<td align='left'><b>Command</b></td>
<td align='left'><b>Enable For</b></td>
<td align='left'><b>Description</b></td>
<td align='left'><b>Permission</b></td>
</tr>
<tr>
<td align='left' nowrap=nowrap><b>/sg challenges [challenge] [number]</b></td>
<td align='left' nowrap=nowrap>true</td>
<td align='left' nowrap=nowrap>Access SkyGrid Player Challenges GUI.
If challenge name is provided, than
this method will complete that challenge
once.
If number is provided, than it will complete
challenge from 0-number times.
</td>
<td align='left' nowrap=nowrap>skygrid.challenges</td>
</tr>
<tr>
<td align='left' nowrap=nowrap><b>/sgadmin challenges</b></td>
<td align='left' nowrap=nowrap>op</td>
<td align='left' nowrap=nowrap>Access SkyGrid Admin Challenges GUI</td>
<td align='left' nowrap=nowrap>skygrid.admin.challenges</td>
</tr>
<tr>
<td align='left' nowrap=nowrap><b>/sgadmin challenges reload [hard]</b></td>
<td align='left' nowrap=nowrap>op</td>
<td align='left' nowrap=nowrap>Ability to reload Challengs addon configuration.
This method clears also cache data.
Parameter <code>hard</code> allows to reset database connection.
</td>
<td align='left' nowrap=nowrap>skygrid.admin.challenges</td>
</tr>
<tr>
<td align='left' nowrap=nowrap><b>/sgadmin challenges import [overwrite]</b></td>
<td align='left' nowrap=nowrap>op</td>
<td align='left' nowrap=nowrap>Ability to import ASkyBlock challenges.
Requires <code>challenges.yml</code> file in 
<code>./plugins/BentoBox/addons/Challenges/</code> folder.
Parameter <code>overwrite</code> allows to overwrite 
existing challenges.
</td>
<td align='left' nowrap=nowrap>skygrid.admin.challenges</td>
</tr>
<tr>
<td align='left' nowrap=nowrap><b>/sgadmin challenges defaults import</b></td>
<td align='left' nowrap=nowrap>op</td>
<td align='left' nowrap=nowrap>Ability to import Default challenges.
This method will not work, if in 
current world already exist challenges 
or levels.
</td>
<td align='left' nowrap=nowrap>skygrid.admin.challenges</td>
</tr>
<tr>
<td align='left' nowrap=nowrap><b>/sgadmin challenges defaults generate</b></td>
<td align='left' nowrap=nowrap>op</td>
<td align='left' nowrap=nowrap>Ability to export existing challenges.
This method will generate <code>defaults.json</code> 
file in <code>./plugins/BentoBox/addons/Challenges/</code> folder.
</td>
<td align='left' nowrap=nowrap>skygrid.admin.challenges</td>
</tr>
</table>
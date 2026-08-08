# ChunkBlock Permissions

Every ChunkBlock permission is prefixed `chunkblock.`. Defaults are chosen so a vanilla install plays the intended game with no permissions plugin at all: everything a player needs is `true`, admin tooling is OP, and the two nodes that would change the game itself — the phases GUI and the chunk-lock bypass — are off until you grant them.

!!! warning "`chunkblock.mod.bypasschunks` is deliberately not an OP default"
    It exempts the holder from chunk locking entirely and enables `/chadmin bypass`. Its default is `false`, **not** `op`, so staff play by the same rules as everyone else until you grant it explicitly in your permissions plugin.

    It is a separate node from `chunkblock.mod.bypasslock`, which is BentoBox's island *lock* bypass and does nothing for chunk locks.

!!! note "Two nodes are off by default"
    - `chunkblock.phases` — the `/ch phases` GUI. Grant it if you want players browsing and replaying phases.
    - `chunkblock.island.setcount` — replaying a phase. OP only by default, and the phases GUI checks it before offering *"Click to change"*.

## ChunkBlock-specific permissions

| Permission | Description | Default |
|------------|-------------|---------|
| `chunkblock.admin.chunks` | Allow use of '/chadmin chunks' command - inspect, set or recalculate a player's unlocked chunks | OP |
| `chunkblock.admin.phases` | Allow use of '/chadmin phases' command - open the phase order editor | OP |
| `chunkblock.admin.sanity` | Allow use of '/chadmin sanity' command - display a sanity check of the phase probabilities in the console | OP |
| `chunkblock.admin.setchest` | Allow use of '/chadmin setchest' command - put the looked-at chest in a phase with the rarity specified | OP |
| `chunkblock.admin.setcount` | Allow use of '/chadmin setcount' command - set player's block count | OP |
| `chunkblock.count` | Allow use of '/ch count' command - show the block count and phase | `true` |
| `chunkblock.island.actionbar` | Allow use of '/ch actionbar' command - toggle the actionbar | `true` |
| `chunkblock.island.bossbar` | Allow use of '/ch bossbar' command - toggle the bossbar | `true` |
| `chunkblock.island.chunks` | Allow use of '/ch chunks' command - show your unlocked chunks and territory map | `true` |
| `chunkblock.island.setcount` | Allow use of '/ch setCount' command - set block count to previously completed value | OP |
| `chunkblock.mod.bypasschunks` | Exempts the holder from chunk locking entirely; also allows '/chadmin bypass' to toggle it. Not given to ops by default - it must be granted explicitly so staff play by the same rules until they opt in. | `false` |
| `chunkblock.phases` | Allow use of '/ch phases' command - show a list of all the phases | `false` |
| `chunkblock.respawn-block` | Allow use of '/ch respawnBlock' command - respawns magic block in situations when they disappear | `true` |

## Complete list

| Permission | Description | Default |
|------------|-------------|---------|
| `chunkblock.admin` | Allow use of '/chadmin' command - admin command | OP |
| `chunkblock.admin.blueprint` | Allow use of '/chadmin blueprint' command - manipulate blueprints | OP |
| `chunkblock.admin.blueprint.copy` | Allow use of '/chadmin blueprint copy' command - copy the clipboard set by pos1 and pos2 and optionally the air blocks | OP |
| `chunkblock.admin.blueprint.delete` | Allow use of '/chadmin blueprint delete' command - delete the blueprint | OP |
| `chunkblock.admin.blueprint.list` | Allow use of '/chadmin blueprint list' command - list available blueprints | OP |
| `chunkblock.admin.blueprint.load` | Allow use of '/chadmin blueprint load' command - load blueprint into the clipboard | OP |
| `chunkblock.admin.blueprint.origin` | Allow use of '/chadmin blueprint origin' command - set the blueprint's origin to your position | OP |
| `chunkblock.admin.blueprint.paste` | Allow use of '/chadmin blueprint paste' command - paste the clipboard to your location | OP |
| `chunkblock.admin.blueprint.pos1` | Allow use of '/chadmin blueprint pos1' command - set 1st corner of cuboid clipboard | OP |
| `chunkblock.admin.blueprint.pos2` | Allow use of '/chadmin blueprint pos2' command - set 2nd corner of cuboid clipboard | OP |
| `chunkblock.admin.blueprint.rename` | Allow use of '/chadmin blueprint rename' command - rename a blueprint | OP |
| `chunkblock.admin.blueprint.save` | Allow use of '/chadmin blueprint save' command - save the copied clipboard | OP |
| `chunkblock.admin.chunks` | Allow use of '/chadmin chunks' command - inspect, set or recalculate a player's unlocked chunks | OP |
| `chunkblock.admin.deaths` | Allow use of '/chadmin deaths' command - edit deaths of players | OP |
| `chunkblock.admin.deaths.add` | Allow use of '/chadmin deaths add' command - adds deaths to the player | OP |
| `chunkblock.admin.deaths.remove` | Allow use of '/chadmin deaths remove' command - removes deaths to the player | OP |
| `chunkblock.admin.deaths.reset` | Allow use of '/chadmin deaths reset' command - resets deaths of the player | OP |
| `chunkblock.admin.deaths.set` | Allow use of '/chadmin deaths set' command - sets deaths of the player | OP |
| `chunkblock.admin.delete` | Allow use of '/chadmin delete' command - deletes a player's island | OP |
| `chunkblock.admin.getrank` | Allow use of '/chadmin getrank' command - get a player's rank on their island or the island of the owner | OP |
| `chunkblock.admin.noban` | Player cannot be banned from an island | OP |
| `chunkblock.admin.noexpel` | Player cannot be expelled from an island | OP |
| `chunkblock.admin.phases` | Allow use of '/chadmin phases' command - open the phase order editor | OP |
| `chunkblock.admin.purge` | Allow use of '/chadmin purge' command - purge islands abandoned for more than [days] | OP |
| `chunkblock.admin.purge.protect` | Allow use of '/chadmin purge protect' command - toggle island purge protection | OP |
| `chunkblock.admin.purge.status` | Allow use of '/chadmin purge status' command - displays the status of the purge | OP |
| `chunkblock.admin.purge.stop` | Allow use of '/chadmin purge stop' command - stop a purge in progress | OP |
| `chunkblock.admin.purge.unowned` | Allow use of '/chadmin purge unowned' command - purge unowned islands | OP |
| `chunkblock.admin.range` | Allow use of '/chadmin range' command - admin island range command | OP |
| `chunkblock.admin.range.add` | Allow use of '/chadmin range add' command - increases the island protected range | OP |
| `chunkblock.admin.range.display` | Allow use of '/chadmin range display' command - show/hide island range indicators | OP |
| `chunkblock.admin.range.remove` | Allow use of '/chadmin range remove' command - decreases the island protected range | OP |
| `chunkblock.admin.range.reset` | Allow use of '/chadmin range reset' command - resets the island protected range to the world default | OP |
| `chunkblock.admin.range.set` | Allow use of '/chadmin range set' command - sets the island protected range | OP |
| `chunkblock.admin.register` | Allow use of '/chadmin register' command - register player to unowned island you are on | OP |
| `chunkblock.admin.reload` | Allow use of '/chadmin reload' command - reload | OP |
| `chunkblock.admin.resetflags` | Allow use of '/chadmin resetflags' command - Reset all islands to default flag settings in config.yml | OP |
| `chunkblock.admin.resets` | Allow use of '/chadmin resets' command - edit player reset values | OP |
| `chunkblock.admin.resets.add` | Allow use of '/chadmin resets add' command - adds this player's island reset count | OP |
| `chunkblock.admin.resets.remove` | Allow use of '/chadmin resets remove' command - reduces the player's island reset count | OP |
| `chunkblock.admin.resets.set` | Allow use of '/chadmin resets set' command - sets how many times this player has reset his island | OP |
| `chunkblock.admin.sanity` | Allow use of '/chadmin sanity' command - display a sanity check of the phase probabilities in the console | OP |
| `chunkblock.admin.setchest` | Allow use of '/chadmin setchest' command - put the looked-at chest in a phase with the rarity specified | OP |
| `chunkblock.admin.setcount` | Allow use of '/chadmin setcount' command - set player's block count | OP |
| `chunkblock.admin.setprotectionlocation` | Allow use of '/chadmin setprotectionlocation' command - set current location or [x y z] as center of island's protection area | OP |
| `chunkblock.admin.setrank` | Allow use of '/chadmin setrank' command - set a player's rank on their island or the island of the owner | OP |
| `chunkblock.admin.setspawn` | Allow use of '/chadmin setspawn' command - set an island as spawn for this gamemode | OP |
| `chunkblock.admin.setspawnpoint` | Allow use of '/chadmin setspawnpoint' command - set current location as spawn point for this island | OP |
| `chunkblock.admin.settings` | Allow use of '/chadmin settings' command - open settings GUI or set settings | OP |
| `chunkblock.admin.tp` | Allow use of '/chadmin tp/tpnether/tpend' command - teleport to a player's island | OP |
| `chunkblock.admin.unregister` | Allow use of '/chadmin unregister' command - unregister owner from island, but keep island blocks | OP |
| `chunkblock.admin.version` | Allow use of '/chadmin version' command - display BentoBox and addons versions | OP |
| `chunkblock.admin.why` | Allow use of '/chadmin why' command - toggle console protection debug reporting | OP |
| `chunkblock.count` | Allow use of '/ch count' command - show the block count and phase | `true` |
| `chunkblock.island` | Allow use of '/ch' command - the main island command | `true` |
| `chunkblock.island.actionbar` | Allow use of '/ch actionbar' command - toggle the actionbar | `true` |
| `chunkblock.island.ban` | Allow use of '/ch ban' or '/ch unban' or '/ch banlist' command - banned players | `true` |
| `chunkblock.island.bossbar` | Allow use of '/ch bossbar' command - toggle the bossbar | `true` |
| `chunkblock.island.chunks` | Allow use of '/ch chunks' command - show your unlocked chunks and territory map | `true` |
| `chunkblock.island.create` | Allow use of '/ch create' command - create an island, using optional blueprint (requires permission) | `true` |
| `chunkblock.island.deletehome` | Allow use of '/ch deletehome' command - delete a home location | OP |
| `chunkblock.island.expel` | Allow use of '/ch expel' command - expel a player from your island | `true` |
| `chunkblock.island.home` | Allow use of '/ch go' command - teleport you to your island | `true` |
| `chunkblock.island.homes` | Allow use of '/ch homes' command - list your homes | OP |
| `chunkblock.island.info` | Allow use of '/ch info' command - display info about your island or the player's island | `true` |
| `chunkblock.island.language` | Allow use of '/ch language' command - select language | `true` |
| `chunkblock.island.lock` | Allows island locking in settings | `true` |
| `chunkblock.island.name` | Allow use of '/ch setname' or '/ch resetname' command - your island name | `true` |
| `chunkblock.island.near` | Allow use of '/ch near' command - show the name of neighboring islands around you | `true` |
| `chunkblock.island.renamehome` | Allow use of '/ch renamehome' command - rename a home location | OP |
| `chunkblock.island.reset` | Allow use of '/ch reset' command - restart your island and remove the old one | `true` |
| `chunkblock.island.setcount` | Allow use of '/ch setCount' command - set block count to previously completed value | OP |
| `chunkblock.island.sethome` | Allow use of '/ch sethome' command - set your home teleport point | `true` |
| `chunkblock.island.settings` | Allow use of '/ch settings' command - display island settings | `true` |
| `chunkblock.island.spawn` | Allow use of '/ch spawn' command - teleport you to the spawn | `true` |
| `chunkblock.island.team` | Allow use of '/ch team' command - manage your team | `true` |
| `chunkblock.island.team.accept` | Allow use of '/ch team accept' command - accept an invitation | `true` |
| `chunkblock.island.team.coop` | Allow use of '/ch team coop, uncoop' commands | `true` |
| `chunkblock.island.team.invite` | Allow use of '/ch team invite' command - invite a player to join your island | `true` |
| `chunkblock.island.team.kick` | Allow use of '/ch team kick' command - remove a member from your island | `true` |
| `chunkblock.island.team.leave` | Allow use of '/ch team leave' command - leave your island | `true` |
| `chunkblock.island.team.promote` | Allow use of '/ch team promote, demote' command | `true` |
| `chunkblock.island.team.reject` | Allow use of '/ch team reject' command - reject an invitation | `true` |
| `chunkblock.island.team.setowner` | Allow use of '/ch team setowner' command - transfer your island ownership to a member | `true` |
| `chunkblock.island.team.trust` | Allow use of '/ch team trust, untrust' commands | `true` |
| `chunkblock.mod.bypassban` | Bypasses island ban | OP |
| `chunkblock.mod.bypasschunks` | Exempts the holder from chunk locking entirely; also allows '/chadmin bypass' to toggle it. Not given to ops by default - it must be granted explicitly so staff play by the same rules until they opt in. | `false` |
| `chunkblock.mod.bypasscooldowns` | Allow moderator to bypass cooldowns | OP |
| `chunkblock.mod.bypassdelays` | Allow moderator to bypass delays | OP |
| `chunkblock.mod.bypassexpel` | Allow moderator to bypass island expulsion | OP |
| `chunkblock.mod.bypasslock` | Bypasses an island lock | OP |
| `chunkblock.mod.bypassprotect` | Allow moderator to bypass island protection | OP |
| `chunkblock.mod.clearreset` | Allow clearing of island reset limit | `false` |
| `chunkblock.mod.deletehomes` | Allow use of '/chadmin deletehomes' command - deletes all named homes from an island | OP |
| `chunkblock.mod.info` | Allow use of '/chadmin info' command - get info on where you are or player's island | OP |
| `chunkblock.mod.lock` | Allows lock or unlock of an island | OP |
| `chunkblock.mod.resetname` | Allow use of '/chadmin resetname' command - reset player island name | OP |
| `chunkblock.mod.switch` | Allow use of '/chadmin switch' command - switch on/off protection bypass | OP |
| `chunkblock.mod.team` | Allow use of '/chadmin team' command - manage teams | `false` |
| `chunkblock.mod.team.add` | Allow use of '/chadmin team add' or '/chadmin add' command - add player to owner's team | OP |
| `chunkblock.mod.team.disband` | Allow use of '/chadmin team disband' or '/chadmin disband' command - disband owner's team | OP |
| `chunkblock.mod.team.fix` | Allow use of '/chadmin team fix' or '/chadmin fix' command - scans and fixes cross island membership in database | OP |
| `chunkblock.mod.team.kick` | Allow use of '/chadmin team kick' or '/chadmin kick' command - kick a player from a team | OP |
| `chunkblock.mod.team.setowner` | Allow use of '/chadmin team setowner' command - transfers island ownership to the player | OP |
| `chunkblock.phases` | Allow use of '/ch phases' command - show a list of all the phases | `false` |
| `chunkblock.respawn-block` | Allow use of '/ch respawnBlock' command - respawns magic block in situations when they disappear | `true` |
| `chunkblock.settings.*` | Allow use of settings on island | `true` |
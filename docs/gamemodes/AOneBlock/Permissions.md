# AOneBlock Permissions

| Permission                       | Enable For | Description                                        |
|-----------------------------------|------------|----------------------------------------------------|
| aoneblock.admin                   | op         | Allow use of '/obadmin' command - admin command    |
| aoneblock.admin.blueprint         | op         | Allow use of '/obadmin blueprint' command - manage blueprints |
| aoneblock.admin.clearresetall     | op         | Allow clearing of island reset limit of all players |
| aoneblock.admin.delete            | op         | Let a player completely remove a player (including island) |
| aoneblock.admin.getrank           | op         | Get a player's rank                                |
| aoneblock.admin.noban             | op         | Player cannot be banned from an island             |
| aoneblock.admin.noexpel           | op         | Player cannot be expelled from an island           |
| aoneblock.admin.purge             | op         | Allow use of '/obadmin purge' command - purge islands abandoned for more than specified days |
| aoneblock.admin.range             | op         | Allow use of '/obadmin range' command - manage island range |
| aoneblock.admin.register          | op         | Let a player register the nearest island to another player |
| aoneblock.admin.reload            | op         | Reload the config.yml                              |
| aoneblock.admin.setchest          | op         | Puts the looked-at chest into a phase with a given rarity |
| aoneblock.admin.setlanguage       | op         | Resets all player languages and sets the default language |
| aoneblock.admin.setrank           | op         | Set a player's rank                                |
| aoneblock.admin.setrange          | op         | Allows setting of island protection range          |
| aoneblock.admin.setspawn          | op         | Allows use of spawn tools                          |
| aoneblock.admin.settingsreset     | op         | Resets all the islands to default protection settings |
| aoneblock.admin.tp                | op         | Allows teleport to an island                       |
| aoneblock.count                   | true       | Allow use of the aoneblock count command           |
| aoneblock.island                  | true       | Allow use of '/ob' command - the main island command |
| aoneblock.island.ban              | true       | Allow use of '/ob ban' or '/ob unban' command - manage banned players |
| aoneblock.island.create           | true       | Allow use of '/ob create' command - create an island, using optional blueprint |
| aoneblock.island.deletehome       | op         | Allow use of '/ob deletehome' command - delete a home location |
| aoneblock.island.expel            | true       | Allow use of '/ob expel' command - expel visitors  |
| aoneblock.island.home             | true       | Allow use of '/ob go' command - teleport to your island |
| aoneblock.island.homes            | op         | Allow use of '/ob homes' command - list your homes |
| aoneblock.island.info             | true       | Allow use of '/ob info' command - display island info |
| aoneblock.island.language         | true       | Allow use of '/ob language' command - select a language |
| aoneblock.island.lock             | true       | Allows island locking in settings                  |
| aoneblock.island.name             | true       | Allow use of '/ob setname' or '/ob resetname' command - set your island name |
| aoneblock.island.near             | true       | Allow use of '/ob near' command - show the name of nearby islands |
| aoneblock.island.renamehome       | op         | Allow use of '/ob renamehome' command - rename a home location |
| aoneblock.island.reset            | true       | Allow use of '/ob reset' command - restart your island |
| aoneblock.island.setcount         | op         | Allow use of '/ob setCount' command - set block count to completed value |
| aoneblock.island.sethome          | true       | Allow use of '/ob sethome' command - set your home teleport point |
| aoneblock.island.settings         | true       | Allow use of '/ob settings' command - display island settings |
| aoneblock.island.spawn            | true       | Allow use of '/ob spawn' command - teleport to island spawn if set |
| aoneblock.island.team             | true       | Allow use of '/ob team' command - manage your team |
| aoneblock.island.team.accept      | true       | Allow use of '/ob team accept' command - accept an invitation |
| aoneblock.island.team.coop        | true       | Allow use of '/ob team coop' command - cooperate with other players |
| aoneblock.island.team.invite      | true       | Allow use of '/ob team invite' command - invite a player to join your island |
| aoneblock.island.team.kick        | true       | Allow use of '/ob team kick' command - remove a member from the team |
| aoneblock.island.team.leave       | true       | Allow use of '/ob team leave' command - leave the island team |
| aoneblock.island.team.promote     | true       | Allow use of '/ob team promote' command - promote a team member |
| aoneblock.island.team.reject      | true       | Allow use of '/ob team reject' command - reject an invite |
| aoneblock.island.team.setowner    | true       | Allow use of '/ob team setowner' command - transfer island ownership |
| aoneblock.island.team.trust       | true       | Allow use of '/ob team trust' command - trust a player on your island |
| aoneblock.mod.bypassban           | op         | Bypasses island ban                                |
| aoneblock.mod.bypassexpel         | op         | Allow moderator to bypass island expulsion         |
| aoneblock.mod.bypasslock          | op         | Bypasses an island lock                            |
| aoneblock.mod.bypasscooldowns     | op         | Allow moderator to bypass cooldowns                |
| aoneblock.mod.bypassdelays        | op         | Allow moderator to bypass delays                   |
| aoneblock.mod.bypassprotect       | op         | Allow moderator to bypass island protection        |
| aoneblock.mod.clearreset          | false      | Allow clearing of island reset limit               |
| aoneblock.mod.info                | op         | Let a moderator see info on a player               |
| aoneblock.mod.lock                | op         | Allows lock or unlock of an island                 |
| aoneblock.mod.switch              | op         | Allow use of '/obadmin switch' command - toggle protection bypass |
| aoneblock.respawn-block           | true       | Allow use of '/ob respawnBlock' command - respawn magic block |
| aoneblock.settings.*              | true       | Allow use of settings on island                    |

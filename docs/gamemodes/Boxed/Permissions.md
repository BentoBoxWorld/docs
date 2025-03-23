# Boxed Permissions

| **Permission**                          | **Enable For** | **Description**                                                |
|------------------------------------------|----------------|----------------------------------------------------------------|
| boxed.admin.clearresetall                | op             | Allow clearing of island reset limit of all players             |
| boxed.admin.delete                       | op             | Let a player completely remove a player (including island)      |
| boxed.admin.deleteisland                 | op             | Let a player completely remove the island the player is on      |
| boxed.admin.noban                        | op             | Player cannot be banned from an island                         |
| boxed.admin.purge                        | op             | Let a player purge old islands                                  |
| boxed.admin.register                     | op             | Let a player register the nearest island to another player      |
| boxed.admin.reload                       | op             | Reload the config.yml                                           |
| boxed.admin.reserve                      | op             | Reserves an empty spot for a player's next island               |
| boxed.admin.setlanguage                  | op             | Resets all player languages and sets the default language       |
| boxed.admin.setrange                     | op             | Allows setting of island protection range                      |
| boxed.admin.setspawn                     | op             | Allows use of spawn tools                                       |
| boxed.admin.settingsreset                | op             | Resets all the islands to default protection settings           |
| boxed.admin.tp                           | op             | Allows teleport to an island                                    |
| boxed.admin.tpuser                       | op             | Allows teleporting a player to another player's island          |
| boxed.admin.getrank                      | op             | Allows retrieving a player's rank in their box                  |
| boxed.admin.setrank                      | op             | Allows setting a player's rank in their box                    |
| boxed.admin.version                      | op             | Displays BentoBox and addons versions                          |
| boxed.admin.blueprint                    | op             | Allows manipulation of blueprints                               |
| boxed.admin.blueprint.load               | op             | Load blueprint into the clipboard                               |
| boxed.admin.blueprint.paste              | op             | Paste the clipboard to your location                            |
| boxed.admin.blueprint.origin             | op             | Set the blueprint's origin to your position                     |
| boxed.admin.blueprint.copy               | op             | Copy the clipboard set by pos1 and pos2                         |
| boxed.admin.blueprint.save               | op             | Save the copied clipboard                                       |
| boxed.admin.blueprint.rename             | op             | Rename a blueprint                                              |
| boxed.admin.blueprint.delete             | op             | Delete the blueprint                                            |
| boxed.admin.blueprint.pos1               | op             | Set 1st corner of cuboid clipboard                              |
| boxed.admin.blueprint.pos2               | op             | Set 2nd corner of cuboid clipboard                              |
| boxed.admin.blueprint.list               | op             | List available blueprints                                       |
| boxed.admin.range                        | op             | Admin box range command                                         |
| boxed.admin.range.display                | op             | Show/hide box range indicators                                  |
| boxed.admin.range.set                    | op             | Sets the box protected range                                    |
| boxed.admin.range.reset                  | op             | Resets the protected range to the world default                 |
| boxed.admin.range.add                    | op             | Increases the island protected range                            |
| boxed.admin.range.remove                 | op             | Decreases the island protected range                            |
| boxed.admin.resets                       | op             | Edit player reset values                                        |
| boxed.admin.resets.set                   | op             | Set how many times a player has reset their island              |
| boxed.admin.resets.add                   | op             | Add to a player's island reset count                            |
| boxed.admin.resets.remove                | op             | Reduce a player's island reset count                            |
| boxed.admin.delete                       | op             | Deletes a player and regenerates their box                      |
| boxed.admin.why                          | op             | Toggle console protection debug reporting                       |
| boxed.admin.deaths                       | op             | Edit deaths of players                                          |
| boxed.admin.deaths.reset                 | op             | Reset deaths of the player                                      |
| boxed.admin.deaths.set                   | op             | Set deaths of the player                                        |
| boxed.admin.deaths.add                   | op             | Add deaths to the player                                        |
| boxed.admin.deaths.remove                | op             | Remove deaths from the player                                   |
| boxed.admin.setspawnpoint                | op             | Set current location as spawn point for this island             |
| boxed.admin.resetflags                   | op             | Reset all islands to default flag settings in config.yml        |
| boxed.admin.level                        | op             | Calculate the island level for player                           |
| boxed.admin.top                          | op             | Show the top ten list                                           |
| boxed.admin.top.remove                   | op             | Remove player from Top Ten                                      |
| boxed.admin.levelstatus                  | op             | Show how many islands are in the queue for scanning             |
| boxed.admin.level.sethandicap            | op             | Set or change the island handicap                               |
| boxed.admin.stats                        | op             | Show stats on islands on this server                            |
| boxed.mod.bypasscooldowns                | op             | Allow moderator to bypass cooldowns                             |
| boxed.mod.bypassdelays                   | op             | Allow moderator to bypass delays                                |
| boxed.mod.bypassexpel                    | op             | Allow moderator to bypass island expulsion                      |
| boxed.mod.bypasslock                     | op             | Bypasses an island lock                                         |
| boxed.mod.bypassprotect                  | op             | Allow moderator to bypass island protection                     |
| boxed.mod.clearreset                     | false          | Allow clearing of island reset limit                            |
| boxed.mod.info                           | op             | Let a moderator see info on a player and island                 |
| boxed.mod.lock                           | op             | Locks or unlocks an island                                      |
| boxed.mod.resethome                      | op             | Allows setting or resetting of a player's home position         |
| boxed.mod.name                           | false          | Enables naming of player's islands                              |
| boxed.mod.resetname                      | false          | Enables reset of player's island names                          |
| boxed.mod.team                           | false          | Enables modification of teams via kick and add commands         |
| boxed.mod.tp                             | op             | Allows teleport to an island                                    |
| boxed.island                             | true           | Allow island command usage                                      |
| boxed.island.ban                         | true           | Allows banning of visitors                                      |
| boxed.island.create                      | true           | Allow island creation                                           |
| boxed.island.expel                       | true           | Allows expelling of visitors                                    |
| boxed.island.home                        | true           | Allow teleporting to player island                              |
| boxed.island.info                        | true           | Let the player use the island info command                      |
| boxed.island.language                    | true           | Player can select a language                                    |
| boxed.island.lock                        | false          | Allows island locking                                           |
| boxed.island.name                        | true           | Player can set the name of their island                         |
| boxed.island.number                      | false          | x sets how many islands the player can make                     |
| boxed.island.reset                       | true           | Player can use the island reset or restart command              |
| boxed.island.sethome                     | true           | Let the player use the sethome command                          |
| boxed.island.settings                    | true           | Player can see server settings                                  |
| boxed.island.spawn                       | true           | Player can use the island spawn command if spawn exists         |
| boxed.island.team.*                      | true           | Let a player use all team commands (Recommended)                |
| boxed.island.team                        | true           | Let a player use team command                                   |
| boxed.island.team.invite                 | true           | Let a player invite others                                      |
| boxed.island.team.accept                 | true           | Player can accept team invites                                  |
| boxed.island.team.reject                 | true           | Player can reject team invites                                  |
| boxed.island.team.coop                   | true           | Let a player coop other players                                 |
| boxed.island.team.trust                  | true           | Let a player trust other players                                |
| boxed.island.team.promote                | true           | Let a player promote others                                     |
| boxed.island.team.kick                   | true           | Let a player kick another player from their team                |
| boxed.island.team.leave                  | true           | Let a player leave a team                                       |
| boxed.island.team.setowner               | true           | Let a player set another player as owner of island              |
| boxed.settings.*                         | true           | Allow use of settings on island.                                |
| boxed.team.maxsize.[NUMBER]              | false          | Let a player get a larger team size than default value          |
| boxed.island.maxhomes.[NUMBER]           | false          | Let a player get more homes than default value                  |
| boxed.island.range.[NUMBER]              | false          | Let a player get a larger protection range than default value. Not recommended for Boxed! |

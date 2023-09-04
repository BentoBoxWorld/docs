# Concurrent Islands

Bentobox 2.0.0 and later enable admins to allow players to have more than one island per world. This page explains about how it works and some of the implications of allowing it.

## How to enable

By default, players have one island. The number can be increased globally via the BentoBox `config.yml` under the `island.concurrent-islands` setting. This value may be overridden by individual game mode config settings if they offer this setting too.

## How to use

### Creation

If players are allowed to make more than one island, then they can do so by using the `create` command, for example:

`/island create`

This operates the same as any other island creation and the player will usually be teleported to the island after it is created.

### Going to islands

Once players have more than one island, they can teleport between them by using the `go` command, for example:

`/island go`

This command will show any named homes that they player has set along with the names of any islands the player has. If the player has named their island using the `setname` command, then it will be in the list, but if they have not, then the island will be listed by the default island name followed by a number, for example "tastybento's island 2". The number of the island may change when the server is restarted, so players should be encouraged to name their islands.

### Setting homes

Players can set the default location of their island by running the `sethome` command. If players have the ability to set multiple homes, then they can set them using the `sethome [home name]` command. The maximum number of homes allowed in the config for the game world is shared across all the islands tat the player owns.

### Teams

*[IN DEVELOPMENT - STILL NEEDS TO BE WORKED OUT]*

- Teams are island based and do not cross islands.
- TBD: It is/is not possible for a player to have multiple teams, one for each island.
- TBD: Players can only have one team.
- Players cannot be on more than one team.
- Team chat needs more testing 

## Game Mode Support

All game modes should support concurrent islands.

## Addon Support

This lists the addons and their compatibility with concurrent islands.

| Addon | Comments          |
|-------|-------------------|
| Bank 1.7.0 | Banks are per-island. Money is not pooled across islands |
| Biomes 2.1.1 | Compatible |
| Border 4.1.1 | Compatible  |
| CauldronWitchery 2.0.1 |   |
| Challenges 1.2.0 |   |
| Chat 1.1.4 |   |
| CheckMeOut 1.1.1 | Compatible  |
| DimensionalTrees 1.6.0 |   |
| ExtraMobs 1.12 |   |
| Greenhouses 1.7.3 | Compatible  |
| InvSwitcher 1.11.0 | Compatible  |
| IslandFly 1.11.0 | Compatible  |
| Level 2.11.0 | Levels are calculated by island. The Top Ten will show the score for the last calculated island.
If teleporting is allowed when clicking on the Top Ten head, then players will go to the player's current island.  |
| Likes 2.3.1 |   |
| Limits 1.19.1 | Compatible. Limits are per-island.  |
| MagicCobblestoneGenerator 2.5.1 |   |
| TwerkingForTrees 1.4.3 | Compatible  |
| Visit 1.6.0 |   |
| VoidPortals 1.5.0.0 |   |
| Warps 1.13.0 | As usual, players may have only one active warp sign.   |






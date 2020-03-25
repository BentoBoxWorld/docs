BentoBox request handlers are a nice feature that allows getting access to internal add-on data without necessary inject and overwrite add-on. The Biomes add-on has got 3 useful request handlers that provide information about biomes and even allows to request biome change.

## Usage
Biomes Request Handler works the same as all BentoBox Request Handlers. You can see it in this PullRequest: https://github.com/BentoBoxWorld/BentoBox/pull/400

## Request Handlers

### Biome Data Request Handler
This handler returns map that contains all information about requested Biomes Object.

**Magic string**: `biome-data`

**Input data Map**: 
* `biomeId`: String - an object that represents biome unique id.

If biomeId is not provided output will be empty. The same will happen if requested biomeId is not found in the database.

**Output data**: 

This handler will return a map that contains information about the current biome object (Map<String, Object>):
- `uniqueId`: the same id that was passed to this handler.
- `world`: a string that represents world name where biome operates.
- `biome`: a string that represents Minecraft Biome name.
- `name`: a string object of display name for the biome.
- `deployed`: a boolean object of deployment status.
- `description`: List of strings that represents biomes description.
- `icon`: ItemStack object that represents biome.
- `order`: Integer object of order number for the given biome.
- `cost`: Integer that represents biomes change the cost.
- `level`: Long that represents minimal island level for this biome to work.
- `permissions`: Set of strings that represent required permissions.

### Biome List Request Handler
This handler returns a list of all biomes uniqueIds that are defined in a given world.

**Magic string**: 
`biomes-list`

**Input data Map**: 
* `world-name`: a string - an object that represents world name.

If the provided map is empty, world-name is not given or a world with a given name does not exist or is not a GameMode world, then the current request handler will return an empty list.

**Output data**: 

This handler will return a list with defined biomes unique-ids from the provided world. (`List<String>`)

### Biome Change Request Handler
This handler requests biome change with given parameters.

**Magic string**: `biome-request-change`

**Input data Map**: 

_Required data_:
- `player` -> UUID that represents targeted player UUID.
- `world-name` -> String that represents world name where biome must be changed
- `biomeId` -> String that represents biome unique ID.

_Mandiatory data_:
- `updateMode` -> String that represents how biome is necessary to be changed. If not provided then will use the default from config.
- `range` -> Integer that represents a range of biome update change. If not provided then will use the default from config.
- `checkRequirements` -> Boolean that represents if requirements must be checked or not. By default it is true.
- `withdraw` -> Boolean that indicates that money will be withdrawn from the players account. By default it is true.

**Output data**: 

This handler will return a map that contains information about change status (Map<String, Object>):
* `status` - boolean that indicates if biome change was successful.
* `reason` - a string that returns message what happened.


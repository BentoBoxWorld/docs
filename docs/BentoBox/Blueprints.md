# Starter Islands (Blueprints)

When a player creates an island, BentoBox pastes a starter island for them. These starter islands are **blueprints**, which you build and save in game. A **bundle** groups an Overworld, Nether and End blueprint into one choice in the Create Island menu, with its own icon, name and description.

Each game mode comes with a few bundles. You can change them, add your own, offer VIP-only islands, charge for them, and run commands when one is chosen.

!!! info "Commands on this page"
    Commands are shown for BSkyBlock (`/bsbadmin`). Use your game mode's admin command instead, for example `/oba` for AOneBlock or `/acid` for AcidIsland. `blueprint` can be shortened to `bp`.

## Make a starter island

1. **Build it.** Build the island somewhere in the game mode's world, away from other islands. Put at least one **bedrock** block in it: the highest bedrock block becomes the island's centre, and BentoBox won't save a blueprint without one.
2. **Add the signs (optional).** Place a sign with `[spawn_here]` on the first line where players should appear, facing the way they should look. Add a sign with `[start]` on the first line for a welcome message. See [Signs](#signs).
3. **Select it.** Stand at one corner and run `/bsbadmin bp pos1`, then at the opposite corner `/bsbadmin bp pos2`. Use these, not WorldEdit's selection.
4. **Copy it.** `/bsbadmin bp copy`. Add `air` if the island will be pasted into water or stone (AcidIsland, CaveBlock, Poseidon), so the air around it is pasted too. Add `biome` to keep the biomes, or `nowater` to leave out water blocks. See [What `air` and `nowater` do](#what-air-and-nowater-do).
5. **Check it.** Go somewhere empty and run `/bsbadmin bp paste` to see what you copied.
6. **Save it.** `/bsbadmin bp save <name>`, for example `/bsbadmin bp save vip_island`.
7. **Offer it to players.** Open `/bsbadmin bp` and put the blueprint into a bundle (next section).

To replace a game mode's default island instead of adding a new one, save over its blueprint (usually `island`, `nether-island` and `end-island`). You'll be asked to confirm.

!!! tip "Keep it small"
    The fun of island game modes is growing from very little. Start players with just enough blocks and items to get going.

**Converting WorldEdit schematics:** blueprints aren't schematics, but you can paste a schematic with WorldEdit, add the bedrock and signs, then select, copy and save it with the blueprint commands as above. Do this for each Nether and End island too.

### What `air` and `nowater` do

Without `air`, only the blocks you built are copied. When the island is pasted, every other spot in the area is left as it is in the world, so water or stone there stays.

With `air`, every spot in the area is copied, so the whole area replaces what's in the world, air included. Since BentoBox 3.24.0, the most common plain block in the area (usually air, or water for an island in the sea) is stored once rather than once per spot, so a large `air` copy doesn't make a large file.

`nowater` leaves out water: wherever there was water, the world is left as it is when pasted. Used with `air`, this means the area is no longer fully copied, so every air block is stored one by one and the file is bigger. Only use `air nowater` when you need the world's own water to stay, for example in an ocean.

## Bundles: the choices in the Create Island menu

Open the Blueprint Manager with **`/bsbadmin bp`**. It lists the bundles; click one to edit it.

| To… | Do this |
|---|---|
| Create a bundle | Click the green banner, then type a name in chat |
| Put a blueprint in a bundle | Click a blueprint at the bottom so it glows, then click the green (Overworld), red (Nether) or yellow (End) slot |
| Empty a slot | Right-click it |
| Change the bundle's icon | Click an item in your own inventory |
| Rename it | Right-click the bundle in the main list, then type the name in chat |
| Change the description | Inside the bundle, click its icon (top left), then type in chat. Colour codes like `&c` work |
| Choose where it appears in the menu | Left-click the slot icon to move it later, right-click to move it earlier |
| Make it VIP-only | Click the painting to require a permission. The permission is shown on the icon, for example `bskyblock.island.create.vip_island` |
| Charge for it | Click the gold ingot: left/right click adds/removes 1, shift-click 100. Needs Vault and an economy plugin |
| Run commands when it's chosen | Click the command block and type commands in chat |
| Limit how many times a player can choose it | Click the clock. Only shown when players can own more than one island |
| Delete it | Right-click the TNT |

Every game mode has a bundle called `default`, which can't be deleted. It's used when a player doesn't choose (for example when islands are created automatically on first login).

A bundle **must** have an Overworld blueprint; if it doesn't, the default island is used and an error is logged. Nether and End blueprints are optional; without them, nothing is pasted in those worlds.

**Rename bundles and blueprints in the manager or with `/bsbadmin bp rename`**, not by renaming files.

### Commands when a bundle is chosen

Commands run each time an island is created with the bundle, for example to give a starter kit or set a rank. `[player]` and `[owner]` are replaced with the player's name. Commands run from the console unless they start with `[SUDO]`, which runs them as the player:

```
lp user [player] parent add skyblock-starter
[SUDO] kit starter
```

### Charging for a bundle

Set a cost on the bundle with the gold ingot. The player pays when they create or reset an island with it, and can't pick it if they can't afford it. This needs `use-economy: true` in BentoBox's `config.yml` and Vault with an economy plugin; without them the gold ingot isn't shown.

## Signs

| First line of the sign | What happens |
|---|---|
| `[spawn_here]` | Players appear at this spot, facing the way the sign faces. The sign is removed. Works in Nether and End blueprints too |
| `[start]` | Replaced with the welcome text from the game mode's locale file (`bskyblock.sign.line0` to `line3`), in the owner's language. `[name]` in that text becomes the owner's name |
| Anything else | Pasted as written |

**Named mobs:** rename a name tag to include `[name]` in an anvil and put it on a mob in your island before copying. The mob is named after the island owner when the island is pasted.

## All blueprint commands

| Command | What it does |
|---|---|
| `/bsbadmin bp` | Open the Blueprint Manager |
| `/bsbadmin bp pos1`, `pos2` | Set the corners of the area to copy |
| `/bsbadmin bp copy [air] [biome] [nowater]` | Copy the area to your clipboard |
| `/bsbadmin bp origin` | Set the paste origin to the block you're looking at |
| `/bsbadmin bp paste` | Paste your clipboard where you stand |
| `/bsbadmin bp save <name>` | Save your clipboard as a blueprint |
| `/bsbadmin bp load <name>` | Load a blueprint into your clipboard to change it |
| `/bsbadmin bp list` | List the blueprints |
| `/bsbadmin bp rename <name> <new name>` | Rename a blueprint |
| `/bsbadmin bp delete <name>` | Delete a blueprint |
| `/bsbadmin bp sink` | Toggle whether this blueprint sinks to the sea floor when pasted |

## The files

Blueprints and bundles are stored per game mode in `plugins/BentoBox/addons/<GameMode>/blueprints/`:

- `<name>.blueprint`: a blueprint, as plain JSON. Older `.blu` files (compressed) still load.
- `<bundle>.json`: a bundle, as plain JSON.

You can copy these files between servers, keep them in version control, or edit them. For every field, see [Blueprint File Format](Blueprint-Format.md).

## Pasting speed

Copying and pasting happen a little at a time, so large islands don't freeze the server; a big island can take a few seconds. Two settings under `island` in BentoBox's `config.yml` control this:

| Setting | Default | What it does |
|---|---|---|
| `paste-time-budget` | `10` | Milliseconds of each tick that pasting and copying may use. A tick is 50 ms. BentoBox keeps placing batches until this time is used up, so large islands paste much faster when the server has time to spare. `0` places one batch per tick, as before 3.24.0. |
| `paste-speed` | `64` | Blocks in one batch. |

If island creation causes lag, lower `paste-time-budget` first. `paste-time-budget` needs BentoBox 3.24.0 or later; older versions place one `paste-speed` batch per tick.

## Troubleshooting

**"At least one bedrock block must be in a blueprint!"**
Add a bedrock block to the island, copy again, then save.

**Players appear in the wrong place, or fall.**
Add a `[spawn_here]` sign, with air above it for the player.

**The island is surrounded by water (or stone) gaps that shouldn't be there**, or water from the world flows into it.
Copy with `air` so the space around the island is part of the blueprint. Since 3.24.0, the air is stored once for the whole area, so a bigger selection costs little.

**A boat sinks into the water, or a mob is stuck in a slab, after pasting.**
The blueprint was copied before BentoBox 3.24.0, which didn't record how high an entity stood within its block. Paste it, then copy and save it again.

**My new bundle doesn't show in the Create Island menu.**
Check that it has an Overworld blueprint, that it doesn't require a permission the player lacks, and, if it has a use limit, that the player hasn't used it up. With `hide-used-blueprints: true` in BentoBox's `config.yml`, used-up bundles are hidden.

**The console reports a missing or broken `default` bundle at startup.**
Since 3.24.0, BentoBox checks each game mode's `default` bundle when it loads and names the file to fix, instead of leaving players with an empty island. Restore the bundle file it names, or fix the blueprint the bundle points to. If there is no `default` bundle and exactly one other bundle, that one is used.

**The welcome sign shows `[start]`.**
The `[start]` text comes from the game mode's locale file. Check `<gamemode>.sign.line0` to `line3` exist in it.

## See also

- [Islands](About/IslandManagement.md): creating, resetting and sizing islands
- [Bigger Create Island Menu](../Tutorials/generic/Bigger-Create-Island-Menu.md) and [Customizing Menus](../Tutorials/generic/Customizable-GUI.md): the menu players choose from
- [Blueprint File Format](Blueprint-Format.md): for editing the files

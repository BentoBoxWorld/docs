# Border

**Border** can create and show a border around islands which players cannot pass.  
The border can be:

- the vanilla world border
- a custom border that shows up when the player is near (visuals can be configured).

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("Border") }}

## Installation

1. Restart the server (to enable the addon and have the `config.yml` file generated)
2. Put the addon jar into the `plugins/BentoBox/addons` folder
3. Customize settings in `config.yml` (optional)
4. Restart the server to apply new settings

## Commands

!!! tip
    `[player_command]` is a command that differs depending on the gamemode you are running.
    The Gamemodes' `config.yml` file contains settings that allows you to modify this value.
    As an example, on BSkyBlock, the default `[player_command]` is `island`.

### border
**Command**: `/[player command] border`  
**Description**: Turns the border on/off.  
**Permission**: `[gamemode].border.toggle`. Default: `op`.  
**Notes**: Since Version 3.0.0 it requires a permission.  

### border type {...}
**Command**: `/[player command] border type {barrier | vanilla}`  
**Description**: Sets the border type. Run with no argument to toggle between the available types.  
**Permission**: `[gamemode].border.type`. Default: `true`.  
**Example**: `/[player command] border type barrier`  

### border color {red|green|blue}
**Command**: `/[player command] border color {red | green | blue}`  
**Description**: Sets the vanilla world border color for the player. Only applies when using the vanilla border type.  
**Permission**: `[gamemode].border.color.red`, `[gamemode].border.color.green`, `[gamemode].border.color.blue` (or `[gamemode].border.color.*` for all). Default: `op`.  
**Example**: `/[player command] border color green`  

!!! tip
    `[gamemode]` is a prefix that differs depending on the gamemode you are running.
    The prefix is the lowercased name of the gamemode, i.e. if you are using BSkyBlock, the prefix is `bskyblock`.
    Similarly, if you are using AcidIsland, the prefix is `acidisland`.

## Configuration

The `config.yml` file contains settings.  
The default value is usually the example value unless explicitly stated.

### Disable game modes
You can disable the addon with this setting.  
By default, Border will operate in all game mode worlds on the BentoBox server.

You can disable a game mode by writing its name on a new line that starts with `-`.  
Example to disable BSkyBlock:

```yml
disabled-gamemodes:
  - BSkyBlock
```

Default value:

```yml
disabled-gamemodes: []
```

### Border type
The default kind of border new players get. There are two choices:

- `VANILLA` — uses Minecraft's own round world-border effect (the wobbly wall you see in the vanilla game). It can be tinted a colour.
- `BARRIER` — uses invisible barrier blocks and coloured particles that only appear as you get close to the edge.

Players who have permission can switch their own border with `/[player command] border type`. If they don't have permission, they get whatever you set here.

```yml
type: VANILLA
```

### Vanilla border colour
The colour of the vanilla world border. Only used when the border type is `VANILLA`.  
Choices are `RED`, `GREEN`, or `BLUE`. Players with permission can pick their own colour with `/[player command] border color`.

```yml
color: BLUE
```

### Bounce items back
If `true`, items a player throws at the border are bounced back inside instead of flying out. Set to `false` to let thrown items pass through.

```yml
bounce-back: true
```

### Return teleport
Controls whether if players somehow manage to pass through the border (e.g. teleport in the same world), should they be teleported back to their islands.

Set to `true` if you want players to be teleported back.

**Warning**: If you set this value to `false` along with having `use-barrier-blocks` as `false`, players will be able to just simply walk through the border.

```yml
return-teleport: true
```

!!! tip
    If you want to use this addon **only to show** the borders for the players, use the following settings:
    ```yml
    use-barrier-blocks: false
    return-teleport: false
    ```

### Return teleport safety block
Only used when `return-teleport` is `true`. If a player gets teleported back inside the border and lands somewhere unsafe (for example over a drop or in lava), this places a safe block under their feet so they don't get hurt.

```yml
return-teleport-safety-block: true
```

### Use barrier blocks.
Only applies for players who are **not** using the vanilla border type.

- `true`: the border will be made of barrier blocks.  
- `false`: there will be no barrier block-based border. This means it is up to the `return-teleport` setting whether players are teleported back when leaving the island.

```yml
use-barrier-blocks: true
```

### Default border behavior
Players can turn the border on and off with a command if they have the right permission.  
This setting makes the default on or off; set it to `true` to have it on by default.

```yml
show-by-default: true
```

### Show max-protection range border.
Only applies for players who are **not** using the vanilla border type.

Set to `true` to show barrier (🚫) particles shown at the max protection range.  
This is useful for game modes like Boxed where the player's protection area can move around.

Note that these are **not barrier blocks** but _particles_, so the "air" just _looks like_ them.

```yml
show-max-border: true
``` 

### Show particles
Enables/disables all types of wall particles shown by the addon (border and max-protection range particles).

Set to `false` if you don't want **any** wall particles to be shown.

```
show-particles: true
```

### Barrier offset
Only applies for players who are **not** using the vanilla border type.

Normally the border sits exactly at the edge of the player's protection range. This setting pushes the barrier **outwards** by the number of blocks you give it, so players can walk a bit past their protected area before hitting the wall.

Important things to know:

- It does **not** make the protected area bigger — players still can't build or protect the extra space, they can only stand in it.
- The border will never go further out than the island distance, no matter how big a number you set.
- The minimum (and default) value is `0`, which means the border sits right on the protection range.

```yml
barrier-offset: 0
```

## Placeholders

| Placeholder | Description | Version |
|---|---|---|
| `%Border_color%` | The current border color for the player (`red`, `green`, or `blue`) | 4.8.0 |

## FAQ

??? question "How do I change the size of the border?"
    The border isn't a size of its own — it's drawn around each island's **protection range**. So to make the border bigger or smaller, you change the protection range.

    - Give players a bigger range with a permission like `[gamemode].island.range.<number>` (for example `bskyblock.island.range.150`).
    - Admins can set the range on a specific island with the admin range command, e.g. `/bsbadmin range set <player> <number>`.
    - The range can never be bigger than **half the distance between islands**, and that distance is set once when the world is created and can't be changed afterwards.

    See [Island Range and Spacing](../../BentoBox/About/IslandManagement.md#island-range-and-spacing) for the full details.

??? question "Can I make the border a bit bigger than the island's range?"
    Yes! Use the `barrier-offset` setting in `config.yml`. It pushes the border outwards by however many blocks you choose, so players can step a little past their protected area before hitting the wall.

    Remember this only moves the wall — it does **not** give players any extra land they can build on or protect. See the [Barrier offset](#barrier-offset) setting above.

??? question "What's the difference between the barrier and vanilla border types?"
    - **Vanilla** uses Minecraft's built-in world-border effect — the shimmering wall you already know from the normal game. You can tint it red, green or blue.
    - **Barrier** uses invisible barrier blocks plus coloured particles that only show up when you get near the edge.

    Players with permission can switch between them with `/[player command] border type`.

??? question "I don't want a solid wall — can I just show a line players can cross?"
    Yes. Set `use-barrier-blocks: false` so there's no solid wall, and `return-teleport: false` so players aren't pulled back. That leaves only the visual border. Put this in `config.yml`:

    ```yml
    use-barrier-blocks: false
    return-teleport: false
    ```

??? question "How do I change the border's colour?"
    Colours only work with the **vanilla** border type. Set a server-wide default with the `color` setting in `config.yml` (`RED`, `GREEN` or `BLUE`). Players with permission can pick their own colour in-game with `/[player command] border color {red|green|blue}`.

??? question "How do I turn the border off?"
    Players can toggle their own border on or off with `/[player command] border` (they need the `[gamemode].border.toggle` permission). To have it off for everyone by default, set `show-by-default: false` in `config.yml`.

??? question "The border isn't showing up — what should I check?"
    - Make sure the game mode isn't listed under `disabled-gamemodes` in `config.yml`.
    - Check the player actually has the border toggled on (`/[player command] border`) and that `show-by-default` is `true`.
    - The border only appears around your own island's protection range, so you need to be near an edge to see it.
    - If you're using the **barrier** type with `show-particles: false`, the wall is invisible until you touch it — that's expected.

??? question "Can you add a feature X?"
    Please request it on the [issue tracker](https://github.com/BentoBoxWorld/Border/issues).

## Changelog

??? note "What's new in v4.7.0 → v4.8.2"
    **Released:** 2026-02-16 to 2026-04-04

    - **Vanilla world border color selection.** Players using the vanilla border type can now choose their border color — red, green, or blue — via `/[player_command] color {red|green|blue}`.
    - New `%Border_color%` placeholder returns the player's current border color.
    - New permissions `[gamemode].color.red`, `[gamemode].color.green`, `[gamemode].color.blue` (or `[gamemode].color.*` for all colors). Default: op.
    - Bug fix: border teleportation bypass when a player is outside all island spaces (4.7.0).
    - Bug fix: vanilla world border not resetting when a player teleports between islands — was causing Bedrock/Geyser players to enter a restricted state (4.8.1).
    - Bug fix: `%Border_color%` placeholder throwing null error in some configurations (4.8.1).
    - Bug fix: border incorrectly activating in vanilla nether and end worlds (4.8.1).

    [Release v4.7.0](https://github.com/BentoBoxWorld/Border/releases/tag/4.7.0) · [v4.8.0](https://github.com/BentoBoxWorld/Border/releases/tag/4.8.0) · [v4.8.1](https://github.com/BentoBoxWorld/Border/releases/tag/4.8.1) · [v4.8.2](https://github.com/BentoBoxWorld/Border/releases/tag/4.8.2)

??? note "What's new in v4.8.3"
    **Released:** 2026-04-26

    - 🔡 All locale files converted from legacy `&`-colour codes to MiniMessage format.
    - 🔡 Missing `set-color` keys added to every non-English locale.
    - 🔡 Bug fixes for Polish, Ukrainian, and Chinese locale files.
    - 🔺 Minimum BentoBox API bumped to **3.12.0**.

    🔺 **If you maintain custom locale overrides** under `plugins/BentoBox/addons/Border/locales/`, migrate colour codes from `&a` style to MiniMessage tags (e.g. `<green>`) before restarting.

    [Release v4.8.3](https://github.com/BentoBoxWorld/Border/releases/tag/4.8.3)

??? note "What's new in v4.8.4"
    **Released:** 2026-05-26

    - 🐛 **Fixed `NoSuchMethodError: WorldBorder.changeSize` on Paper/Purpur 1.21.10.** The 4.8.3 build was compiled against Paper 1.21.11, which renamed the world-border lerp method, so the vanilla border type crashed on 1.21.10 servers when `/[player_command] bordertype vanilla` was used. Border now uses the cross-version `setSize` API and works on **both 1.21.10 and 1.21.11**.
    - 🐛 Fixed the Modrinth publish workflow (incorrect artifact path).

    No config or locale changes are required. If you worked around the bug with `bordertype barrier`, you can switch back to `vanilla` once 4.8.4 is installed.

    [Release v4.8.4](https://github.com/BentoBoxWorld/Border/releases/tag/4.8.4)

## Translations

{{ translations("Border") }}

## Source
Want to contribute? See this documentation's source code at [GitHub](https://github.com/BentoBoxWorld/docs/blob/master/docs/addons/Border/).

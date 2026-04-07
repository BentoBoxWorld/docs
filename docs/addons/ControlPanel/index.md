# ControlPanel

**ControlPanel** gives your players a clickable GUI menu to run their most-used island commands — no typing required. Server admins build fully customizable panels using a simple YAML file, with support for multiple click actions, custom icons, and live placeholders.

Created and maintained by [BONNe](https://github.com/BONNe).

{{ addon_description("ControlPanel") }}

## Installation

1. Place the ControlPanel addon jar in the `addons` folder of the BentoBox plugin.
2. Restart the server. ControlPanel will create a default `controlPanelTemplate.yml` inside `plugins/BentoBox/addons/ControlPanel/`.
3. Edit `controlPanelTemplate.yml` to build your panels (see [Configuration](#configuration) below).
4. Import the panels with the admin command:
```
/{admin} cp import
```

!!! tip
    Replace `{admin}` with your gamemode's admin command label, e.g. `bsb` for BSkyBlock, `oa` for AOneBlock, `acid` for AcidIsland.

## Commands

### Player command

| Command | Description | Permission |
|---|---|---|
| `/[label] controlpanel` | Opens the player's assigned control panel | `[gamemode].controlpanel` |
| `/[label] cp` | Shorthand alias for the command above | `[gamemode].controlpanel` |

Replace `[label]` with the gamemode's player command, e.g. `island` for BSkyBlock or `ob` for AOneBlock.

The panel shown depends on the player's permissions. Players without a specific panel permission see the panel marked `defaultPanel: true`. If a player has permission for a particular panel via `[gamemode].controlpanel.panel.<suffix>`, that panel is shown instead.

### Admin command

| Command | Description | Permission |
|---|---|---|
| `/{admin} cp import` | Import panels from `controlPanelTemplate.yml` | `[gamemode].controlpanel.admin` |
| `/{admin} cp import <filename>` | Import panels from a custom YAML file | `[gamemode].controlpanel.admin` |

The filename does not need the `.yml` extension — it is added automatically. The file must be located in `plugins/BentoBox/addons/ControlPanel/`.

!!! warning
    If panels already exist for the gamemode, importing will ask for confirmation before replacing them.

## Permissions

| Permission | Default | Description |
|---|---|---|
| `[gamemode].controlpanel` | `true` | Allows the player to open the control panel |
| `[gamemode].controlpanel.admin` | `op` | Allows use of the admin import command |
| `[gamemode].controlpanel.panel.default` | `true` | Grants access to the default panel |
| `[gamemode].controlpanel.panel.<suffix>` | — | Grants access to a custom panel with the given suffix |

Replace `[gamemode]` with the lowercase gamemode name, e.g. `bskyblock`, `acidisland`, `aoneblock`, `caveblock`, `skygrid`.

!!! note
    If a player has multiple panel permissions, the first panel marked `defaultPanel: true` among those they have access to is shown. If the player has wildcard `*` permissions, the first defined default panel is used.

## Configuration

ControlPanel uses two files:

- `config.yml` — general addon settings
- `controlPanelTemplate.yml` — defines panels and buttons

Both are located in `plugins/BentoBox/addons/ControlPanel/`.

### config.yml

The main configuration file has one setting:

??? note "disabled-gamemodes"
    A list of GameMode addon names where ControlPanel should not operate. ControlPanel will not hook into these gamemodes.

    Default: `[]`

    Example:
    ```yaml
    disabled-gamemodes:
      - BSkyBlock
      - AcidIsland
    ```

### controlPanelTemplate.yml

This file defines all control panels and their buttons. After editing it, run `/{admin} cp import` to load your changes.

#### Panel structure

```yaml
panel-list:
  <panel-key>:
    defaultPanel: true|false
    panelName: '<title>'
    permission: '<suffix>'
    buttons:
      <slot>:
        name: '<display name>'
        material: MATERIAL_NAME
        icon: 'namespace:item_id'
        itemsadder: 'namespace:item_id'
        description: |-
          line one
          line two
        command: '<left-click command>'
        right_click_command: '<right-click command>'
        shift_click_command: '<shift+left-click command>'
```

#### Panel fields

| Field | Type | Description |
|---|---|---|
| `defaultPanel` | boolean | Set to `true` to show this panel to players with no specific panel permission. |
| `panelName` | string | Title of the inventory GUI. Supports `&` color codes. |
| `permission` | string | The suffix appended to `[gamemode].controlpanel.panel.<suffix>`. Players with that permission see this panel. |

#### Button fields

| Field | Required | Description |
|---|---|---|
| `slot` | Yes | Inventory slot number (0–53). Use a quoted range like `"0-8"` to fill multiple slots with the same button. |
| `name` | Yes | Display name of the button. Supports `&` color codes. |
| `material` | No | Vanilla Minecraft material, e.g. `GRASS_BLOCK`. Used as a fallback icon. |
| `icon` | No | BentoBox `ItemParser` format, e.g. `minecraft:diamond_block`. Takes priority over `material`. |
| `itemsadder` | No | [ItemsAdder](https://github.com/LoneDev6/ItemsAdder) custom item ID, e.g. `iasurvival:ruby`. Requires ItemsAdder to be installed. Falls back to paper if it is not. |
| `description` | No | Lore lines shown below the button name. Supports `&` color codes, multiline with `|-`, PlaceholderAPI `%placeholders%`, and `[gamemode]` substitution. |
| `command` | No | Command executed on left-click (and as fallback for all other click types). |
| `right_click_command` | No | Command executed on right-click or shift+right-click. Falls back to `command` if omitted. |
| `shift_click_command` | No | Command executed on shift+left-click. Falls back to `command` if omitted. |

!!! info "Icon priority"
    If multiple icon fields are specified, the priority is: `itemsadder` > `icon` > `material`. If none are set, the button defaults to `PAPER`.

#### Click types

Each button can respond differently depending on how the player clicks it:

| Click action | Command used |
|---|---|
| Left click | `command` |
| Right click | `right_click_command` (falls back to `command`) |
| Shift + Left click | `shift_click_command` (falls back to `command`) |
| Shift + Right click | `right_click_command` (falls back to `command`) |
| Any other click | `command` |

#### Command placeholders

These placeholders can be used inside the `command`, `right_click_command`, and `shift_click_command` fields:

| Placeholder | Replaced with |
|---|---|
| `[label]` | The gamemode's player command label, e.g. `island`, `ob` |
| `[player]` | The clicking player's username |
| `[server]` | Makes the command run as the server console instead of the player |

#### Description placeholders

These placeholders can be used inside the `description` field:

| Placeholder | Replaced with |
|---|---|
| `[gamemode]` | Lowercase gamemode name, e.g. `bskyblock`, `aoneblock` |
| `%placeholder%` | Any registered PlaceholderAPI placeholder |

#### Slot layout

The GUI is a chest inventory. Each row has 9 slots (0–8), and the maximum is a 6-row chest with 54 slots (0–53):

```
Row 1:  0  1  2  3  4  5  6  7  8
Row 2:  9 10 11 12 13 14 15 16 17
Row 3: 18 19 20 21 22 23 24 25 26
Row 4: 27 28 29 30 31 32 33 34 35
Row 5: 36 37 38 39 40 41 42 43 44
Row 6: 45 46 47 48 49 50 51 52 53
```

Use a quoted range like `"0-8"` to place the same button across an entire row. This is useful for decorative borders.

## Example: Default and VIP Panels

Below is a practical example showing two panels — a default panel for all players and a VIP panel for donors. It demonstrates slot ranges, multiple click actions, console commands, PlaceholderAPI placeholders, and ItemsAdder icons.

```yaml
panel-list:

  # Default panel — shown to all players
  default:
    defaultPanel: true
    panelName: '&0&l Control Panel'
    permission: 'default'
    buttons:

      # Decorative top border using a slot range
      "0-8":
        name: ' '
        material: BLACK_STAINED_GLASS_PANE
        description: ''
        command: ''

      # Go to island with multiple click actions
      9:
        name: '&a&l Go to Island'
        icon: minecraft:grass_block
        description: |-
          &7 Left-click: teleport to your island
          &7 Right-click: go to nether
          &7 Shift-click: set home
          &7 Island level: &e%Level_[gamemode]_island_level%
        command: '[label] go'
        right_click_command: '[label] go nether'
        shift_click_command: '[label] sethome'

      10:
        name: '&e&l Set Home'
        icon: minecraft:white_bed
        description: |-
          &7 Set your island home
          &7 to your current location.
        command: '[label] sethome'

      11:
        name: '&b&l Team'
        icon: minecraft:player_head
        description: |-
          &7 View and manage
          &7 your island team.
        command: '[label] team'

      13:
        name: '&6&l Settings'
        icon: minecraft:anvil
        description: |-
          &7 Configure your island
          &7 protection settings.
        command: '[label] settings'

      # Console command — runs as server, not player
      17:
        name: '&c&l Report Bug'
        icon: minecraft:writable_book
        description: |-
          &7 Opens a support ticket.
        command: '[server] ticket create [player] bug-report'

  # VIP panel — players need bskyblock.controlpanel.panel.vip
  vip:
    defaultPanel: false
    panelName: '&d&l VIP Control Panel'
    permission: 'vip'
    buttons:

      "0-8":
        name: ' '
        material: PURPLE_STAINED_GLASS_PANE
        description: ''
        command: ''

      9:
        name: '&a&l Go to Island'
        icon: minecraft:grass_block
        description: |-
          &7 Teleport to your island.
        command: '[label] go'

      # VIP exclusive — grants a kit via console
      13:
        name: '&d&l VIP Kit'
        icon: minecraft:chest
        description: |-
          &d VIP exclusive!
          &7 Claim your weekly VIP kit.
        command: '[server] kit vipweekly [player]'

      # ItemsAdder custom icon example
      14:
        name: '&6&l VIP Perks'
        itemsadder: 'iasurvival:vip_star'
        description: |-
          &7 Browse all your VIP perks.
        command: 'vipperks'
```

## Tips

??? tip "Creating decorative borders"
    Use slot ranges with glass panes to create clean borders around your panel. Set `command: ''` and `name: ' '` to make the button non-interactive:
    ```yaml
    "0-8":
      name: ' '
      material: BLACK_STAINED_GLASS_PANE
      description: ''
      command: ''
    ```

??? tip "Running commands as the console"
    Prefix a command with `[server]` to execute it as the server console. This lets you grant kits, run economy commands, or perform admin actions that the player would not have permission to run directly:
    ```yaml
    command: '[server] give [player] diamond 64'
    ```

??? tip "Using multiple panels for ranks"
    Create separate panels for different player groups such as default, VIP, or staff. Assign them using permissions like `bskyblock.controlpanel.panel.vip` or `bskyblock.controlpanel.panel.staff`. Each group sees a tailored panel with the appropriate buttons.

??? tip "Using PlaceholderAPI in descriptions"
    Button descriptions are processed by PlaceholderAPI at the time the panel is opened, so they always show live data. Use `[gamemode]` inside placeholder names so the same template works across gamemodes:
    ```yaml
    description: |-
      &7 Level: &e%Level_[gamemode]_island_level%
      &7 Rank: &6%Level_[gamemode]_island_rank%
      &7 Balance: &a%vault_balance%
    ```

??? tip "Reloading after changes"
    After editing `controlPanelTemplate.yml`, run `/{admin} cp import` to reload. If you've made changes to `config.yml`, use the BentoBox reload command instead: `/{admin} bentobox reload`.

## FAQ

??? question "How can I change the ControlPanel?"
    ControlPanel stores panels in the database, but you edit them through the template file. After making changes to `controlPanelTemplate.yml`, import them by running `/{admin} controlpanel import`. You can also create additional template files and import them by name: `/{admin} controlpanel import myPanels`.

??? question "Can I have different panels for different users?"
    Yes. Define multiple panels in the template file, each with a different `permission` suffix. Then assign players the corresponding permission, e.g. `bskyblock.controlpanel.panel.vip`. Players without a specific panel permission see the panel marked `defaultPanel: true`.

??? question "What icon types are supported?"
    ControlPanel supports three icon types, checked in this priority order: ItemsAdder custom items (`itemsadder` field), BentoBox ItemParser format (`icon` field), and vanilla Minecraft materials (`material` field). If none are specified, the button defaults to paper.

??? question "Can I run a command as the server console?"
    Yes. Prefix the command with `[server]` and it will be executed by the console instead of the player. You can also use `[player]` in the command string to insert the clicking player's name. For example: `[server] give [player] diamond 64`.

??? question "Can a single button do different things depending on how I click it?"
    Yes. Each button supports up to three different commands: `command` for left-click, `right_click_command` for right-click, and `shift_click_command` for shift+left-click. If a specific click command is not set, it falls back to the regular `command`.

??? question "Can you add feature X?"
    Please add it to the list [here](https://github.com/BentoBoxWorld/ControlPanel/issues).

## Translations

{{ translations("ControlPanel") }}

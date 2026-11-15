# Customizing Menus

Most of the menus players see in BentoBox (the team menu, island settings, the Create Island menu, homes, language and more) are built from **panel templates**: YAML files you can edit. You can change the title, the size of the menu, the background, which icon each button uses, its text, and where it sits.

You can't invent new kinds of buttons. Each menu only understands the button types its code provides. For a menu of your own with buttons that run commands, use the [ControlPanel](../../addons/ControlPanel/index.md) addon.

## Where the menu files are

| Menus from | Folder |
|---|---|
| BentoBox | `plugins/BentoBox/panels/` |
| A game mode, for that game mode only | `plugins/BentoBox/addons/<GameMode>/panels/` |
| An addon (Level, Challenges, Warps…) | `plugins/BentoBox/addons/<Addon>/panels/` |

BentoBox writes its templates to `plugins/BentoBox/panels/` the first time each menu is used. Addons write theirs to their own folder.

### BentoBox's menus

| File | Menu | Can a game mode have its own copy? |
|---|---|---|
| `island_creation_panel.yml` | Choosing an island when creating or resetting | Yes |
| `island_homes_panel.yml` | `/island homes` | Yes |
| `language_panel.yml` | `/island language` | Yes |
| `settings_panel.yml` | `/island settings` | Yes |
| `admin_settings_panel.yml` | `/bsbadmin settings` | Yes |
| `command_ranks_panel.yml` | Command Ranks page in the settings menu | Yes |
| `team_panel.yml` | `/island team` | No |
| `team_invite_panel.yml` | The invite screen in the team menu | No |
| `placeholder_panel.yml`, `placeholder_list_panel.yml` | The placeholder browser | No |

**Different menus per game mode:** copy the file from `plugins/BentoBox/panels/` into the game mode's `panels` folder (create the folder if needed) and edit the copy. For example, `plugins/BentoBox/addons/AOneBlock/panels/island_creation_panel.yml` changes the Create Island menu for AOneBlock only. The other game modes keep using the BentoBox version.

### Addon menus

Addons that use templates include Level (`top_panel`, `value_panel`, `detail_panel`, `donation_panel`), Challenges, Biomes, Warps, Upgrades, Likes, Visit, TopBlock, CheckMeOut, MagicCobblestoneGenerator, AOneBlock (`phases_panel`) and CauldronWitchery. Look in each addon's `panels` folder. They use the same format as below.

## Making a change

1. Stop players from opening the menu, or do this on a test server first.
2. Edit the `.yml` file. Keep a copy of the original.
3. Run `/bentobox reload`. This closes open menus and reloads the templates.
4. Open the menu in game and check it.

If a menu stops opening or shows nothing, the YAML is probably invalid. Check the server console for an error and paste the file into a YAML checker. **To get the default back**, delete the file. BentoBox copies its default back the next time the menu opens. For an addon's file, restart the server.

## Common changes

### Change the title or button text

Text can be either plain text or a **locale key**. The default templates use locale keys so the menus are translated:

```yaml
team_panel:
  title: commands.island.team.gui.titles.team-panel
```

- **Change the text in every language:** edit that key in the locale files (`plugins/BentoBox/locales/`, or the addon's `locales` folder). See [Languages & Messages](../../BentoBox/About/Multilingual.md).
- **Use the same text for everyone:** replace the key with your own text, for example `title: "&6My Team"`.

### Change the background or border

```yaml
  background:
    icon: GRAY_STAINED_GLASS_PANE
    title: "&b&r"     # shows no name
  border:
    icon: LIGHT_BLUE_STAINED_GLASS_PANE
    title: "&b&r"
```

Delete the `background` or `border` section to leave those slots empty. `"&b&r"` is the usual way to show an item with no name; Minecraft always shows a tooltip, so it can't be hidden completely.

### Change a button's icon

Set `icon` on the button. Any item works, including items with data, potion colours and player heads. See [Item Format](../../BentoBox/ItemParser.md).

```yaml
      icon: DIAMOND
      icon: tipped_arrow[potion_contents={custom_color:11546150}]
```

Some buttons pick their own icon if you leave `icon` out. For example, the team menu shows the player's head and the Create Island menu shows the island's icon.

### Move a button

Buttons are placed by **row** (1–6) and **column** (1–9) under `content`. To move one, change its row or column number:

```yaml
  content:
    1:        # row 1
      1:      # column 1
        data:
          type: STATUS
```

### Make a menu taller

Menus shrink to fit the rows that have buttons. To keep rows even when they're empty, use `force-shown`:

```yaml
  force-shown: 6        # always show rows 1 to 6
  force-shown: [2, 4]   # always show rows 2 and 4
```

This only adds empty rows. To show **more items per page** (more islands, more homes), add more of the repeating buttons too. The [Bigger Create Island Menu](Bigger-Create-Island-Menu.md) page walks through this.

### Remove a button

Delete the button from `content`. The slot then shows the background. Some buttons are needed for the menu to work: keep `NEXT`/`PREVIOUS` buttons in menus that can have more than one page.

## How a template is laid out

Every template has the same parts. This shortened example is based on the Create Island menu:

```yaml
island_creation_panel:          # must match the file name
  title: panels.island_creation.title
  type: INVENTORY               # INVENTORY (chest), HOPPER (5 slots) or DROPPER (9 slots)
  background:
    icon: BLACK_STAINED_GLASS_PANE
    title: "&b&r"
  border:
    icon: BLACK_STAINED_GLASS_PANE
    title: "&b&r"
  force-shown: []
  content:
    2:
      2: blueprint_bundle_button    # a name refers to a button in `reusable`
      3: blueprint_bundle_button
    3:
      9:                            # or define the button right here
        icon: ARROW
        title: panels.buttons.next.name
        description: panels.buttons.next.description
        data:
          type: NEXT
        actions:
          next:
            click-type: UNKNOWN
            tooltip: panels.tips.click-to-next
  reusable:
    blueprint_bundle_button:
      title: panels.island_creation.buttons.bundle.name
      description: panels.island_creation.buttons.bundle.description
      data:
        type: BUNDLE
      actions:
        select:
          click-type: UNKNOWN
          tooltip: panels.tips.click-to-choose
```

### Button settings

| Setting | What it does |
|---|---|
| `icon` | The item shown. See [Item Format](../../BentoBox/ItemParser.md) |
| `title` | The item's name: text or a locale key |
| `description` | The lines under the name: text or a locale key |
| `data` | **What the button is.** `type` picks the button type (see below). Some types take extra settings, for example `tab` on a settings tab button |
| `actions` | What each click does, and the tooltip line added for it |
| `fallback` | Another button to show when this one can't be shown, for example when there's nothing left to fill a slot on the last page. It can be a full button or the name of a `reusable` button. Needs BentoBox 3.23.0 or later |

### Repeating buttons (`reusable`)

Menus that list things (islands, homes, team members, languages, flags) use one button design for every entry. Define it once under `reusable` and put its name in each slot where an entry can appear. The menu fills those slots in order and pages through the rest.

### Click actions

Each action has a name, a click type and a tooltip:

```yaml
        actions:              # the team menu's member button
          kick:
            click-type: SHIFT_RIGHT
            tooltip: commands.island.team.gui.tips.SHIFT_RIGHT.kick
          setowner:
            click-type: SHIFT_LEFT
            tooltip: commands.island.team.gui.tips.SHIFT_LEFT.setowner
```

- `click-type` is a Minecraft click: `LEFT`, `RIGHT`, `SHIFT_LEFT`, `SHIFT_RIGHT`, `MIDDLE`, `DROP` and so on. `UNKNOWN` means any click.
- The action name (`kick`, `setowner`) is what the menu does. Use the names already in the default file. You can change which click triggers an action, or remove an action you don't want players to use from the menu.
- Tooltips are added below the description, in the order the actions are listed.

### Button types in BentoBox's menus

| Menu | Button types (`data: type:`) |
|---|---|
| Create Island | `BUNDLE`, `NEXT`, `PREVIOUS` |
| Homes | `ISLAND`, `NEXT`, `PREVIOUS` |
| Language | `LOCALE`, `NEXT`, `PREVIOUS` |
| Team | `STATUS`, `MEMBER`, `RANK`, `INVITE`, `INVITED` |
| Team invite | `PROSPECT`, `SEARCH`, `BACK`, `NEXT`, `PREVIOUS` |
| Settings / admin settings | `FLAG`, `TAB`, `MODE`, `RESET`, `NEXT`, `PREVIOUS` |
| Command ranks | `COMMAND`, `NEXT`, `PREVIOUS` |
| Placeholders | `BENTOBOX`, `ADDON`, `PLACEHOLDER`, `BACK`, `NEXT`, `PREVIOUS` |

The default files have comments explaining each one. The settings menus are covered in detail in [Protection, Flags & Ranks](../../BentoBox/Island-Protection,-Flags-&-Ranks.md#customizing-the-settings-panel).

## Troubleshooting

**My change doesn't show.**
Run `/bentobox reload`, then reopen the menu. If the game mode has its own copy in `addons/<GameMode>/panels/`, that copy is used instead of the one in `plugins/BentoBox/panels/`.

**The menu is empty or won't open after editing.**
The YAML is invalid or the top-level name no longer matches the file name. Check the console, fix the file, or delete it to get the default back.

**I added rows but nothing appears in them.**
`force-shown` only adds space. Add the repeating button (for example `blueprint_bundle_button`) to the new slots.

**Text shows as `commands.island.…` instead of words.**
That key is missing from the locale file for the player's language. Add it, or use plain text instead.

**I want a button that runs a command.**
Templates can't do this. Use the [ControlPanel](../../addons/ControlPanel/index.md) addon.

## See also

- [Bigger Create Island Menu](Bigger-Create-Island-Menu.md): a full worked example
- [Item Format](../../BentoBox/ItemParser.md): writing icons
- [Languages & Messages](../../BentoBox/About/Multilingual.md): changing menu text
- [Templated Panel API](../api/Templated-Panel.md): for developers adding templates to their own addons

# Making the Create Island menu bigger (more rows)

**Question:** "Is it possible to get a bigger *Create Island* menu — up to 5 or 6 rows instead of the default 3?"

**Answer:** Yes. The Create Island menu is a fully [customizable GUI](Customizable-GUI.md). You control how many rows it has and how many blueprint bundles appear on each page by editing the `island_creation_panel.yml` template. This page shows you exactly how.

First decide which of these you actually want, because they need different changes:

- **Just want the menu to *look* taller** (more rows of space, e.g. for a framed/roomy look) → use the one-line [`force-shown` shortcut](#just-want-a-taller-menu-force-shown) below. The extra rows will be empty background.
- **Want more islands visible at once / fewer pages** → you need to [add more bundle buttons](#example-a-6-row-menu). `force-shown` alone will *not* do this.

## Just want a taller menu? (`force-shown`)

If all you want is a taller menu — more visible rows, without necessarily fitting more islands on screen — this is a one-line change. Add (or edit) the `force-shown` line in `island_creation_panel.yml`:

```yaml
force-shown: 6
```

`force-shown: 6` forces rows 1 through 6 to always render, giving you a full **6-row (54-slot)** panel. Use `5` for 5 rows, and so on.

**Important:** `force-shown` controls the panel **height only**. The extra rows it opens up are filled with your `background`/`border` item — they do **not** contain more island bundles. The bundles still appear only where `blueprint_bundle_button` entries exist in the `content` section. So if your goal is to show *more islands at once* (not just make the box bigger), skip ahead to [the 6-row example](#example-a-6-row-menu), which adds the extra bundle buttons too.

## Background: how the menu is built

The Create Island menu (and the identical menu shown when a player resets their island) is generated from a panel template called `island_creation_panel.yml`. BentoBox ships a default version with **3 rows** and up to **7 bundle buttons per page** (with a "previous"/"next" arrow pair for paging when there are more bundles than fit).

Two rules decide how many rows the player actually sees:

1. **The panel grows to fit its content.** A row appears if it contains at least one button. Internally the grid is always 6 rows, but empty rows are trimmed away, so the default template only *looks* like 3 rows because rows 1, 5 and 6 are empty.
2. **`force-shown` can pin rows open** even when they are empty (useful for keeping a fixed layout while your bundle list grows).

So to get a bigger menu you simply add more `blueprint_bundle_button` entries on more rows. There is a hard maximum of **6 rows** (54 slots) because that is the largest a Minecraft chest inventory can be.

## Where to put the file

The menu can be overridden at two levels. BentoBox looks for the file in this order:

1. **Per game mode** (recommended) — `plugins/<GameMode>/panels/island_creation_panel.yml`
   e.g. `plugins/AcidIsland/panels/island_creation_panel.yml`, `plugins/BSkyBlock/panels/island_creation_panel.yml`.
   This only affects that one game mode.
2. **Global fallback** — `plugins/BentoBox/panels/island_creation_panel.yml`
   Used for any game mode that does not have its own copy.

If neither file exists, the built-in default (inside the BentoBox jar) is used.

> **Tip:** Copy the default file rather than writing one from scratch. Start the server once so BentoBox writes out its defaults, then copy `plugins/BentoBox/panels/island_creation_panel.yml` into your game mode's `panels/` folder and edit it there. Reload with `/bentobox reload` (or restart) after saving.

## Example: a 6-row menu

This template shows a full 6-row menu with a bordered layout. Rows 2–5 hold blueprint bundle buttons (up to **28** bundles per page), and row 6 holds the paging arrows.

```yaml
island_creation_panel:
  title: panels.island_creation.title
  type: INVENTORY
  background:
    icon: BLACK_STAINED_GLASS_PANE
    title: "&b&r"
  border:
    icon: BLACK_STAINED_GLASS_PANE
    title: "&b&r"
  # Pin all 6 rows open even if some are empty. Use [] to let the panel
  # auto-size to its content instead.
  force-shown: 6
  content:
    2:
      2: blueprint_bundle_button
      3: blueprint_bundle_button
      4: blueprint_bundle_button
      5: blueprint_bundle_button
      6: blueprint_bundle_button
      7: blueprint_bundle_button
      8: blueprint_bundle_button
    3:
      2: blueprint_bundle_button
      3: blueprint_bundle_button
      4: blueprint_bundle_button
      5: blueprint_bundle_button
      6: blueprint_bundle_button
      7: blueprint_bundle_button
      8: blueprint_bundle_button
    4:
      2: blueprint_bundle_button
      3: blueprint_bundle_button
      4: blueprint_bundle_button
      5: blueprint_bundle_button
      6: blueprint_bundle_button
      7: blueprint_bundle_button
      8: blueprint_bundle_button
    5:
      2: blueprint_bundle_button
      3: blueprint_bundle_button
      4: blueprint_bundle_button
      5: blueprint_bundle_button
      6: blueprint_bundle_button
      7: blueprint_bundle_button
      8: blueprint_bundle_button
    6:
      1:
        icon: tipped_arrow[potion_contents={custom_color:11546150}]
        title: panels.buttons.previous.name
        description: panels.buttons.previous.description
        data:
          type: PREVIOUS
          indexing: true
        actions:
          previous:
            click-type: UNKNOWN
            tooltip: panels.tips.click-to-previous
      9:
        icon: tipped_arrow[potion_contents={custom_color:8439583}]
        title: panels.buttons.next.name
        description: panels.buttons.next.description
        data:
          type: NEXT
          indexing: true
        actions:
          next:
            click-type: UNKNOWN
            tooltip: panels.tips.click-to-next
  reusable:
    blueprint_bundle_button:
      # icon: GRASS_BLOCK   # Uncomment to force one icon for every bundle;
                            # otherwise each bundle uses its own configured icon.
      title: panels.island_creation.buttons.bundle.name
      description: panels.island_creation.buttons.bundle.description
      data:
        type: BUNDLE
      actions:
        select:
          click-type: UNKNOWN
          tooltip: panels.tips.click-to-choose
```

### Want a 5-row menu instead?

Delete row `5` from `content` and change `force-shown: 6` to `force-shown: 5`. Move the paging arrows up to row `5` if you like. Any row count from 1 to 6 works the same way — just add or remove rows of `blueprint_bundle_button` entries.

## How the pieces work

| Setting | What it does |
|---|---|
| `content` rows `1`–`6` | Each key `1`–`6` is a row; each nested key `1`–`9` is a column. A row is only shown if it has content (or is forced). |
| `blueprint_bundle_button` | A reusable button of `type: BUNDLE`. The **number of these buttons in the template = the number of bundles shown per page.** Add more to fit more bundles at once. |
| `force-shown` | `force-shown: 6` forces rows 1 through 6 to always render (fixed height). `force-shown: [2,4]` forces only rows 2 and 4. `force-shown: []` (or omitting it) lets the panel auto-size to its content. |
| `type: PREVIOUS` / `type: NEXT` | The paging arrows. They only appear when there are more bundles than fit on one page, so it is safe to always include them. |
| `unique_id` (optional) | Adding `unique_id: <bundleId>` under a button's `data:` pins one specific bundle to that exact slot instead of filling slots in order. |

## Common questions

**"I added rows but the menu is still small."**
A row only shows if it has a button in it *or* it is listed in `force-shown`. Make sure each new row actually contains `blueprint_bundle_button` entries, and check the YAML indentation (rows and columns are numeric keys nested under `content`).

**"Can I go bigger than 6 rows?"**
No. 6 rows / 54 slots is the maximum size of a Minecraft chest GUI, so it is the hard limit for an `INVENTORY` type panel.

**"My changes did nothing."**
Confirm the file is in the correct folder for the game mode you are testing (per-mode folder wins over the global BentoBox one), the file is named exactly `island_creation_panel.yml`, and you ran `/bentobox reload` or restarted the server after editing. A YAML syntax error will make BentoBox fall back to the built-in default — check the server console for warnings on startup.

**"Does this also change the menu when players *reset* their island?"**
Yes. The reset island menu uses the same `island_creation_panel.yml` template.

## See also

- [Customizable GUIs](Customizable-GUI.md) — the general system these menus are built on, including the full list of item/icon options.
- [ItemParser](https://docs.bentobox.world/en/latest/BentoBox/ItemParser/) — the syntax for the `icon:` field.

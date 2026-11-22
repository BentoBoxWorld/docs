# Languages & Messages

Every message, menu and item name in BentoBox and its addons comes from **locale files**: one YAML file per language. Players pick their own language, and you can change any text, colour, or how a message is shown (chat, action bar, title, sound).

## Languages

BentoBox ships with 25 languages:

| Language | File | Language | File |
|---|---|---|---|
| English (default) | `en-US` | Italian | `it` |
| Chinese (Simplified) | `zh-CN` | Japanese | `ja` |
| Chinese (Traditional, Hong Kong) | `zh-HK` | Korean | `ko` |
| Chinese (Traditional, Taiwan) | `zh-TW` | Latvian | `lv` |
| Croatian | `hr` | Polish | `pl` |
| Czech | `cs` | Portuguese | `pt` |
| Dutch | `nl` | Portuguese (Brazil) | `pt-BR` |
| French | `fr` | Romanian | `ro` |
| German | `de` | Russian | `ru` |
| Hungarian | `hu` | Spanish | `es` |
| Indonesian | `id` | Turkish | `tr` |
| | | Ukrainian | `uk` |
| | | Vietnamese | `vi` |

Addons may have fewer. Each [game mode](../../gamemodes/Comparison.md) and [addon](Addons.md) page has a table showing how complete each language is.

### The server's default language

New players see the default language until they choose one. Set it in BentoBox's `config.yml`, using a file name from the table:

```yaml
general:
  default-language: en-US
```

Then restart or run `/bentobox reload`. BentoBox doesn't detect a player's Minecraft language automatically.

### Players choosing a language

Players change language with **`/island language`** (or the game mode's own command), which opens a menu of the languages installed. Their choice applies to BentoBox and all addons, in every game mode.

If a message is missing from the player's language, BentoBox uses the server's default language, then English.

## Changing messages

The locale files are in:

| Text from | Folder |
|---|---|
| BentoBox | `plugins/BentoBox/locales/BentoBox/` |
| A game mode or addon | `plugins/BentoBox/locales/<AddonName>/`, for example `locales/BSkyBlock/` |

To change a message:

1. Find it: search the language file (for example `en-US.yml`) for the text players see.
2. Change the text after the key, keeping the key and indentation. Leave anything in square brackets, like `[name]`, `[number]` or `[prefix_island]`, as it is; those are filled in by BentoBox. (`[prefix_island]` becomes the game mode's word for an island, such as "island", "cave" or "box".)
3. Run `/bentobox reload locales`.

```yaml
commands:
  island:
    create:
      creating-island: "<green>Building your [prefix_island], hang tight...</green>"
```

Change every language your players use, or the others will still show the old text.

**Your changes are kept when you update.** When BentoBox or an addon is updated, new messages are added to the files on your server, but messages already there aren't overwritten. This also means that if an update improves a message's wording, you won't see it until you delete that line (or the whole file) and reload.

**To hide a message**, set it to an empty string: `creating-island: ""`. Empty messages aren't sent.

**To check for missing translations**, run `/bentobox locale`. It compares each language file, for BentoBox and every addon, with English and reports what's missing.

## Colours and formatting

Messages use [MiniMessage](https://docs.advntr.dev/minimessage/format.html) tags:

```yaml
example: "<green>Welcome to the island!</green>"
example: "<bold><red>Warning!</red></bold> Something happened."
example: "<gradient:gold:yellow>Island Name</gradient>"
```

Old-style colour codes (`&a`, `&l`, `§c`) still work.

## How a message is shown

By default a message goes to chat. Start it with a tag to show it somewhere else:

| Tag | Shows the message |
|---|---|
| `[actionbar]` | Above the hotbar |
| `[title]` | As a big title in the middle of the screen. Add `[subtitle]` to put text in a smaller line underneath |
| `[sound:name:volume:pitch]` | Plays a sound as well. Volume and pitch are optional. Use Minecraft sound names with underscores, for example `entity_experience_orb_pickup` |

```yaml
example: "[actionbar]Teleporting..."
example: "[title]Teleporting...[subtitle]Wait a second."
example: "[sound:entity_experience_orb_pickup:1:1][title]Teleporting...[subtitle]Wait a second."
```

Messages to the console always go to the console log.

### Clickable messages

Add these anywhere in a message to make the whole message clickable or show text on hover:

| Tag | Effect |
|---|---|
| `[run_command: /command]` | Clicking runs the command |
| `[suggest_command: /command]` | Clicking puts the command in the chat box |
| `[open_url: https://...]` | Clicking opens a link |
| `[copy_to_clipboard: text]` | Clicking copies the text |
| `[hover: text]` | Shows the text when the player hovers over the message |

```yaml
example: "You're not on your island. Click to go home![run_command: /island go][hover: Teleport home]"
```

## Menu text

Menu titles and button text are also in the locale files, referenced from the menu templates. See [Customizing Menus](../../Tutorials/generic/Customizable-GUI.md#change-the-title-or-button-text).

## Fixing or adding translations

Translations are made with AI help and corrected by the community. If you spot a mistake, fix it in the locale file in the project's GitHub repository and open a pull request, or tell us on [Discord](https://discord.bentobox.world). See [Translating BentoBox](../Translate-BentoBox-and-addons.md) for guidelines and each project's translation status.

## Troubleshooting

**My change didn't show.**
Run `/bentobox reload locales`. Check that you edited the player's language (they may not be using English) and the right folder (BentoBox's own messages are in `locales/BentoBox/`, game mode messages in `locales/<GameMode>/`).

**The server shows `commands.island...` instead of a message.**
The key is missing in the player's language, the server's default language and English. Delete the file so BentoBox writes a fresh copy, or add the key back.

**After an update, a message still has the old wording.**
Your file keeps the old text. Delete that line or the whole file and run `/bentobox reload locales`.

**Every rank in a protection flag's tooltip is the same colour, or flags have no "Left click / Right click" hints.**
The locale files were first written by an old BentoBox and still have the old text. BentoBox 3.23.7 shows the rank colours correctly again with old files, but only fresh files have the click hints and every later wording fix. To refresh them: stop the server, rename `plugins/BentoBox/locales/BentoBox/` (for example to `BentoBox-old`), start the server so the current files are written, then copy your own edits back across. The same works for an addon's folder in `plugins/BentoBox/locales/<AddonName>/`.

**The YAML file won't load after editing.**
Usually a missing quote or wrong indentation. Put messages containing `:` or `#` in quotes, and check the console for the line number.

## Available locales

{{ translations(2855, ["cs", "de", "es", "fr", "hu", "id", "it", "ja", "lv", "pl", "pt", "ro", "ru", "tr", "vi", "zh-CN", "zh-HK", "zh-TW", "hr", "ko", "uk", "nl"]) }}

## MiniMessage Formatting

BentoBox uses [MiniMessage](https://docs.advntr.dev/minimessage/format.html) for all locale strings. This means you can use MiniMessage tags in your translations to apply rich text formatting. For example:

```yaml
my-message: "<green>Welcome to the island!</green>"
my-message: "<bold><red>Warning!</red></bold> Something happened."
my-message: "<gradient:gold:yellow>Island Name</gradient>"
```

Legacy `§` color codes are still supported for backwards compatibility and will be automatically converted to MiniMessage format when loaded.

## Message Delivery Tags

Locale strings can control how messages are delivered to players using special inline tags. When no delivery tag is present, the message is sent in chat (the default behavior).

### `[actionbar]`

Sends the message as an **action bar** message (the text displayed above the hotbar).

```yaml
island-go: "[actionbar]Teleporting..."
```

### `[title]` and `[subtitle]`

Sends the message as a **title** overlay on screen. Use `[title]` for the large text and `[subtitle]` for the smaller text below it. They can be used together in the same string.

```yaml
island-go: "[title]Teleporting...[subtitle]Wait a second."
```

### `[sound:name:volume:pitch]`

Plays a **sound** for the player. Volume and pitch are optional (default `1.0`). Use underscore-separated sound names from the Bukkit/Minecraft sound list (e.g. `entity_experience_orb_pickup`). The sound tag can be combined with any delivery type tag.

```yaml
island-go: "[sound:entity_experience_orb_pickup:1:1][title]Teleporting...[subtitle]Wait a second."
```

!!! note
    Non-player senders (e.g. the console) will fall back to chat output when action bar or title tags are used.

## Guidelines

* We now have a tool to enable translations of file at [https://download.bentobox.world/translate.html](https://download.bentobox.world/translate.html). This runs localling in your browser and may help translation. Submit new files as PRs on GitHub.
* Translators get a special badge!
* Do not translate text inside square brackets because those are placeholders, e.g. [name] should remain in English
* Test your translations - try to check everything you can before submitting it
* Do not include any advertising, swear words, or derogatory comments in the translations. We do check them before accepting the PR.
* Feel free to ask questions on Discord about translations.

## Addons
- [AcidIsland](/gamemodes/AcidIsland/#translations)
- [BSkyBlock](/gamemodes/BSkyBlock/#translations)
- [CaveBlock](/gamemodes/CaveBlock/#translations)
- [SkyGrid](/gamemodes/SkyGrid/#translations)
- [Biomes](/addons/Biomes/#translations)
- [Border](/addons/Border/#translations)
- [CauldronWitchery](/addons/CauldronWitchery/#translations)
- [Challenges](/addons/Challenges/#translations)
- [Chat](/addons/Chat/#translations)
- [ControlPanel](/addons/ControlPanel/#translations)
- [DimensionalTrees](/addons/DimensionalTrees/#translations)
- ~~[ExtraMobs](Addons)~~
- [Greenhouses](/addons/Greenhouses/#translations)
- [IslandFly](/addons/IslandFly/#translations)
- ~~[InvSwitcher](Addons)~~
- [Level](/addons/Level/#translations)
- [Likes](/addons/Likes/#translations)
- [Limits](/addons/Limits/#translations)
- [MagicCobblestoneGenerator](/addons/MagicCobblestoneGenerator/#translations)
- ~~[TwerkingForTrees](Addons)~~
- [VoidPortals](/addons/VoidPortals/#translations)

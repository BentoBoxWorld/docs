## Available locales

{{ translations("BentoBox") }}

## MiniMessage Formatting

BentoBox uses [MiniMessage](https://docs.advntr.dev/minimessage/format.html) for all locale strings. This means you can use MiniMessage tags in your translations to apply rich text formatting. For example:

```yaml
my-message: "<green>Welcome to the island!</green>"
my-message: "<bold><red>Warning!</red></bold> Something happened."
my-message: "<gradient:gold:yellow>Island Name</gradient>"
```

Legacy `§` or `&` color codes are still supported for backwards compatibility and will be automatically converted to MiniMessage format when loaded.

## Message Delivery Tags

Locale strings can control how messages are delivered to players using special inline tags. When no delivery tag is present, the message is sent in chat (the default behavior).

### `[actionbar]`

Sends the message as an **action bar** message (the text displayed above the hotbar).

```yaml
island-go: "[actionbar]Teleporting..."
```

### `[title]` and `[subtitle]`

Sends the message as a **title** overlay on screen. `[title]` displays the large heading text and `[subtitle]` displays smaller text below it. `[subtitle]` is not a standalone delivery type — it only works as a separator inside a `[title]` message. Without `[title]`, it falls through to the chat path.

```yaml
# Title with subtitle
island-go: "[title]Teleporting...[subtitle]Wait a second."
# Title only (empty title, text as subtitle)
scooping: "[title][subtitle]You scooped the lava!"
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

## Game Modes

- [AcidIsland](../gamemodes/AcidIsland/index.md#translations)
- [AOneBlock](../gamemodes/AOneBlock/index.md#translations)
- [Boxed](../gamemodes/Boxed/index.md#translations)
- [BSkyBlock](../gamemodes/BSkyBlock/index.md#translations)
- [CaveBlock](../gamemodes/CaveBlock/index.md#translations)
- [Poseidon](../gamemodes/Poseidon/index.md#translations)
- [SkyGrid](../gamemodes/SkyGrid/index.md#translations)
- [Stranger Realms](../gamemodes/StrangerRealms/index.md#translations)

## Addons

- [Bank](../addons/Bank/index.md#translations)
- [Biomes](../addons/Biomes/index.md#translations)
- [Border](../addons/Border/index.md#translations)
- [CauldronWitchery](../addons/CauldronWitchery/index.md#translations)
- [Challenges](../addons/Challenges/index.md#translations)
- [Chat](../addons/Chat/index.md#translations)
- [CheckMeOut](../addons/CheckMeOut/index.md#translations)
- [ControlPanel](../addons/ControlPanel/index.md#translations)
- [DimensionalTrees](../addons/DimensionalTrees/index.md#translations)
- [ExtraMobs](../addons/ExtraMobs/index.md#translations)
- [FarmersDance](../addons/FarmersDance/index.md#translations)
- [Greenhouses](../addons/Greenhouses/index.md#translations)
- [InvSwitcher](../addons/InvSwitcher/index.md#translations)
- [IslandFly](../addons/IslandFly/index.md#translations)
- [Level](../addons/Level/index.md#translations)
- [Likes](../addons/Likes/index.md#translations)
- [Limits](../addons/Limits/index.md#translations)
- [MagicCobblestoneGenerator](../addons/MagicCobblestoneGenerator/index.md#translations)
- [TopBlock](../addons/TopBlock/index.md#translations)
- [TwerkingForTrees](../addons/TwerkingForTrees/index.md#translations)
- [Upgrades](../addons/Upgrades/index.md#translations)
- [Visit](../addons/Visit/index.md#translations)
- [VoidPortals](../addons/VoidPortals/index.md#translations)
- [Warps](../addons/Warps/index.md#translations)

# Multilingual Support

BentoBox and its addons support a wide range of languages out of the box. All in-game messages, GUI text, and item names that players see can be shown in their own language — no extra plugins needed.

## Supported Languages

BentoBox currently ships with translations for:

| Language | Code |
|---|---|
| English (default) | `en-US` |
| Chinese (Simplified) | `zh-CN` |
| Chinese (Traditional, HK) | `zh-HK` |
| Chinese (Traditional, TW) | `zh-TW` |
| Croatian | `hr` |
| Czech | `cs` |
| Dutch | `nl` |
| French | `fr` |
| German | `de` |
| Hungarian | `hu` |
| Indonesian | `id` |
| Italian | `it` |
| Japanese | `ja` |
| Korean | `ko` |
| Latvian | `lv` |
| Polish | `pl` |
| Portuguese | `pt` |
| Romanian | `ro` |
| Russian | `ru` |
| Spanish | `es` |
| Turkish | `tr` |
| Ukrainian | `uk` |
| Vietnamese | `vi` |

Individual addons may support a different subset of languages. Check each addon's page for its specific translation status.

## Setting the Default Language

To set the language all players see by default, edit BentoBox's `config.yml`:

```yaml
# Default language for new players.
# Refer to the /locale folder in the BentoBox plugin folder for available languages.
default-language: en-US
```

Set this to any language code from the table above. After changing it, reload the server or run `/bentobox reload`.

## Player Language Selection

If enabled, players can switch to their own preferred language using:
```
/bentobox locale
```

This is useful on international servers where the player base speaks multiple languages.

## Translations Are Community-Made

The translations for BentoBox and its addons are contributed by the community. The BentoBox team cannot review every translation in depth, but all contributions are checked for quality before being accepted.

!!! note "Translation quality"
    Because translations are community-contributed, quality varies. If you spot errors in a translation, please help improve it!

## How to Contribute a Translation

If your language is not yet available, or if the existing translation needs improvement:

1. Visit the translation page for BentoBox or the specific addon on [GitLocalize](https://gitlocalize.com/repo/2855).
2. Select your language (or request a new one on our [Discord](https://discord.bentobox.world)).
3. Translate the strings — do **not** translate text inside square brackets, e.g. `[name]` should stay as-is.
4. Submit your work. Translators earn a special community badge!

A translation helper tool is available at [download.bentobox.world/translate.html](https://download.bentobox.world/translate.html) — it runs entirely in your browser.

See the full list of addon translation pages at [Translate BentoBox and Addons](../Translate-BentoBox-and-addons.md).

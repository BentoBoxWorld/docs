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

Most translations are now generated with the help of AI, so the bulk of the
work is already done — but **AI is not perfect**. The most valuable thing the
community can do is **report errors** and **suggest corrections**.

* **Spotted a mistake?** Open an issue or a PR on the relevant repository at
  [bentobox.world](https://bentobox.world) (a short link to our GitHub org),
  or tell us on [Discord](https://discord.bentobox.world).
* **Want to correct a string?** Edit the locale file under
  `src/main/resources/locales/` in the relevant repo and open a PR. Do **not**
  translate text inside square brackets — e.g. `[name]` should stay as-is.
* **Want to add a brand-new language?** Open a PR adding a new locale file
  alongside the existing ones, or ask on Discord and we'll get you started.

A translation helper tool is available at
[download.bentobox.world/translate.html](https://download.bentobox.world/translate.html)
— it runs entirely in your browser. Translators earn a special community badge!

See the full list of addon translation pages at [Translate BentoBox and Addons](../Translate-BentoBox-and-addons.md).

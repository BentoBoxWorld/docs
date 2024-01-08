# ControlPanel

**ControlPanel** lets you create a GUI that serves as a shortcut for players.

Created and maintained by [BONNe](https://github.com/BONNe).

{{ addon_description("ControlPanel") }}

## Installation

1. Place the addon jar in the addons folder of the BentoBox plugin
2. Restart the server
3. Use admin command to import control panels.


## FAQ

??? question "How can I change ControlPanel?"
    ControlPanel stores all GUI's in the database, but this does not mean you need to edit database file. You still can use template file, however, to see your changes, you need to import the file: `/[admin_cmd] controlpanel import <filename>`.

??? question "Can I have different panels for different users?"
    Yes, ControlPanel supports the option to allow multiple different panels. To activate a certain panel for a user, you must add permission: `[gamemode].controlpanel.panel.[suffix]` where suffix is an ID name for your ControlPanel.

??? question "Can you add a feature X?"
    Please add it to the list [here](https://github.com/BentoBoxWorld/ControlPanel/issues).

## Translations

{{ translations(3135, ["cs", "de", "es", "fr", "lv", "zh-CN", "zh-TW", "ko", "pl", "ru", "id", ]) }}

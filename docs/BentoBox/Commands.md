BentoBox implements a few commands to help you manage your whole BentoBox installation.

**Available commands (as of 2.2.0)**

| Command                                 | Permission                   | Description                                                 |
|-----------------------------------------|------------------------------|-------------------------------------------------------------|
| /bentobox [help/h]                      | bentobox.admin               | Displays all available BentoBox commands                    |
| /bentobox about                         | bentobox.about               | Displays copyright and license information                  |
| /bentobox catalog                       | bentobox.admin.catalog       | Displays the Catalog                                        |
| /bentobox locale                        | bentobox.admin.locale        | Performs localization files analysis                        |
| /bentobox manage/overview               | bentobox.admin.manage        | Displays the Management Panel                               |
| /bentobox migrate                       | bentobox.admin.migrate       | Migrates data from one database to another                  |
| /bentobox perms                         | bentobox.admin.perms         | Displays the effective perms for BentoBox and Addons in a YAML format |
| /bentobox rank [list \| add \| remove] [rank reference] [rank value] | bentobox.admin.rank | list, add, or remove ranks              |
| /bentobox reload/rl                     | bentobox.admin.reload        | Reloads BentoBox and all addons, settings and locales       |
| /bentobox version/v/versions/addons     | bentobox.version             | Displays BentoBox and addons versions                       |

An alias for `/bentobox` is `/bbox`.

When filing bug reports or asking for support, you **must** provide the output of the `/bentobox version` command so that we know what version of the software, database and addons you are using.
# BentoBox Permissions

Permissions listed here are for BentoBox. Addons register their own permissions.

**BentoBox permissions (as of 1.6.0)**

| Permission             | Parent permission | Default value | Description                            |
|------------------------|-------------------|---------------|----------------------------------------|
| bentobox.admin         |                   | op            | Allows most of BentoBox commands usage |
| bentobox.admin.catalog | bentobox.admin    | op            | Allows to use /bentobox catalog        |
| bentobox.admin.locale  | bentobox.admin    | op            | Allows to use /bentobox locale         |
| bentobox.admin.manage  | bentobox.admin    | op            | Allows to use /bentobox manage         |
| bentobox.admin.migrate | bentobox.admin    | op            | Allows to use /bentobox migrate        |
| bentobox.admin.reload  | bentobox.admin    | op            | Allows to use /bentobox reload         |
| bentobox.about         |                   | true          | Allows to use /bentobox about          |
| bentobox.version       |                   | true          | Allows to use /bentobox version        |
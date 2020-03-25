#### LikesAddon permissions (as of 1.7.0)

| Permission                      | Parent permission     | Default value | Description                                          |
|---------------------------------|-----------------------|---------------|------------------------------------------------------|
| [gamemode].likes                |                       | true          | Allows to use `/[gamemode_user] likes`               |
| [gamemode].likes.top            | [gamemode].likes      | true          | Allows to use `/[gamemode_user] likes top`           |
| [gamemode].likes.view           | [gamemode].likes      | true          | Allows to use `/[gamemode_user] likes view`          |
| [gamemode].likes.view.others    | [gamemode].likes.view | op            | Allows to use `/[gamemode_user] likes view <player>` |
| [gamemode].likes.bypass-cost    | [gamemode].likes      | op            | Allows to  bypass payment for liking and disliking   |
| [gamemode].likes.admin          |                       | op            | Allows to use `/[gamemode_admin] likes`              |
| [gamemode].likes.admin.settings | [gamemode].likes.admin| op            | Allows to use `/[gamemode_admin] likes settings`     |
| [gamemode].likes.icon.X         |                       |               | Allows to set custom icon (x is Material) for player |
# Chat

**Chat** provides a **Team Chat** and **Island Chat** to let your players talk privately to their visitors or fellow island members.

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("Chat") }}

## Island chat

When enabled, chat is limited to just players on the island, including visitors. Admins or mods can listen into island chats using a spy command.

## Team chat

When enabled, chats will go only to team members. Team players can toggle whether their chat will go onto the team chat channel or not. Admins can listen into all team chats using a spy command.

## Commands
### Player commands

* `chat` - toggles island chat on and off
* `teamchat` - toggles whether player's chat goes to the team channel or not

### Admin commands

* `chatspy` - toggles island chat on and off
* `teamchatspy` - toggles whether player's chat goes to the team channel or not

The config also has settings to log all chats if required.

## Configuration

```
# Configuration file for Chat
team-chat:
  gamemodes:
  - BSkyBlock
  - AcidIsland
  - CaveBlock
  - SkyGrid
  # Log team chats to console.
  log: false
island-chat:
  # Lists the gamemodes in which you want the Chat addon to be effective.
  gamemodes:
  - BSkyBlock
  - AcidIsland
  - CaveBlock
  - SkyGrid
  # Log island chats to console.
  log: false
chat-listener:
  # Sets priority of AsyncPlayerChatEvent. Change this if Chat addon
  # is conflicting with other plugins which listen to the same event
  # Acceptable values: lowest, low, normal, high, highest, monitor
  priority: normal
```

## Permissions

```
permissions:
  '[gamemode].chat.team-chat':
    description: Player can use team chat
    default: true
  '[gamemode].chat.island-chat':
    description: Player can use island chat
    default: true
  '[gamemode].chat.spy':
    description: Player can use team or island chat spy
    default: op

```

## Like this addon?
You can [sponsor](https://github.com/sponsors/tastybento) to get more addons like this and make this one better!

## Translations

{{ translations(3680, ["cs", "de", "es", "fr", "ja", "tr", "zh-CN", "hu", "it", "lv", "pl", "ru", "vi"]) }}

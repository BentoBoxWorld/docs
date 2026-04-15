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
* `muteteamchat` (alias `mtc`) - silences incoming team chat messages without disabling team chat. Requires the `[gamemode].chat.team-chat.mute` permission. Mute state is cleared automatically when the player leaves or is kicked from their team.

### Admin commands

* `chatspy` - toggles island chat spy on and off
* `teamchatspy` - toggles team chat spy on and off

The config also has settings to log all chats if required.

## Configuration

```yaml
# Configuration file for Chat
team-chat:
  # Lists the gamemodes in which you want the Team Chat to be effective.
  gamemodes:
  - BSkyBlock
  - AcidIsland
  - CaveBlock
  - SkyGrid
  # If players are outside a game world, team chat can still exist for one game mode.
  default-teamchat-gamemode: ''
  # Additional worlds (per game mode) where team chat should be captured.
  # Useful for shared spawn/hub worlds where players still want team chat to work.
  # If more than one game mode covers a world, chat may go to multiple teams.
  # Example:
  #   extra-chat-worlds:
  #     BSkyBlock:
  #       - world
  #       - world_nether
  #       - spawn_world
  extra-chat-worlds: {}
  # Log team chats to console.
  log: false
island-chat:
  # Lists the gamemodes in which you want the Island Chat to be effective.
  gamemodes:
  - BSkyBlock
  - AcidIsland
  - CaveBlock
  - SkyGrid
  # Log island chats to console.
  log: false
chat-listener:
  # Sets priority of AsyncPlayerChatEvent. Change this if Chat addon
  # is conflicting with other plugins which listen to the same event.
  # Acceptable values: lowest, low, normal, high, highest, monitor
  priority: NORMAL
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
  '[gamemode].chat.team-chat.mute':
    description: Player can mute incoming team chat with /is muteteamchat
    default: true
  '[gamemode].chat.spy':
    description: Player can use team or island chat spy
    default: op
```

## Like this addon?
You can [sponsor](https://github.com/sponsors/tastybento) to get more addons like this and make this one better!

## Changelog

??? note "What's new in v1.4.0"
    **Released:** 2026-04-13

    - **Team chat in extra worlds** — Team chat now works outside game-mode worlds. Use `team-chat.extra-chat-worlds` in `config.yml` to list additional worlds (spawn, hub, etc.) per game mode where team chat should be captured.
    - **Mute team chat** — Players can silence incoming team chat with `/is muteteamchat` without leaving their team. Mute is cleared automatically on team leave/kick.
    - **MiniMessage migration** — All 23 locale files converted from legacy `&` colour codes to MiniMessage. If you have customised locale files, update `&a` → `<green>` etc., or delete them to regenerate.
    - Bug fix: null pointer exception when a player used `/is teamchat` without an island.

    [Release v1.4.0](https://github.com/BentoBoxWorld/Chat/releases/tag/1.4.0)

## Translations

{{ translations("Chat") }}

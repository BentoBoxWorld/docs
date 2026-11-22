# Teams & Ranks

Teams let several players share one island. Every island has one **owner**, and the owner can invite other players to join as **members**. Players who only need to help out for a while can be **trusted** or **cooped** instead of joining.

This page explains how teams work, what you can configure as an admin, and how to handle the common requests you will get from players.

!!! info "Commands on this page"
    Commands are shown for BSkyBlock (`/island`, `/bsbadmin`). Other game modes use their own command names, for example `/ob` in AOneBlock or `/acid` in AcidIsland. Permissions start with the game mode's prefix, for example `bskyblock.` or `aoneblock.`.

## How teams work

- A player starts a team by inviting someone with `/island team invite <player>`. The invited player accepts, gives up their own island (by default), and is teleported to the team island.
- Everyone on the island has a **rank**. The rank decides what they can do: break blocks, open chests, invite players, kick players and so on.
- The owner decides what each rank can do in the island settings menu (`/island settings`). See [Protection, Flags & Ranks](../Island-Protection,-Flags-&-Ranks.md).
- There is one owner. The owner can hand the island to another member, but must do that before leaving.

### The ranks

| Rank | Value | Who has it | Counts toward team size? |
|---|---|---|---|
| Owner | 1000 | The player who owns the island | Yes |
| Sub-Owner | 900 | Members promoted by the owner | Yes |
| Member | 500 | Players who accepted a team invite | Yes |
| Trusted | 400 | Players trusted with `/island team trust` | No (separate limit) |
| Coop | 200 | Players cooped with `/island team coop` | No (separate limit) |
| Visitor | 0 | Everyone else on the island | No |
| Banned | -1 | Players banned with `/island ban` | No |

Higher ranks can do everything lower ranks can do. You can add your own ranks between these with `/bentobox rank add` (see [Custom ranks](#custom-ranks)).

### Trusted and coop: helping without joining

Trusted and coop players can work on an island without becoming team members. They keep their own island.

- **Trusted** players keep their rank until someone removes it with `/island team untrust <player>`.
- **Coop** players keep their rank only while the island has a team member online. When the last team member logs off, every coop player on that island loses the rank. A coop player who logs off also loses their coop ranks.

Trust and coop work the same way as team invites: the other player gets an invite and must accept it.

## What players can do

Players open the team menu with `/island team`. From the menu they can see their team, invite players, and change ranks without typing commands. All the same actions are also available as commands:

| Command | What it does |
|---|---|
| `/island team` | Opens the team menu |
| `/island team invite <player>` | Invites an online player to join the team |
| `/island team uninvite <player>` | Withdraws a pending team, trust or coop invite |
| `/island team accept` | Accepts a pending invite (team, trust or coop) |
| `/island team reject` | Rejects a pending invite |
| `/island team leave` | Leaves the team. The owner cannot leave; they must give the island away first |
| `/island team kick <player>` | Removes a member from the team. Works when the player is offline |
| `/island team promote <player>` | Moves a member up one rank (never to Owner) |
| `/island team demote <player>` | Moves a member down one rank (never below Member) |
| `/island team setowner <player>` | Gives the island to another member. The old owner becomes Sub-Owner |
| `/island team trust <player>` | Gives a player the Trusted rank |
| `/island team untrust <player>` | Removes the Trusted rank |
| `/island team coop <player>` | Gives an online player the Coop rank |
| `/island team uncoop <player>` | Removes the Coop rank |

A player can only have **one** pending invite at a time. A new invite replaces the old one.

An invite that isn't accepted or rejected **expires after 24 hours** by default (see [Invite expiry, cooldowns and confirmations](#invite-expiry-cooldowns-and-confirmations)). Before then, it can be taken back with `/island team uninvite <player>`. The player who sent the invite can always withdraw it; anyone else on the island needs the rank that is allowed to invite. The command uses the same permission as `team invite`. Both need BentoBox 3.24.0 or later.

On Minecraft 26 and later, a player who receives a team invite sees an **Accept / Decline** dialog, so they don't need to type the command. Sensitive commands like `kick` and `leave` also ask for confirmation in a dialog. Both can be turned off in BentoBox's `config.yml` (`island.dialogs.team-invites` and `island.dialogs.confirmations`).

### Letting members manage the team

By default only the owner can invite, kick, promote, demote, trust and coop. The owner can let lower ranks use these commands from the **Command Ranks** page of the settings menu. For example, an owner can let Sub-Owners invite and kick.

The same page also controls island commands such as `ban`, `unban`, `expel`, `lock`, `setname` and `sethome`. Home commands (`sethome`, `renamehome`, `deletehome`) default to Member; the others default to Owner.

Players can never kick, promote or demote someone of the same or higher rank than themselves.

## Setting up teams (admins)

### Team size

Team size is set in the game mode's `config.yml`. **The limit includes the owner**, so `max-team-size: 4` means the owner plus three members.

```yaml
island:
  # Owner + members
  max-team-size: 4
  # Separate limits for coop and trusted players
  max-coop-size: 4
  max-trusted-size: 4
```

### Bigger teams for VIPs or ranks

Give the **island owner** a permission with the size on the end:

| Permission | Effect |
|---|---|
| `bskyblock.team.maxsize.<number>` | Team size for islands this player owns |
| `bskyblock.coop.maxsize.<number>` | Coop limit |
| `bskyblock.trust.maxsize.<number>` | Trusted limit |

For example, with LuckPerms:

```
/lp group vip permission set bskyblock.team.maxsize.8 true
```

The permission is checked when the owner is online, and the island remembers the result. Only the owner's permission matters; members' permissions are ignored.

To change one island's limit without permissions, use `/bsbadmin team maxsize <player> <size>`.

### What happens to items and money when players join or leave

When a player accepts a team invite, they normally **lose their own island**. Before they accept, they are warned and asked to confirm.

BentoBox can also clear the player's inventory, ender chest, money, health, hunger and XP when they join or leave a team. This stops players carrying items from one island to another. Set it in the game mode's `config.yml`:

```yaml
island:
  reset:
    # Leaving or being kicked uses up one of the player's island resets
    leavers-lose-reset: false
    # Kicked players keep their inventory even if on-leave inventory is true
    kicked-keep-inventory: false
    on-join:      # when a player joins a team or makes an island
      inventory: false
      ender-chest: false
      money: false
      exp: false
      health: true
      hunger: true
    on-leave:     # when a player leaves or is kicked
      inventory: false
      ender-chest: false
      money: false
      # ... same options as on-join
```

!!! warning "Recommended for most servers"
    The defaults keep inventories so you don't lose items while testing. On a live server, consider setting `on-join` and `on-leave` `inventory` and `ender-chest` to `true`, and `leavers-lose-reset: true`. Otherwise a player can fill their inventory, join a friend's island, leave, and repeat.

You can also run commands when players join or leave, for example to reset their challenges or give a kit:

```yaml
island:
  commands:
    on-join:
      - 'bsbadmin deaths set [name] 0'
    on-leave: []
```

These run from the console unless the command starts with `[SUDO]`, which runs it as the player.

### Invite expiry, cooldowns and confirmations

These are in **BentoBox's** `config.yml` (in `plugins/BentoBox/`), and apply to all game modes:

```yaml
island:
  invite-expiry-hours: 24   # hours a team, trust or coop invite stays open; 0 = never expires
  cooldown:
    time:
      invite: 60   # minutes before a kicked or leaving player can be invited back to that island
      coop: 5      # minutes before an uncooped player can be cooped again
      trust: 5     # minutes before an untrusted player can be trusted again
  confirmation:
    time: 10       # seconds players have to confirm
    commands:
      kick: true
      leave: true
    invites: false # also ask trust/coop invitees to confirm (team invites always confirm)
```

The invite cooldown stops players from repeatedly joining, finishing challenges, leaving, and rejoining.

`invite-expiry-hours` was added in BentoBox 3.24.0; before that, invites did not expire. Invites that are open when you upgrade get one full expiry period from the first time they are checked. Set it to `0` to keep invites open, as before.

### Turning teams off

Some game modes are designed for solo play. A game mode can disable teams for its world. Then the invite, kick, leave, promote, demote and setowner commands refuse to run, but trust and coop still work so players can still help each other. If you switch this on for a world that already has teams, run `/bsbadmin team disbandall` once to break up the existing teams.

### Players with more than one island

If you allow multiple islands per player (`concurrent-islands` above 1), `disallow-team-member-islands: true` stops team members from creating their own islands as well. See [Multiple Islands](../ConcurrentIslands.md).

## Common admin tasks

| I want to… | Do this |
|---|---|
| See who is on a player's team | `/bsbadmin info <player>` |
| Add a player to a team | `/bsbadmin team add <owner> <player>` |
| Remove a player from a team | `/bsbadmin team kick <player>` |
| Give an island to another member (owner left the server) | `/bsbadmin team setowner <player>` |
| Break up a team | `/bsbadmin team disband <owner>` |
| Break up every team in this world | `/bsbadmin team disbandall` |
| Let one island have a bigger team | `/bsbadmin team maxsize <player> <size>` |
| Let a rank of players have bigger teams | Give them `bskyblock.team.maxsize.<number>` |
| Let members invite other players | Owner opens `/island settings` → Command Ranks |
| Change what members can do on the island | Owner opens `/island settings`; admins set defaults in the game mode config. See [Protection, Flags & Ranks](../Island-Protection,-Flags-&-Ranks.md) |

## Custom ranks

You can add ranks between the built-in ones with the `/bentobox rank` command:

```
/bentobox rank list
/bentobox rank add ranks.veteran 700
/bentobox rank remove ranks.veteran
```

The value decides where the rank sits. `700` is between Member (500) and Sub-Owner (900), so promoting a Member makes them a Veteran, and promoting again makes them a Sub-Owner. Add the rank's display name to your locale files under the reference you used (here `ranks.veteran`).

## Troubleshooting

**"The island is full" but the team looks small.**
The limit includes the owner. Check `max-team-size`, and whether the owner has a `team.maxsize` permission. The owner must log in once for a new permission to apply.

**A player can't be invited.**
They may already be on a team (they must leave first), already have a pending invite, or be in the invite cooldown after leaving or being kicked from that island. A pending invite from your island can be withdrawn with `/island team uninvite <player>`; otherwise it expires after `invite-expiry-hours`.

**Coop players keep losing their rank.**
That is how coop works: it ends when no team member is online. Use trust instead for players who should keep access.

**The owner wants to leave.**
Owners can't leave. They must give the island to someone with `/island team setowner <player>` first, or an admin can do it with `/bsbadmin team setowner`.

**Players are exploiting team join/leave to duplicate items or rewards.**
Turn on the `on-join` and `on-leave` resets, set `leavers-lose-reset: true`, and keep the invite cooldown.

## See also

- [Protection, Flags & Ranks](../Island-Protection,-Flags-&-Ranks.md): what each rank can do on an island
- [Islands](IslandManagement.md): creating, resetting and deleting islands
- [Multiple Islands](../ConcurrentIslands.md)
- [Customizing Menus](../../Tutorials/generic/Customizable-GUI.md): the team menu is `plugins/BentoBox/panels/team_panel.yml`

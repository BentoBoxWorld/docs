# Permissions & VIP Perks

BentoBox works with any permissions plugin (LuckPerms is the most common). This page explains how BentoBox's permissions are named, which ones players already have, and how to give ranks or VIPs bigger teams, bigger islands, more homes and other perks.

!!! info "Examples on this page"
    Examples use BSkyBlock, whose permissions start with `bskyblock.`, and LuckPerms commands. Each game mode has its own prefix, for example `aoneblock.`, `acidisland.` or `caveblock.`, so a perk must be given once for each game mode.

## How the permissions are named

| Permission starts with | Used for | Who has it by default |
|---|---|---|
| `bentobox.` | The `/bentobox` command | Operators (`bentobox.about` is for everyone) |
| `<gamemode>.island.` | Player commands, such as `bskyblock.island.team.invite` | Players, mostly. See [below](#check-what-players-have-by-default) |
| `<gamemode>.admin.` | Admin commands, such as `bskyblock.admin.delete` | Operators |
| `<gamemode>.mod.` | Moderator commands and protection bypasses, such as `bskyblock.mod.info` | Operators |
| `<gamemode>.settings.` | Changing island settings in `/island settings` | Players |
| `<gamemode>.<thing>.<number>` | Limits, such as `bskyblock.team.maxsize.8` | Nobody: the config value is used |

Addons add their own permissions. They're listed on each [addon's page](../addons/Bank/index.md).

### Check what players have by default

Run **`/bentobox perms`** in the console. It prints every BentoBox and game mode command permission with its default (`TRUE` for everyone, `OP` for operators, `FALSE` for nobody), in a format you can paste into a permissions plugin.

!!! warning "Some player commands are operator-only by default"
    In BSkyBlock and AcidIsland, `island.deletehome` and `island.renamehome` default to operators only. In AcidIsland, so does `island.homes`. If you give players more than one home, give these to them as well:

    ```
    /lp group default permission set bskyblock.island.homes true
    /lp group default permission set bskyblock.island.deletehome true
    /lp group default permission set bskyblock.island.renamehome true
    ```

## Perks with a number

These permissions end with a number. The number replaces the value in the game mode's `config.yml` for that player.

| Perk | Permission | Config default | Checked for |
|---|---|---|---|
| Team size (including the owner) | `bskyblock.team.maxsize.<n>` | `island.max-team-size` | Island owner |
| Coop players | `bskyblock.coop.maxsize.<n>` | `island.max-coop-size` | Island owner |
| Trusted players | `bskyblock.trust.maxsize.<n>` | `island.max-trusted-size` | Island owner |
| Island size (protection range) | `bskyblock.island.range.<n>` | `world.protection-range` | Island owner |
| Number of homes | `bskyblock.island.maxhomes.<n>` | `island.max-homes` | Island owner |
| Number of islands | `bskyblock.island.number.<n>` | `world.concurrent-islands` | The player |
| Players they can ban | `bskyblock.ban.maxlimit.<n>` | `world.ban-limit` (`-1` = no limit) | The player |

How the number is worked out:

- **The highest number wins.** A player with both `team.maxsize.6` and `team.maxsize.10` gets 10. Ranks can stack without conflicting.
- **The number replaces the config value, even if it's lower.** `team.maxsize.2` gives a team of 2 even if the config says 4. Only give these permissions to raise limits.
- **`.*` is ignored.** A player with `bskyblock.team.maxsize.*` (for example through a wildcard or operator plugin) gets the config value, not unlimited. Use a large number instead.
- **Island perks follow the owner.** Team size, range and homes come from the island **owner's** permissions, not each member's. They're updated when the owner logs in, and range is also set when the island is created.
- **Island size is capped** at `distance-between-islands`; asking for more has no effect. See [Islands](About/IslandManagement.md#island-size-protection-range).

## Other perks

| Perk | Permission |
|---|---|
| A VIP starter island in the Create Island menu | `bskyblock.island.create.<bundle-name>`, after setting that bundle to require a permission in `/bsbadmin blueprint`. See [Islands](About/IslandManagement.md#creating-islands) |
| Colour codes in island names | `bskyblock.island.name.format` |
| Skip command cooldowns (resets, invites) | `bskyblock.mod.bypasscooldowns` |
| Skip the teleport delay | `bskyblock.mod.bypassdelays` |
| Can't be banned or expelled from islands | `bskyblock.admin.noban`, `bskyblock.admin.noexpel` |
| Can't change a particular island setting | Remove `bskyblock.settings.<FLAG_ID>`. See [Protection, Flags & Ranks](Island-Protection,-Flags-&-Ranks.md#settings-tab) |

Things that are **not** permissions: extra island resets (use `/bsbadmin resets`, see [Islands](About/IslandManagement.md#resetting-islands)), and the right to invite, kick or ban on someone else's island (island owners control that with ranks, see [Teams & Ranks](About/Teams.md#letting-members-manage-the-team)).

## Example: a VIP rank

A VIP group in BSkyBlock with a team of 8, a bigger island, three homes and a VIP starter island:

```
/lp creategroup vip
/lp group vip permission set bskyblock.team.maxsize.8 true
/lp group vip permission set bskyblock.island.range.100 true
/lp group vip permission set bskyblock.island.maxhomes.3 true
/lp group vip permission set bskyblock.island.homes true
/lp group vip permission set bskyblock.island.deletehome true
/lp group vip permission set bskyblock.island.renamehome true
/lp group vip permission set bskyblock.island.create.vip true
/lp user <player> parent add vip
```

The player must **log out and back in** for the team size, range and homes to apply to an island they already own.

To sell upgrades step by step (bigger islands, more team slots, more homes) with in-game money, see the [Upgrades](../addons/Upgrades/index.md) addon.

## Staff permissions

| Role | Give |
|---|---|
| Full admin for one game mode | `bskyblock.admin.*` and `bskyblock.mod.*` |
| Moderator who can look but not change islands | `bskyblock.mod.info`, `bskyblock.admin.tp`, `bskyblock.mod.bypasslock`, `bskyblock.mod.bypassban` |
| Moderator who can build anywhere | add `bskyblock.mod.bypassprotect` and `bskyblock.mod.switch` (lets them turn the bypass off with `/bsbadmin switch`) |
| BentoBox admin (reload, manage, migrate) | `bentobox.admin` and its sub-permissions |

All the protection bypass permissions are explained in [Protection, Flags & Ranks](Island-Protection,-Flags-&-Ranks.md#bypass-the-protection).

## Troubleshooting

**A perk doesn't apply.**
Island perks come from the island owner and are updated when they log in. Have the owner log out and in. For range, check `distance-between-islands` isn't lower than the number.

**A VIP got a smaller team than normal players.**
A lower number in another group replaced the config value. Remove it; the highest number a player has is used.

**Players can't use a command.**
Run `/bentobox perms` and check the default for that command. Give the permission to your default group if it's `OP` or `FALSE`.

**The perk works in one game mode but not another.**
Each game mode has its own prefix. Give the permission again for `aoneblock.`, `acidisland.` and so on.

## See also

- [Permissions reference](Permissions.md): every BentoBox and game mode permission
- [Commands reference](Commands.md)
- [Teams & Ranks](About/Teams.md), [Islands](About/IslandManagement.md), [Protection, Flags & Ranks](Island-Protection,-Flags-&-Ranks.md)

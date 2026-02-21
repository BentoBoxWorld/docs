# Your First 30 Minutes with BentoBox

You've installed BentoBox and a game mode addon. Now what? This guide walks you through everything to check and do before you open your server to players.

---

## Step 1 — Confirm Everything Loaded

Start your server and look for any error messages in the console. Then run:

```
/bentobox version
```

You should see BentoBox's version number, followed by a list of every loaded addon and their versions. If your game mode addon appears in this list, BentoBox has found and loaded it correctly.

!!! warning "If an addon is missing from the list"
    Check that the `.jar` file is in `plugins/BentoBox/addons/` and **not** in `plugins/`. Then check the console for any error messages during startup. Common causes are version mismatches or a missing dependency.

---

## Step 2 — Test Island Creation as a Player

Join your server as a regular player (use an alt account or ask a friend) and run the game mode's main player command. For BSkyBlock:

```
/island
```

A new island should be created and you should be teleported to it. If this works, the core setup is correct.

Try a few things from the island:

- Break a block ✅ (should work — it's your island)
- Place a block ✅
- Check your island info: `/island info`

---

## Step 3 — Test Protection

Stand on your island and ask another player (or use an alt) to visit. As a visitor, they should **not** be able to:

- Break blocks
- Open chests
- Interact with most objects

If visitors can break blocks, check the island's protection flags. The island owner opens the settings GUI with:
```
/island settings
```

And as an admin you can open the world settings with:
```
/[admin_command] settings
```

---

## Step 4 — Review Key Config Settings

Before players arrive, open the game mode's `config.yml` (found in `plugins/BentoBox/addons/[GameMode]/`) and review these settings:

| Setting | What it controls | Recommendation |
|---|---|---|
| `distance-between-islands` | Space between island centres | Set this **before** any islands are created — it cannot be changed later |
| `island-protection-range` | Default protection radius | Should be less than half the distance above to give space to growth |
| `reset-limit` | How many times players can reset their island | `-1` for unlimited, or a number like `3` |
| `max-team-size` | Maximum players per island team | `4` is the default; increase for more cooperative play |

!!! warning "Island distance cannot be changed later"
    Once any islands have been created, changing `distance-between-islands` will cause BentoBox to refuse to start. Choose your value and set it before opening to players. The default (400 blocks radius = 800 blocks between centres) works well for most servers.

---

## Step 5 — Set Up Permissions

BentoBox uses your server's permissions plugin (such as LuckPerms) to control what players can do. Players will usually be given a set of default permissions, which include:

```
[gamemode].island.create       # Create an island
[gamemode].island.home         # Teleport to their island
[gamemode].island.settings     # Open island settings GUI
[gamemode].island.team         # Use team commands
```

Replace `[gamemode]` with the game mode's prefix (e.g. `bskyblock`, `acidisland`, `oneblock`).

To see the full list of permissions, run:
```
/bentobox perms
```

---

## Step 6 — Install Recommended Addons

A bare BentoBox game mode works, but players will expect a few extras. Consider adding these before opening:

- **Warps** — Players can create warp signs on their island so others can visit easily
- **Level** — Calculates an island score and shows a leaderboard; gives players something to work towards
- **Challenges** — Gives players tasks and rewards; dramatically improves retention
- **InvSwitcher** — Essential if you run more than one game mode or have other worlds; keeps inventories separate

Download addons from [BentoBoxWorld](https://download.bentobox.world), place the `.jar` in `plugins/BentoBox/addons/`, and restart the server.

---

## Step 7 — Customise Your Starter Island (Optional)

The default starter island is functional but generic. To make your server feel unique, build a custom starter island and save it as a Blueprint.

Quick summary:
1. Build the island you want somewhere in the world
2. Use `/[admin_command] blueprint pos1` and `pos2` to select it
3. Use `/[admin_command] blueprint copy` then `save myisland`
4. Open `/[admin_command] blueprint` to manage bundles

See [Blueprints](About/BlueprintsSummary.md) for the full walkthrough.

---

## Step 8 — Open to Players

You're ready. A few final things to check before announcing:

- [ ] Test that new players can create an island without errors - especially if you are using other plugins
- [ ] Confirm protection is working (visitors can't grief)
- [ ] Confirm the game mode appears in `/bentobox version`
- [ ] Read through the [FAQ](../FAQ.md) for common gotchas

---

## Getting Help

If something isn't working:

1. Run `/bentobox version` and copy the output
2. Check the console for error messages
3. Search the [FAQ](../FAQ.md)
4. Ask on the [BentoBox Discord](https://discord.bentobox.world) — include your `/bentobox version` output and the console errors
5. Report bugs at [github.com/BentoBoxWorld/BentoBox/issues](https://github.com/BentoBoxWorld/BentoBox/issues)

# Player Guide

New to a BentoBox server? This page covers the basics: getting your island, inviting friends, keeping your island safe and getting around.

!!! info "Your server's command"
    This page uses `/island`, the command for SkyBlock (BSkyBlock). Other game modes have their own: for example `/ob` for OneBlock, `/ai` for AcidIsland, `/cave` for CaveBlock. Swap it in wherever you see `/island`. Your server may also have turned some features off or changed the defaults.

## Get started

Type **`/island`**.

- If you don't have an island yet, you'll be asked to pick one (if there's a choice) and then teleported to it.
- If you already have one, `/island` takes you home.

That's it. Everything else is optional.

## Getting around

| Command | What it does |
|---|---|
| `/island` or `/island go` | Teleports you to your island |
| `/island sethome` | Sets your home point to where you're standing |
| `/island sethome <name>` | Sets an extra named home, if your server allows more than one |
| `/island go <name>` | Teleports to a named home |
| `/island homes` | Lists your homes |
| `/island spawn` | Teleports you to the game mode's spawn |
| `/island info` | Shows details about the island you're on |
| `/island near` | Shows the names of nearby islands |

## Playing with friends

You have two ways to let friends help you.

**Join as a team.** Team members share the island permanently.

1. Invite them: `/island team invite <name>`. They must be online.
2. They accept with `/island team accept` (or click **Accept** if a pop-up appears).

!!! warning "Joining someone else's island"
    When you accept a team invite, you usually **lose your own island**. You'll be asked to confirm first. Depending on the server, your inventory may be cleared too.

**Let them help without joining.** They keep their own island.

- `/island team trust <name>`: they can help until you remove them with `/island team untrust <name>`.
- `/island team coop <name>`: they can help until everyone on your team logs off.

Open **`/island team`** to see your team, invite players and manage ranks from a menu.

| Command | What it does |
|---|---|
| `/island team leave` | Leave the team. The owner can't leave without giving the island away first |
| `/island team kick <name>` | Remove a member |
| `/island team promote <name>` | Give a member more rights |
| `/island team demote <name>` | Take rights away |
| `/island team setowner <name>` | Give your island to another member |

## Keeping your island safe

Your island is protected. Visitors can look around but can't break blocks, open chests or hurt your animals unless you allow it.

Open **`/island settings`** to choose what visitors, coop players, trusted players and team members can do. Click a setting to cycle through the ranks that are allowed.

| Command | What it does |
|---|---|
| `/island settings` | Choose what each rank can do |
| `/island lock` | Lock your island so visitors can't come in (run again to unlock) |
| `/island expel <name>` | Send a visitor off your island |
| `/island ban <name>` | Ban a player from your island |
| `/island unban <name>` | Lift a ban |
| `/island banlist` | See who is banned |

Something blocked and you're not sure why? The message usually says what's not allowed. Ask your island owner, or check `/island settings`.

## Your island

| Command | What it does |
|---|---|
| `/island setname <name>` | Name your island |
| `/island resetname` | Remove the name |
| `/island language` | Change the language of BentoBox messages |
| `/island reset` | Start over with a new island. **Your old island is deleted.** Your server may limit how many resets you get |

## Extras your server may have

Servers add features with addons. Some common ones:

| Command | Addon | What it does |
|---|---|---|
| `/island level` | [Level](../addons/Level/index.md) | Calculates your island level |
| `/island top` | [Level](../addons/Level/index.md) | Shows the top islands |
| `/island challenges` | [Challenges](../addons/Challenges/index.md) | Opens the challenges menu |
| `/island warps` | [Warps](../addons/Warps/index.md) | Lists player warps; write `[Welcome]` on the first line of a sign to add yours |
| `/island bank` | [Bank](../addons/Bank/index.md) | Your island's shared bank |
| `/island fly` | [IslandFly](../addons/IslandFly/index.md) | Fly on your island |

Type `/island help` to see every command available to you.

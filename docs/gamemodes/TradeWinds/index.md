<!-- Hero screenshot goes here once the game is public:
<img width="600" height="300" alt="TradeWinds" src="..." />
-->

# 🌬️ TradeWinds

Created and maintained by [tastybento](https://github.com/tastybento).

**TradeWinds** is a sea-trading game mode for BentoBox: an endless, procedurally generated ocean scattered with NPC trading islands. Your players start with nothing but a rowing boat and a pocketful of coal—and the boat **is** their cargo hold. Buy low at a farming island, sell high at an industrial port, and watch the money roll in… or take the shortcut through smuggling, bounty hunting, and piracy, and deal with what follows.

If you ever lost a weekend to *Elite* or *TradeWars 2002*, this is that feeling, rebuilt in Minecraft. If you didn't—your players are about to find out why you would have.

## 🧭 Why players get hooked

- 🏝️ **An endless seeded ocean world.** Every island's position, type, tech level, security band, biome, and name derives from a single seed. Players can explore and find novel locations. Use the default seed or pick a new one to have a unique world. Share your seed and another server gets the exact same world.
- ⛵ **The boat IS the hold.** Cargo lives in the ship, the ship can be upgraded through **20 hull ranks** (Bamboo Raft → Pale Oak Chest Boat), and losing the ship *means something*. One player, one boat—every hull decision matters.
- 📈 **A market worth reading.** Eight island personalities (farms, mines, fisheries, forests, industry, luxury, frozen ports…) each buy and sell differently, and every trade nudges local prices. The good routes are *discovered*, not posted.
- ⚡ **Two ways to travel, both fair.** Rowing is free, slow, and takes you through lawless water, but potential riches. Warping is instant but burns fuel from the hold—and a 5% misjump drops you into the **Interstice**, a hostile nether sea where the wart, the blaze rods, and the wither watchtowers are. Neither way ever strictly beats the other; that tension is the game.
- 🗺️ **Charts, stars, and rank.** Raising the chart floats a hologram compass of everything you've charted. Every island charted by players climbs the **Seafarer ladder**—19 ranks from Deck Hand to Mythic Mariner, with a built-in top-ten leaderboard and placeholders for your scoreboard.
- 🏠 **An island of your own—earned.** Reach **Tide Captain** (36 islands charted) and carry serious coin, and any wild islet you find can become yours: protection, team, home point, a members-only warp node, and night-sky navigation home by the stars. First come, first claimed.
- 🚨 **Crime that pays you into danger.** Contraband only sells where the law is thin; a criminal record locks you out of safe markets and puts a bounty on your head that other players can lawfully collect. The richest smugglers are structurally pushed toward the dangerous edge of the map—where the pirates already are.
- 🐡 **A sea that pushes back.** Guardian pickets by day, drowned raiders by night, phantoms, deep terrors, boat-borne pirate crews, sea witches—scaled by how lawless the water is. Even the safe lanes get the occasional puffer shoal, just to keep the helmsman awake.

**Difficulty is geography.** The waters near spawn are patrolled and calm—new and younger players can trade in peace. Danger, contraband, and PvP bounty space are all *somewhere else*, and going there is always a choice. That makes TradeWinds one of the few economy games that works for a family server and a cut-throat one at the same time, from the same config.

## ⚓ How a session feels

You cast off from the spawn port with three slots of cargo and a hunch: the fishing village two islands east was paying double for wheat. You row the first leg—fuel is money—and chart a new islet on the way, one more notch toward Tide Captain. At the border curtain the warp dialog offers the crossing for 14 units of coal; you take it, because the sun is setting and drowned raiders own the night out here. The market pays out, the hold refills with cheap cod, and on the chart home you notice a red-banded island you've never dared visit is buying fish at *silly* prices. It would only take one quiet run…

That loop—plan, sail, trade, risk a little more than last time—is the whole game, and it does not let go.

## 🔧 Setup

!!! warning "Vault and an economy plugin are required"
    All trading runs through Vault. Install Vault plus any Vault-compatible economy (EssentialsX Economy, CMI, etc.) before first launch. TradeWinds formats money itself—whole coins, no cents—using the `economy.currency-symbol` from its config. If you want BentoBox's option, use InvSwitcher with money turned on - it's an economy for BentoBox.

1. **Download the TradeWinds addon** and place it in `/plugins/BentoBox/addons/`
2. **Start the server**—`tradewinds_world` (the ocean) and `tradewinds_world_nether` (the Interstice) generate automatically. There is deliberately **no End world**.
3. **Log in and look around as Op**: `/twadmin islands` lists the nearest trading islands and `/twadmin tpisland <#>` teleports you to one.
4. **Pick your world seed** *(optional, before players join)*: set `ocean.seed` in `config.yml`. Every island position, type, and name flows from this one number—change it later and it is a different ocean.
5. **Tune the economy to taste** *(optional)*: prices, boat costs, warp fuel rates, crime, and encounter tables are all in `config.yml` with the intended defaults already in place.

!!! tip "Recommended companions"
    - **InvSwitcher**—keeps inventories, health and hunger separate from your other game modes. Includes an economy.
    - **Bank**—claimed player islands attach to the Bank addon automatically if it is installed. Allows pooling of money between team members.

## ✅ Compatibility

| Feature           | Supported                          |
|-------------------|------------------------------------|
| Server            | ✅ Paper 26.2+                     |
| BentoBox Version  | ✅ 3.18.0 or later                 |
| Java Version      | ✅ Java 25                         |
| Economy           | ⚠️ Vault + economy plugin required |

## 🎮 Commands

The player command is `/tw` (or `/tradewinds`); the admin command is `/twadmin`. Bare `/tw` sets sail—it is the door into the ocean, and the game's one careful teleport: it returns you to the water you left, steps you to your home point if you are standing on your own island, and anywhere else at sea it tells you the **bearing and distance** home rather than giving you a ride. Nothing in TradeWinds teleports cargo.

The full command reference is [here](Commands.md).

## ⚙️ Configuration

Everything gameplay-shaped lives in `config.yml`, introduced stage by stage with comments explaining *why* each default is what it is. The one setting every admin should look at before launch:

```yaml
ocean:
  # The ocean seed. Every island position, type, security band, biome, name and
  # route cost derives deterministically from this one number - share it and another
  # server gets the same trading ocean. 0 means: use the world seed.
  seed: 20260729
```

Other sections worth a skim: `boats` (the hull ladder and prices), `travel.warp` (fuel cost and misjump chance), `ranks` (the Seafarer ladder), `claims` (the price of a player island), `crime` (the whole law layer has a master switch), and `encounters`.

## 📄 More documentation

- **[The Sailor's Handbook](Gameplay.md)**—the full gameplay guide: trading, boats, charts, claiming, crime, and the Interstice. Read this one to see what your players will see.
- **[Commands](Commands.md)**—every player and admin command.
- **[Permissions](Permissions.md)**—every permission node and its default.
- **[Placeholders](Placeholders.md)**—rank and leaderboard placeholders for scoreboards.

## Translations

{{ translations("TradeWinds") }}

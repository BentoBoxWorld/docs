# 🧭 The Sailor's Handbook

Everything a player discovers in their first weeks on the water, in one place—and everything an admin needs to know about how the pieces interlock. TradeWinds is a game of simple rules with deep consequences; the rules are below, the consequences are up to your players.

## ⛵ Your first hour

You arrive at the **spawn port** with a starter Oak Boat—3 cargo slots, coal already in the tank—and a piece of advice worth repeating: *the boat is your hold and your livelihood; keep it close.*

1. **Right-click your boat** to open the hold. Cargo and fuel live here—never in your pockets. Trading at any market moves goods in and out of the hold directly.
2. **Talk to the traders** on the plaza. Every island posts buy and sell prices; the spread is the game.
3. **Set sail** and row away from the island. When you are far enough out you can chose to warp or carry on rowing. Crossing a new island's waters **charts** it permanently on your map, and adds a small step up the Seafarer ladder.
4. **Sell high.** Congratulations: you are a trader. Everything else in this handbook is about doing this faster, bigger, and closer to the edge.

## 🚢 One boat, twenty hulls

Your boat is your only hold, and you have exactly one. Its hull decides your cargo slots:

| | | |
|---|---|---|
| Bamboo Raft: 2 | Oak Boat: 3 | Spruce Boat: 4 |
| Bamboo Chest Raft: 5 | Birch Boat: 6 | Oak Chest Boat: 7 |
| Jungle Boat: 8 | Spruce Chest Boat: 9 | Acacia Boat: 10 |
| Birch Chest Boat: 11 | Dark Oak Boat: 12 | Jungle Chest Boat: 13 |
| Mangrove Boat: 14 | Acacia Chest Boat: 15 | Cherry Boat: 16 |
| Dark Oak Chest Boat: 17 | Pale Oak Boat: 18 | Mangrove Chest Boat: 19 |
| Cherry Chest Boat: 20 | Pale Oak Chest Boat: 21 | |

- **Shipwrights sell** every hull the island's tech level can build, except the size you already sail. Bring your ship to the quay and buy bigger: that's a **trade-in**: same hold, same cargo, more slots, and the hull under you (or in your pack, or moored at the dock) visibly becomes the new type. Buy with your ship an ocean away and it's an **outright purchase**: new boat in hand, the old one left **UNOWNED** wherever it lies, cargo aboard, first come first served. The dialog warns you before your money moves.
- **Boats can be captured.** Board or pick up a hull that isn't yours and you'll be asked: take the boat (abandoning yours where it lies), take just its cargo (only if your own ship is close enough to load—cargo never teleports), or leave it. An owned boat parked inside a lawful island's protection is untouchable; the same boat parked in anarchic water is not.
- **Death is not the end.** Your boat stays afloat where you left it, still yours, and the chart marks it. If you were *carrying* it, the wreck site is marked instead. Respawn boatless and the port lends you a raft for the recovery row.
- **Lava is the only true destroyer.** Everything else just changes who's holding the hull.
- **The endgame is expanders.** Top-tech ports sell cargo expanders that grow the hold beyond the ladder—at a price that doubles per unit installed. The wallet is the only cap.

## 🏝️ Reading the ocean

Every trading island has a **type** (what it grows, digs, or builds—and therefore what it sells cheap and buys dear), a **tech level** (what its shipwright can build and its outfitter stocks), and a **security band**:

| Band | The water | The rules |
|------|-----------|-----------|
| **SAFE** | Around spawn | Patrolled, no hostile spawns ashore, customs sharp-eyed |
| **POLICED** | The trade lanes | Law present, contraband risky, guardians picket by day |
| **FRONTIER** | The long routes | Thin law, better margins, worse company |
| **ANARCHIC** | The edge | No law at all—contraband gold, pirate crews, and other players |

Prices follow the geography: the farther from safety, the better the deals—on both sides of the law. Every purchase and sale also **drifts the local price**, so a route can be fished out and a neglected port can quietly become a goldmine.

## 🗺️ Getting around

**Rowing** is free and charts everything you pass. **Warping** happens at the island border—sail into the visible curtain and the dialog offers every charted destination with its fuel price (about 1 fuel unit per 100 blocks). Fuel is anything that burns, valued sensibly: logs 1, kelp blocks 4, coal and charcoal 8, blaze rods 12, coal blocks 80, a lava bucket 100—all carried in the hold's fuel row, eating into cargo space. That tradeoff is what player's will have to make.

- `/tw chart` raises the **hologram compass**: charted islands, the dock bearing, your boats, and—if you own one—home.
- `/tw starchart` draws your charted world onto a **map item** you can take out and put away.
- `/tw rank` shows your Seafarer rank and the top ten sailors by islands charted.

!!! danger "The misjump"
    Every warp carries a small chance (5% by default) of dropping you in the **Interstice**—a dark nether sea under a burning sky. Re-engaging the warp to your original destination is **always free**… but the Interstice is the only place in the game where nether wart grows on the soul-sand shoals, blaze pickets man their crow's nests, and wither watchtowers keep loot worth the detour. What starts as an accident becomes a destination. There are no nether portals in TradeWinds—the sea has its own way in, and the lore-books ashore explain why the portals refuse to light.

## 🎖️ Ranks and the ladder

Charting islands is the game's odometer, and 19 Seafarer ranks mark the distance—**Deck Hand** at the start; **Bay Explorer** at 10; **Chart Maker** at 20; **Tide Captain** at 36, where claiming unlocks; **Salty Commodore** at 56; all the way to **Mythic Mariner** at 100. The `/tw rank` top ten and the `%tradewinds_rank%` / `%tradewinds_top_name_1%` placeholders give servers a ready-made leaderboard culture. Admins can promote, demote, or reset with `/twadmin rank`.

## 🏠 An island of your own

Scattered between the trading islands are **wild islets**—small, unowned, and claimable:

- **The gates:** stand on the islet, hold **Tide Captain** rank, and pay the price (default **$150,000**—deliberately above the top boat, because the hull ladder comes first). First come, first claimed.
- **What you get:** BentoBox protection with the standard flags GUI, a team, `/tw sethome` and `/tw home` around the base, and `/tw go` steps you home when you're standing on your island. If the Bank addon is installed, your island gets an account automatically.
- **Getting home across the sea:** your claim becomes a **members-only warp node** in every border dialog. Prefer to sail? `/tw go` at sea sets a **course home**: a rough compass bearing by day, and at night—when the stars come out—exact distance and progress. Teach the kids to navigate by the night sky; it works.
- **Team members need no rank.** Only the claimer passes the gate; a Tide Captain can bring the whole crew home.
- **Unclaiming hurts on purpose.** Owner only, the team must be emptied first, and there's no refund—everything stays exactly as it was left, back in the wild for the next captain.

## 🚨 The law and the lawless

The crime layer (one master switch in config) is what turns the map's geography into a story:

- **Reputation** runs from Upstanding to **Fugitive**. Customs scans at lawful ports catch contraband in the hold; get caught enough and safe markets close their doors to you.
- **Contraband** (sugar, configurable) is worthless where it's legal to be poor and priceless where nobody asks questions. The scan risk—not the price—is the cost of smuggling.
- **Fines** (`/tw fine`) buy a record clean at any port that will still talk to you.
- **Bounties** on wanted players can be collected by anyone, lawfully, in the water where fugitives are forced to trade. Police mobs enforce the peace at lawful islands—and never drop loot, so there is nothing to farm.

The design is deliberate: crime pays, and it pays you *into danger*. The richest smugglers end up trading exactly where the pirate crews and the bounty hunters already are.

## 🌊 Things that find you at sea

Open water rolls encounters scaled by distance from the dock and the band you're in:

| Encounter | Waters | When |
|-----------|--------|------|
| 🐡 Puffer shoal | SAFE–POLICED | Any time—a sting, not an ambush, and never worth farming |
| 🔱 Guardian picket | POLICED+ | Day |
| 🧟 Drowned raiders | POLICED+ | Night—some carry tridents |
| 👻 Phantom flight | FRONTIER+ | Night, above the mast |
| 🦑 Deep terror | FRONTIER+ | Below the keel |
| 🏴‍☠️ Pirate crew | ANARCHIC | Boat-borne, they fight from the deck |
| 🧪 Sea witch | ANARCHIC | Boat-borne, keeps her distance |

Encounter kills pay **booty**—customs-stamped salvage straight into the hold, the only money the sea itself pays. Every roster, pack size, and chance is in `encounters` in the config.

## 🛠️ For the admin at the helm

- **The seed is the world.** Back up `config.yml` with the database; `galaxy.seed` *is* your world. Publish it if you want players theory-crafting routes on Discord, keep it secret if you want explorers.
- **The boat logbook** (`boats.logbook`, on by default) writes one console line per boat lifecycle event—placed, broken up, captured, bought, went down with its sailor—with coordinates. When a player asks *"where did my boat go?"*, the answer is in the log.
- **`/twadmin boat <player>`** reads their boat records straight from the database: cargo, fuel, last-seen position, and whether the hull is actually afloat there, in someone's pack, or sitting in an unloaded chunk. `restore` regenerates a genuinely lost boat, cargo intact—it refuses while the real hull is loaded, so it can't be used to duplicate.
- **`/twadmin islands` / `tpisland`** for touring, **`customs`** to see the law's view of any spot, **`priceaudit`** to verify every good has a price, and **`warpfail`** to test the Interstice on demand.
- **Dropped-boat cleanup**: abandoned boat *items* (and their cargo records) expire after a configurable TTL. Boat *entities* never expire—an abandoned ship stays part of the world until someone takes it.

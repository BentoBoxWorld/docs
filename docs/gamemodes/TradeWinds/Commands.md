# TradeWinds Commands

The player command is **`/tw`** (alias `/tradewinds`); the admin command is **`/twadmin`**. Running bare `/tw` performs the default action, `go`.

## Player commands

| Command | Description | Permission |
|---------|-------------|------------|
| `/tw go` (aliases: `spawn`, `sail`) | Set sail — enter the ocean where you left it. On your own island: step to your home point. At sea: toggle a course home (bearing by day, exact distance under the stars at night). Never a ride across the sea. | `tradewinds.island.spawn` |
| `/tw chart` | Raise the chart compass — hologram markers for charted islands, the dock, your boats, and home. `/tw chart list` prints the text version. | `tradewinds.island.chart` |
| `/tw starchart` | Receive a Star Chart map of your charted islands. | `tradewinds.island.starchart` |
| `/tw rank` (alias: `ranks`) | Your Seafarer rank and the top ten sailors by islands charted. | `tradewinds.island.rank` |
| `/tw claim` | Claim the wild islet you are standing on as your island (rank and price gates apply). | `tradewinds.island.claim` |
| `/tw sethome` | Set your home point — only while standing on your own island. | `tradewinds.island.sethome` |
| `/tw home` | Step to your home point — only while already standing on your own island. | `tradewinds.island.home` |
| `/tw unclaim` | Give your claimed islet back to the wild. Owner only, team must be emptied first, no refund; every block stays as it was left. | `tradewinds.island.unclaim` |
| `/tw fine` | Settle your criminal record at a port (returns you to Clean). | `tradewinds.island.fine` |
| `/tw restart` | Restart your trading career (limited uses, config-capped). | `tradewinds.island.restart` |
| `/tw info` | Information about the island you are on. | `tradewinds.island.info` |
| `/tw settings` | View island settings. | `tradewinds.island.settings` |
| `/tw language` | Select your language. | `tradewinds.island.language` |
| `/tw warp` | Open the warp dialog from anywhere in island waters. **Op by default** — the intended path is sailing to the border curtain, which offers the dialog automatically. | `tradewinds.island.warp` |
| `/tw trade` | Open the island market from anywhere in its protection range. **Op by default** — the intended path is docking and right-clicking a trader. | `tradewinds.island.trade` |
| `/tw prices` | Your price logbook — what ports you have called at were paying, and how long ago. Only registered when the `economy.price-logbook-enabled` feature flag is on (off by default). | `tradewinds.island.prices` |

## Admin commands

`/twadmin` carries all the standard BentoBox admin commands (`version`, `tp`, `getrank`, `setrank`, blueprints, and so on), plus the TradeWinds-specific set:

| Command | Description | Permission |
|---------|-------------|------------|
| `/twadmin islands` | List the nearest trading islands with type, tech level, band, and distance. | `tradewinds.admin.islands` |
| `/twadmin tpisland <#>` | Teleport to a trading island from the islands list. | `tradewinds.admin.tpisland` |
| `/twadmin boat <player>` | Inspect a player's boat records straight from the database: material, cargo, fuel, last-seen position, and whether a hull is actually loaded there or in someone's pack. | `tradewinds.admin.boat` |
| `/twadmin boat <player> restore` | Regenerate a lost active boat as a stamped item in the player's pack, cargo record intact. Refuses while the real hull is loaded or carried. | `tradewinds.admin.boat` |
| `/twadmin rank <player>` | Show a player's Seafarer rank: effective islands, real charted count, and adjustment. | `tradewinds.admin.rank` |
| `/twadmin rank <player> <rank\|islands\|reset>` | Set a player's rank by rank slug or island count, or reset the adjustment. Real charting keeps counting on top. | `tradewinds.admin.rank` |
| `/twadmin customs` | Show what customs make of you where you stand: contraband aboard, scan odds, patrol strength. | `tradewinds.admin.customs` |
| `/twadmin priceaudit` | Audit price coverage — what can be sold, what is salvage, what is unsellable — and write the full report to `price-audit.txt`. | `tradewinds.admin.priceaudit` |
| `/twadmin warpfail <player>` | Rig a player's next warp to fail into the Interstice (run again to clear). For testing the misjump path on demand. | `tradewinds.admin.warpfail` |
| `/twadmin reflag` | Re-apply security-band flags to all trading islands. | `tradewinds.admin.reflag` |

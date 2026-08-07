# TradeWinds Permissions

Defaults are chosen so a vanilla install plays the intended game with no permissions plugin at all: everything a sailor needs is `true`, shortcuts that skip the sailing are `op`, and the real gates (claim rank, claim price) live in `config.yml` rather than in permissions.

## Player permissions

| Permission | Description | Default |
|------------|-------------|---------|
| `tradewinds.island` | Allow use of the TradeWinds player command | `true` |
| `tradewinds.island.spawn` | Allow `/tw go` — the door into the ocean, and the way home within the rules. From outside it returns the player to the water they left; on their own island it steps them to their home point; anywhere else at sea it tells them the direction and distance home, never a ride. | `true` |
| `tradewinds.island.chart` | Allow viewing the chart (holograms afloat, list ashore) | `true` |
| `tradewinds.island.starchart` | Allow receiving the Star Chart map | `true` |
| `tradewinds.island.rank` | Allow viewing Seafarer rank and the charted-islands top ten | `true` |
| `tradewinds.island.claim` | Allow claiming a wild islet as a player island. The real gates are in config — Seafarer rank (`claims.minimum-rank`) and price (`claims.price`) — so this stays on by default; turn it off to disable claiming outright. | `true` |
| `tradewinds.island.sethome` | Allow setting a home point on your own island — only while standing inside its protection range (owner or team member). | `true` |
| `tradewinds.island.home` | Allow teleporting to your home point — only while already standing on your own island, so it is a convenience around the base and never a way home across the sea. | `true` |
| `tradewinds.island.unclaim` | Allow the owner to give a claimed islet back to the wild. Requires the team to be emptied first; no refund; every block stays as it was left. | `true` |
| `tradewinds.island.fine` | Allow settling a criminal record at a port. On by default — a player who cannot pay off a reputation has no way back except waiting it out. | `true` |
| `tradewinds.island.restart` | Allow restarting the trading career (config-capped) | `true` |
| `tradewinds.island.prices` | Allow the trader's logbook — what ports you have called at were paying, and how long ago. Prices only enter it by visiting a market or buying a harbour report, so this reads a player's own knowledge back to them. | `true` |
| `tradewinds.island.info` | Allow use of the island info command | `true` |
| `tradewinds.island.settings` | Allow viewing island settings (editing is rank-gated) | `true` |
| `tradewinds.island.language` | Allow use of the language command | `true` |
| `tradewinds.island.warp` | Shortcut: open the warp dialog from anywhere in island waters. Off by default — the intended path is to row to the island border, which offers the dialog automatically. Grant to bypass the sailing. | `op` |
| `tradewinds.island.trade` | Shortcut: open the market from anywhere in an island's protection range. Off by default — the intended path is to dock and right-click a trader on the plaza. Grant to bypass the walk. | `op` |

## Admin permissions

| Permission | Description | Default |
|------------|-------------|---------|
| `tradewinds.admin` | Allow use of the TradeWinds admin command | `op` |
| `tradewinds.admin.islands` | Allow listing the nearest trading islands | `op` |
| `tradewinds.admin.tpisland` | Allow teleporting to trading islands | `op` |
| `tradewinds.admin.boat` | Inspect a player's boat records — cargo, fuel, last-seen position, whether a hull is actually loaded there — and restore a lost active boat from the database as an item in their pack. | `op` |
| `tradewinds.admin.rank` | Inspect or set a player's Seafarer rank — stores an adjustment on top of their real charted count, so promotion, demotion and reset all work and the claim gate and leaderboard follow. | `op` |
| `tradewinds.admin.customs` | Show the customs state at your position (contraband, scan odds, patrol) | `op` |
| `tradewinds.admin.priceaudit` | Audit price coverage and write the report to `price-audit.txt` | `op` |
| `tradewinds.admin.warpfail` | Rig a player's next warp to fail, dropping them into the interstice | `op` |
| `tradewinds.admin.reflag` | Allow re-applying security-band flags to all islands | `op` |
| `tradewinds.admin.*` | All TradeWinds admin permissions | `op` |

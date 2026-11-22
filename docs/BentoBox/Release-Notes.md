# BentoBox Release Notes

Highlights of recent BentoBox releases for server admins. For every change, see the [GitHub releases](https://github.com/BentoBoxWorld/BentoBox/releases). Game modes and addons list their own changes at the bottom of their pages.

!!! note "What's new in v3.24.0 — smaller blueprints, faster pasting, invite expiry & PVP outside islands"
    **Released:** 2026-11-22

    A feature release. Compatibility: Paper Minecraft 1.21.5 – 26.3, Java 25+.

    - 🔺 **Smaller blueprints.** A blueprint now stores its air (or water) once as a "fill" instead of once per block, so blueprint files are much smaller and load faster. Old blueprints load as before and are converted only when saved again. See [Blueprints](Blueprints.md) and the [file format](Blueprint-Format.md#compact-blueprints-fill).
    - ⚙️ **Faster island pasting.** Pasting and copying now run for `island.paste-time-budget` milliseconds each tick (default 10) instead of placing one batch per tick, so large islands appear much sooner when the server has time to spare. See [Pasting speed](Blueprints.md#pasting-speed).
    - ⚙️ **Vehicles are turned back from locked and banned islands.** A player riding a boat, minecart or mount into an island they may not enter is turned back with the vehicle instead of being thrown out and stranded. A locked island briefly shows its border to the player who was turned away. See [Locks, bans and expels](Island-Protection,-Flags-&-Ranks.md#locks-bans-and-expels).
    - ⚙️🔡 **Withdraw and expire team invites.** `/island team uninvite <player>` takes back a team, trust or coop invite, and invites now expire after 24 hours by default. See [Teams](About/Teams.md#what-players-can-do).
    - 🔡 **PVP outside islands.** A new world setting, `PVP_OUTSIDE_ISLANDS`, off by default, allows PVP where there is no island. See [World Settings](Island-Protection,-Flags-&-Ranks.md#what-each-world-setting-does).
    - 🔡 **Per-island creeper block damage.** A new island setting, `CREEPER_BLOCK_DAMAGE`, hidden unless an admin shows it. See [Settings Tab](Island-Protection,-Flags-&-Ranks.md#settings-tab).
    - **Command and Close buttons in every menu.** Menu templates can have a button that runs a command as the player or closes the menu, in BentoBox and in every addon. See [Customizing Menus](../Tutorials/generic/Customizable-GUI.md#command-and-close-buttons).
    - **Visitor list placeholders.** `%[gamemode]_island_visitors_list%` and `%[gamemode]_visited_island_visitors_list%` give the names of the players visiting an island. See [Placeholders](Placeholders.md).
    - 🔡 **Dialog forms, paged panels and value pickers** for addon developers. See [Developer Documentation](Developer-Documentation.md#dialog-forms).
    - **MythicMobs names kept.** A MythicMobs mob spawned by an addon without a name keeps the display name from its MythicMobs config.
    - 🐛 **Items with data components** (such as attribute modifiers) are no longer replaced with air when read back from the database.
    - 🐛 **Housekeeping no longer stalls the server.** It saves only the worlds it is purging, one per tick, and does nothing on the main thread when there is nothing to purge.
    - 🐛 **Protection fixes.** Throwing experience bottles checks `EXPERIENCE_BOTTLE_THROWING`; placing items on blocks checks the block that was clicked; the ban check looks at the team of the island the ban applies to; rank change events name the right player and previous rank.
    - 🐛 **Missing or broken `default` blueprint bundle** is reported at startup, naming the file to fix.
    - 🐛 Also fixed: blueprint copy sizes and boats sinking after a paste; Slimefun block data left behind by a purge (not yet tested against a live Slimefun server); the old material name `GRASS` now loads as `SHORT_GRASS`; a misleading "Could not hook with Vault" error at startup.

    🔺 **Blueprints saved by this version are not for older servers.** A blueprint saved by 3.24.0 still loads in an older BentoBox, but pastes without its air or water fill. Do not share newly saved blueprints with servers running 3.23.7 or earlier.

    🔺 **Team invites now expire.** Invites that are open when you upgrade get one full expiry period from the first time they are checked. Set `island.invite-expiry-hours` to `0` to keep invites open forever, as before.

    ⚙️ **Config note:** four settings are added under `island` in `config.yml`. Each uses its default if you do nothing.

    | Setting | Default | What it does |
    | --- | --- | --- |
    | `invite-expiry-hours` | `24` | Hours a team, trust or coop invite stays open. `0` never expires. |
    | `locked-border.show` | `true` | Show a locked island's border to a player who is turned away from it. |
    | `locked-border.color` | `RED` | Color of that border: `RED`, `GREEN` or `BLUE`. |
    | `paste-time-budget` | `10` | Milliseconds per tick for pasting and copying blueprints. Lower it if island creation causes lag; `0` is the old behavior. |

    🔡 **Locale note:** new keys for the uninvite command, the `CREEPER_BLOCK_DAMAGE` and `PVP_OUTSIDE_ISLANDS` flags, and the value pickers (`panels.picker`). They are added to existing locale files automatically and are translated in every bundled language.

    [Release v3.24.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.24.0)

??? note "What's new in v3.23.7 — rank colours with old locale files & click hints"
    **Released:** 2026-11-11

    A small fix release. No `config.yml` or panel template changes. Compatibility: Paper Minecraft 1.21.5 – 26.3, Java 25+.

    - 🔺 **Protection flags looked as if they couldn't be changed.** On servers whose locale files were first written by BentoBox 3.12 or earlier, every rank in a protection flag's tooltip showed in the same cyan, so allowed, blocked and minimum ranks looked identical and a click seemed to do nothing. Old locale files show green, red and dark green ranks again. This also affected the team menu's rank filter and the Command Ranks panel.
    - 🔡 **Click hints restored in nine languages.** Czech, German, Spanish, French, Italian, Japanese, Latvian, Polish and Turkish were missing the "Left click / Right click" hints on protection flags and the "Click to toggle / open" hints on settings. The Italian layouts and the Turkish blocked-rank line are also fixed.

    🔡 **Refresh your locale files** if you have upgraded from an older BentoBox. BentoBox never overwrites existing locale text, so a server upgraded over many versions keeps the wording it was first installed with. See [Languages & Messages](About/Multilingual.md#troubleshooting) for how.

    [Release v3.23.7](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.23.7)

??? note "What's new in v3.23.6 — always-allowed entity types & blueprint loading fix"
    **Released:** 2026-11-07

    No `config.yml` changes. Compatibility: Paper Minecraft 1.21.5 – 26.3, Java 25+.

    - 🔡 **Always-allowed entity types (`ALLOW_MOBS`).** A new world setting in each game mode's admin settings panel (iron ingot icon) lists entity types that spawn even when animal or monster spawning is off, at world and island level. Iron Golem is on the list by default, so village iron farms keep working. The **Limit entity type spawning** block list still wins if a type is on both. Permission: `[gamemode].admin.settings.ALLOW_MOBS`. See [Mob spawning precedence](Island-Protection,-Flags-&-Ranks.md#mob-spawning-precedence).
    - 🔺 **"All blueprints loaded" could fail to fire.** With several game modes loading blueprints at once, BentoBox could miss a completion and never reach its ready state, so addon `allLoaded()` hooks, ready-gated commands and `BentoBoxReadyEvent` never ran. Fixed, along with four related main-thread/async races.
    - 📊 **bStats:** failed commands now report the locale key the player saw as the reason and are counted per server; a new `worldSize` chart reports the on-disk size of island worlds as a bracket.
    - Fixed a spurious first-run `File not found` log from the new core world settings store.

    🔺 **Iron farms:** where animal spawning was turned off to stop golems, golems will spawn again. Remove Iron Golem from "Always-allowed entity types" to restore the old behaviour.

    🔺 **New data store:** the allow list is saved per game mode by BentoBox, not in the game mode's `config.yml` — `plugins/BentoBox/database/CoreWorldSettings/<GameMode>.json` on flat-file, the `WorldSettings` table on SQL/Mongo.

    🔡 **Locale note:** new keys under `protection.flags.ALLOW_MOBS` (`name`, `description`, `always`, `flags`). Custom locale files without them show the key names.

    [Release v3.23.6](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.23.6)

??? note "What's new in v3.23.5 — Sulfur Cube TNT protection & `/island go` underscores"
    **Released:** 2026-10-31

    A bug-fix release. No `config.yml`, locale or panel template changes. Compatibility: Paper Minecraft 1.21.5 – 26.3, Java 25+.

    - 🔺 **Sulfur Cube explosions now follow the TNT flags.** A Sulfur Cube that had absorbed TNT exploded as itself rather than as primed TNT, so it was not checked against `TNT_DAMAGE` and could destroy builds on islands with TNT damage turned off. Its explosions now follow `TNT_DAMAGE` on islands and `WORLD_TNT_DAMAGE` off-island, for both block and entity damage. A player lighting a Sulfur Cube with flint and steel or a fire charge is checked against `TNT_PRIMING`, as for a TNT block. Ignition by redstone, dispensers or other explosions has no player, so `TNT_PRIMING` cannot apply, but the explosion still follows `TNT_DAMAGE`. Servers older than Minecraft 26.2 have no Sulfur Cube, so nothing changes there.
    - 🐛 **`/island go` treats underscores as spaces.** `/island go happy_place` now finds a home named `Happy Place`. An exact match still wins, and a name that matches more than one destination is rejected rather than guessed. See [Finding the right home](About/IslandManagement.md#homes).

    **AOneBlock note:** AOneBlock ships with `TNT_DAMAGE: true` by default, so Sulfur Cube explosions there still do damage unless you set it to `false`.

    [Release v3.23.5](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.23.5)

??? note "What's new in v3.23.4 — safe End arrival & inventory use in panels"
    **Released:** 2026-10-17

    A bug-fix release. No `config.yml`, locale or panel template changes. Compatibility: Paper Minecraft 1.21.5 – 26.3, Java 25+.

    - 🐛 **End portal no longer drops players into the void.** With `create-obsidian-platform: false`, the player was sent straight to the portal destination whether or not there was a floor. Unsafe End arrivals now go to the nearest safe spot, then the highest block, then a pod. Repeat portal events while the player stands in the portal are cancelled, so they are not sent to the vanilla End spawn. Arrivals that are already safe still teleport instantly, and nothing changes when the platform is on. Safe-spot pods now place the player in the centre of the block.
    - ✨ **Use your own inventory while a panel is open.** Players can pick up, place, swap and drop items (Q / Ctrl+Q) and use bundles in their own inventory while a BentoBox panel such as `/island settings` is open. Shift-clicks, double-click collecting and drags that touch a panel slot stay blocked, so items cannot end up in the panel.
    - 🧩 **Addon API:** `PanelListener` has a new default method, `allowsPlayerInventoryClicks()`, which returns `false`, so panels with a listener (such as icon pickers in Challenges and Biomes) behave as before. Return `true` to opt in. See [Templated Panel](../Tutorials/api/Templated-Panel.md#listener-method). `Addon.getConfig()` now returns an empty configuration instead of `null` when the addon has no `config.yml`, so `saveConfig()` no longer throws.

    [Release v3.23.4](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.23.4)

??? note "What's new in v3.23.3 — obsidian dupe fix & Command Ranks template"
    **Released:** 2026-10-03

    A bug-fix and panels release. No `config.yml` or locale changes. Compatibility: Paper Minecraft 1.21.5 – 26.3, Java 25+.

    - 🐛 **Obsidian scooping dupe fixed.** With OBSIDIAN_SCOOPING, the lava was handed out one tick after the click without re-checking, so mining the obsidian in that tick gave both the obsidian and the lava, and moving the bucket out of the hand could give lava without using a bucket. Both are now re-checked first. **Updating is recommended for every server with OBSIDIAN_SCOOPING enabled.**
    - ⚙️ **Customisable Command Ranks panel.** Laid out by the new `panels/command_ranks_panel.yml` (written on first start; a game mode's own copy takes precedence), with `COMMAND`, `NEXT` and `PREVIOUS` buttons. It now pages at 45 commands — the old panel silently dropped every command after the 49th. See [Customizing the Command Ranks panel](Island-Protection,-Flags-&-Ranks.md#customizing-the-command-ranks-panel).
    - ✨ **Settings panel improvements.** `/island settings` opens in the Basic/Advanced/Expert mode the player last chose, and the Protection and Settings tabs share one mode (the admin panel still opens in Expert). Command Ranks hides sub-commands the player has no permission for (ops still see everything). The Break Spawners icon no longer shows vanilla's spawn egg tooltip.
    - 🐛 **Multiverse `auto-load` respected.** Since 3.22.0 the Multiverse hook reset `auto-load: false` on every BentoBox world at every startup. It is now set only when BentoBox first imports a world; existing Multiverse entries are left as configured.
    - 🧩 **Addon API:** the admin `deaths set|add|remove|reset` commands fire `PlayerDeathsChangedEvent` (world, player, action, amount, old and new counts), so Level can follow admin changes. It is not fired for natural deaths.

    [Release v3.23.3](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.23.3)

??? note "What's new in v3.23.1 — Minecraft 26.3 & template-driven settings panels"
    **Released:** 2026-09-25

    Compatibility: Paper Minecraft 1.21.5 – 26.3, Java 25+.

    - 🎮 **Minecraft 26.3 "Wilderness Bound" support.** The new cushions are protected by existing flags — placing needs PLACE_BLOCKS, hitting or shooting needs BREAK_BLOCKS, and sitting needs RIDING — and straw beds are protected by BED, so visitors can no longer sleep in (and use up) an island's straw beds. No new flags. At release, Paper 26.3 was only available as alpha builds (tested on build 41).
    - ⚙️🔡 **Customisable settings panels.** `/island settings` and `/admin settings` are built from `panels/settings_panel.yml` and `panels/admin_settings_panel.yml`, written on first start. Tab layout, pinned flags, the panel title and the order of a flag's lore can be customised; the defaults look exactly like the old panels. See [Customizing the Settings Panel](Island-Protection,-Flags-&-Ranks.md#customizing-the-settings-panel).
    - 🐛 **Deleted islands no longer count against a player.** After a reset or `/[admin] delete`, the island stayed in the per-player index until restart, which blocked transfers ("player already owns N islands") and confused `/[admin] delete`.
    - 🐛 A template button's `fallback:` record now renders correctly.

    🔡 **Locale note.** One new key, `panels.settings.title`, sets the settings panel title separately from the tab names. Custom locale files without it fall back to the bundled text. The flag lore layout (`protection.panel.flag-item.description-layout`) can now use the `[ranks]` and `[tooltips]` placeholders, but is unchanged unless you opt in.

    [Release v3.23.1](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.23.1)

??? note "What's new in v3.23.0 — console-ready setrank"
    **Released:** 2026-09-19

    Compatibility: Paper Minecraft 1.21.x – 26.2, Java 25+.

    - 🔡 **`/[admin] setrank` works from the console.** New syntax `/[admin] setrank <player> <rank> [island owner | x,y,z]`, backwards compatible. Ranks can be given by keyword, translated name or number; the right island is picked when the player owns one island and is a member of another; and an island can be named by its centre. Tab completion was off by one and is fixed. The affected player is told their rank changed — see the [command table](Commands.md#admin-commands) above.
    - 💡 **Behaviour change:** with no island argument, `setrank` now acts on the island the player is a *member* of rather than their own island, so it can no longer accidentally demote an owner. Setting `owner` is refused with a pointer to `setowner`.
    - 🐛 **Metadata console spam fixed.** Player and island metadata maps are now thread-safe. A corrupted map previously threw `NoSuchElementException` on every player move (seen via Border) until restart.

    🔡 **Locale note.** `commands.admin.setrank` gained `cannot-set-owner`, `already-rank` and `admin-changed-rank`; `unknown-rank` now takes `[rank]` and `[ranks]`. All 24 bundled locales are updated; add the new keys to any custom locale file.

    [Release v3.23.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.23.0)

??? note "What's new in v3.22.4"
    **Released:** 2026-09-06

    A bug-fix and performance release. Compatibility: Paper Minecraft 1.21.x – 26.2, Java 25+.

    - 🔡 **`/[admin] info <player>` shows every island.** All of a player's islands in the world (owned and team) are listed, each block headed by the island name, and a new optional `[island name]` argument picks just one — see the [command table](Commands.md#admin-commands) above. Name matching is forgiving (exact, then case- and space-insensitive, then unique prefix), multi-word names need no quotes, and tab completion offers the player's island and home names.
    - ⚙️ **Island history cap.** A new `island.history.max-entries` option in `config.yml` caps how many history (log) entries each island keeps; the oldest are dropped first. The default **`0`** means unlimited, so existing servers keep their current behaviour. Capping can undercount the historical-members placeholder once old `JOINED` entries are dropped.
    - 🐛 **Purge no longer crashes.** `/[admin] purge <days> confirm` failed with `IslandEvent may only be triggered synchronously` on the first fully reaped island and left its database row behind. Island events are now fired on the main thread after the async region deletion.
    - 🐛 **Sub-command labels no longer change.** Typing an alias such as `/ob h` renamed the shared `go` command to `h` in everyone's tab completion and help — much more visible since Brigadier registration in 3.22.0. Fixed; the `home` / `h` aliases are unchanged.
    - 🐛 **Player heads resolve through the server.** Online players' heads come from their live profile and everyone else is looked up in Paper's own profile cache before falling back to mc-heads or Mojang, so panels such as TopBlock show real heads instead of Steve after rate limits.
    - ⚡ Performance: bounds checks no longer allocate, map sweeps use iterators, and a shared GSON instance replaces per-call construction.

    🔡 **Locale note.** `commands.admin.info.parameters` now reads `<player> [island name]` and a new key `commands.admin.info.island-name` was added. All 24 bundled locales are updated; if you maintain a custom locale file, add the new key or the admin info block will show the raw key for the island name line.

    [Release v3.22.4](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.22.4)

??? note "What's new in v3.22.3 — bStats opt-out & Paper 26.2"
    **Released:** 2026-08-22

    Mostly a bug-fix and API release. Compatibility: Paper Minecraft 1.21.5 – 26.2, Java 25+.

    - ⚙️ **bStats metrics opt-out.** A new `general.metrics` option in `config.yml` (default **`true`**) lets you disable BentoBox's anonymous, aggregate usage statistics without touching the global switch in `plugins/bStats/config.yml`, which turns bStats off for every plugin on the server. Set it to `false` and **restart** — the collector is registered at startup, so `/bbox reload` is not enough. No personal data is ever sent; see [Privacy & Data Collection](Privacy.md).
    - 🔺 **Built against Paper 26.2 and Adventure 5.** Addon authors: Adventure 5 seals `Component` (Mockito can no longer mock it) and replaces `ClickEvent.value()` with `payload()`. Addons already deployed on a 26.2 server may be affected at runtime; recompiling against BentoBox 3.22.3 surfaces any issues at compile time — see [PR #3067](https://github.com/BentoBoxWorld/BentoBox/pull/3067) for the full removal list. Server admins need do nothing.
    - 🔲 **Dialog grid layout for addon developers.** `DialogBuilder#columns(int)` lays a multi-action dialog's buttons out in a grid instead of the default two-wide list, and `DialogButton` gains a width (1–1024) plus `withWidth(int)`. Existing callers are unaffected.
    - 🐛 **Player-head 429 spam fixed.** Opening a panel with player heads (a top-ten list, say) could flood the console with HTTP 429 errors from `sessionserver.mojang.com`, because heads delivered without texture data were re-resolved on every open. Texture-less heads now degrade to a plain head, and a failed fetch no longer evicts a cached head that already works.
    - 🐛 **YAML numbers load into the declared field type.** A config value such as `20`, written without a decimal point, now loads correctly into `double`, `float` and `long` fields instead of throwing `ClassCastException`.
    - 🐛 **Literal colour names in panels.** The Management panel showed addon names like `whiteChallenges` after a colour refactor; fixed.
    - 📄 Published JSON Schemas (draft 2020-12) for the `.blueprint` and blueprint-bundle file formats.

    [Release v3.22.3](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.22.3)

??? note "What's new in v3.22.2"
    **Released:** 2026-08-10

    A bug-fix patch on top of 3.22.0 — no new features, config keys or locale changes; a drop-in replacement. There is no 3.22.1 release. Compatibility: Paper Minecraft 1.21.5 – 26.2, Java 25+.

    - 🔺 🐛 **Player name lookups resolve to the right account.** `/[player_command] team trust <name>` and `/[player_command] info <name>` could silently answer for a UUID that had not held that name in months: superseded name records were never deleted from the database, and the lookup took the first match. Names are now matched ignoring case, stale records are deleted, and online players are checked first. **Take a backup before updating** — existing databases heal themselves as players log in (the purge runs once per rename, not per join) and no manual migration is needed.
    - 🐛 **Bedrock players can use panels again.** Geyser expands one tap into several Java click packets in the same tick, and the `panel.click-cooldown-ms` check introduced in 3.22.0 was swallowing the one that mattered — every tap got `slow-down` and nothing happened. Same-tick clicks are now treated as one gesture; spam protection is unchanged at one action-bearing click per tick.
    - 🐛 **A disabled addon no longer leaves broken commands behind.** A game mode dropped for a missing dependency (ChunkBlock without Level, for instance) kept its commands registered, and every subcommand threw an NPE. Commands, flags and listeners are now all withdrawn when an addon fails to enable.
    - 🐛 **Returning from a standard nether lands you on your own island.** With a shared nether and `create-and-link-portals: false` (AOneBlock's default), players coming back through a portal were dumped on whichever island sits nearest 0,0. The destination now falls back to the island's home location.

    [Release v3.22.2](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.22.2)

??? note "What's new in v3.22.0 — Brigadier commands"
    **Released:** 2026-08-01

    A commands-and-visibility release. Compatibility: Paper Minecraft 1.21.5 – 26.2, Java 25+.

    - ⚙️ 🔺 **Commands are registered with Paper's Brigadier API.** Players now see BentoBox subcommands and completions *as they type* — `/island t…` offers `team` in the chat bar — instead of the client knowing nothing until enter or TAB. The subcommand tree is advertised to a depth of 4; deeper subcommands still work, they just are not pre-advertised. Aliases and the `plugin:label` form are sent as redirects rather than duplicated trees. A new `general.brigadier-commands` option in `config.yml` defaults **on**; set it to `false` and `/bbox reload` to fall back to the legacy command map if another plugin conflicts. BentoBox also falls back automatically if it cannot hook the registrar.
    - 🔺 **Structure searches are suppressed automatically in worlds that generate no structures.** A cartographer rolling an explorer-map trade — or an Eye of Ender, dolphin or treasure map — used to run a synchronous structure search that could never succeed in a void world, scanning to the radius cap and blowing past the 60-second watchdog. BentoBox now asks the world's generator whether it places structures at all and skips the search if it does not, with **no configuration needed**. AOneBlock and BSkyBlock get this automatically; SkyGrid, Boxed, CaveBlock and AcidIsland are unaffected because they do generate structures. A per-world `structures` entry of `true` still force-enables a structure, as an escape hatch for converted worlds that contain pre-existing ones. This complements the opt-in `world.disabled-structures` list added in 3.20.0.
    - **`/island settings` now opens out in the world.** Players away from any island, or in a game mode where they never own one, used to get "You do not have an island!". The panel now opens with a read-only **World Protections** tab showing which protection flags are active for the world — which is exactly what governs them where they are standing. See [Protection](Island-Protection,-Flags-&-Ranks.md#world-protection-view).
    - 🐛 **Addon data queued during shutdown is no longer discarded.** Anything an addon saved from `onDisable()` was queued into a database pipeline that had already stopped draining, so it was silently, intermittently lost on every restart. Nine bundled addons save on disable — Boxed, AOneBlock, Raft, Challenges, Limits, DragonFights, CheckMeOut, ControlPanel and InvSwitcher — and with InvSwitcher the stale stored inventory was then re-applied on join, making it a rollback rather than just a lost write. Shutdown writes are now drained before the database closes.
    - 🐛 **BentoBox commands work from NPCs, signs and GUI plugins again.** Brigadier registration had taken BentoBox commands out of the Bukkit command map that other plugins dispatch through, so an NPC running `/oneblock go` answered with the server's no-permission message and ran nothing. Commands are now registered with the command map as well. This only ever affected 3.22.0 development builds.
    - 🐛 **`Island.setFlag` no longer discards writes.** Setting a protection rank on an island that had no entry yet for that flag — which is every freshly created island — silently did nothing. `SETTING` and `WORLD_SETTING` flags were unaffected.
    - 🐛 **Repeated warnings stay throttled.** A player alternating between two different limit messages bypassed the 4-second notification cooldown entirely. Each distinct message is now throttled independently.
    - 🐛 **BlueMap marker sets stay in their own worlds.** An addon's marker set no longer appears in the sidebar of every other map on the server, and `createMarkerSet()` / `removeMarkerSet()` no longer throw during a `/bluemap reload`.
    - 🐛 **Multiverse tidy-up.** BentoBox worlds now get `auto-load: false` even when Multiverse already knew about them, and the dead seed-world (`<world>/bentobox`) registration is gone. Existing stale entries still need `/mv remove`.
    - 🐛 **Flags from addons dropped for missing dependencies are cleaned up.** An addon whose hard dependency was absent had already registered its flags and listeners before being dropped, leaving listeners firing for a world that never existed.
    - **Six new bStats charts** report addon and game mode versions, addon API levels, settings changed away from their defaults, and how and where commands fail. Only the failure kind and a stable permission-derived command key are submitted — never arguments or player names.
    - 🔡 **Traditional Chinese (`zh-TW`) locale** added, contributed by @qwe664. No existing locale keys changed, so custom locale files need no work.

    [Release v3.22.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.22.0)

??? note "What's new in v3.21.0 — modal dialogs"
    **Released:** 2026-07-22

    A player-experience release. Compatibility: Paper Minecraft 1.21.5 – 26.2, Java 25+.

    - ⚙️ 🔡 **Modal dialogs for high-friction flows.** Sensitive-command confirmations, the `/island go` destination picker, team invites, and a first-join game-mode chooser can now appear as real modal dialogs the player cannot misread or scroll past. A new `island.dialogs` section in `config.yml` holds one toggle per flow — `confirmations`, `go-picker` and `team-invites` default **on**, `game-mode-selection` defaults **off** because it is intrusive by design. Dialogs need a Minecraft 26+ server; on anything older every toggle is ignored and the classic chat/command behaviour is used, so no action is needed there.
    - **Forgiving `/island go` matching.** `/island go myisland`, `hom`, or a name typed with the wrong case or a stray double space now teleports the player where they meant instead of failing an exact match and dumping the full list. See [Home Locations](About/IslandManagement.md#homes).
    - 🔡 **Locale note:** new dialog keys (`general.dialogs.*`, plus dialog and picker keys under the confirmation, `island go` and team-invite commands) were added to all 22 bundled locales. Regenerate or update any custom locale files.
    - 🔧 **Addon developers** get the same `world.bentobox.bentobox.api.dialogs` API used by core — see [Modal dialogs](Developer-Documentation.md#modal-dialogs).

    [Release v3.21.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.21.0)

??? note "What's new in v3.20.0 — command suggestions & core structure suppression"
    **Released:** 2026-07-11

    A quality-of-life release. Compatibility: Paper Minecraft 1.21.5 – 26.2, Java 25+. Nothing changes on upgrade unless you opt in.

    - 🔡 ⚙️ **Did-you-mean command suggestions.** A mistyped command like `/teams` or `/island invit Floris` now offers the closest matching BentoBox command — clickable, or accept by typing `yes`/`y` within 30 seconds — instead of dumping the help text. Suggestions match labels and aliases across every command tree, are permission-filtered, and use the game-mode world the player is standing in to disambiguate. Two new toggles under `general.did-you-mean` in `config.yml` — `unknown-commands` and `subcommands` — both default **on**; set either to `false` and `/bbox reload` to disable.
    - ⚙️ 🔺 **Core vanilla-structure suppression for every game mode.** Disabling a vanilla structure is now a single core setting instead of a per-addon job. A new `world.disabled-structures` list in `config.yml` (applied to every BentoBox overworld/nether/end) stops the listed structures generating **and** skips them in structure searches — `/locate`, Eyes of Ender, explorer/treasure maps, dolphins and villager cartographer trades — fixing the long-standing `/locate` main-thread freeze and near-spawn structure leaks. Keys are case- and separator-insensitive (`trial_chambers`, `ancient-city`). A game mode can override the list per-structure. **The list is empty by default, so behaviour is unchanged until you opt in.**
    - 🔌 **Nexo hook.** BentoBox can now place and detect [Nexo](https://nexomc.com/) custom blocks and items, alongside the other custom-item integrations.
    - 🔌 **Oraxen block placement.** `OraxenHook.placeBlock` exposes Oraxen custom-block placement to addons, matching the other custom-block hooks.
    - 🔡 **Locale note:** three new `general.did-you-mean` keys were added to all 22 bundled locales, and the pre-existing missing key `commands.admin.team.setowner.specify-island` was filled in every non-English file. Regenerate or update any custom locale files.

    [Release v3.20.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.20.0)

??? warning "What's new in v3.19.0 — bed/anchor respawns now honored"
    **Released:** 2026-07-08

    Compatibility: Paper Minecraft 1.21.5 – 26.2, Java 25+.

    - 🔡 **New `FISHING` protection flag.** Stops players fishing into protected areas from outside the island (the flag checks the hook's location). Defaults to visitor rank, so nothing changes until you raise it.
    - 🔺 **Bed & respawn-anchor spawns are now honored.** Dying on an island now respawns you at your bed or charged respawn anchor when it's on an island you're a member of. Controlled by the new `BED_ANCHOR_RESPAWN` world setting (**enabled by default**); economy-sensitive servers that want the old "always respawn at island home" behaviour should disable it.
    - 🐛 **End exit portal no longer dumps you at world spawn.** Jumping through the end exit portal now routes you to your safe island home on multi-gamemode servers.
    - 🐛 **Item frames and paintings survive blueprints.** Frames keep their facing and contents, and paintings restore their artwork, instead of popping off or facing the wrong way.
    - 🔡 **Recover islands pending deletion.** New `/[admin] undelete`, a stand-on `/[admin] delete` (no player argument), and a confirmation prompt on `/[admin] register` can now rescue soft-deleted islands before their region files are purged (see the Per-Game-Mode Admin Commands table above).
    - ⚙️ **BlueMap island layer survives reloads.** Owner pins and area boxes no longer vanish after `/bluemap reload`. A new `bluemap` section in `config.yml` adds `island-markers` and `island-areas` toggles (both default `true`), mirroring the Dynmap toggles, plus marker customization.
    - ⚙️ **Configurable team panel button icons + member/prospect text.** The STATUS, RANK-filter and INVITE buttons in the team panel now honour the `icon:` set in `team_panel.yml`, and the member/prospect button name and description are now driven by locale keys. Defaults reproduce the previous appearance exactly.
    - ⚡ **Settings-GUI click spam no longer spikes MSPT.** Spam-clicking `/is settings` dropped from ~30–40 MSPT to negligible via in-place panel refresh and a translation cache.

    [Release v3.19.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.19.0)

??? warning "What's new in v3.18.0 — Minecraft 26.2 support requires Java 25 (server)"
    **Released:** 2026-06-27

    - 🔺 **Minecraft 26.2 support + Java 25.** BentoBox now runs on the Minecraft 26.x line (26.2 supported at runtime) and the build has migrated to the Java 25 toolchain. **Your server must run on a Java 25-capable Paper build for the 26.x line.** Already-built addon jars keep working unchanged — only addon *developers* recompiling against this release need to move their own build to Java 25. Compatibility: Paper Minecraft 1.21.5 – 26.2, Java 25+.
    - ⚙️ **Dynmap island marker / area toggles.** A new `dynmap` section in `config.yml` adds `island-markers` (the house icon at the centre of every island) and `island-areas` (the protected-area border box) switches. Both default to `true`, preserving existing behaviour; set either to `false` and run `/bbox reload` to hide those overlays on servers where dense islands flood the map.
    - **Admin range bonus management.** New `/[admin] range removebonus` and `/[admin] range purgebonus` commands clear bonus protection ranges from one island or every island — ideal after uninstalling an addon that granted them (see the Per-Game-Mode Admin Commands table above).
    - 🐛 `/is team setowner` is no longer blocked by the island limit when transferring to an existing team member.
    - 🐛 The Vault hook now retries after addons enable, fixing economy integration that depended on load order.

    [Release v3.18.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.18.0)

??? note "What's new in v3.18.1"
    **Released:** 2026-07-01

    Maintenance release.

    - 🐛 **Multi-line lore & names keep their colour.** Text after the first line of a GUI tooltip no longer falls back to the default purple — the serializer now re-emits the active colour (and decorations) after each newline, fixing tooltips across all addons.

    [Release v3.18.1](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.18.1)

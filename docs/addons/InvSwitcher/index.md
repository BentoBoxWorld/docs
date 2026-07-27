# InvSwitcher

**InvSwitcher** separates player inventories and other aspects between the various worlds.

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("InvSwitcher") }}

The following are switched per-world:

* Inventory & armor
* Advancements
* Food level
* Experience
* Health
* Game mode (creative, survival, etc.)
* Money (per-world economy, added in 1.18.0)

## How to use

1. Place the addon jar in the addons folder of the BentoBox plugin
2. Restart the server
3. Done!

## Compatibility with other inventory plugins

!!! warning "Do not run two inventory managers"
    InvSwitcher must be the only plugin managing per-world inventories. Running it alongside
    Multiverse-Inventories, PerWorldInventory, MultiInv or similar makes both plugins save and
    restore the player on every world change, and they overwrite each other's data.

The usual symptom is disappearing items: pick up an item on your island, go to the lobby, come
back, and the island inventory is empty. Nothing appears in the console, because neither plugin is
failing — each is faithfully saving a player state the other has already rewritten. In testing, the
island inventory ended up filed under the *lobby's* storage key, and an empty inventory under the
island's.

The InvSwitcher version makes no difference. If you are seeing this, check for a second inventory
plugin before anything else.

### Multiverse-Inventories

Two things commonly mislead admins here:

- **Leaving the BentoBox worlds out of every inventory group does not help.** Groups control which
  worlds *share* an inventory, not which worlds Multiverse-Inventories handles. It still writes a
  per-world profile for a world that is in no group.
- **`/mv remove <world>` does not help either.** Multiverse-Core re-registers BentoBox worlds as
  they are created, so the removal is silently undone on the next restart. Setting
  `auto-import-3rd-party-worlds: false` does not prevent this — it only suppresses the import sweep
  that runs when Multiverse-Core starts, which is before BentoBox has created its worlds.

Multiverse-Inventories has no config option to ignore a world, but it does have a bypass
permission. First enable it in the Multiverse-Inventories `config.yml` (it ships as `false`):

```yml
share-handling:
  enable-bypass-permissions: true
```

Then grant `mvinv.bypass.world.<world>` for each BentoBox world — including its nether and end — to
every player. With [LuckPerms](https://luckperms.net/):

```
lp group default permission set mvinv.bypass.world.bskyblock_world true
lp group default permission set mvinv.bypass.world.bskyblock_world_nether true
lp group default permission set mvinv.bypass.world.bskyblock_world_the_end true
```

Setting the nodes on a group that every player inherits (such as `default`) covers new players
automatically. Repeat for each game mode world you run.

!!! tip "Operators do not get this permission automatically"
    Granting op is not enough — the node has to be given explicitly. Testing as an op without it
    looks exactly like the fix not working.

Use one node per world. Avoid `mvinv.bypass.world.*`, which switches Multiverse-Inventories off for
every world, including the ones you still want it to manage.

## Config.yml

InvSwitcher has a `config.yml` with two main sections.

### Worlds

Lists the gamemode worlds that InvSwitcher operates in. Nether and End worlds are included automatically.

```yml
worlds:
- bskyblock_world
- acidisland_world
- oneblock_world
# ... etc.
```

### Options

Controls which player aspects are switched per-world and, optionally, per-island.

```yml
options:
  inventory: true
  health: true
  food: true
  advancements: true
  gamemode: true       # game mode (Survival/Creative/etc.)
  experience: true
  ender-chest: true
  statistics: true
  money: true          # Per-world money (added in 1.18.0). Requires Vault.
  # Per-island inventory switching (added in 1.17.0)
  # The world-level option must also be true for the island option to take effect.
  islands:
    active: true       # Enable per-island switching overall
    inventory: true    # Give players a different inventory on each island they own
    health: false
    food: false
    advancements: false
    gamemode: false
    experience: false
    ender-chest: true
    statistics: false
    money: false       # Per-island wallets (added in 1.18.0). False = per-world money only.
```

Set `islands.active: true` to allow players who own more than one island to maintain separate inventories (and other aspects) per island, not just per gamemode world.

### Economy

Added in 1.18.0. When `options.money` is enabled, InvSwitcher registers itself as the Vault economy provider and keeps a **separate balance for each switched world**. Transactions (shop sales, `/pay`, jobs, etc.) are routed to the balance of the world they belong to — even when the target player is offline or in a different world. Worlds InvSwitcher does not manage are passed through to your existing economy plugin (e.g. EssentialsX); if no other economy is present, InvSwitcher handles every world itself.

!!! warning "Requires Vault"
    Per-world money requires the [Vault](https://www.spigotmc.org/resources/vault.34315/) plugin. A separate economy plugin is optional — InvSwitcher can be the only economy. If you run the **Bank** addon, island wallets become per-world too.

The `economy:` block is only used when `options.money` is `true`:

```yml
economy:
  starting-balance: 0.0              # Balance given on first entry to a managed world (unless imported)
  currency-name-singular: Dollar
  currency-name-plural: Dollars
  fractional-digits: 2               # Digits after the decimal point
  import-existing-balances: true     # Import each player's existing balance once, on first entry
  delegate-unmanaged-worlds: true    # Pass unmanaged worlds through to the previous economy plugin
  debug: false                       # Log every transaction to the console (verbose)
```

## Commands

Added in 1.18.0. Each managed game mode gains its own economy commands, scoped to that game mode's world, so `/bsb balance` shows your BSkyBlock balance and `/ai balance` your AcidIsland balance regardless of where you are standing.

!!! tip
    `[player_command]` and `[admin_command]` are the commands that differ depending on the gamemode you are running.

=== "Player commands"

    | Command | Description |
    |---|---|
    | `/[player_command] balance` | Show your money balance for this world |
    | `/[player_command] pay <player> <amount>` | Pay another player |

=== "Admin commands"

    | Command | Description |
    |---|---|
    | `/[admin_command] eco give <player> <amount>` | Give money to a player |
    | `/[admin_command] eco take <player> <amount>` | Take money from a player |
    | `/[admin_command] eco set <player> <amount>` | Set a player's balance |
    | `/[admin_command] eco balance <player>` | Show a player's balance |

## What it does
This addon will give players a separate inventory, health, food level, advancements and experience for each gamemode installed and their corresponding worlds. It enables players to play each gamemode independently of each other.

## An example
**BSkyBlock**'s Inventory, Health, Food level, Advancements and Experience are shared only between its corresponding worlds:
- BSkyBlock_world
- BSkyBlock_world_nether
- BSkyBlock_world_the_end

**Please note:**
- It is not limited to just BentoBox worlds. It applies to all worlds on the server (right now).

## Changelog

??? note "What's new in v1.19.1"
    **Released:** 2026-07-02

    Bug-fix release — drop-in replacement, no config or locale changes.

    - 🐛 **Fixed per-island health death loop.** With per-island health enabled, a player who owned more than one island could get trapped in an endless respawn/death screen after dying. When their state was captured mid-death it recorded a health of `0`; loading that value back on the death island applied `setHealth(0)`, killing them again the instant the world loaded. InvSwitcher now never applies a fatal stored health to a live player — a stored value of `0` (only ever produced mid-death) restores full health instead, matching vanilla respawn behaviour.

    [Release v1.19.1](https://github.com/BentoBoxWorld/InvSwitcher/releases/tag/1.19.1)

??? note "What's new in v1.19.0"
    **Released:** 2026-06-21

    Follow-up to the 1.18.0 per-world economy release. Drop-in replacement — no config or locale changes.

    - 🐛 **Standalone economy now works on its own.** InvSwitcher registers its own per-world Vault economy, but BentoBox hooks Vault before addons enable, so when InvSwitcher was the only economy on the server that early hook found nothing and was discarded — and economy-dependent addons such as **Bank** disabled themselves with *"Vault is required"*. InvSwitcher now registers a fresh Vault hook with BentoBox once its provider is live, so it works as the server's only economy (no separate economy plugin such as EssentialsX is needed).
    - 🐛 **Correct balance reported for offline economy transactions.** Admin `eco give/set/take` on an offline player reported a stale balance (e.g. "New balance: 0.00" right after giving 2,000). The money was always stored correctly; the confirmation message re-read the balance before the asynchronous save had flushed. Commands now report the authoritative balance returned by the transaction itself, and the offline read-after-write path was hardened so two rapid sequential transactions can no longer lose an update.

    [Release v1.19.0](https://github.com/BentoBoxWorld/InvSwitcher/releases/tag/1.19.0)

??? note "What's new in v1.17.0"
    **Released:** 2026-03-31

    - **Per-island inventory switching.** Players who own more than one island can now maintain separate inventories (and optionally health, food, experience, ender-chest, statistics) per island within the same gamemode. Enable with `options.islands.active: true` and configure each sub-option. The world-level option must also be `true` for its island counterpart to take effect.
    - ⚙️ New `options.islands` section in `config.yml`.
    - Bug fix: inventory was lost when returning to the original island.

    [Release v1.17.0](https://github.com/BentoBoxWorld/InvSwitcher/releases/tag/1.17.0)

??? note "What's new in v1.17.1"
    **Released:** 2026-05-09

    - 🐛 **Fixed inventory cleared when teleporting from a BentoBox world to a non-BentoBox world.** When a player left a BentoBox game world (e.g. BSkyBlock) for a non-BentoBox world (e.g. the default overworld or a third-party plugin world), their "outside" inventory could be lost because each non-BentoBox world stored data under its own key. All non-BentoBox worlds now share a single storage key, so the player's inventory is always restored correctly. Includes automatic migration for data saved under the old per-world keys.

    [Release v1.17.1](https://github.com/BentoBoxWorld/InvSwitcher/releases/tag/1.17.1)

??? warning "What's new in v1.18.0 — requires BentoBox 3.17.0"
    **Released:** 2026-05-31

    - 🔺⚙️🔡 **Per-world money.** InvSwitcher can now give every game world its own separate economy, on top of the inventories, health, XP and stats it already switches. With `options.money` enabled it registers itself as the Vault economy provider and routes every transaction to the correct world's balance — even when the player is offline or in a different world.
    - ⚙️ **New config:** `options.money`, `options.islands.money`, and an `economy:` block (starting balance, currency names, fractional digits, import toggle, delegate toggle, debug). Existing configs keep working; the new keys are added with safe defaults.
    - 🔡 **New commands & placeholders:** per-game-mode `balance` and `pay` for players, admin `eco give/take/set/balance`, plus `<gamemode>_invswitcher_balance` and `<gamemode>_invswitcher_balance_formatted` placeholders, translated into every language BentoBox ships.
    - 🐛 Advancements no longer inflate experience on world switch.
    - 🐛 BentoBox island resets no longer wipe the wrong world's inventory — InvSwitcher now clears the *stored* data for the correct world instead.

    🔺 **Requires BentoBox 3.17.0:** InvSwitcher now listens to BentoBox's player-reset events (including the new money-reset event), which were introduced in 3.17.0. It will not load on older BentoBox versions.

    🔺 **Economy behaviour change:** when `options.money` is enabled, InvSwitcher becomes the server's Vault economy provider. Worlds it does not manage are passed through to your existing economy (e.g. EssentialsX); managed worlds get their own per-world balance. Requires the Vault plugin.

    [Release v1.18.0](https://github.com/BentoBoxWorld/InvSwitcher/releases/tag/1.18.0)

## Placeholders

{{ placeholders_source("InvSwitcher") }}

## Translations

{{ translations("InvSwitcher") }}

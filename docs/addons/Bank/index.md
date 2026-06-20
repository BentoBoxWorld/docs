# Bank

**Bank** provides an **island bank** to enable island members to share money.

Created and maintained by [tastybento](https://github.com/tastybento).

{{ addon_description("Bank") }}

## Introduction

Each island has a bank account. Players can deposit or withdraw money from their regular economy accounts into the island account where it is pooled. The island owner can decide which rank of team member can access the account via the settings menu. There is a `baltop` command that players can use to see which island has the most, or least money. 

### Features

* Save or spend money as an island team
* Compete to have the highest balance in the game
* See a full history of transactions on the account

### Requirements
**Bank** requires an economy to be installed on the server that uses Vault. Ideally, the economy should be multi-world aware otherwise money may end up being shared between worlds and game modes.

## Commands
### Player commands

The default player command is `bank` and it can be changed in the config.yml. So you use the bank you do `/island bank` for example.

* `bank deposit <amount>` - deposit money into the island bank
* `bank withdraw <amount>` - withdraw money from the island bank
* `bank balance` - see your island bank balance
* `bank statement` - see a fancy statement of deposits/withdrawals, etc. on you island bank account

### Admin commands

The default admin command is `bank` and it can be changed in the config.yml.

Admin commands make money by magic.
* `bank give <player> <amount>` - deposit money into the player's island bank
* `bank take <player> <amount>` - withdraw money from the player's island bank
* `bank set <player> <amount>` - set the player's island bank balance to an amount
* `bank balance <player>` - see a player's island bank balance
* `bank statement <player>` - see a fancy statement of deposits/withdrawals, etc. on the player's island bank account

## Placeholders

Placeholders can be found [here](Placeholders).


## Configuration

```
bank:
  # BentoBox GameModes that can use Bank
  game-modes:
  - BSkyBlock
  - AOneBlock
  - AcidIsland
  - SkyGrid
  - CaveBlock
  commands:
    # User command
    user: bank
    # Admin command
    admin: bank
  placeholders:
    # This is how many ranks will be registered with the placeholder API.
    # There are two placeholders per rank:
    # %Bank_[gamemode]_top_name_1% with island level: %Bank_[gamemode]_top_value_1%
    # [gamemode] is bskyblock, acidisland, etc.
    number-of-ranks: 10
```

## Permissions

```
permissions:
  '[gamemode].bank.user':
    description: Player can use bank command
    default: true
  '[gamemode].bank.user.balance':
    description: Player can use bank balance command
    default: true
  '[gamemode].bank.user.deposit':
    description: Player can use the bank deposit command
    default: true
  '[gamemode].bank.user.withdraw':
    description: Player can use bank withdraw command
    default: true
  '[gamemode].bank.user.statement':
    description: Player can use the bank statement command
    default: true
  '[gamemode].bank.user.baltop':
    description: Player can use bank baltop command
    default: true
  '[gamemode].bank.admin':
    description: Player can use admin command
    default: op
  '[gamemode].bank.admin.balance':
    description: Player can use admin balance command
    default: op
  '[gamemode].bank.admin.give':
    description: Player can use the admin give command
    default: op
  '[gamemode].bank.admin.take':
    description: Player can use admin take command
    default: op
  '[gamemode].bank.admin.statement':
    description: Player can use the admin statement command
    default: op
  '[gamemode].bank.admin.set':
    description: Player can use admin set command
    default: op

```

## Like this addon?
You can [sponsor](https://github.com/sponsors/tastybento) to get more addons like this and make this one better!

## Changelog

??? warning "What's new in v1.10.0 — Breaking changes (Java 21, BentoBox 3.14.0, MiniMessage)"
    **Released:** 2026-06-16

    A modernisation release. Bank now targets **Java 21, Paper 1.21.11 and BentoBox 3.14.0**, and its entire locale set has been migrated to BentoBox's **MiniMessage** colour format.

    - 🔡 **New placeholder `%Bank_[gamemode]_latest_transaction%`** — shows a user's most recent island bank transaction, rendered as `[Username] [TxType] $[Amount]` (e.g. `tastybento Deposited $500.0`). Fully localised.
    - 🔡 **Complete language coverage** — Bank now matches the full BentoBox locale set (23 languages).
    - 🔡 🔺 **MiniMessage locale format.** All locale files were converted from legacy `&`/`§` colour codes to MiniMessage. Any customised Bank language files must be re-expressed in MiniMessage syntax — back them up, delete the old files to let them regenerate, then redo your edits.
    - 🔺 **Platform modernization.** Build upgraded to Java 21 / Paper 1.21.11 / BentoBox 3.14.0; `plugin.yml` `api-version` bumped to 1.21; test suite migrated to JUnit 5 + MockBukkit.
    - 🐛 Hardened bank transaction-history parsing against malformed entries and localised the latest-transaction placeholder fallback text.

    🔺 **Updating:** Update BentoBox to 3.14.0 and ensure the server runs Java 21 **before** installing this version. Back up any customised locale files first.

    [Release v1.10.0](https://github.com/BentoBoxWorld/Bank/releases/tag/1.10.0)

??? note "What's new in v1.9.1"
    **Released:** 2026-03-28

    - **Top island name placeholders.** `%Bank_[gamemode]_top_island_<number>%` now exposes the island name (not just the owner name) for each leaderboard position. Island names are cached alongside owner names and balances.
    - ⚙️ Interest compounding documentation and config comments corrected — the `compound-periods-per-year` calculation had an off-by-one that caused slightly incorrect compound interest. Update your config comments by replacing the old jar.

    [Release v1.9.1](https://github.com/BentoBoxWorld/Bank/releases/tag/1.9.1)

## Translations

{{ translations("Bank") }}

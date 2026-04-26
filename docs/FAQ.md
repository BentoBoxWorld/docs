# FAQ

This FAQ is ordered by how often each question comes up in the [BentoBox Discord](https://discord.bentobox.world) `#support-en` channel — the most common questions are at the top, and rare or legacy issues are grouped at the bottom.

!!! info "Diagnosis cheat sheet — run these *before* asking for help"
    - `/bentobox version` — shows BentoBox + addon versions and the server build
    - `/[admin_command] why <player>` — explains exactly which BentoBox flag (if any) is blocking a player's action; this is by far the fastest way to debug "I can't break/place/interact" reports
    - `/papi parse me <placeholder>` — verifies whether a PlaceholderAPI placeholder actually resolves on your server

## Contents

- [Installation and versions](#installation-and-versions)
- [Worlds and generation](#worlds-and-generation)
- [Mobs, spawning and entities](#mobs-spawning-and-entities)
- [Islands: size, protection and resets](#islands-size-protection-and-resets)
- [Teams, coop and visitors](#teams-coop-and-visitors)
- [Placeholders](#placeholders)
- [AOneBlock](#aoneblock)
- [Level addon](#level-addon)
- [Challenges addon](#challenges-addon)
- [Database and storage](#database-and-storage)
- [Customization: locales, colours and blueprints](#customization-locales-colours-and-blueprints)
- [Miscellaneous](#miscellaneous)
- [API and addon development](#api-and-addon-development)
- [Less common / legacy issues](#less-common-legacy-issues)
- [Sources](#sources)

## Installation and versions

### How do I install BentoBox, BSkyBlock and all those other addon things?

The easiest way to start is to download a "pack" of addons and BentoBox from [https://download.bentobox.world](https://download.bentobox.world).
You can also check out [this tutorial](BentoBox/Install-Bentobox.md) to learn about other ways.
**Welcome to our community!**

### Which BentoBox version do I need for my Minecraft version?

The major BentoBox versions track Minecraft versions:

- **BentoBox 3.x** — Minecraft **1.21.3 and newer**
- **BentoBox 2.7** — Minecraft **1.21.1**
- **BentoBox 2.6** — Minecraft **1.20.6**

If you upgrade your server's Minecraft version you must also upgrade BentoBox (and the matching addons), and vice versa. Mixing a newer BentoBox with an older Minecraft will fail to start, and using an old BentoBox on a newer Minecraft typically produces missing-particle errors, "internal error occurred attempting to perform this command", or broken GUIs. Older versions are linked from each project's GitHub *Releases* page.

### Which addon versions do I need for my BentoBox version?

Pick addons whose release notes target the same BentoBox major version. The easiest way is to download a "pack" from [https://download.bentobox.world](https://download.bentobox.world), which always contains a compatible set. Mixing BentoBox 3.x with addons that require BentoBox 2.x (or vice versa) is the single most common cause of plugins failing to load.

### Why does it say "internal error occurred attempting to perform this command" when I try to make an island?

In almost every case this is a BentoBox/Minecraft version mismatch (see above). Run `/bentobox version` and confirm BentoBox major version matches your Minecraft version. If it does, share the full server log (not just the chat error) when reporting the issue.

## Worlds and generation

### How do I make a BentoBox world the default world of my server?

Follow [Set a BentoBox world as the server default world](BentoBox/Set-a-BentoBox-world-as-the-server-default-world.md) step by step. The two things people miss are (1) setting the correct generator for the world in `bukkit.yml`, and (2) setting `level-name` in `server.properties` to the BentoBox world name. Skipping either causes superflat chunks to generate — see [Superflat chunks are generating in my worlds](#superflat-chunks-are-generating-in-my-worlds) at the bottom of this page.

### Can I run two gamemodes (e.g. BSkyBlock and Boxed) on the same server?

Yes — you cannot run two gamemodes in the **same world**, but every BentoBox gamemode addon creates and manages its own worlds, so installing multiple gamemode addons side by side just gives you multiple sets of worlds. Players choose which one to play with the relevant `/island` (or `/box`, `/ob`, etc.) command. To remove a gamemode you can simply delete the addon jar; deleting the world folders is optional.

### How do I completely reset BentoBox / wipe all islands?

Stop the server, delete the gamemode's world folders (e.g. `bskyblock_world`, `bskyblock_world_nether`, `bskyblock_world_the_end`), and delete the matching files in `plugins/BentoBox/database/Island/` and `plugins/BentoBox/database/Players/` (or the corresponding rows if you use SQL). On next startup BentoBox will regenerate everything fresh.

### How do I change the island distance?

All the game modes have a configuration for the distance between player islands. In BSkyBlock, is is called `distance-between-islands` and it is found in the config.yml file here:

```
# Radius of island in blocks. (So distance between islands is twice this)
  # It is the same for every dimension : Overworld, Nether and End.
  # This value cannot be changed mid-game and the plugin will not start if it is different.
  # /!\ BentoBox currently does not support changing this value mid-game. If you do need to change it, do a full reset of your databases and worlds.
  distance-between-islands: 400
```

In the case of BSkyBlock, the default value is 400, which means that players will start 800 blocks apart from each other. It also means that a player's protection area can grow up to a value of 400.

Most of the time, the default setting should be sufficient for your server. However, some admins like to space out players even further, or sometimes, have them closer together. Whatever you choose, once the game is running, **you cannot change this value**. If you do try to change it, BentoBox will refuse to start and give a warning in the console like this:

```
[14:08:20 ERROR]: [BentoBox] *****************CRITIAL ERROR!******************
[14:08:20 ERROR]: [BentoBox] Island distance mismatch!
World 'bskyblock_world' distance 800 != island range 400!
Island ID in database is BSkyBlock99ea1c15-f5f8-410a-9019-d6b843a5a254.
Island distance in config.yml cannot be changed mid-game! Fix config.yml or clean database.
[14:08:20 ERROR]: [BentoBox] Could not load islands! Disabling BentoBox...
[14:08:20 ERROR]: [BentoBox] *************************************************
```
This is a protection mechanism, because if you do change the value and were able to proceed, islands could end up on top of each other and that would lead to very unhappy players!

** But I am just starting my server! How do I change this value and clean the database? **

I will assume you are using the default JSON database (flat file). Follow these steps:

1. Stop the server
2. Change the config.yml value for the island distance to whatever you want.
3. If you have no other BentoBox games running, or just want to reset everything, then delete the `plugins/BentoBox/database` and the `plugins/BentoBox/database_backup` folders
4. Delete the worlds that the game modes made, for BSkyBlock, this is by default these folders in your server folder: `bskyblock_world`, `bskyblock_world_nether`, and `bskyblock_world_the_end`
5. Restart the server.

If you already have other BentoBox game modes running on your server, then things are a little more complex:
1. Stop the server
2. Change the config.yml value for the island distance to whatever you want.
3. Open the `plugins/BentoBox/database/Island` folder and delete all the files that start with the name of your game mode, e.g., `BSkyBlock99ea1c15-f5f8-410a-9019-d6b843a5a254.json`
4. Delete the worlds that the game modes made, for BSkyBlock, this is by default these folders in your server folder: `bskyblock_world`, `bskyblock_world_nether`, and `bskyblock_world_the_end`
5. Restart the server.

If you are using other databases like MySQL, then the steps are the same, but you will need to use SQL commands to remove the database, tables, or entries.

### How can I enable nether portals to link together?

In BentoBox 1.16 we implemented an option to properly link together portals. However this option works only if `allow-nether` is enabled in server.properties and `allow-end` in bukkit.yml.

To enable linking nether portals you need to find option in gamemode config: `create-and-link-portals` and set it to `true`.

To enable creating proper end obsidian platform (like in vanilla end) you need to find option `create-obsidian-platform` and set it to `true`.

Be aware, that enabling these options opens the same exploits with unlimitated obsidian generation that original Minecraft has.

### How do I disable structure generation in Boxed?

In the Boxed `config.yml` there is a `structures` list. Removing entries from that list prevents those structures from generating in newly created box areas. Existing boxes are unaffected.

### Can I use Multiverse with BentoBox?

Multiverse generally works with most gamemodes, **except Boxed and Poseidon**, which require their own world generator to be set in `bukkit.yml`. If you use Multiverse with one of those, the world won't generate correctly. MyWorlds is a popular alternative.

## Mobs, spawning and entities

### Why do my fish, dolphins or squid only spawn near bedrock at y -63?

This is a [Mojang flat-world bug](https://github.com/BentoBoxWorld/BentoBox/issues/2593) that affects Minecraft 1.21.2+: aquatic mobs only spawn near the bottom of flat worlds. Newly created BentoBox worlds on recent BentoBox versions include the workaround. Existing worlds need manual NBT editing of the world's level data — there is no in-game fix.

### Why do mobs not spawn on islands at all?

Run `/op` and check the server console while standing on the island:

1. BentoBox prints which plugin (if any) cancelled the spawn. If nothing is printed, Minecraft never even attempted the spawn — check `spawn-limits` and `gamerule` settings in `bukkit.yml`, your world plugin (Multiverse, MyWorlds…), and the `/[admin_command]` settings.
2. Check the gamemode's `config.yml` `world.spawn-limits` section.
3. For visiting players who can't be attacked by hostiles, look at the *Visitor protection* flag.

## Islands: size, protection and resets

### How can I increase a player's island size?

Each island has a protected area. You can increase the protected area up to the inter-island distance. There are three mechanisms and you must pick **one**, because they are mutually exclusive in some gamemodes (notably Boxed):

- **Permissions** — grant `[gamemode].island.range.<number>` (e.g. `bskyblock.island.range.150`). Permissions are checked only when a player logs in, so the owner must reconnect for it to take effect. If the island owner changes, then the island range will adjust to the new owner's permission, or revert to the default range if the new owner has none.
- **Admin command** — `/[admin_command] range set <player> <number>` — applies instantly.
- **Advancements (Boxed only, default)** — the box grows as the owner unlocks advancements. To use commands or permissions on Boxed instead, set `ignore-advancements: true` in the Boxed config.

The protection range can never exceed the gamemode's `distance-between-islands` value. Remember, the protected range applies to the island as a whole.

### Why does my Boxed area shrink back to the default after every restart?

This is the advancements mode in action: on startup BentoBox recalculates the box size from how many advancements the owner has unlocked. Either give the owner more advancements, or set `ignore-advancements: true` in the Boxed config and use commands/permissions instead.

### How do I stop players from seeing nearby islands?

The minimum value of `distance-between-islands` that hides neighbours is:

```
distance-between-islands ≥ max_protection_range + (server view-distance × 16) / 2
```

For example, with a maximum protection range of 50 (a 100×100 island) and a 11-chunk view distance:

```
distance-between-islands ≥ 50 + (11 × 16) / 2 = 138
```

`distance-between-islands` cannot be changed mid-game without a full reset (see [How do I change the island distance?](#how-do-i-change-the-island-distance)).

### Can I sell island upgrades / let players pay to expand their island?

BentoBox has no built-in shop. The pinned messages in `#support-en` describe two community recipes: (1) use the [Upgrades addon](addons/Upgrades/index.md) with the Vault economy, or (2) use any external GUI/shop plugin to grant the `[gamemode].island.range.<number>` permission on purchase.

### Why does the island border show the new size but the player still can't build there?

The visual border lives at the protection range. If a player has been granted a higher range permission but hasn't relogged, the border still shows the old radius. Have them rejoin (or use the admin range command which applies instantly).

## Teams, coop and visitors

### What's the difference between team, coop, trust and visit?

- **Visitor** — anyone who teleports to or walks onto someone else's island. By default they can't break, place or interact with most blocks.
- **Coop** — a temporary upgrade granted via `/island coop <player>`. Lasts until the player logs off (configurable). Coop ranks can be tuned in *Settings → Protection*.
- **Trust** — a persistent upgrade granted via `/island trust <player>`. Survives logout.
- **Team member** — granted via `/island team invite <player>`. The invitee must accept and **loses their own island in the process**. There is one owner per island; team members are not owners.
- **Owner promotion** — `/island team setowner <player>` transfers ownership.

For all of the above, the exact rank required for each protection action is configured in the island's `Settings` GUI under the *Protection flags* and *Command ranks* tabs.

### How do I let someone help me build without giving them my island?

Use **trust**. Trust persists across logouts, and you can configure exactly which actions trusted players can perform via the island settings menu.

## Placeholders

### How do I show a BentoBox placeholder in chat / tab / scoreboard?

You need [PlaceholderAPI](https://www.spigotmc.org/resources/placeholderapi.6245/) installed, and a chat/tab/scoreboard plugin that itself supports PlaceholderAPI. See [Placeholders](BentoBox/Placeholders.md) for the full list of available placeholders. To verify a placeholder works at all, run:

```
/papi parse me %bentobox_island_name%
```

If that returns a value, the placeholder is fine and the issue is in your chat/tab/scoreboard plugin's configuration.

### Why is `%Level_<gamemode>_island_level%` returning empty?

Three checks, in order:

1. The Level addon is installed and enabled for that gamemode.
2. The player has actually run `/[player_command] level` at least once — by default the level is only calculated when the player runs the command. (You can enable `calculate-level-on-login` in the Level addon config to compute it on join instead.)
3. `/papi parse me %Level_<gamemode>_island_level%` returns a number when run by that player. If yes, the issue is in your chat/tab plugin, not in BentoBox.

## AOneBlock

### How do I add custom blocks (or ItemsAdder / Oraxen blocks) to a phase?

Edit the relevant phase file in `plugins/BentoBox/addons/AOneBlock/phases/`. Phase files use either the legacy short syntax or the explicit `block-data` syntax — see the example in [AOneBlock phase config files](gamemodes/AOneBlock/index.md#phase-config-files). For ItemsAdder / Oraxen blocks you'll need the actual block form (not the item form) and your phase entry has to use `block-data` with the underlying namespaced ID.

### How do I edit the loot in a phase chest?

Place a chest, fill it with the items you want, then look at it and run `/[admin_command] setchest`. The chest's contents (and any container NBT) are written into the phase file.

### Players spawn at world spawn instead of getting an island on first join — how do I fix it?

In the AOneBlock `config.yml`, enable the *create island on first login* option. Without it, players who join for the first time end up at the server spawn and have to run `/island create` manually.

### Why does the magic block break nearby blocks when a large mob spawns?

This is intentional. AOneBlock clears blocks inside the spawning entity's bounding box so that players can't trap their own magic block by placing a cube above it (which would otherwise immediately kill the spawning mob). The behaviour can be disabled with `mobs-clear-blocks: false` in the AOneBlock config, at the cost of allowing that exploit.

## Level addon

### Why is my Level not updating in real time?

Island level is calculated only when the player runs `/[player_command] level`, or on login if you've enabled `calculate-level-on-login` in the Level addon config. There's no continuous tracking — recalculating an entire island every block change would be far too expensive.

### Why aren't my custom Oraxen / ItemsAdder / custom blocks counted?

The Level addon only counts blocks listed in its `blockconfig.yml`. Custom blocks from item-adder plugins must be added there explicitly with the value you want them to score. If the entry is missing, the block falls back to its underlying base block's value (or zero, if even that isn't listed).

### Should I use the Level addon with Boxed?

Generally no — Boxed worlds are pre-filled with terrain, so an island's "level" is dominated by the underlying chunks rather than what the player has built. Use it on void-style gamemodes (BSkyBlock, AOneBlock, AcidIsland) where it actually reflects player effort.

## Challenges addon

### I ran `/[admin_command] challenges` and the menu is empty — how do I get the default challenges?

Open the menu, click *Library*, pick a default challenge set (e.g. "default" for BSkyBlock), and confirm by typing `confirm` in chat when prompted. The default challenges are bundled with the addon but are not loaded automatically — you have to import them once per gamemode.

### Can I run challenges from a different world / overworld?

No. Challenges are bound to the gamemode world they were created in. If you want quest-style content in your overworld you'll need a separate quest plugin.

## Database and storage

### What version of any database is required?

Minimum required versions:

* **MySQL** 5.7 or later
* **MariaDB** 10.2.3 or later
* **MongoDB** 3.6 or later
* **SQLite** 3.28 or later
* **PosgreSQL** latest is always recommended

### My BentoBox world folder is huge — how do I shrink it?

The two big space-eaters are (1) chunks generated by players who never came back, and (2) old island regions left behind after resets. To recover space:

- **BentoBox 3.15.0+:** Use `/[admin_command] purge <days>` — this now identifies stale islands *and* deletes their region files in one step. For soft-deleted islands (those flagged after a reset or `/admin delete`), run `/[admin_command] purge deleted` to reap their region files. Restart the server after purging so Paper's chunk cache is cleared.
- **Older BentoBox:** Use `/[admin_command] purge <days>` to flag islands, then `/[admin_command] purge regions` to delete the region files.
- **Always back up the world folder first.**
- For really old worlds, a third-party tool such as Regionerator can prune unused chunks.

### MariaDB vs MySQL — does it matter?

Yes. In the BentoBox `config.yml` you must set the correct `database` type: pick `MARIADB` if your server is MariaDB, and `MYSQL` if your server is MySQL. The wire protocol is similar but the JDBC drivers and reserved-word lists differ enough that mixing them up causes connection or query errors at startup.

### How do I migrate from JSON to MySQL/MariaDB?

See [Database transition](BentoBox/Database-transition.md). Briefly: stop the server, change the database type in `config.yml`, start the server with `database-transition` enabled — BentoBox copies all records into the new database on startup, then disable `database-transition` and restart.

## Customization: locales, colours and blueprints

### How do I make my own custom islands?

You are referring to our **in-house schematic format** we call **_Blueprints_**.
The [Blueprints page](BentoBox/Blueprints.md) provides all the relevant information to get you started with the Blueprints, as well as a few hints and tricks you can use to further customize them.
You can also have a look at [this video](https://youtu.be/4gvaG89uxAs) which, although outdated, might help you create your first Blueprint within minutes.

### How do I change a language string / message?

Locale files live under `plugins/BentoBox/locales/` (BentoBox core) and `plugins/BentoBox/addons/<AddonName>/locales/` (each addon). Edit the relevant `<lang>.yml` file. If you only ever want one language, set the `default-language` in BentoBox's `config.yml` and remove permissions for players to switch.

### How do I change the `[BentoBox]` chat prefix?

Look in `plugins/BentoBox/locales/en-US.yml` (or whichever locale you use) for an entry under `prefixes:`. Each addon may also have its own prefix in its locale file.

### How do I use hex (RGB) colours in messages?

Use `&#RRGGBB`, e.g. `&#ff8800Hello` for orange. This works in any place where BentoBox accepts colour codes. Note that some external chat formatters may need their own hex syntax — BentoBox cannot control that.

### Where can I help translate BentoBox into my language?

[https://download.bentobox.world/translate.html](https://download.bentobox.world/translate.html) — translations are run via Crowdin and pulled automatically into release builds.

## Miscellaneous

### Why does my Magic Cobblestone Generator do nothing?

The player has to **activate** a generator first with `/[player_command] generator` and pick one from the GUI. Just placing lava and water without activating a generator will give vanilla cobblestone.

### How do I pre-generate islands so players don't wait?

There's no built-in pregenerator, but you can script `/[admin_command] register <fakeplayer>` to create islands ahead of time. For chunk pregeneration use a server-side tool such as Chunky.

## API and addon development

### How do I start writing addons for BentoBox? Is there an API?

Yes, there is definitely an API.
Writing addons is very similar to writing plugins except there is a lot more API available for things like teams, protections, commands, panels and pasting.

Follow [this tutorial](Tutorials/api/Create-an-addon.md) to create your first addon!

## Less common / legacy issues

The questions in this section come up rarely now, but the answers are kept here for the few servers that still hit them.

### Superflat chunks are generating in my worlds

*Relevant issues:*
[BentoBox#1212](https://github.com/BentoBoxWorld/BentoBox/issues/1232),
[BSkyBlock#247](https://github.com/BentoBoxWorld/BSkyBlock/issues/247).

![Superflat world](https://static.planetminecraft.com/files/resource_media/screenshot/1215/2012-04-15_205556_2000620.jpg)
*A superflat world. (Credit: [1213videogamer on PlanetMinecraft](https://www.planetminecraft.com/member/1213videogamer/)).*

If you start seeing superflat chunks being generated in your world, then it is because the world generator is not working for the world anymore.
There are a few reasons why this may be the case. They are ordered according to their likeliness.

**We strongly recommend you revert to backups made prior to this situation**.
Although we are providing instructions to help recover from such an event in case you do not have backups available, we **do not guarantee their effectiveness**. Moreover, these solutions are **designed to address the problem as much as possible, however, ignoring the impact on performance or player islands**. Use them knowingly.

As a quick fix, there is a setting in the admin settings console to remove super flat chunks. This is the main tool to fix the damage, but unless you fix the root cause it will just cause super lag and never fix the issue properly.

In any case, **stop your server immediately to prevent further damage from being done to your worlds**.

#### Causes

##### BentoBox or the Gamemode addon is no longer running

**Why?**

BentoBox or the Gamemode addon is not enabled on the server.
This can occur if you updated BentoBox or the Gamemode addon to a version which is not compatible with your server or which is incompatible with one of your plugins.

**Solutions**

Investigate as to why BentoBox or the Gamemode addon is no longer enabled.
Read the logs to find errors at startup.
Try booting your server up while adding a single plugin at a time to find out which plugin is causing the issue.

##### There is no generator set for this world in the `bukkit.yml` file

**Why?**

This is often the situation.
While setting the default world of your server to be the Gamemode addon's world, you forgot to specify the right generator for said world in the `bukkit.yml` file.

**Solutions**

Make sure you followed each step of [this tutorial](BentoBox/Set-a-BentoBox-world-as-the-server-default-world.md) thoroughly.

##### The `use-own-generator` option from the Gamemode's config is set to `true`

**Why?**

This is a common mistake.

Users tend to misunderstand this option as allowing them to activate a "magic" cobblestone generator (but [it's an addon](addons/MagicCobblestoneGenerator/index.md)!).
This is indeed not what this option is designed for, and this is clearly explained in the comments surrounding this option in the config file:

```yaml
# Use your own world generator for this world.
# In this case, the plugin will not generate anything.
# If used, you must specify the world name and generator in the bukkit.yml file.
# See https://bukkit.gamepedia.com/Bukkit.yml
use-own-generator: false
```

Ultimately, this can also happen if you forgot the specify the world name and generator in the `bukkit.yml` file.

**Solutions**

If you do not plan to use an external plugin to generate the world, then you should set this option back to `false`.

On the contrary, you should make sure you have specified the world name and the corresponding plugin name as its generator in the `bukkit.yml` file.

##### Another plugin is trying to control the generator of this world

**Why?**

Although very rare, this can still happen.

Some plugins, especially world management ones (e.g. Multiverse), tend to provide settings that could override the generator of our worlds.

**Solutions**

Review all of your plugins to find out which one is the most likely to cause the issue.
World management plugins or custom-coded ones that are interacting with worlds are to be investigated first.
Either report the issue to their developers or fix the configuration files that are involved.

##### There is a bug in BentoBox or in the Gamemode addon

**Why?**

*Woopsie!*

Nowadays, this is extremely rare.
But it might still happen for some reasons.

**Solutions**

Make sure this is actually a BentoBox-related bug: remove all the plugins from your server one by one until only BentoBox is left.

If the issue is no longer occurring, this means another plugin is causing it.
In that case, please refer yourself to [this section](https://bentobox-world.readthedocs.io/en/latest/FAQ/#another-plugin-is-trying-to-control-the-generator-of-this-world).

If the issue still occurs, this means this is a BentoBox bug.
Please [report it on our bug tracker](https://github.com/BentoBoxWorld/BentoBox/issues).

#### How to clean the superflat chunks afterwards?

If you have backups, use them to revert your server's worlds and BentoBox databases to their previous states.

If you do not have backups, log into your server and open the Admin Settings Panel using the `/[admin-command] settings` command.
Find the "*Clean Super Flat*" flag and toggle it on.
Depending on your settings, locales and on the BentoBox version you are running, the name, icon or description might be different.
But we are sure you will be able to find that flag by yourself nonetheless!

![image](https://user-images.githubusercontent.com/20014332/77770414-8256c380-7045-11ea-8ab6-8efe31d6fb87.png)
*The Clean Super Flat flag in BSkyBlock's Admin Settings Panel*.

This flag will **slowly regenerate any superflat chunk from your world over time**.
This happens when chunks are loaded, so you might want to either teleport to said chunks to force the regeneration, or you could leave the flag enabled for a few days.
**Do not forget to disable the flag at some point!**
It is quite resource-intensive...

### My server lags when a player creates their island!

Pasting the island or generating the chunks are the main causes of this issue.

Firstly, the paste speed may be too much for your server.
Try lowering it.
Look in the BentoBox `config.yml` for this setting:

```yaml
# Number of blocks to paste per tick when pasting blueprints.
# Smaller values will help reduce noticeable lag but will make pasting take slightly longer.
# On the contrary, greater values will make pasting take less time, but this benefit is quickly severely impacted by the
# resulting amount of chunks that must be loaded to fulfill the process, which often causes the server to hang out.
paste-speed: 64
```

If you are running timings, the `BlueprintPaster` task should ideally be taking a long time, yet take a low percentage of a tick time.

If the server still struggles when pasting islands, then that implies it struggles to generate the chunks.
That is something we have little control on as a plugin, but here are a few things you could do to mitigate this:

* Try reducing the "distance between islands" setting in the gamemode's config file.
Lower values means fewer chunks to generate.
This will require you to entirely reset the worlds and databases.
* Use Paper as your server software.
Paper handles asynchronous chunk generation.
* Pre-generate the world.
Especially for gamemodes whose generators are resource-intensive, such as CaveBlock or SkyGrid.

### I can't place saplings on my island!

*Relevant issue:*
[BentoBox#277](https://github.com/BentoBoxWorld/BentoBox/issues/277).

If no message shows up to the player telling them that they can't place the sapling, then it means that BentoBox **does not** cause this issue.

If you are using **GriefPrevention** on your server, there is a [config option](https://github.com/TechFortress/GriefPrevention/wiki/Setup-and-Configuration#preventing-tree-grief) in this plugin that prevents players from placing so-called "Sky Trees".

## Sources

The Discord-sourced entries above were drawn from the `#support-en` channel between January 2025 and April 2026. Sample threads (one per topic, for context):

- Versions and compatibility — [discord thread](https://discord.com/channels/272499714048524288/310623455462686720/1490517535152410745)
- Worlds and generation — [discord thread](https://discord.com/channels/272499714048524288/310623455462686720/1488648048589672488)
- Mob spawning — [discord thread](https://discord.com/channels/272499714048524288/310623455462686720/1475550306799583316)
- Permissions and ranks — [discord thread](https://discord.com/channels/272499714048524288/310623455462686720/1480457734842220566)
- Island creation and reset — [discord thread](https://discord.com/channels/272499714048524288/310623455462686720/1468577190126948455)
- Island size and protection — [discord thread](https://discord.com/channels/272499714048524288/310623455462686720/1471174102957031506)
- Teams and coop — [discord thread](https://discord.com/channels/272499714048524288/310623455462686720/1467986323137757357)
- Placeholders — [discord thread](https://discord.com/channels/272499714048524288/310623455462686720/1465642012341698713)
- Level addon — [discord thread](https://discord.com/channels/272499714048524288/310623455462686720/1459181292175360162)
- AOneBlock — [discord thread](https://discord.com/channels/272499714048524288/310623455462686720/1466486743287988346)
- Challenges — [discord thread](https://discord.com/channels/272499714048524288/310623455462686720/1426655803473133795)
- Database and storage — [discord thread](https://discord.com/channels/272499714048524288/310623455462686720/1461304120668323910)
- Localization — [discord thread](https://discord.com/channels/272499714048524288/310623455462686720/1482135823947272203)
- Border addon — [discord thread](https://discord.com/channels/272499714048524288/310623455462686720/1462044129448951872)
- Bank addon — [discord thread](https://discord.com/channels/272499714048524288/310623455462686720/1440031441995169833)
- BSkyBlock — [discord thread](https://discord.com/channels/272499714048524288/310623455462686720/1486436566032318474)
- Boxed — [discord thread](https://discord.com/channels/272499714048524288/310623455462686720/1415368394374647948)
- Errors and crashes — [discord thread](https://discord.com/channels/272499714048524288/310623455462686720/1441184039175327757)

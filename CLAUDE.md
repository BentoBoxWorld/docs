# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is the source repository for the BentoBox main documentation site at **https://docs.bentobox.world**. It is built with [MkDocs](https://www.mkdocs.org/) using the Material theme. When commits are pushed to the `master` branch, [ReadTheDocs.org](https://readthedocs.org/) automatically pulls the changes, builds the site, and publishes the updated documentation live within minutes.

## Commands

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Serve locally with live reload
mkdocs serve

# Build static site
mkdocs build
```

The local server runs at `http://127.0.0.1:8000` by default.

## Architecture

### Directory Structure

- `docs/` — All Markdown source files, mirroring the nav structure in `mkdocs.yml`
  - `docs/BentoBox/` — Core BentoBox documentation (API, commands, config, permissions)
  - `docs/gamemodes/` — One subdirectory per game mode (AcidIsland, AOneBlock, BSkyBlock, Boxed, CaveBlock, Poseidon, SkyGrid, StrangerRealms, etc.)
  - `docs/addons/` — One subdirectory per addon (Bank, Biomes, Border, Challenges, Level, etc.)
  - `docs/Tutorials/` — Developer tutorials (addon creation, API guides)
- `data/` — CSV and JSON files used by MkDocs macros to generate dynamic content
  - `placeholders.csv` — All placeholder variables across BentoBox and addons
  - `flags.csv` — Protection flags (type, icon, description, defaults, ranks)
  - `minecraft-block-and-entity.json` — Block/entity icon CSS class mapping
- `docs/stylesheets/` — Custom CSS loaded via `extra_css` in `mkdocs.yml`
  - `bentobox-theme.css` — Blueprint palette override for the Material slate scheme (navy/cyan; Space Grotesk + Inter Tight + JetBrains Mono). Also defines all `.bb-*` layout classes used exclusively by `docs/index.md`.
  - `icons-minecraft-0.5.css` — Minecraft block/entity icon sprites
- `main.py` — MkDocs macros plugin entry point (`define_env`); defines all Jinja2 macros used in docs
- `mkdocs.yml` — Site configuration: nav tree, theme, plugins, Markdown extensions

### Homepage (docs/index.md)

`index.md` is structurally different from all other pages. It uses `hide: [navigation, toc]` frontmatter and its body is a single raw HTML block (no Markdown) built from `.bb-*` CSS classes defined in `bentobox-theme.css`. Do not add Markdown content or macros directly inside the `.bb-homepage` wrapper — use plain HTML.

### Macros (main.py)

The `mkdocs-macros-plugin` allows Jinja2 macro calls inside Markdown files. Macros defined in `main.py`:

- `{{ addon_description("AddonName") }}` — Renders a standard "Useful links" info box (GitHub, issues, CI) for an addon
- `{{ translations("RepoName") }}` — Renders the translation status table for an addon. At build time it fetches `src/main/resources/locales/` from `BentoBoxWorld/<RepoName>` on GitHub (defaults to the `develop` branch) and computes a real percentage per locale by comparing each YAML file against `en-US.yml`. Falls back gracefully if GitHub is unreachable. Set the `GITHUB_TOKEN` env var on the build host to lift the unauthenticated 60/hr rate limit.
- `{{ placeholders_bundle("gamemode_name") }}` — Renders all placeholders for a specific gamemode from `data/placeholders.csv`
- `{{ placeholders_source("SourceName") }}` — Renders placeholders from a specific addon/source
- `{{ flags_bundle("FLAG_TYPE") }}` — Renders a table of flags by type (e.g., `PROTECTION`, `SETTING`) across all sources
- `{{ flags_source("SourceName", "FLAG_TYPE") }}` — Renders flags for a specific source

### Adding a New Game Mode or Addon

1. Create the directory under `docs/gamemodes/<Name>/` or `docs/addons/<Name>/`
2. Add an `index.md` with the main documentation; use macros like `{{ addon_description("Name") }}` and `{{ translations(...) }}`
3. Register the new entry in the `nav:` section of `mkdocs.yml`
4. Add any new placeholders to `data/placeholders.csv` and flags to `data/flags.csv`

### Markdown Extensions Available

The following pymdownx extensions are configured and usable in any doc page:
`admonition`, `details`, `superfences`, `tabbed`, `tasklist`, `tilde`, `keys`, `progressbar`, `footnotes`, `attr_list`

Admonition types commonly used: `note`, `warning`, `info`, `tip`

## Dependency Source Lookup

When you need to inspect source code for a dependency (e.g., BentoBox, addons):

1. **Check local Maven repo first**: `~/.m2/repository/` — sources jars are named `*-sources.jar`
2. **Check the workspace**: Look for sibling directories or Git submodules that may contain the dependency as a local project (e.g., `../bentoBox`, `../addon-*`)
3. **Check Maven local cache for already-extracted sources** before downloading anything
4. Only download a jar or fetch from the internet if the above steps yield nothing useful

Prefer reading `.java` source files directly from a local Git clone over decompiling or extracting a jar.

In general, the latest version of BentoBox should be targeted.

## Project Layout

Related projects are checked out as siblings under `~/git/`:

**Core:**
- `bentobox/` — core BentoBox framework

**Game modes:**
- `addon-acidisland/` — AcidIsland game mode
- `addon-bskyblock/` — BSkyBlock game mode
- `Boxed/` — Boxed game mode (expandable box area)
- `CaveBlock/` — CaveBlock game mode
- `OneBlock/` — AOneBlock game mode
- `SkyGrid/` — SkyGrid game mode
- `RaftMode/` — Raft survival game mode
- `StrangerRealms/` — StrangerRealms game mode
- `Brix/` — plot game mode
- `parkour/` — Parkour game mode
- `poseidon/` — Poseidon game mode
- `gg/` — gg game mode

**Addons:**
- `addon-level/` — island level calculation
- `addon-challenges/` — challenges system
- `addon-welcomewarpsigns/` — warp signs
- `addon-limits/` — block/entity limits
- `addon-invSwitcher/` / `invSwitcher/` — inventory switcher
- `addon-biomes/` / `Biomes/` — biomes management
- `Bank/` — island bank
- `Border/` — world border for islands
- `Chat/` — island chat
- `CheckMeOut/` — island submission/voting
- `ControlPanel/` — game mode control panel
- `Converter/` — ASkyBlock to BSkyBlock converter
- `DimensionalTrees/` — dimension-specific trees
- `discordwebhook/` — Discord integration
- `Downloads/` — BentoBox downloads site
- `DragonFights/` — per-island ender dragon fights
- `ExtraMobs/` — additional mob spawning rules
- `FarmersDance/` — twerking crop growth
- `GravityFlux/` — gravity addon
- `Greenhouses-addon/` — greenhouse biomes
- `IslandFly/` — island flight permission
- `IslandRankup/` — island rankup system
- `Likes/` — island likes/dislikes
- `Limits/` — block/entity limits
- `lost-sheep/` — lost sheep adventure
- `MagicCobblestoneGenerator/` — custom cobblestone generator
- `PortalStart/` — portal-based island start
- `pp/` — pp addon
- `Regionerator/` — region management
- `Residence/` — residence addon
- `TopBlock/` — top ten for OneBlock
- `TwerkingForTrees/` — twerking tree growth
- `Upgrades/` — island upgrades (Vault)
- `Visit/` — island visiting
- `weblink/` — web link addon
- `CrowdBound/` — CrowdBound addon

**Data packs:**
- `BoxedDataPack/` — advancement datapack for Boxed

**Documentation & tools:**
- `docs/` — main documentation site
- `docs-chinese/` — Chinese documentation
- `docs-french/` — French documentation
- `BentoBoxWorld.github.io/` — GitHub Pages site
- `website/` — website
- `translation-tool/` — translation tool

Check these for source before any network fetch.

## Key Dependencies (source locations)

- `world.bentobox:bentobox` → `~/git/bentobox/src/`

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
- `main.py` — MkDocs macros plugin entry point (`define_env`); defines all Jinja2 macros used in docs
- `mkdocs.yml` — Site configuration: nav tree, theme, plugins, Markdown extensions

### Macros (main.py)

The `mkdocs-macros-plugin` allows Jinja2 macro calls inside Markdown files. Macros defined in `main.py`:

- `{{ addon_description("AddonName") }}` — Renders a standard "Useful links" info box (GitHub, issues, CI) for an addon
- `{{ translations(gitlocalize_id, ["lang-codes"]) }}` — Renders the translation status table for an addon
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

# addons

This is where add-ons are placed.

# locales

This is where language files are placed

# database

This is where the flat file database is stored (YAML files). It is where data is stored from add-ons.

BentoBox keeps its own tables here too, for example `Islands`, `Players`, `Names` and `WorldSettings`. The `WorldSettings` table holds one file per game mode for the world settings that BentoBox stores itself rather than the game mode's `config.yml`, currently the always-allowed entity types list.

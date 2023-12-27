## Introduction

**Setting a BentoBox world as the server default world** allows to avoid the generation of the **default vanilla worlds**.

!!! warning 
    In this step-by-step example/tutorial, we are considering you are doing this for `BSkyBlock`.
    The process is the same for other gamemodes, but **mind the worlds' names**!

## Preparations

1. The whole procedure needs to be executed while the server is **switched off**.
2. Delete the vanilla worlds (`world`, `world_nether`, `world_the_end`) by deleting their folders.

![worlds to delete](https://user-images.githubusercontent.com/20014332/62977233-bebf1180-be1e-11e9-9ec8-ddcfd3352b13.png)

*Highlighted folders are those of the default world. They must be deleted.*

## server.properties

Open the `server.properties` file.

Find the following line:
```properties
level-name=world
```

Replace `world` with the name of the BentoBox world. It usually is `[gamemode]_world`, where `[gamemode]` is the lowercased gamemode's name (e.g. `bskyblock` or `caveblock`). However, it can be modified in the gamemode's `config.yml` file, so make sure it is the correct one.

For the sake of simplicity, we will expect the world name to remain untouched and generic, and therefore being `bskyblock_world`.

The line should now look like this:
```properties
level-name=bskyblock_world
```

## bukkit.yml

Open the `bukkit.yml` file: we need to tell Bukkit that the default world uses a custom generator, **otherwise it will mess up the world generation**. Note that if you want to use the vanilla nether or end, do not list them in this file.

The configuration section we're adding likely does not exist already in your `bukkit.yml` file, so you need to create it. See the official [Bukkit Wiki](https://bukkit.fandom.com/wiki/Bukkit.yml) for more details about the section.

Add the following section to your file. The names listed **must** be the names of the worlds:
```yaml
worlds:
  bskyblock_world:
    generator: BentoBox
  bskyblock_world_nether:
    generator: BentoBox
  bskyblock_world_the_end:
    generator: BentoBox
```

If you are going to use the vanilla nether or end, do not list them. Just list the overworld. For example:
```yaml
worlds:
  bskyblock_world:
    generator: BentoBox
```


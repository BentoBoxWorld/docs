# Blueprints (Custom Starter Islands)

When a player creates a new island, BentoBox pastes a pre-built starting island for them. These templates are called **Blueprints**. By default, each game mode comes with a basic starter island, but you can design your own.

## Why Customise Your Starter Island?

- Give your server a unique look and feel
- Control exactly what resources players start with
- Create different difficulty tiers (easy starter, hard starter) that players can choose between
- Add welcome signs and hints for new players

## How It Works in Brief

Blueprints are created entirely inside the game. The basic process is:

1. Build the island you want players to start with somewhere in the world.
2. Use the admin Blueprint commands to select the area, copy it, and save it.
3. Use the Blueprint Manager GUI to assign it to a **Bundle** (a named set of starter islands).
4. Players will see the available bundles when they create a new island and can pick one.

You can have different blueprints for the Overworld, Nether, and End, all within the same bundle.

!!! tip
    Keep starter islands small. The fun of Skyblock-style games is in the struggle to grow. Too many resources at the start removes the challenge.

## Blueprint Manager

The Blueprint Manager is an in-game GUI opened with:
```
/[admin_command] blueprint
```

From here you can create new bundles, assign blueprints, set icons, add descriptions, and require a permission for specific bundles (e.g. a VIP starter island).

## Performance

Blueprint pasting is done asynchronously — it will not freeze your server no matter how large the blueprint is. If you notice lag during island creation, reduce the `paste-speed` setting in BentoBox's `config.yml`.

## Full Documentation

For step-by-step instructions, command reference, and tips for working with WorldEdit schematics, see the [full Blueprints page](../Blueprints.md).

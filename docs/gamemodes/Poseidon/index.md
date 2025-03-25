# 🌊 Poseidon

Created and maintained by [tastybento](https://github.com/tastybento).

**Poseidon** is an immersive underwater survival experience for Minecraft. Stranded after a mysterious shipwreck, you awaken with the uncanny ability to breathe underwater—but there's a catch. Like a shark, you must keep moving to survive.

Welcome to a world where the ocean is both your sanctuary and your greatest threat. From deep-sea ruins to glowing coral cities, Poseidon challenges you to survive, build, and explore in a realm where the sea is your only constant—until you dare to set foot on the dreaded, burning land above.

## 🐚 Features

- 🧭 **Survival Reimagined**: Keep moving to stay alive. Stillness invites danger.
- 🏰 **Underwater Realm Building**: Construct coral-covered castles and aquatic cities in the deep.
- ⚔️ **Challenging Encounters**: Face relentless drowned, sea monsters, and secrets buried beneath.
- 🌋 **The Water-Filled Nether**: Discover a submerged version of the underworld.
- 📖 **Lore-Driven Challenges**: Complete multi-level quests and unlock mysterious books that expand Poseidon's world.
- 🏝️ **Custom Starter Islands**: Choose your beginning—simple shipwreck, small monument, or a grand coral-laced domain.

## 🔧 Setup Instructions

> Recommended: Install alongside the [BentoBox Challenges Addon](https://github.com/BentoBoxWorld/Challenges) for full Poseidon functionality.

1. **Download and install the Poseidon addon.**
2. **Place it in your `/plugins/BentoBox/addons/` folder.**
3. **Start your server** – new worlds for Poseidon will be generated automatically.
4. **Let pre-generation run.** It only works when no players are online. The more chunks that are pre-generated, the better the performance.
5. **Log in and configure challenges**:
    - Use `/padmin challenges`
    - Click the 🕸️ web icon to download the **Poseidon Challenges**
6. **Choose a starting island**:
    - Shipwreck with coral
    - Shipwreck with a small monument
    - Shipwreck with both small and large monuments
    - Customize islands using `/padmin bp`
7. **(Optional)** Tweak `config.yml` or use the admin settings GUI.
    - Major changes may require deleting the database and resetting worlds.

## ⚠️ Notes

- The End world is currently **underdeveloped**.
- Lag may occur if islands are not pre-generated. Allow pre-gen to complete before inviting players.

## ✅ Compatibility

| Feature             | Supported                         |
|---------------------|------------------------------------|
| Minecraft Version   | ✅ 1.21.4+ (not compatible with older versions) |
| BentoBox Version    | ✅ 3.3.0 or later                  |
| Java Version        | ✅ Java 21                         |

## Player command

The default player command is `/poseidon` or `/po` for short.

## Config.yml

The config.yml file is similar to other GameModes in that there is a section specially for Poseidon settings, and then more generic world and island settings. In Poseidon, islands are called realms. The unique Poseidon settings are:

```
poseidon:
  air-effect:
    # The time a player can be out of the water without suffering in seconds.
    grace-period: 3
    # Damage per second from being in the air.
    damage: 2
    # The time drinking water will prevent damage from air in seconds. Drinking water is the same as drinking a water breathing potion.
    water-effect-time: 30
  # Chance that water mobs will ignore posiedon's children. In percent.
  # Makes game easier..
  water-mob-ignore: 50
```

## Permissions

Permissions can be found [here](Permissions).

## Commands

Commands can be found [here](Commands).

## Placeholders

Placeholders can be found [here](Placeholders).


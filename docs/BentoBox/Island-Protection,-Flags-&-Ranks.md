# Island Protection, Flags & Ranks

[TOC]

## Introduction
Player (and even Environment, such as entities, pistons...) interactions with islands are ruled by a set of **Flags** that **determine *who* or *what* can do what on an island**. These Flags are mostly handled and provided by BentoBox, yet addons (e.g. [Greenhouses](https://github.com/BentoBoxWorld/Greenhouses)) can add their own.

See a list of flags [here](https://github.com/BentoBoxWorld/BentoBox/wiki/Flags).

## Settings Panel

The **Settings Panel** is the GUI in which the island owner is able to edit how the Flags are configured for his island. Other players, including island members, are only able to view them.

This GUI can be opened using the following command: `/[player_command] settings` (which requires the following permission: `[gamemode].island.settings`).

![Default view of the Settings Panel](https://user-images.githubusercontent.com/20014332/80591492-1689c100-8a1e-11ea-9a59-c55f35ab6ad9.png)

*Default view of the Settings Panel.*

Admins can change the settings of a player's island by using the admin settings command: `/[admin_command] settings <player_name>`

### Protection Tab

The **Protection Tab** is the tab displayed upon opening the Setting Panel. It includes the **Protection Flags**.

**Protection Flags** are Flags that can be set by [rank](https://github.com/BentoBoxWorld/BentoBox/wiki/Island-Protection,-Flags-&-Ranks#ranks). By **left-** or **right-clicking** on the icon of a Flag, the island owner will cycle through the various ranks so that the interaction the Flag is ruling will be allowed or disallowed depending on the rank of a player.

![Example of a Protection Flag](https://user-images.githubusercontent.com/20014332/62974085-b31c1c80-be17-11e9-8b27-2fd4bf54ae87.png)

*Example of a Protection Flag.*

By default, most of the Protection Flags are set to allow only island members (or above rank) to do the interaction. However, some are initially allowed for visitors too. See [the gamemode's config.yml].

![Example of a Protection Flag which is, by default, allowing visitors to do the interaction.](https://user-images.githubusercontent.com/20014332/62974359-553c0480-be18-11e9-8679-0033fd8bf8bd.png)

*Example of a Protection Flag which is, by default, allowing visitors to do the interaction.*

Admins can set how protections will work outside of island boundaries by using the admin settings command: `/[admin_command] settings`

### Settings Tab

### Display mode

### Hide Flags

As of [BentoBox 1.4.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/1.4.0), admins can hide Flags in the GUI by opening the Settings Panel and **shift-left-clicking** on the icon of the Flag they want to hide. This will apply a "Curse of Vanishing" enchantment to the icon and will result in the corresponding Flag being hidden to the players. Admins can later unhide the Flag by reiterating the same procedure.

![Default flags](https://user-images.githubusercontent.com/20014332/80591609-45a03280-8a1e-11ea-9e37-4725d62cdb3c.png)

*Player's view of all the basic Flags being allowed to be displayed.*

![Curse of Vanishing](https://user-images.githubusercontent.com/20014332/80591692-6799b500-8a1e-11ea-9ab8-e076f47d2220.png)

*The "Curse of Vanishing" being applied to one of the Flag.*

![A bunch of hidden flags](https://user-images.githubusercontent.com/20014332/80591757-839d5680-8a1e-11ea-8864-83b09252a7b9.png)

*Player's view of the basic Flags, with the "trapdoor" Flag being hidden.*

## Ranks

TODO.

* BANNED: -1 (partially unused)
* VISITOR: 0
* COOP: 200
* TRUSTED: 400
* MEMBER: 500
* SUB-OWNER: 900
* OWNER: 1000
* MOD: 5000 (unused)
* ADMIN: 10000 (unused)

## Bypass the protection

## Admin Settings Panel

### World Settings

### World Default Protection
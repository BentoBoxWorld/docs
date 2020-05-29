# How to fill in the addon.yml file?

## What is this file?

The **addon.yml** file gives precious information about your addon to BSkyBlock when it tries to load it. This file consists in a set of attributes, each one being defined on a new line and without any indentation.

Without this file or if it isn't correctly filled in, BSkyBlock won't load your addon and mark it as `INVALID_DESCRIPTION`.

## Mandatory attributes

### name

**Description:** The name of this addon.

**Code:**
```yaml
name: "MySuperAddon"
```

**Notes:**
1. Must consist in all alphanumeric characters and underscores (a-z,A-Z,0-9, \_).
2. Spaces are not supported and will be automatically converted to underscores.
3. It is used to identify the addon inside the entire BSkyBlock's API.
4. Displayed when the user types `/bsadmin version YourSuperAddon`.

### main

**Description:** Address that points to the class extending `BSAddon`.

**Code:**
```yaml
main: fr.poslovitch.myaddon.MySuperAddon
```

**Notes:**
1. This must contain the full namespace including the class file itself, like Bukkit. Therefore if your namespace is `fr.poslovitch.myaddon`, and your class file is called `MySuperAddon`, this must be `fr.poslovitch.myaddon.MySuperAddon`.

### version

**Description:** The version of your addon.

**Code:**
```yaml
version: 1.0.0
```

**Notes:**
1. Version is an arbitrary string, however the most common format is MajorRelease.MinorRelease.FixRelease (e.g: 3.6.1).
2. Displayed when the user types `/bsadmin version YourSuperAddon`.

## Optional attributes

Mandatory attributes aside, there are a few more attributes that can be useful to give more information about your addon to BSkyBlock.

These attributes are optional.

### authors

**Description:** Allows you to list all the super kind devs that made this addon, or just you.

**Code:**
```yaml
authors: ["Poslovitch", "Tastybento", "you, maybe? :P"]
# Don't hesitate to add our nicknames into the authors list of your addon, we would appreciate that!
```

**Notes:**
1. Gives credit to the developer(s)
2. Displayed when the user types `/bsadmin version YourSuperAddon`.

### description

**Description:** Chicken-friendly description of the functionality your addon provides.

**Code:**
```yaml
description: "It makes you die when you jump. So 2017."
```

**Notes:**
1. The description can have multiple lines (_cause you need a lot of place to explain what your super addon is doing!_).
2. Displayed when the user types `/bsadmin version YourSuperAddon`.

### website

**Description:**  The plugin's or author's website.

**Code:**
```yaml
website: "https://github.com/tastybento/bskyblock"
```

**Notes:**
1. If you have no dedicated website, a link to the addon's GitHub repository should do the job.
2. Displayed when the user types `/bsadmin version YourSuperAddon`.

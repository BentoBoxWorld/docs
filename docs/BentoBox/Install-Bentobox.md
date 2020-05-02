# Video tutorial

[![Video thumbnail](https://i.ytimg.com/vi/01MagYDuOCk/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCzVNO0ObSEMOOpYtUEtv4LjsMhBA)](https://www.youtube.com/watch?v=01MagYDuOCk)

# Introduction

BentoBox is a powerful yet specific plugin to install and run on your server. We at BentoBoxWorld have discussed lengthily the most user-friendly installation method that would fit the best the defining features of BentoBox.

Compared to most Spigot plugins, BentoBox's installation will take a bit more time than a quick drag-and-drop in your server's plugins folder; but the countless possibilities it will bring you are worth it.

Let's get started!

***

# Download BentoBox

You can download BentoBox **for free** on different websites. Official releases can be found on the plugin's Spigot page or in the [GitHub `Releases` tab](https://github.com/BentoBoxWorld/bentobox/releases), whereas **untested** development builds can be downloaded from [Jenkins](https://ci.codemc.org/job/BentoBoxWorld/job/BentoBox/).

# Setup BentoBox

Once you have downloaded BentoBox, you have to put it in your server's `plugins` folder. Unlike ASkyBlock, there are no required dependencies: BentoBox will automatically hook into plugins it finds (such as Vault, PlaceholderAPI, Multiverse-Core, ...) to extend its capacity.

Boot up your server and wait until all plugins are fully enabled. If you connect on your server, you will notice BentoBox doesn't do anything special. As a matter of fact, **BentoBox does nothing on its own**: it needs you to add [Addons](https://github.com/BentoBoxWorld/bentobox/wiki/Addons) so it can "learn" to manage e.g. the Skyblock gamemode.

Now, turn off your server. You can have a look at BentoBox's `config.yml` file.

# Install Addons

[Addons](/BentoBox/Addons) are what makes BentoBox special. However, note that these **are not plugins**: they **won't launch** if you just put them in the `plugins` folder.

Firstly, you need to download the Addons you want to add to your server. Official ones can be found in [BentoBoxWorld's repositories list](https://github.com/BentoBoxWorld) and can be downloaded from their `Releases` tab (or from [Jenkins](https://ci.codemc.org/job/BentoBoxWorld/) for **untested** development builds). We will setup a website at some point so it gets easier for you to download them later on.

Once you have downloaded everything you need, you just have to put them all in the `plugins\BentoBox\addons` folder, boot up your server so that config files and folders get created, and finally turn it off again in order to be able to edit everything without causing any harm to your server.

Please note that Addons may sometimes be incompatible with the version of BentoBox you're using. Official Addons will **always** be provided with a clear statement of which version they support. However, note that they often support newer versions without needing to be updated.

# Conclusion

You should be good to go!
We are glad you are using our plugin, and we hope you will enjoy it as much as we enjoy improving it.
# Welcome to the BentoBox developer documentation!

BentoBox is a platform plugin that supports a suite of API's for Addons that run on it. The architecture is virtually identical to the Bukkit plugin system. You can create GameModeAddons like BSkyBlock that provide players with your own game mode experience, or you can develop utility Addons, like Warps that enable players to use warp signs in those game modes.

## Pladdons

Due to changes in the way servers operate (remapping of code when beingg loaded), it is now recommended that all Addons now run inside a Bukkit Plugin wrapper, which is provided by BentoBox and called a Pladdon - 
Pladdons = Plugin + Addon. by being a Plugin, they will be correctly remapped when loaded, which is important for servers such a Paper. 

The Pladdon wrapper's job is to generate the Addon instance and supply it any time it is requested via the `getAddon` method.

As a result of Addons being Plugins, they will be listed as such by the server, however they should still be placed in the `Bentobox/Addons` folder. 

# JavaDocs
Javadocs are here: [https://javadocs.bentobox.world](https://ci.codemc.io/job/BentoBoxWorld/job/BentoBox/javadoc/)

The core API package is `world.bentobox.bentobox.api.*`. Methods in those packages are kept as stable as possible over the long term. Methods and classes outside of the api package may change a lot or more frequently.

# Example Addon

@BONNe maintains an example addon here: [https://github.com/BONNePlayground/ExampleAddon](https://github.com/BONNePlayground/ExampleAddon)

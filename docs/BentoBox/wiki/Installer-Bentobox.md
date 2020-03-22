:fr: | [:us:](https://github.com/BentoBoxWorld/bentobox/wiki/Install-Bentobox) [:es:](https://github.com/BentoBoxWorld/bentobox/wiki/Instalar-BentoBox)

# Introduction

BentoBox est un plugin puissant mais particulier à installer et à utiliser sur votre serveur. Chez BentoBoxWorld, nous avons longuement discuté de la méthode d'installation la plus facile d'utilisation qui correspondrait le mieux aux caractéristiques qui définissent BentoBox.

En comparaison avec la plupart des plugins Spigot, l'installation de BentoBox prendra un peu plus de temps qu'un simple glisser-déposer dans le dossier plugins de votre serveur ; mais les innombrables possibilités qu'il vous apportera en valent la peine.

Commençons tout de suite !

***

# Télécharger BentoBox

Vous pouvez télécharger BentoBox **gratuitement** sur différents sites web. Les versions officielles peuvent être trouvées sur la page Spigot du plugin ou dans [l'onglet `Releases` sur GitHub](https://github.com/BentoBoxWorld/bentobox/releases), tandis que les versions de développement **non testées** peuvent être téléchargées depuis [Jenkins](https://ci.codemc.org/job/BentoBoxWorld/job/bentobox/).

# Installer BentoBox

Une fois que vous avez téléchargé BentoBox, vous devez le mettre dans le dossier `plugins` de votre serveur. Contrairement à ASkyBlock, il n'y a pas de dépendances requises : BentoBox [se connecte automatiquement aux plugins](https://github.com/BentoBoxWorld/bentobox/wiki/Hooks) qu'il trouve (comme Vault, PlaceholderAPI, Multiverse-Core, ...) pour étendre sa capacité.

Démarrez votre serveur et attendez que tous les plugins soient complètement activés. Si vous vous connectez sur votre serveur, vous remarquerez que BentoBox ne fait rien de spécial. En fait, **BentoBox ne fait rien tout seul** : il a besoin que vous ajoutiez des [Addons](https://github.com/BentoBoxWorld/bentobox/wiki/Addons) pour qu'il puisse "apprendre" à gérer, par exemple, le mode de jeu Skyblock.

Maintenant, éteignez votre serveur. Vous pouvez consulter le fichier `config.yml` de BentoBox.

# Installer des Addons

Les [Addons](https://github.com/BentoBoxWorld/bentobox/wiki/Addons) sont ce qui rend BentoBox si spécial. Cependant, notez que ce **ne sont pas des plugins** : ils **ne se lanceront pas** si vous les mettez dans le dossier `plugins`.

Tout d'abord, vous devez télécharger les Addons que vous voulez ajouter à votre serveur. Les versions officielles peuvent être trouvées dans la [liste des repositories de BentoBoxWorld](https://github.com/BentoBoxWorld) et peuvent être téléchargées à partir de l'onglet `Releases` (ou de [Jenkins](https://ci.codemc.org/job/BentoBoxWorld/) pour les versions de développement **non testées**). Nous mettrons en place un site Web à un moment donné afin qu'il vous soit plus facile de les télécharger.

Une fois que vous avez téléchargé tout ce dont vous avez besoin, il vous suffit de les mettre tous dans le dossier `plugins\BentoBox\addons`, de démarrer votre serveur, afin que les fichiers et dossiers de configuration soient créés, et finalement de le désactiver à nouveau pour pouvoir tout modifier sans causer aucun dommage à votre serveur.

Veuillez noter que les addons peuvent parfois être incompatibles avec la version de BentoBox que vous utilisez. Les addons officiels auront **toujours** une déclaration claire de la version qu'ils supportent. Cependant, notez qu'ils supportent souvent des versions plus récentes sans avoir besoin d'être mis à jour.

# Conclusion

Tout devrait fonctionner à présent !
Nous sommes heureux que vous utilisiez notre plugin, et nous espérons que vous l'apprécierez autant que nous aimons l'améliorer.
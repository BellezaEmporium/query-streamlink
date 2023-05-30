# query-streamlink

Une application sous Python destinée à renvoyer à l'utilisateur final le flux vidéo voulu, fonctionnant avec Streamlink.

## Programmes alternatifs

- Le programme [liveproxy](https://github.com/back-to/liveproxy) codé par back-to. Il est un membre actif du projet Streamlink, donc n'hésitez pas à l'aider en donnant au projet Streamlink !

## Donner au projet Streamlink

Ce programme est possible grâce à Streamlink.

Pour les soutenir, veuillez effectuer une donation sur leur [page Open Collective](https://opencollective.com/streamlink)

## Fonctionnement :

Ce programme fonctionne en demandant à Streamlink, en se basant sur l'URL donnée, un lien menant au flux vidéo, lisible par (quasiment !) tous les lecteurs connus à ce jour.
query-streamlink n'agit qu'en tant qu'intermédiaire entre Streamlink et l'utilisateur final.

## Attendez... ce programme est-il légal ?

Oui, ce programme est légal, puisqu'il à été conçu comme un intermédiaire à [Streamlink](https://github.com/streamlink/streamlink). Cependant, il peut le devenir si vous décidez de déformer le programme à des fins malicieuses, auquel cas je ne me tiens pas responsable.

### Sites supportés :

Quasiment tout les sites Internet supporté officiellement par [Streamlink](https://streamlink.github.io/plugin_matrix.html) (attention, certains sites sont restreints géographiquement)

## Paramètres :

streaming-ip (obligatoire) : L'URL du site dont vous souhaitez le flux vidéo.

## Comment lancer le programme localement :

C'est simple : il vous suffit de lancer le programme en écrivant ```python main.py```

## Comment déployer query-streamlink sur un service dédié :
- Heroku : [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https%3A%2F%2Fgithub.com%2FLaneSh4d0w%2Fquery-streamlink) (merci à [@adrianpaniagualeon](https://github.com/adrianpaniagualeon))

- Autres services (repl, glitch...) : Pour les autres services du même type, un simple fork du programme avec votre compte devrait suffire à le faire fonctionner, mais veuillez vérifier néanmoins s'il y existe des configurations spécifiques.

## Remerciements :

-  [@keystroke3](https://github.com/keystroke3) pour la refonte du programme, et de la création de l'API.

- Le groupe @iptv-org pour les premières implémentations et conseils (remerciements spéciaux à Nintendocustom / Dum4G)

- Les testeurs

- Les membres et contributeurs de Streamlink pour ce superbe logiciel.

### Sites disponibles (au 30/05/2023)

Il y a une très grande quantité de forks disponibles de query-streamlink afin que vous puissiez jouer avec !

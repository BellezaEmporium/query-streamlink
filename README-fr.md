# query-streamlink

Une application sous Python destinée à renvoyer à l'utilisateur final le flux vidéo voulu, fonctionnant avec Streamlink.

## Donner au projet Streamlink

Ce programme est possible grâce à Streamlink.

Pour les soutenir, veuillez effectuer une donation sur leur [page Open Collective](https://opencollective.com/streamlink)

## Comment lancer le programme :

- Localement :
```python main.py```

- En ligne (sur serveur repl / heroku etc...) :

Un simple fork du programme avec votre compte devrait pouvoir le faire fonctionner, mais veuillez vérifier néanmoins s'il y a des configurations spécifiques.

## Fonctionnement :

Ce programme fonctionne en demandant à Streamlink, en se basant sur l'URL donnée, un lien menant au flux vidéo, lisible par (quasiment !) tous les lecteurs connus à ce jour.
query-streamlink n'agit qu'en tant qu'intermédiaire entre Streamlink et l'utilisateur final.

### Sites supportés :

Tout site internet supporté officiellement par [Streamlink](https://streamlink.github.io/plugin_matrix.html) (attention, certains sites sont restreints géographiquement)

## Différentes options disponibles :

streaming-ip (obligatoire) : L'URL du site dont vous souhaitez le flux vidéo.

quality (optionnel) : La qualité voulue pour ce flux. Ne pas renseigner la qualité revient à choisir la meilleure, renseigner "unsure" revient à donner toutes les qualités disponibles pour ce flux.

## Remerciements :

-  [@keystroke3](https://github.com/keystroke3) pour la refonte du programme, et de la création de l'API.

- Le groupe @iptv-org pour les premières implémentations et conseils (remerciements spéciaux à Nintendocustom / Dum4G)

- Les testeurs

- Les membres et contributeurs de Streamlink pour ce superbe logiciel.


### Sites disponibles (au 22/11/2021)

Voici les sites utilisant ce programme recensés en ligne à ce jour : 

[Link-A-Stream - Hosted website (keystroke3) (WIP)](https://linkastream.co/)

[FullSpeed - DCT EU (dct-infra)](http://free.fullspeed.tv/)

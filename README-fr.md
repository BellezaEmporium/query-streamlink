# query-streamlink
query-streamlink est une application web Python destinée à retourner les liens donnés par toutes les sources supportées par Streamlink.

## Programmes alternatifs

- [liveproxy](https://github.com/back-to/liveproxy) : Si vous êtes un partisan de Streamlink, montrez votre soutien en faisant un don au projet Streamlink !

## Faire un don au projet Streamlink

query-streamlink doit son existence au projet Streamlink. Pour soutenir leur développement continu, envisagez de faire un don sur leur [Open Collective page](https://opencollective.com/streamlink).

## Comment ça marche

Le fonctionnement de query-streamlink repose sur l'envoi de requêtes à Streamlink en fonction de l'URL fournie par l'utilisateur. Il récupère ensuite une réponse contenant une URL qui peut être utilisée par la plupart des lecteurs multimédias courants. Ce programme agit comme un pont entre l'utilisateur final et Streamlink, garantissant des expériences de streaming fluides.

## Légalité

query-streamlink est un programme légal, car son but est de servir de passerelle vers [Streamlink](https://github.com/streamlink/streamlink). La seule utilisation illégale serait s'il était employé à des fins malveillantes, auquel cas je ne peux être tenu pour responsable.

### Sites web pris en charge

query-streamlink supporte une large gamme de sites web, compatibles avec [Streamlink](https://streamlink.github.io/plugin_matrix.html). Toutefois, il convient de faire attention aux problèmes liés aux blocages géographiques liés à l'usage de certains services.

## Paramètres de la requête

- `streaming-ip` (obligatoire) : L'URL du flux pour lequel vous avez besoin d'un lien.

## Déploiement local

Pour exécuter query-streamlink localement, il suffit d'exécuter la commande suivante : `python main.py`.

## Déploiement à distance de query-streamlink

- Heroku : [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https%3A%2F%2Fgithub.com%2FBellezaEmporium%2Fquery-streamlink) (merci à [@adrianpaniagualeon](https://github.com/adrianpaniagualeon))
- Autres services (repl / glitch...) : Pour les autres services, vérifiez s'ils nécessitent des configurations spécifiques. Dans la plupart des cas, forker le programme sur votre propre compte devrait être suffisant pour le faire fonctionner.

## Contribuer

Les contributions à Query-Streamlink sont les bienvenues ! Si vous souhaitez contribuer au projet, veuillez suivre les étapes suivantes :

1. Forkez le dépôt sur votre compte GitHub.
2. Créez une nouvelle branche pour votre fonctionnalité ou correction de bug.
3. Effectuez vos modifications et proposez-les avec un message expliquant votre démarche.
4. Insérez vos changements vers votre fork du projet.
5. Soumettez une demande de tirage au dépôt principal.

## Remerciements

- [@keystroke3](https://github.com/keystroke3) pour le support et les améliorations apportées à l'application.
- Les membres de la communauté IPTV qui ont contribué à rendre ce projet possible (remerciements particuliers à Nintendocustom / Dum4G).
- Les testeurs qui ont fourni des informations précieuses tout au cours du processus de développement.
- Les membres et contributeurs de Streamlink pour leur incroyable outil.

## Sites web disponibles (au 30/05/2023)

Il y a beaucoup de forks de query-streamlink disponibles dans la nature pour jouer avec !

## Licence

Query-Streamlink est sous licence [BSD-2 Clause license](./LICENSE).

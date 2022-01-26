# query-streamlink

Una aplicación python destinada a redireccionar al usuario final en el flujo de video deseado, funcionando con Streamlink.

## Contribuir al proyecto Streamlink:

Este programa es posible gracias a Streamlink.

Para contribuir en este proyecto, por favor haz una donación en su [página Open Collective](https://opencollective.com/streamlink)

## Como iniciar este programa:

- Localmente :
```python main.py```

- Servidor (repl / heroku etc...) :

Un fork del programa debe ser suficiente para hacerlo funcionar, sin embargo, verifica con el servidor las configuraciones específicas.

## Como eso funciona:

Este programa funciona por preguntar Streamlink, y basado en la URL, repuesta con una URL de flujo video que puede utilizar en (casi!) todos los reproductores de video conocido ahora.
query-streamlink solo es un intermediario entre el usuario final y Streamlink.

## Sitios soportados:

Prácticamente todos los sitios que [Streamlink](https://streamlink.github.io/plugin_matrix.html) soporte (atención con los problemas de restricción geográfica con unas servicios)

## Opciones diferentes:

streaming-ip (obligatorio) : La URL del stream que quiere ver.

quality (opcional): La calidad del stream en cualquier quieres verlo. No calidad especificada va a escoger la mejor calidad disponible. Especificar "unsure" va a mostrar todas las calidades disponibles.

## Gracias:

-  [@keystroke3](https://github.com/keystroke3) por el soporte y el rehacimiento de la aplicación.

- Las personas del grupo @iptv-org que eran implícito (especialmente Nintendocustom / Dum4G)

- Los probadores

- Los miembros y contribuyentes de Streamlink para este magnificente programa.


## Sitios disponibles (al 22/11/2021):

Aquí son las sitios web reconocidos que usan query-streamlink en el Internet:

[Link-A-Stream - Hosted website (keystroke3) (WIP)](https://linkastream.co/)

[FullSpeed - DCT EU (dct-infra)](http://free.fullspeed.tv/)

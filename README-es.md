# query-streamlink

Un aplicacion Python destinado a redirrecionar el usuario final en el flujo de vídeo querido, functionando con Streamlink.

## Contribuir al projecto Streamlink

Este programa es posible gracias a Streamlink.

Para contribuir en este projecto, por favor hace un donacion en su [pagina Open Collective](https://opencollective.com/streamlink)

## Como iniciar este programa :

- Localmente :
```python main.py```

- Servidor (repl / heroku etc...) :

Un fork del programa debe ser suficiente para hacerlo functionar, sin embargo, verifica con el servidor por configuraciones specificas.

## How it works :

This program works by asking Streamlink, based on the URL you gave, an URL that can be used for (almost !) all known players to this date. query-streamlink simply acts like an intermediary/redirector between the end-user and Streamlink.

### Supported websites :

Basically any website that [Streamlink](https://streamlink.github.io/plugin_matrix.html) supports (beware of geo-location issues for some services)

## Different queries available :

streaming-ip (mandatory) : The URL of the stream you need the link to.

quality (optional) : The streaming quality you want to watch in. No quality specified results in automatically choosing the best quality available for this stream.

## Thank yous :

-  [@keystroke3](https://github.com/keystroke3) for the support and rework of the application (He's looking for a full-time job ! If anyone's interested, contact him directly).

- The IPTV peepz that were involved in making this possible (special thanks to Nintendocustom / Dum4G)

- The testers

- The Streamlink members and contributors for this amazing tool that is.


### Available websites (as of 22/11/2021)

Here are the actual recensed websites that uses query-streamlink on the Internet :

[Link-A-Stream - Hosted website (keystroke3) (WIP)](https://linkastream.co/)

[FullSpeed - DCT EU (dct-infra)](http://free.fullspeed.tv/)

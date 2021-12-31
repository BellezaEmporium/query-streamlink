# query-streamlink

A Python webapp that is designed to redirect the end user to the stream they want, backed up by Streamlink.

## Donating to the streamlink project

This program is made possible thanks to Streamlink.

To support them, please make a donation to their [Open Collective page](https://opencollective.com/streamlink)

## How to load the program :

- Locally :
```python main.py```

- Remote (repl / heroku etc...) :
See if they have specific configurations, but a simple fork of the program using your account is sufficient to make it work !

## How it works :

This program works by asking Streamlink, based on the URL you gave, an URL that can be used for (almost !) all known players to this date. 
query-streamlink simply acts like an intermediary/redirector between the end-user and Streamlink.

### Supported websites :

Basically any website that [Streamlink](https://streamlink.github.io/plugin_matrix.html) supports (beware of geo-location issues for some services)

## Different queries available :

- streaming-ip (mandatory) : The URL of the stream you need the link to.

- quality (optional) : The streaming quality you want to watch in. No quality specified results in automatically choosing the best quality available for this stream. Specifying "unsure" gives you all the available qualities for the stream.

## Thank yous :

-  [@keystroke3](https://github.com/keystroke3) for the support and rework of the application.

- The IPTV peepz that were involved in making this possible (special thanks to Nintendocustom / Dum4G)

- The testers

- The Streamlink members and contributors for this amazing tool that is.


### Available websites (as of 22/11/2021)

Here are the actual recensed websites that uses query-streamlink on the Internet :

[Link-A-Stream - Hosted website (keystroke3) (WIP)](https://linkastream.co/)

[FullSpeed - DCT EU (dct-infra)](http://free.fullspeed.tv/)

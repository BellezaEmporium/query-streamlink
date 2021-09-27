# query-streamlink
A Python webapp that is destined to spit out links given by all sources supported by Streamlink.

## How it works :

This program works by asking Streamlink, based on the base URL you're giving him, an URL that is readable on (almost !) all known players to this date. The service acts like a redirector for the website you've chosen.

### Supported websites :

Basically any website that [Streamlink](https://streamlink.github.io/plugin_matrix.html) supports (beware of some geo-locked streams for some services)

## Different queries available :

streaming-ip (mandatory) : The URL of the stream you need the link to.

quality (optional) : The streaming quality you want to watch in. No quality specified results in automatically choosing the best quality available for this stream.

## Thank yous :

- keystroke3 for the support and rework of the application.

- The IPTV peepz that were involved in making this possible (special thanks to Nintendocustom / Dum4G)

- The testers

- The Streamlink members and contributors for this amazing tool that is.


### Available websites (as of 27/09/2021)

Here are the actual recensed websites that uses query-streamlink on the Internet :

[Query-Streamlink - Heroku EU (LaneSh4d0w)](https://query-streamlink.herokuapp.com/)

[Query-Streamlink - Heroku US (LaneSh4d0w)](https://query-streamlink-us.herokuapp.com/)

[Link-A-Stream - Hosted website (keystroke3) (WIP)](https://linkastream.co/)

[IPTv - DCT EU (dct-infra)](https://iptv.dc-team.com/)

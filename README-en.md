# query-streamlink

A Python webapp that is designed to redirect the end user to the stream they want, backed up by Streamlink.

## Alternative programs

- back-to's liveproxy (https://github.com/back-to/liveproxy). He's a streamlink member, so show him support by actually donating to the Streamlink project !

## Donating to the Streamlink project

This program is made possible thanks to Streamlink.

To support them, please make a donation to their [Open Collective page](https://opencollective.com/streamlink)

## How it works

This program works by asking Streamlink, based on the URL you give, to answer you with an URL that can be used for (almost !) all known players to this date. 
query-streamlink simply acts like an intermediary/redirector between the end-user and Streamlink.

## Wait... is that legal ?

Yes, this program is legal, since it is designed as a bridge for [Streamlink](https://github.com/streamlink/streamlink), the only illegal thing you might do with it is hijacking the main program for malicious causes, in this case I won't be held responsible.

### Supported websites

Basically any website that [Streamlink](https://streamlink.github.io/plugin_matrix.html) supports (beware of geo-location issues for some services)

## Query parameters

- streaming-ip (mandatory) : The URL of the stream you need the link to.

## How to load the program locally

Simple: launch the program by using ```python main.py```

## How to deploy query-streamlink on a remote service

- Heroku : [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https%3A%2F%2Fgithub.com%2FLaneSh4d0w%2Fquery-streamlink) (kudos to [@adrianpaniagualeon](https://github.com/adrianpaniagualeon))
- Other services (repl / glitch...) :
For the other kinds, see if they have specific configurations, but a simple fork of the program using your account is sufficient to make it work !

## Thank you

-  [@keystroke3](https://github.com/keystroke3) for the support and rework of the application.

- The IPTV peepz that were involved in making this possible (special thanks to Nintendocustom / Dum4G)

- The testers

- The Streamlink members and contributors for this amazing tool that is.

## Available websites (as of 30/05/2023)

There's lots of forks of query-streamlink out in the wild to play with !

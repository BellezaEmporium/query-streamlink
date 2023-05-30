# query-streamlink

Una aplicación web en Python diseñada para redirigir al usuario final al stream que desee, respaldado por Streamlink.

## Programas alternativos

- [liveproxy](https://github.com/back-to/liveproxy): Es miembro de Streamlink, ¡así que demuéstrale tu apoyo donando al proyecto Streamlink!

## Donando al proyecto Streamlink

Este programa ha sido creado gracias a Streamlink. Para apoyarles, por favor haz una donación en su [página de Open Collective](https://opencollective.com/streamlink).

## Cómo funciona

Este programa funciona solicitando a Streamlink, basándose en la URL que le facilites, una respuesta con una URL que pueda ser utilizada por (¡casi!) todos los reproductores conocidos hasta la fecha. Query-streamlink simplemente actúa como un intermediario/redirector entre el usuario final y Streamlink.

## Espera... ¿es legal?

Sí, este programa es legal, ya que está diseñado como puente para [Streamlink](https://github.com/streamlink/streamlink). Lo único ilegal que podrías hacer con él es secuestrar el programa principal por causas maliciosas.

### Sitios web soportados

Básicamente cualquier sitio web que soporte [Streamlink](https://streamlink.github.io/plugin_matrix.html) (cuidado con los problemas de geolocalización de algunos servicios).

## Parámetros de consulta

- `streaming-ip` (obligatorio): La URL del stream al que necesita el enlace.

## Cómo cargar el programa localmente

Simple: lanza el programa usando `python main.py`.

## Cómo desplegar query-streamlink en un servicio remoto

- Heroku: [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https%3A%2F%2Fgithub.com%2FLaneSh4d0w%2Fquery-streamlink) (gracias a [@adrianpaniagualeon](https://github.com/adrianpaniagualeon))
- Otros servicios (repl / glitch...): ¡Para los otros servicios, mira si tienen configuraciones específicas, pero un simple fork del programa usando tu cuenta es suficiente para hacerlo funcionar!

## Gracias

- [@keystroke3](https://github.com/keystroke3) por el apoyo y la reelaboración de la aplicación.
- Los IPTV peepz que estuvieron involucrados en hacer esto posible (agradecimientos especiales a Nintendocustom / Dum4G).
- Los testeadores.
- Los miembros y colaboradores de Streamlink por esta increíble herramienta.

## Sitios web disponibles (a 15/08/2022)

Aquí están los sitios web disponibles que utilizan query-streamlink en Internet:

- [FullSpeed - DCT EU (dct-infra)](http://free.fullspeed.tv/)
- ... ¡así como todas las demás bifurcaciones disponibles en GitHub!

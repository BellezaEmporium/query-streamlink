# query-streamlink

query-streamlink es una webapp en Python diseñada para redirigir al usuario final al stream que desee, respaldado por Streamlink.

## Programas alternativos

- [liveproxy](https://github.com/back-to/liveproxy): Si eres partidario de Streamlink, ¡muestra tu apoyo donando al proyecto Streamlink!

## Donar al proyecto Streamlink

query-streamlink debe su existencia al proyecto Streamlink. Para apoyar su desarrollo continuo, considera hacer una donación en su [página de Open Collective](https://opencollective.com/streamlink).

## Cómo funciona

Este programa funciona solicitando a Streamlink, basándose en la URL que le facilites, una respuesta con una URL que pueda ser utilizada por (¡casi!) todos los reproductores conocidos hasta la fecha. Query-streamlink simplemente actúa como un intermediario/redirector entre el usuario final y Streamlink, garantizando experiencias de reproducción sin problemas.

## Legalidad

query-streamlink es legal, ya que está diseñado como puente para [Streamlink](https://github.com/streamlink/streamlink). El único uso ilegal sería si se empleara con fines maliciosos, y en este caso no puede ser responsable.

### Sitios web soportados

Básicamente cualquier sitio web que soporte [Streamlink](https://streamlink.github.io/plugin_matrix.html) (cuidado con los problemas de geolocalización de algunos servicios).

## Parámetros de consulta

- `url` (obligatorio): La URL del stream al que necesita el enlace.
- `no_redirect` (opcional, valor : null) : Si no necesites ser redirigido en el sitio.
- `quality` (opcional, valor : best) : Si necesitas poner un parametro de calidad;

## Despliegue local

Para ejecutar query-streamlink localmente, simplemente ejecute el siguiente comando: `python main.py`.

## Despliegue remoto

- Heroku: [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https%3A%2F%2Fgithub.com%2FBellezaEmporium%2Fquery-streamlink) (gracias a [@adrianpaniagualeon](https://github.com/adrianpaniagualeon))
- Otros servicios (repl / glitch...): Para otros servicios, comprueba si requieren configuraciones específicas. En la mayoría de los casos, bifurcar el programa usando tu propia cuenta debería ser suficiente para hacerlo funcionar.

## Contribuir

¡Las contribuciones a query-streamlink son bienvenidas! Si quieres contribuir al proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama
3. Realice los cambios con mensajes de confirmación descriptivos.
4. Envíe los cambios a su repositorio.
5. Envíe un pull request al repositorio principal.

## Agradecimientos

- [@keystroke3](https://github.com/keystroke3) por el soporte y las mejoras realizadas en la aplicación.
- A los miembros de la comunidad IPTV que han contribuido a hacer posible este proyecto (gracias especialmente a Nintendocustom / Dum4G).
- Los testeadores que aportaron valiosos comentarios durante el proceso de desarrollo.
- Los miembros y colaboradores de Streamlink por su increíble herramienta.

## Sitios web disponibles (a 30/05/2023)

¡Hay un montón de bifurcaciones de query-streamlink con los que jugar!

## Licencia

Query-Streamlink está licenciado bajo la [BSD-2 Clause license](./LICENSE).

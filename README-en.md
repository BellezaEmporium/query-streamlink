# query-streamlink
query-streamlink is a Python webapp destined to spit out links given by all sources supported by Streamlink.

## Alternative Programs

- [liveproxy](https://github.com/back-to/liveproxy): If you are a supporter of Streamlink, show your support by donating to the Streamlink project!

## Donating to the Streamlink Project

query-streamlink owes its existence to the Streamlink project. To support their ongoing development, consider making a donation on their [Open Collective page](https://opencollective.com/streamlink).

## How It Works

The functioning of query-streamlink relies on making requests to Streamlink based on the URL provided by the user. It then retrieves a response containing a URL that can be used by most popular media players. This program acts as a bridge between the end user and Streamlink, ensuring smooth streaming experiences.

## Legality

query-streamlink is a legal program, as its purpose is to serve as a bridge to [Streamlink](https://github.com/streamlink/streamlink). The only unlawful use would be if it were employed for malicious purposes, which in that case I can't be held responsible.

### Supported Websites

query-streamlink supports a wide range of websites compatible with [Streamlink](https://streamlink.github.io/plugin_matrix.html). However, please be cautious of potential geolocation issues with certain services.

## Query Parameters

- `streaming-ip` (required): The URL of the stream for which you need the link.

## Local Deployment

To run query-streamlink locally, simply execute the following command: `python main.py`.

## Remote Deployment of query-streamlink

- Heroku: [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https%3A%2F%2Fgithub.com%2FBellezaEmporium%2Fquery-streamlink) (thanks to [@adrianpaniagualeon](https://github.com/adrianpaniagualeon))
- Other services (repl / glitch...): For other services, check if they require specific configurations. In most cases, forking the program to your own account should be sufficient to make it work.

## Contributing

Contributions to Query-Streamlink are welcome! If you want to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

## Acknowledgements

- [@keystroke3](https://github.com/keystroke3) for the support and improvements made to the app.
- The IPTV community members who contributed to making this project possible (special thanks to Nintendocustom / Dum4G).
- The testers who provided valuable feedback during the development process.
- The Streamlink members and contributors for their incredible tool.

## Available websites (as of 30/05/2023)

There's lots of forks of query-streamlink out in the wild to play with !

## License

Query-Streamlink is licensed under the [BSD-2 Clause license](./LICENSE).

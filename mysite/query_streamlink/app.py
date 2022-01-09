from ninja import NinjaAPI
from django.shortcuts import redirect

app = NinjaAPI()

import validators
import streamlink
from streamlink import (
    PluginError
)


class Fetch:
    """
    Gets data from host, filters it and returns streams
    (query: str, quality: str,list,tuple)
    """

    def __init__(self, query, quality):
        self.query = query
        if not quality:
            quality = "best"
        if "," in quality:
            self.qualities = quality.split(",")
        else:
            self.qualities = [quality]

    def get_streams(self):
        """
        Get data streams and resolutions
        Returns: (links, resolution), Error string
        """
        try:
            links = streamlink.streams(self.query)
            res = list(links.keys())
            return links, res
        except Exception:
            # returns exceptions raised by streamlink
            raise

    def filtered_streams(self):
        """
        Filter streams according to specified quality.
        Default quality: best
        Returns: {quality: stream_url}
        """
        try:
            payload = self.get_streams()
            streams, resolutions = payload
            if not streams:
                raise ValueError
            res_str = ",".join(resolutions)
        except PluginError as pe:
            return str(pe)
        except ValueError:
            return f"Could not get the link, Streamlink couldn't read {self.query}"
        except TypeError:
            return payload

        if "best" in self.qualities:
            next((x for x in res_str if x == "best"), None)
        elif "worst" in self.qualities:
            next((x for x in res_str if x == "worst"), None)

        for q in self.qualities:
            if q not in resolutions:
                return f"Invalid quality {q}. Available qualities are: {res_str}"
        return {quality: streams[quality].url for quality in self.qualities}


def make_m3u8(output):
    """Creates m3u file and string
    (output: dict, query: str)
    """
    speeds = {
        1000: 5_000_000,
        700: 2_500_000,
        400: 1_100_000,
        300: 700_000,
        200: 400_000,
        100: 200_000,
    }
    link_str = "#EXTM3U\n"
    for res in output:
        r = res.split("p")[0]
        if type(r) == int:
            for speed in speeds:
                if r >= speed:
                    bandwidth = speeds[speed]
                    break
        else:
            bandwidth = 100_000
        title = (
            f"#EXT-X-STREAM-INF:CLOSED-CAPTIONS=NONE,BANDWIDTH={bandwidth},NAME={res}\n"
        )
        link = f"{output[res]}\n"
        link_str += title + link
    with open("stream.m3u8", "w") as f:
        f.write(link_str)
    return link_str


def api_formatted(output, api):
    """Formats the output to json if the endpoint is /api"""
    if api:
        if type(output) == dict:
            return output
        return {"Error": output}
    if type(output) == dict:
        if len(output) == 1:
            return next(iter(output.values()))
        return make_m3u8(output)
    return output


def query_handler(args, api):
    """Checks and tests arguments before serving request"""
    if args:
        query = args[0]
        if not query:
            message = "streaming-ip string is empty"
            return api_formatted(message, api)

        valid = validators.url(query)
        if not valid:
            message = "The URL you've entered is not valid."
            return api_formatted(message, api)

        quality = args[1]
        if quality == "":
            message = "Empty quality string"
            return api_formatted(message, api)

        stream_obj = Fetch(query, quality)
        streams = stream_obj.filtered_streams()
        return api_formatted(streams, api)
    else:
        message = "No queries provided. Nothing to do."
        return api_formatted(message, api)


@app.get("/")
def index(request):
    return "This program permits you to get direct access to streams by using Streamlink.\nIf you have a link that needs to be treated, from this webpage, add /iptv-query?streaming-ip= *your URL*.\nNote that it will work only on Streamlink-supported websites.\nEnjoy ! LaneSh4d0w. Special thanks to Keystroke for the API usage."


@app.get("/query")
def home(request, url: str, quality: str = None):
    answer = [url, quality]
    response = query_handler(answer, False)
    if response.startswith("#EXTM3U"):
        return send_file("stream.m3u8")
    elif response.startswith("http"):
        return redirect(response)
    else:
        return response


@app.get("/api")
def api(request, url: str):
    return query_handler(url, True)

if __name__ == '__main__':
    app.run(threaded=False, port=5000)
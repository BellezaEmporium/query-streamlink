#!/usr/bin/env python
from flask import Flask, request, redirect, send_file
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import validators
from api import Fetch

app = Flask(__name__)

limiter = Limiter(
    app,
    key_func=get_remote_address
)


def make_m3u8(output, query):
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


def api_formated(output, api, query=""):
    """Formats the output to json if the endpoint is /api"""
    if api:
        if type(output) == dict:
            return output
        return {"Error": output}
    if type(output) == dict:
        if len(output) == 1:
            return next(iter(output.values()))
        return make_m3u8(output, query)
    return output


def query_hanlder(args, api):
    """Checks and tests arguments before serving request"""
    if args:
        query = args.get("streaming-ip")
        if not query:
            message = "No streaming IP found. Reason: streaming-ip string is empty"
            return api_formated(message, api)

        valid = validators.url(query)
        if not valid:
            message = "The URL you've entered is not valid."
            return api_formated(message, api)

        quality = args.get("quality")
        stream_obj = Fetch(query, quality)
        streams = stream_obj.filtered_streams()
        return api_formated(streams, api, query)
    else:
        message = "No queries provided. Nothing to do."
        return api_formated(message, api)


@app.route("/")
def index():
    return "This program permits you to get direct access to streams by using Streamlink. Enjoy ! LaneSh4d0w."


@app.route("/iptv-query")
@limiter.limit("30 per minute")
@limiter.limit("1 per second")
def home():
    response = query_hanlder(request.args, False)
    if response.startswith("#EXTM3U"):
        return send_file("stream.m3u8")
    elif response.startswith("http"):
        return redirect(response)
    else:
        return response  

@app.route("/api")
@limiter.limit("30 per minute")
@limiter.limit("1 per second")
def api():
    return query_hanlder(request.args, True)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)

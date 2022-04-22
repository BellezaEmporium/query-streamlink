#!/usr/bin/env python
from flask import Flask, request, redirect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import validators
from api import get_streams

app = Flask(__name__)

limiter = Limiter(
    app,
    key_func=get_remote_address
)


def query_handler(args):
    """Checks and tests arguments before serving request"""
    if not args.get("streaming-ip"):
        return "You didn't give any URL."
    else:
        valid = validators.url(args.get("streaming-ip"))
        if not valid:
            return "The URL you've entered is not valid."
        else:
            return get_streams(args.get("streaming-ip"))


@app.route("/", methods=['GET'])
def index():
    return "This program permits you to get direct access to streams by using Streamlink.\r\nIf you have a link that " \
           "needs to be treated, from this webpage, add /iptv-query?streaming-ip= *your URL*.\r\nNote that it will " \
           "work " \
           "only on Streamlink-supported websites.\r\nEnjoy ! LaneSh4d0w. Special thanks to Keystroke for the API " \
           "usage. "


@app.route("/iptv-query", methods=['GET'])
@limiter.limit("20/minute")
@limiter.limit("1/second")
def home():
    response = query_handler(request.args)
    valid2 = validators.url(response)
    if not valid2:
        return response
    else:
        return redirect(response)


@app.errorhandler(429)
def ratelimit_handler():
    return "Whoa there ! I know you like that service, but there's no need to spam me ! Let the server breathe a " \
           "little bit (RATE LIMIT EXCEEDED) "


# change to your likings, params are "ip", "port", "threaded"
if __name__ == '__main__':
    app.run(threaded=False, port=5000)

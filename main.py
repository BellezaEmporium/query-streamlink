#!/usr/bin/env python
from flask import Flask, request, redirect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import validators
from api import Fetch

app = Flask(__name__)

limiter = Limiter(
    app,
    key_func=get_remote_address
)

def query_handler(args):
    """Checks and tests arguments before serving request"""
    if args:
        query = args.get("streaming-ip")
        if not query:
            return "You didn't give any URL."
        valid = validators.url(query)
        if not valid:
            return "The URL you've entered is not valid."
        return Fetch().get_streams(query)
    else:
        return "No queries provided. Nothing to do."


@app.route("/", methods=['GET'])
def index():
    return "This program permits you to get direct access to streams by using Streamlink.\r\nIf you have a link that " \
           "needs to be treated, from this webpage, add /iptv-query?streaming-ip= *your URL*.\r\nNote that it will work " \
           "only on Streamlink-supported websites.\r\nEnjoy ! LaneSh4d0w. Special thanks to Keystroke for the API usage. "


@app.route("/iptv-query", methods=['GET'])
@limiter.limit("20/minute")
@limiter.limit("1/second")
def home():
    response = query_handler(request.args)
    valid2 = validators.url(response)
    if response is not None:
        if not valid2:
            return f"Link {request.args['streaming-ip']} returned no valid URL as an answer. Instead, it answered {response}. "
        else:
            return redirect(response)
    else:
        return "Nothing was provided by Streamlink."


@app.errorhandler(429)
def ratelimit_handler(e):
    return "Whoa there ! I know you like that service, but there's no need to spam me ! Let the server breathe a little bit (RATE LIMIT EXCEEDED)"

# change to your likings, params are "ip", "port", "threaded"
if __name__ == '__main__':
    app.run(threaded=False, port=5000)

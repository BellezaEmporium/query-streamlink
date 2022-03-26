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
            message = "streaming-ip string is empty"
            return message

        valid = validators.url(query)
        if not valid:
            message = "The URL you've entered is not valid."
            return message

        stream_obj = Fetch().get_streams(query)
        return stream_obj
    else:
        message = "No queries provided. Nothing to do."
        return message


@app.route("/", methods=['GET'])
def index():
    return "This program permits you to get direct access to streams by using Streamlink.\nIf you have a link that needs to be treated, from this webpage, add /iptv-query?streaming-ip= *your URL*.\nNote that it will work only on Streamlink-supported websites.\nEnjoy ! LaneSh4d0w. Special thanks to Keystroke for the API usage."


@app.route("/iptv-query", methods=['GET'])
@limiter.limit("20/minute")
@limiter.limit("1/second")
def home():
    response = query_handler(request.args)
    if response is not None:
        return redirect(response)
    else:
        return f"Link {request.args['streaming-ip']} returned no answer."


@app.errorhandler(429)
def ratelimit_handler(e):
    return "Whoa there ! I know you like that service, but there's no need to spam me ! Let the server breathe a little bit (RATE LIMIT EXCEEDED)"

# change to your likings, params are "ip", "port", "threaded"
if __name__ == '__main__':
    app.run(threaded=False, port=5000)

#!/usr/bin/env python
from flask import Flask, request, redirect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import validators
from api import get_streams

app = Flask(__name__)

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["100 per hour"],
    storage_uri="memory://",
)


# Reads the URL parameters and redirects to Streamlink.
def query_handler(args):
    """Checks and tests arguments before serving request"""
    if not args.get("streaming-ip"):
        return "You didn't give any URL."

    # for dacast, be warned we have MULTIPLE parameters. Get it if exists
    if args.get("provider"):
        valid = validators.url(args.get("streaming-ip"))
        url = args.get("streaming-ip") + "&provider=" + args.get('provider')
        return get_streams(url) if valid else "The URL you've entered is not valid."
    else:
        valid = validators.url(args.get("streaming-ip"))
        return get_streams(args.get("streaming-ip")) if valid else "The URL you've entered is not valid."


# Presentation page
@app.route("/", methods=['GET'])
def index():
    return "This program permits you to get direct access to streams by using Streamlink.\r\nIf you have a link that " \
           "needs to be treated, from this webpage, add /iptv-query?streaming-ip= *your URL*.\r\nNote that it will " \
           "work " \
           "only on Streamlink-supported websites.\r\nEnjoy ! LaneSh4d0w. Special thanks to Keystroke for the API " \
           "usage. "


# iptv-query route -> gives link to Streamlink, link is analyzed
# for correct plugin routing, and redirects (or shows) to the stream link.
@app.route("/iptv-query", methods=['GET'])
@limiter.limit("20/minute")
@limiter.limit("1/second")
def home():
    response = query_handler(request.args)
    valid2 = validators.url(response)
    if response is None or not valid2:
        return response

    return response if request.args.get("noredirect") == "yes" else redirect(response)


# Rate limiting system.
@app.errorhandler(429)
def ratelimit_handler(e):
    return f'{e}. To ensure everyone gets a correct access to the program, we are rate-limiting the server.'


# change to your likings, params are "ip", "port", "threaded"
if __name__ == '__main__':
    app.run(threaded=False, port=5000)

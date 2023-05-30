#!/usr/bin/env python
from flask import Flask, request, redirect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import validators
from api import get_streams

app = Flask(__name__)

# Create a rate limiter to control the number of requests per hour from each IP address.
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["100 per hour"],
    storage_uri="memory://"
)


# Reads the URL parameters and redirects to Streamlink.
def query_handler(args):
    """Checks and tests arguments before serving the request"""
    if not args.get("streaming-ip"):
        return "You didn't provide any URL."

    # For Dacast, be warned we have MULTIPLE parameters. Get it if it exists.
    if args.get("provider"):
        valid = validators.url(args.get("streaming-ip"))
        url = args.get("streaming-ip") + "&provider=" + args.get('provider')
        return get_streams(url) if valid else "The URL you entered is not valid."
    else:
        valid = validators.url(args.get("streaming-ip"))
        return get_streams(args.get("streaming-ip")) if valid else "The URL you entered is not valid."


# Presentation page
@app.route("/", methods=['GET'])
def index():
    """Displays the presentation page with instructions"""
    return (
        "This program allows you to access streams directly using Streamlink.\r\n"
        "To process a link, append '/iptv-query?streaming-ip=*your URL*' to this webpage.\r\n"
        "Please note that it only works with Streamlink-supported websites.\r\n"
        "Enjoy! LaneSh4d0w. Special thanks to Keystroke for the API usage."
    )


# iptv-query route -> provides a link to Streamlink, analyzes the link
# for correct plugin routing, and redirects (or displays) the stream link.
@app.route("/iptv-query", methods=['GET'])
@limiter.limit("20/minute")
@limiter.limit("1/second")
def home():
    """Handles the IPTV query request and redirects to the stream link"""
    response = query_handler(request.args)
    valid2 = validators.url(response)
    if response is None or not valid2:
        return response

    return response if request.args.get("noredirect") == "yes" else redirect(response)


# Rate limiting system.
@app.errorhandler(429)
def ratelimit_handler(e):
    """Handles rate limit exceeded error"""
    return f"{e}. To ensure fair access to the program, we are limiting the number of requests."


# Change the parameters according to your preferences: "host", "port", "threaded".
if __name__ == '__main__':
    app.run(threaded=False, port=5000)

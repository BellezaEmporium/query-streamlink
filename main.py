#!/usr/bin/env python
from flask import Flask, redirect, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from validators import url
import validators
from api import get_streams

app = Flask(__name__)

# Create a rate limiter to control the number of requests per hour from each IP address.
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["100 per hour"],
    storage_uri="memory://"
)


# Reads the URL parameters and redirects to Streamlink.
def query_handler(args):
    streaming_ip = args.get("url")
    provider = args.get("provider")
    quality = args.get("quality")
    if not streaming_ip:
        return "You didn't provide any URL."
    if not quality:
        quality = "best"
    if validators.url(streaming_ip):
        if provider:
            return get_streams(streaming_ip + "&provider=" + provider, quality)
        else:
            return get_streams(streaming_ip, quality)
    else:
        return "The URL you entered is not valid."


# Presentation page
@app.route("/", methods=['GET'])
def index():
    return """
            This program allows you to access streams directly using Streamlink.
            To process a link, append '/iptv-query?streaming-ip=*your URL*' to this webpage.
            Please note that it only works with Streamlink-supported websites.
            Enjoy! LaneSh4d0w. Special thanks to Keystroke for the API usage.
           """

# iptv-query route -> provides a link to Streamlink, analyzes the link
# for correct plugin routing, and redirects (or displays) the stream link.
@app.route("/iptv-query", methods=['GET'])
@limiter.limit("20/minute")
def home():
    no_redirect = request.args.get("no_redirect")
    """Handles the IPTV query request and redirects to the stream link"""
    try:
        response = query_handler(request.args)
    except Exception as e:
        return f"An error occurred: {str(e)}"
    if not url(response):
        return response
    return redirect(response) if not no_redirect else response

# Rate limiting system.
@app.errorhandler(429)
def ratelimit_handler(e):
    """Handles rate limit exceeded error"""
    return "{}. To ensure fair access to the program, we are limiting the number of requests.".format(e)


if __name__ == '__main__':
    app.run(threaded=False, port=5000)
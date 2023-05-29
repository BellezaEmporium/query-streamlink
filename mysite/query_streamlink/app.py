from ninja import NinjaAPI
from django.shortcuts import redirect

app = NinjaAPI()

import validators
import streamlink
from streamlink import (
    NoPluginError
    PluginError
)
from streamlink.stream import DASHStream


class Fetch:
    """
    Get data streams
    Returns: (links), Error string
    """
    try:
        streams = streamlink.streams(query).items()
        if not streams:
            return "No streams found."
        
        for quality, link in streams:
            if query.__contains__('dailymotion.com') or query.__contains__('dai.ly'):
                url = link.to_manifest_url()
                if url.__contains__('https://www.dailymotion.com/cdn/live/video/'):
                    response = urllib.request.urlopen(url)
                    data = response.read()
                    text = data.decode('utf-8')
                    replacements = {'live-3': 'live-0', 'live-2': 'live-0', 'live-1': 'live-0'}
                    for key in replacements:
                        if text.__contains__(key):
                            l0_link = link.to_url()
                            l0_replace = l0_link.replace('live-0', replacements[key])
                            return l0_replace
                    return link.to_url()
                else:
                    return url

            if isinstance(link, DASHStream):
                return link.to_url()
            elif not isinstance(link, DASHStream):
                if "best" in quality and "chunklist" in link.to_url() \
                        or "live" in quality or "http" in quality:
                    return link.to_url()
                else:
                    return link.to_manifest_url()

    except ValueError as ex:
        return f"Streamlink couldn't read {query}, {ex}"
    except NoPluginError:
        return f"No plugin has been implemented for website {query}"
    except PluginError as pex:
        return f"A Plugin error has occurred: {pex}"
    except Exception as nex:
        return f"Something went wrong: {nex}"


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


@app.get("/")
def index(request):
    return "This program permits you to get direct access to streams by using Streamlink.\nIf you have a link that needs to be treated, from this webpage, add /iptv-query?streaming-ip= *your URL*.\nNote that it will work only on Streamlink-supported websites.\nEnjoy ! LaneSh4d0w. Special thanks to Keystroke for the API usage."


@app.get("/query")
def home(request, url: str, quality: str = None):
    response = query_handler(request.args)
    valid2 = validators.url(response)
    if response is None or not valid2:
        return response

    return response if request.args.get("noredirect") == "yes" else redirect(response)


if __name__ == '__main__':
    app.run(threaded=False, port=5000)

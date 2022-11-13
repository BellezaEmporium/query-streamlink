import streamlink
from streamlink import NoPluginError, PluginError
from streamlink.stream import DASHStream
import urllib.request


# Queries Streamlink for stream link retrieval, gives correct redirection measures
def get_streams(query):
    """
    Get data streams
    Returns: (links), Error string
    """
    try:
        streams = streamlink.streams(query).items()
        if not streams:
            return "No streams found."
        for quality, link in streams:
            # Dailymotion no-IP-lock stream workaround
            if query.__contains__('dailymotion.com') or query.__contains__('dai.ly'):
                url = link.to_manifest_url()
                response = urllib.request.urlopen(url)
                data = response.read()
                text = data.decode('utf-8')
                if text.__contains__('live-3'):
                    l0_link = link.to_url()
                    l0_replace = l0_link.replace('live-0', 'live-3')
                    return l0_replace
                elif text.__contains__('live-2') and not text.__contains__('live-3'):
                    l0_link = link.to_url()
                    l0_replace = l0_link.replace('live-0', 'live-2')
                    return l0_replace
                elif text.__contains__('live-1') and not text.__contains__('live-2') and not text.__contains__('live-3'):
                    l0_link = link.to_url()
                    l0_replace = l0_link.replace('live-0', 'live-1')
                    return l0_replace
                else:
                    return link.to_url()

            # Some DASH streams have got some interesting issues, hence we need to fix it directly.
            # All HLS links should work with adaptive.
            if type(link) is DASHStream:
                return link.to_url()
            elif type(link) is not DASHStream:
                return link.to_url() if "best" in quality and "chunklist" in link.to_url() \
                                        or "live" in quality or "http" in quality else link.to_manifest_url()
    # Issue when getting data from query
    except ValueError as ex:
        return f"Streamlink couldn't read {query}, {ex}"
    # Trying to use Streamlink on an unsupported website
    except NoPluginError:
        return f"No plugin has been implemented for website {query}"
    # Plugin issue when getting data from query
    except PluginError as pex:
        return f"A Plugin error has occurred, {pex}"
    # Anything else
    except Exception as nex:
        return f"Something went wrong somewhere, it seems, or else I wouldn't have '{nex}' as a result."

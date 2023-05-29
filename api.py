import streamlink
from streamlink import NoPluginError, PluginError
from streamlink.stream import DASHStream
import urllib.request


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

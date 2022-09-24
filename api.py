import streamlink
from streamlink import NoPluginError, PluginError
from streamlink.stream import DASHStream, HLSStream


def get_streams(query):
    """
    Get data streams
    Returns: (links), Error string
    """
    try:
        streams = list(streamlink.streams(query).items())
        if not streams:
            return "No streams found."
        for quality, link in streams:
            # Some DASH streams have got some interesting issues, hence we need to fix it directly.
            # All HLS links should work with adaptive.
            if type(link) is DASHStream:
                return link.to_url()
            elif type(link) is HLSStream:
                return link.to_url() if "best" in quality and "chunklist" in link.to_url()\
                                    or "live" in quality else link.to_manifest_url()
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

import streamlink
from streamlink import NoPluginError, PluginError
from streamlink.stream import DASHStream


# Queries Streamlink for stream link retrieval, gives correct redirection measures
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
            # Dailymotion no-IP-lock stream workaround
            if query.__contains__('dailymotion.com') or query.__contains__('dai.ly'):
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
        return f"Streamlink couldn't read {query}, for this reason : {ex}"
    except NoPluginError:
        return f"Streamlink was unable to process your query, because no plugin has been implemented for website {query}"
    except PluginError as pex:
        return f"Streamlink couldn't process {query}, because of a Plugin error. Reason is as follows: {pex}"

import streamlink
from streamlink import NoPluginError, PluginError


def get_streams(query):
    """
    Get data streams
    Returns: (links), Error string
    """
    try:
        streams = list(streamlink.streams(query).items())
        if not streams:
            return "No streams found."
        else:
            for quality, link in streams:
                # Suggest that if there's no multiple qualities (live),
                # give manifest (master) URL.
                if "live" not in quality or "best" in quality:
                    return link.to_manifest_url()
                else:
                    return link.to_url()
    except ValueError as ex:
        return f"Streamlink couldn't read {query}, for this reason : {ex}"
    except NoPluginError:
        return f"Streamlink was unable to process your query, because no plugin has been implemented for website {query}"
    except PluginError as pex:
        return f"Streamlink couldn't process {query}, because of a Plugin error. Reason is as follows: {pex}"

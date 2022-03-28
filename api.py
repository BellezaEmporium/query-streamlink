import streamlink
from streamlink import (
    PluginError
)


class Fetch:
    def get_streams(self, query):
        """
        Get data streams
        Returns: (links), Error string
        """
        try:
            streams = list(streamlink.streams(query).items())
            if not streams:
                return None
            else:
                for quality, link in streams:
                    # Suggest that if there's no multiple qualities (live),
                    # give manifest (master) URL.
                    if "live" not in quality:
                        return link.to_manifest_url()
                    else:
                        return link.to_url()
        except ValueError as ex:
            return f"Streamlink couldn't read {query}, for this reason : {ex}"
        except PluginError as pe:
            return str(pe)

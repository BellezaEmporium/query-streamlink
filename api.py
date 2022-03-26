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
                return "No streams have been found."
            else:
                for quality, link in streams:
                    # read HLSStream as "string" even if it isn't conventional
                    string_link = str(link)
                    # specific streann / DASH fix
                    if "streannlive" or "DASHStream" in string_link:
                        return link.to_manifest_url()
                    else:
                        return link.to_url()
        except ValueError as ex:
            return f"Could not get the link, Streamlink couldn't read {query}, for this reason : {ex}"
        except PluginError as pe:
            return str(pe)

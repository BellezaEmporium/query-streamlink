import streamlink
from streamlink import (
    PluginError,
)


class Fetch:
    """
    Gets data from host, filters it and returns streams
    (query: str, quality: str,list,tuple)
    """

    def __init__(self, query, quality):
        self.query = query
        if not quality:
            quality = "best"
        if "," in quality:
            self.qualities = quality.split(",")
        else:
            self.qualities = [quality]

    def get_streams(self):
        """
        Get data streams and resolutions
        Returns: (links, resolution), Error string
        """
        try:
            # FIXME has issues if a channel is hosting another on Twitch
            links = streamlink.streams(self.query)
            res = list(links.keys())
            return links, res
        except Exception:
            # returns exceptions raised by streamlink
            raise

    def filtered_streams(self):
        """
        Filter streams according to specified quality.
        Default quality: best
        Returns: {quality: stream_url}
        """
        try:
            payload = self.get_streams()
            streams, resolutions = payload
            if not streams:
                raise ValueError
            res_str = ",".join(resolutions)
        except PluginError as pe:
            return str(pe)
        except ValueError:
            return f"Could not get the link, Streamlink couldn't read {self.query}"
        except TypeError:
            return payload

        if "best" in self.qualities:
            next((x for x in res_str if x == "best"), None)
        elif "worst" in self.qualities:
            next((x for x in res_str if x == "worst"), None)

        for q in self.qualities:
            if q not in resolutions:
                return f"Invalid quality {q}. Available qualities are: {res_str}"
        return {quality: streams[quality].url for quality in self.qualities}

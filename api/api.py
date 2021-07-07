import streamlink


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
            return (links, res)
        except Exception:
            return 1

    def filtered_streams(self):
        """
            Filter streams according to specified quality.
            Default quality: best
            Returns: {quality: stream_url}
        """
        try:
            streams, resolutions = self.get_streams()
            if not streams:
                raise ValueError
            res_str = ",".join(resolutions)
        except ValueError:
            return f"Could not get the link, Streamlink couldn't read {self.query}"

        # TODO: find a more elegant solution to deal with 'best' and 'worst'
        if "best" in self.qualities:
            self.qualities = [
                resolutions[-3:-2][0] if i == "best" else i for i in self.qualities
            ]
        if "worst" in self.qualities:
            self.qualities = [
                resolutions[1::-2][0] if i == "worst" else i for i in self.qualities
            ]

        for q in self.qualities:
            if q not in resolutions:
                return f"Invalid quality {q}. Available qualities are: {res_str}"
        return {quality: streams[quality].url for quality in self.qualities}

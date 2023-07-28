import streamlink
from streamlink import NoPluginError, PluginError
from streamlink.stream import DASHStream
import urllib.request


def get_streams(query, quality="best"):
    try:
        streams = streamlink.streams(query).items()
        if not streams:
            return "No streams found."
        for stream_quality, link in streams:
            if quality is not None and quality != stream_quality:
                continue
            if 'dailymotion.com' in query or 'dai.ly' in query:
                url = link.to_manifest_url()
                if 'https://www.dailymotion.com/cdn/live/video/' in url:
                    response = urllib.request.urlopen(url)
                    data = response.read().decode('utf-8')
                    replacements = {'live-3': 'live-0', 'live-2': 'live-0', 'live-1': 'live-0'}
                    for key in replacements:
                        if key in data:
                            l0_link = link.to_url()
                            l0_replace = l0_link.replace('live-0', replacements[key])
                            return l0_replace
                    return link.to_url()
                else:
                    return url
            if isinstance(link, DASHStream) or ("best" in stream_quality and "chunklist" in link.to_url()) or "live" in stream_quality or "http" in stream_quality:
                return link.to_url()
        else:
            return link.to_manifest_url()
    except (ValueError, NoPluginError, PluginError, Exception) as ex:
        return f"An error occurred: {ex}"
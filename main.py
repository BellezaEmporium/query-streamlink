from flask import Flask, request, redirect
import streamlink

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World !"

@app.route('/iptv-query')
def home():
  if request.args:
    if request.args.get('streaming-ip') == "" :
      return "No streaming IP found : reason = query string is empty"
    elif request.args.get('streaming-ip') != "":
      if "specific_referer" in request.args:
        streamlink.Streamlink.set_option(streamlink, "http-headers", "Referer=" + request.args.get('specific_referer'))
      print(streamlink.streams(request.args.get('streaming-ip')))
      if "quality" in request.args:
        if request.args.get("quality") == "unsure":
          stream_qualities = streamlink.streams(request.args.get('streaming-ip'))
          sorted_list = list(stream_qualities.keys())
          string_of_the_list = ', '.join(sorted_list)
          return ("Available qualities = " + string_of_the_list)
        return redirect(streamlink.streams(request.args.get('streaming-ip'))[request.args.get('quality')].url)
      elif "quality" not in request.args:
        return redirect(streamlink.streams(request.args.get('streaming-ip'))['best'].url)
  else:
    return "No streaming IP found: reason = no URL provided"

if __name__ == '__main__':
  app.run(
    host='0.0.0.0',
    debug=True,
    port=8888
  )
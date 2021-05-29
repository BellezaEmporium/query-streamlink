from flask import Flask, request, redirect
import streamlink
import validators
import sys

app = Flask(__name__)

@app.route("/")
def index():
    return "This program permits you to get direct access to streams by using Streamlink. Alternative link : https://iptv--iptv.repl.co/streamlink?url=*insert url*. Enjoy ! LaneSh4d0w."

@app.route('/iptv-query')
def home():
  if request.args:
    if request.args.get('streaming-ip') == "" :
      return "No streaming IP found : reason = query string is empty"
    elif request.args.get('streaming-ip') != "":
      valid=validators.url(request.args.get('streaming-ip'));
      if valid == True:
        if "quality" in request.args:
          if request.args.get("quality") == "unsure":
            try:
              stream_qualities = streamlink.streams(request.args.get('streaming-ip'))
            except:
              return ("Could not get the link = ", sys.exc_info())
            sorted_list = list(stream_qualities.keys())
            string_of_the_list = ', '.join(sorted_list)
            return ("Available qualities = " + string_of_the_list)
            try:
              url = streamlink.streams(request.args.get('streaming-ip'))[request.args.get('quality')].url
              return redirect(url)
            except:
              return ("Could not get the stream data = ", sys.exc_info())
        elif "quality" not in request.args:
          try:
              url = streamlink.streams(request.args.get('streaming-ip'))['best'].url
              return redirect(url)
          except:
              return ("Could not get the stream data = ", sys.exc_info())
      else:
        return "The URL you've entered is not valid."
  else:
    return "No streaming IP found: reason = no URL provided"

if __name__ == '__main__':
  app.run(
    host='0.0.0.0',
    debug=True,
    port=8888
  )
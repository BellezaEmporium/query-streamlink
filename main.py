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
    else:
      valid=validators.url(request.args.get('streaming-ip'));
      if valid == True:
        if "quality" in request.args:
          if request.args.get("quality") == "unsure":
            try:
              stream_qualities = streamlink.streams(request.args.get('streaming-ip'))
              sorted_list = list(stream_qualities.keys())
              string_of_the_list = ', '.join(sorted_list)
              return ("Available qualities = " + string_of_the_list)
            except:
              return ("Could not get the link, Streamlink couldn't read ", request.args.get('streaming-ip'))
          else:    
            return redirect(streamlink.streams(request.args.get('streaming-ip'))[request.args.get('quality')].url)
        else:
          return redirect(streamlink.streams(request.args.get('streaming-ip'))['best'].url)
      else:
        return "The URL you've entered is not valid."
  else:
    return "You provided nothing to me."

if __name__ == '__main__':
  app.run(
    host='0.0.0.0',
    port=8888
  )
import os
import random
from flask import Flask, Blueprint, render_template, make_response, request, send_from_directory
#from flask_assets import Environment, Bundle
from hashlib import md5


app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/favicon.ico")
def favicon():
  return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


routes = Blueprint("routes", __name__)

sv_messages = {}
en_messages = {}

all_messages = {}


current_file_path = os.path.dirname(os.path.abspath(__file__))
message_files = [ 
  {"lang":"sv", "file_name": "/messages/sv_messages.txt"}, 
  {"lang":"en", "file_name": "/messages/en_messages.txt"} 
  ]



for num, mess_file in enumerate(message_files, start=0):
  with open(current_file_path  + mess_file['file_name'], 'r',encoding='utf-8') as mess_input:
    temp = {}
    for commit_message in mess_input.readlines():
      all_messages[md5(commit_message.encode('utf-8')).hexdigest()] = {"lang": mess_file['lang'], "message": commit_message}

def get_message_from_hash(mess_hash):
  mess = all_messages[mess_hash]
  return mess


def get_random_message(lang="en"):
  message = {"lang":""}
  while message['lang'] != lang:
    message_hash = random.choice(list(all_messages.keys()))
    message = get_message_from_hash(message_hash)
  return message, message_hash




@routes.route("/<message_hash>")
@routes.route("/")
def get_sv_message(message_hash=None):
  mode = request.args.get("mode", default=None)
  lang = request.args.get("lang", default="en")

  if message_hash is None:
    mess = get_random_message(lang)
    message = mess[0]
    message_hash = mess[1]
    

  else:
    message = get_message_from_hash(message_hash)

  if mode == "raw":
    res =  make_response(message['message'])
    res.mimetype = "text/plain"
    return res
    
  return render_template("message.html", message=message['message'], hash=message_hash)




app.register_blueprint(routes)
import eventlet
import os

eventlet.monkey_patch()
from flask import Flask, render_template
from flask_socketio import SocketIO
from config import SETTINGS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
sio = SocketIO(app)


@app.route('/')
def index():
  return render_template('index.html')


@sio.on('connect')
def connect():
  print('connected')


@sio.on('send_chat_message')
def message(data):
  sio.emit('chat_message', data)


@sio.on('disconnect')
def disconnect():
  print('disconnect')


if __name__ == '__main__':
  app.debug = True
  sio.run(app, host=os.environ.get('HOST') or SETTINGS['app']['host'], port=os.environ.get('PORT') or SETTINGS['app']['port'])

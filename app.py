import eventlet

eventlet.monkey_patch()
from flask import Flask, render_template
from flask_socketio import SocketIO
from config import SETTINGS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
sio = SocketIO(app)


@app.route('/')
def index():
  socket_url = str(SETTINGS['app']['schema']) + str(SETTINGS['app']['host']) + ':' + str(SETTINGS['app']['port'])
  return render_template('index.html', socket_url=socket_url)


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
  sio.run(app, host=SETTINGS['app']['host'], port=SETTINGS['app']['port'])

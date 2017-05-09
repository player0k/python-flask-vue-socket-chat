import socketio
import eventlet
from flask import Flask, render_template

sio = socketio.Server()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@sio.on('connect')
def connect(sid, environ):
    print('connect ', sid)

@sio.on('chat message')
def message(sid, data):
    print('message ', data)
    sio.emit('chat message', data)    

@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    app.debug = True
    app = socketio.Middleware(sio, app)

    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 3000)), app)
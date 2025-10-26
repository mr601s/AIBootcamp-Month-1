"""
ChatFlow - Real-time chat Application
Backend: flask + Socket.10
"""

from flask import Flask, render_template, request, send_from_directory
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from datetime import datetime
import os

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Enable CORS
CORS(app)

# Initialize Socket.IO with CORS allowed
socketio = SocketIO(app, cors_allowed_origins='*')

# Store connected users (in production, use Redis or database)
connected_users = {}

# ============================================================================================================
# HTTP ROUTES (Traditional Flask)
# ============================================================================================================

@app.route('/')
def index():
    """health check endpoint"""
    return {
        'status': 'running',
        'app': 'ShatFlow',
        'version': '1.0',
        'websocket': 'active'
    }

# ============================================================================================================
# WEBSOCKET EVENTS (The New Stuff!)
# ============================================================================================================

@socketio.on('connect')
def handle_connect():
    """
    Called when a client connects
    This is AUTOMATIC - happens when browser opens connection
    """
    print(f'🟢 Client connected: {request.sid}')

    # Send welcome message to THIS client only
    emit('message', {
        'type': 'system',
        'text': 'Connected to ChatFlow! Welcome!',
        'timestamp': datetime.now().isoformat()
    })

@socketio.on('disconnect')
def handle_disconnect():
    """
    Called when a client disconnects
    Also AUTOMATIC - happens when browser closes
    """
    print(f'🔴 Client disconnected: {request.sid}')

@socketio.on('user_join')
def handle_user_join(data):
    """
    Called when a user enters their username
    'data' comes from the client
    """
    username = data.get('username', 'Anonymous')

    # Store this user
    connected_users[request.sid] = username

    print(f'👤 User joined: {username} (SID: {request.sid})')

    # Broadcast to ALL clients (including sender)
    emit('user_joined', {
        'username': username,
        'timestamp': datetime.now().isoformat(),
        'user_count': len(connected_users)
    }, broadcast=True)

@socketio.on('send_message')
def handle_message(data):
    """
    Called when user sends a message
    THIS IS THE CORE FEATURE!
    """
    username = connected_users.get(request.sid, 'Anonymous')
    message_text = data.get('message', '')

    print(f'💬 Message from {username}: {message_text}')

    # Create message object
    message = {
        'type': 'user',
        'username': username,
        'text': message_text,
        'timestamp': datetime.now().isoformat()
    }

    # Broadcast to ALL clients
    emit('new_message', message, broadcast=True)

# ============================================================================================================
# Run server
# ============================================================================================================

if __name__ == '__main__':
    print('🚀 ChatFlow Backend Starting...')
    print('📍 Running on http://localhost:5000')
    print('🔌 WebSocket ready for connections')
    print('💬 Real-time chat enabled!')
    print('')

    # Run with eventlet for Websocket support
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
"""
ChatFlow - Real-Time Chat Application with Authentication
Backend: Flask + Socket.IO + User Authentication
"""

from flask import Flask, request, jsonify, session
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from datetime import datetime
import os

# Import our user manager
from user_management import UserManager

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'
app.config['SESSION_TYPE'] = 'filesystem'

# Enable CORS
CORS(app, supports_credentials=True)

# Initialize Socket.IO with CORS allowed
socketio = SocketIO(app, cors_allowed_origins="*", manage_session=False)

# Initialize User Manager
user_manager = UserManager()

# Store connected users: {session_id: username}
connected_users = {}

# ========================================
# HTTP ROUTES (Authentication)
# ========================================

@app.route('/')
def index():
    """Health check endpoint"""
    return {
        'status': 'running',
        'app': 'ChatFlow',
        'version': '2.0',
        'features': ['authentication', 'websocket', 'real-time']
    }

@app.route('/api/register', methods=['POST'])
def register():
    """Register new user"""
    try:
        data = request.json
        username = data.get('username', '').strip()
        password = data.get('password', '')
        
        success, message = user_manager.register_user(username, password)
        
        if success:
            return jsonify({
                'success': True,
                'message': message
            }), 201
        else:
            return jsonify({
                'success': False,
                'message': message
            }), 400
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@app.route('/api/login', methods=['POST'])
def login():
    """Login user"""
    try:
        data = request.json
        username = data.get('username', '').strip()
        password = data.get('password', '')
        
        success, message, user_data = user_manager.login_user(username, password)
        
        if success:
            return jsonify({
                'success': True,
                'message': message,
                'user': user_data
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': message
            }), 401
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@app.route('/api/user/<username>', methods=['GET'])
def get_user_profile(username):
    """Get user profile"""
    user_data = user_manager.get_user(username)
    
    if user_data:
        return jsonify({
            'success': True,
            'user': user_data
        }), 200
    else:
        return jsonify({
            'success': False,
            'message': 'User not found'
        }), 404

# ========================================
# WEBSOCKET EVENTS
# ========================================

@socketio.on('connect')
def handle_connect():
    """Called when a client connects"""
    print(f'🟢 Client connected: {request.sid}')
    
    emit('message', {
        'type': 'system',
        'text': 'Connected to ChatFlow! Please login or register.',
        'timestamp': datetime.now().isoformat()
    })

@socketio.on('disconnect')
def handle_disconnect():
    """Called when a client disconnects"""
    print(f'🔴 Client disconnected: {request.sid}')
    
    # If user was logged in, notify others
    if request.sid in connected_users:
        username = connected_users[request.sid]
        del connected_users[request.sid]
        
        emit('user_left', {
            'username': username,
            'timestamp': datetime.now().isoformat(),
            'user_count': len(connected_users)
        }, broadcast=True)

@socketio.on('user_login')
def handle_user_login(data):
    """Called when authenticated user joins chat"""
    username = data.get('username')
    
    # Store this connection
    connected_users[request.sid] = username
    
    # Get user data
    user_data = user_manager.get_user(username)
    
    print(f'👤 User logged in to chat: {username}')
    
    # Broadcast to ALL clients
    emit('user_joined', {
        'username': username,
        'avatar_color': user_data['avatar_color'],
        'timestamp': datetime.now().isoformat(),
        'user_count': len(connected_users)
    }, broadcast=True)

@socketio.on('send_message')
def handle_message(data):
    """Called when user sends a message"""
    # Get username from connected users
    username = connected_users.get(request.sid, 'Anonymous')
    message_text = data.get('message', '')
    
    if not message_text.strip():
        return
    
    print(f'💬 Message from {username}: {message_text}')
    
    # Get user data for avatar color
    user_data = user_manager.get_user(username)
    
    # Increment message count
    user_manager.increment_message_count(username)
    
    # Create message object
    message = {
        'type': 'user',
        'username': username,
        'text': message_text,
        'avatar_color': user_data['avatar_color'] if user_data else '#667eea',
        'timestamp': datetime.now().isoformat()
    }
    
    # Broadcast to ALL clients
    emit('new_message', message, broadcast=True)

@socketio.on('get_online_users')
def handle_get_online_users():
    """Get list of currently online users"""
    online_users = []
    
    for sid, username in connected_users.items():
        user_data = user_manager.get_user(username)
        if user_data:
            online_users.append({
                'username': username,
                'avatar_color': user_data['avatar_color']
            })
    
    emit('online_users_list', {
        'users': online_users,
        'count': len(online_users)
    })

# ========================================
# RUN SERVER
# ========================================

if __name__ == '__main__':
    print('🚀 ChatFlow Backend Starting...')
    print('📍 Running on http://localhost:5000')
    print('🔌 WebSocket ready for connections')
    print('🔐 Authentication enabled')
    print('💬 Real-time chat enabled!')
    print('')
    
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
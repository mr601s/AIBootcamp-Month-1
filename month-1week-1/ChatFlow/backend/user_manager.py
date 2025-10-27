"""
User Authentication and Management
Handles user registration, login, and session management
"""

import json
import os
import bcrypt
from datetime import datetime

class UserManager:
    def __init__(self, users_file='data/users.json'):
        """Initialize user manager with file storage"""
        self.users_file = users_file
        self.ensure_users_file()

    def ensure_users_file(self):
        """Create users file if it doesn't exist"""
        os.makedirs(os.path.dirname(self.users_file), exist_ok=True)
        if not os.path.exists(self.users_file):
            with open(self.users_file, 'w') as f:
                json.dump({}, f)

    def load_users(self):
        """Load all users from file"""
        try:
            with open(self.users_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
        
    def save_users(self, users):
        """Save users to file"""
        with open(self.users_file, 'w') as f:
            json.dump(users, f, indent=2)

    def hash_password(self, password):
        """Hash password using bcrypt"""
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')
    
    def verify_password(self, password, hashed_password):
        """Verify password against hash"""
        return bcrypt.checkpw(
            password.encode('utf-8'), 
            hashed_password.encode('utf-8')
        )
    
    def register_user(self, username, password):
        """
        Register a new user
        Returns: (success: bool, message: str)
        """
        users = self.load_users()
        
        # Validation
        if len(username) < 3:
            return False, "Username must be at least 3 characters"
        
        if len(password) < 6:
            return False, "Password must be at least 6 characters"
        
        if username in users:
            return False, "Username already exists"
        
        # Create user
        users[username] = {
            'username': username,
            'password_hash': self.hash_password(password),
            'created_at': datetime.now().isoformat(),
            'avatar_color': self.generate_avatar_color(username),
            'total_messages': 0
        }
        
        self.save_users(users)
        return True, "Registration successful!"
    
    def login_user(self, username, password):
        """
        Authenticate user login
        Returns: (success: bool, message: str, user_data: dict)
        """
        users = self.load_users()
        
        if username not in users:
            return False, "Invalid username or password", None
        
        user = users[username]
        
        if not self.verify_password(password, user['password_hash']):
            return False, "Invalid username or password", None
        
        # Don't send password hash to client
        safe_user_data = {
            'username': user['username'],
            'created_at': user['created_at'],
            'avatar_color': user['avatar_color'],
            'total_messages': user['total_messages']
        }
        
        return True, "Login successful!", safe_user_data
    
    def get_user(self, username):
        """Get user data (without password hash)"""
        users = self.load_users()
        
        if username not in users:
            return None
        
        user = users[username]
        return {
            'username': user['username'],
            'created_at': user['created_at'],
            'avatar_color': user['avatar_color'],
            'total_messages': user['total_messages']
        }
    
    def increment_message_count(self, username):
        """Increment user's message count"""
        users = self.load_users()
        
        if username in users:
            users[username]['total_messages'] += 1
            self.save_users(users)
    
    def generate_avatar_color(self, username):
        """Generate consistent color for user avatar"""
        colors = [
            '#667eea', '#f56565', '#48bb78', '#ed8936',
            '#4299e1', '#9f7aea', '#ed64a6', '#38b2ac'
        ]
        # Use hash of username to pick consistent color
        index = sum(ord(c) for c in username) % len(colors)
        return colors[index]

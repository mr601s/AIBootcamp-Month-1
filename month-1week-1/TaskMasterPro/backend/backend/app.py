"""
TaskMasterPro Backend API
Flask REST API for task management
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS so frontend can talk to backend

# File paths
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
TASKS_FILE = os.path.join(DATA_DIR, 'tasks.json')

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# ========================================
# HELPER FUNCTIONS
# ========================================

def load_tasks():
    """Load tasks from JSON file"""
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

def save_tasks(tasks):
    """Save tasks to JSON file"""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def calculate_stats(tasks):
    """Calculate task statistics"""
    total = len(tasks)
    completed = len([t for t in tasks if t.get('completed', False)])
    active = total - completed
    completion_rate = int((completed / total * 100)) if total > 0 else 0
    
    return {
        'total': total,
        'completed': completed,
        'active': active,
        'completion_rate': completion_rate
    }

# ========================================
# API ENDPOINTS
# ========================================

@app.route('/')
def home():
    """Health check endpoint"""
    return jsonify({
        'status': 'running',
        'message': 'TaskMasterPro API is online',
        'version': '1.0'
    })

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    tasks = load_tasks()
    return jsonify({'tasks': tasks})

@app.route('/tasks', methods=['POST'])
def add_task():
    """Add new task"""
    try:
        data = request.json
        tasks = load_tasks()
        
        # Create new task
        new_task = {
            'id': str(datetime.now().timestamp()),  # Unique ID
            'title': data.get('title', ''),
            'category': data.get('category', 'personal'),
            'priority': data.get('priority', 'medium'),
            'completed': False,
            'created_at': datetime.now().isoformat()
        }
        
        # Add to list and save
        tasks.append(new_task)
        save_tasks(tasks)
        
        return jsonify({
            'message': 'Task added successfully',
            'task': new_task
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/tasks/<task_id>/complete', methods=['PUT'])
def complete_task(task_id):
    """Mark task as complete"""
    try:
        tasks = load_tasks()
        
        # Find and update task
        for task in tasks:
            if task['id'] == task_id:
                task['completed'] = True
                task['completed_at'] = datetime.now().isoformat()
                break
        
        save_tasks(tasks)
        return jsonify({'message': 'Task completed'})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task"""
    try:
        tasks = load_tasks()
        tasks = [t for t in tasks if t['id'] != task_id]
        save_tasks(tasks)
        
        return jsonify({'message': 'Task deleted'})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/stats', methods=['GET'])
def get_stats():
    """Get task statistics"""
    tasks = load_tasks()
    stats = calculate_stats(tasks)
    return jsonify(stats)

@app.route('/weather', methods=['GET'])
def get_weather():
    """Get weather data (simplified)"""
    return jsonify({
        'temperature': '72°F',
        'condition': 'Partly Cloudy',
        'location': 'Bristol, VA',
        'advice': 'Great day for productivity!'
    })

# ========================================
# RUN SERVER
# ========================================

if __name__ == '__main__':
    print('🚀 TaskMasterPro Backend Starting...')
    print('📍 Running on http://localhost:5000')
    print('🔌 Frontend can connect now!')
    app.run(debug=True, port=5000)
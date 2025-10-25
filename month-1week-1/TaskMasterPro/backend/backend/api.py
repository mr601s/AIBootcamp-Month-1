"""
Flask API for TaskMasterPro
RESTful endpoints for web frontend
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import sys
import os

# Add backend directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from task_manager import TaskManager
from task_types import WorkTask, PersonalTask, ShoppingTask
from decorators import AppDecorators, get_activity_log, get_performance_stats
from weather_service import WeatherService

#Initialize Flask app
app = Flask(__name__)
CORS(app)  # enable CORS for frontend


# Initialize services
task_manager = TaskManager()
weather_service = WeatherService()

# ===========================================================================================================
# TASK ENDPOINTS
# ===========================================================================================================

@app.route('/api/tasks', methods=['GET'])
@AppDecorators.timer
def get_tasks():
    """Get all tasks"""
    tasks_data = []
    for task in task_manager.tasks:
        tasks_data.append({
            'title': task.title,
            'description': task.description,
            'priority': task.priority,
            'completed': task.completed
        })

    return jsonify({
        'success': True,
        'tasks': tasks_data,
        'count': len(tasks_data)
    })

@app.route('/api/tasks', methods=['POST'])
@AppDecorators.timer
@AppDecorators.audit_log('API_CREATE_TASK')
def create_task():
    """Create a new task"""
    data = request.json


    #Validate required fields
    if not data.get('title'):
        return jsonify({'success': False, 'message': 'Title is required'}), 400
    
    #Determine task type and create
    category = data.get('category', 'General')

    if category == 'Work':
        task = WorkTask(
            title=data['title'],
            description=data.get('description', ''),
            priority=data.get('priority', 'Medium'),
            project=data.get('project', 'General')
        )
    elif category == 'Personal':
        task = PersonalTask(
            title=data['title'],
            description=data.get('description', ''),
            priority=data.get('priority', 'Medium'),
            location=data.get('location', 'Home')
        )
    elif category == 'Shopping':
        task = ShoppingTask(
            title=data['title'],
            description=data.get('description', ''),
            priority=data.get('priority', 'Medium'),
            store=data.get('store', 'General')
        )
    else:
        # Generic task
        from task import Task
        task = Task(
            title=data['title'],
            description=data.get('description', ''),
            priority=data.get('priority', 'Medium')
        )
        task.category = category

    # Add to manager
    task_manager.add_task(task)

    return jsonify({
        'success': True,
        'message': 'task created successfully'
    }), 201

@app.route('/api/tasks/<int:index>/complete', methods=['PUT'])
@AppDecorators.timer
@AppDecorators.audit_log('API_COMPLETE_TASK')
def complete_task(task_id):
    """Mark a task as complete"""
    success = task_manager.complete_task(task_id)

    if success:
        return jsonify({
            'success': True,
            'message': 'Task marked as complete'
        })
    else:
        return jsonify({
            'success': False,
            'message': 'Invalid task index'
        }), 404
    
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
@AppDecorators.timer
@AppDecorators.audit_log('API_DELETE_TASK')
def delete_task(task_id):
    """Delete a task"""
    success = task_manager.delete_task(task_id)

    if success:
        return jsonify({
            'success': True,
            'message': 'Task deleted successfully'
        })
    else:
        return jsonify({
            'success': False,
            'message': 'Invalid task index'
        }), 404
    
# ===========================================================================================================
# Statistics Endpoints
# ===========================================================================================================

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get task statistics"""
    stats = task_manager.get_statistics()

    return jsonify({
        'success': True,
        'statistics': stats
    })

@app.route('/api/stats/priority', methods=['GET'])
@AppDecorators.timer
def get_priority_breakdown():
    """Get tasks by priority"""
    breakdown = {
        'low': len(task_manager.get_tasks_by_priority('Low')),
        'medium': len(task_manager.get_tasks_by_priority('Medium')),
        'high': len(task_manager.get_tasks_by_priority('High'))
    }

    for task in task_manager.tasks:
        breakdown[task.priority] = breakdown.get(task.priority, 0) + 1

        return jsonify({
            'success': True,
            'breakdown': breakdown 
        })
    
@app.route('/api/stats/category', methods=['GET'])
@AppDecorators.timer
def get_category_breakdown():
    """Get tasks by category"""
    breakdown = {}

    for task in task_manager.tasks:
        category = task.category
        breakdown[category] = breakdown.get(category, 0) + 1

    return jsonify({
        'success': True,
        'breakdown': breakdown
    })

# ===========================================================================================================
# Weather Endpoints
# ===========================================================================================================

@app.route('/api/weather/<city>', methods=['GET'])
@AppDecorators.timer
def get_weather(city):
    """Get weather for a city"""
    weather_data = weather_service.get_weather(city)

    if weather_data:
        return jsonify({
            'success': True,
            'weather': weather_data
        })
    else:
        return jsonify({
            'success': False,
            'message': 'Unable to fetch weather data'
        }), 500
    
@app.route('/api/weather/<city>/advice', methods=['GET'])
@AppDecorators.timer
def get_weather_advice(city):
    """Get task advice based on weather"""
    advice = weather_service.get_weather_advice(city)

    return jsonify({
        'success': True,
        'advice': advice
    })

# ===========================================================================================================
# System Endpoints
# ===========================================================================================================

@app.route('/api/logs/activity', methods=['GET'])
@AppDecorators.timer
def get_logs():
    """Get activity logs"""
    logs = get_activity_log()

    return jsonify({
        'success': True,
        'logs': logs
    })

@app.route('/api/stats/performance', methods=['GET'])
@AppDecorators.timer
def get_performance():
    """Get performance statistics"""
    stats = get_performance_stats()

    return jsonify({
        'success': True,
        'performance': stats
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'success': True,
        'message': 'API is healthy'
    })

# ===========================================================================================================
# ERROR HANDLING
# ===========================================================================================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'success': False,
        'message': 'Resource not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'success': False,
        'message': 'Internal server error'
    }), 500

# ===========================================================================================================
# MAIN
# ===========================================================================================================

if __name__ == '__main__':
    print('='*60)
    print(''*15 + 'TASKMASTERPRO API')
    print('='*60)   
    print("\n🚀 Starting server...")
    print("📍 API running at: http://localhost:5000")
    print("📚 API endpoints:")
    print("   GET    /api/health          - Health check")
    print("   GET    /api/tasks           - Get all tasks")
    print("   POST   /api/tasks           - Create task")
    print("   PUT    /api/tasks/:id/complete - Complete task")
    print("   DELETE /api/tasks/:id       - Delete task")
    print("   GET    /api/stats           - Get statistics")
    print("   GET    /api/weather/:city   - Get weather")
    print("   GET    /api/logs/activity   - Get activity logs")
    print("   GET    /api/logs/performance - Get performance stats")
    print("\n✅ Server ready! Open http://localhost:5000/api/health to test")
    print("="*60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
/**
 * TASKMASTERPRO - FRONTEND JAVASCRIPT
 * Day 16 Bootcamp Project
 * Connects to Flask backend API
 */

// ========================================
// CONFIGURATION & STATE
// ========================================

// API Configuration - Change this to your backend URL
const API_BASE_URL = 'http://localhost:5000';

// Application State - Like a Python class with attributes
const AppState = {
    tasks: [],           // All tasks from backend
    currentFilter: 'all', // Current filter selection
    stats: {
        total: 0,
        completed: 0,
        active: 0,
        completionRate: 0
    }
};

// ========================================
// API FUNCTIONS - Backend Communication
// ========================================

/**
 * Fetch all tasks from backend
 * Python equivalent: requests.get(url)
 */
async function fetchTasks() {
    try {
        const response = await fetch(`${API_BASE_URL}/tasks`);
        if (!response.ok) throw new Error('Failed to fetch tasks');
        const data = await response.json();
        AppState.tasks = data.tasks || [];
        return data.tasks || [];
    } catch (error) {
        console.error('Error fetching tasks:', error);
        showNotification('Failed to load tasks', 'error');
        return [];
    }
}

/**
 * Add new task to backend
 * Python equivalent: requests.post(url, json=data)
 */
async function addTask(taskData) {
    try {
        const response = await fetch(`${API_BASE_URL}/tasks`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(taskData)
        });
        
        if (!response.ok) throw new Error('Failed to add task');
        const data = await response.json();
        showNotification('Task added successfully!', 'success');
        return data;
    } catch (error) {
        console.error('Error adding task:', error);
        showNotification('Failed to add task', 'error');
        throw error;
    }
}

/**
 * Complete a task
 * Python equivalent: requests.put(url)
 */
async function completeTask(taskId) {
    try {
        const response = await fetch(`${API_BASE_URL}/tasks/${taskId}/complete`, {
            method: 'PUT'
        });
        
        if (!response.ok) throw new Error('Failed to complete task');
        showNotification('Task completed!', 'success');
        return await response.json();
    } catch (error) {
        console.error('Error completing task:', error);
        showNotification('Failed to complete task', 'error');
        throw error;
    }
}

/**
 * Delete a task
 * Python equivalent: requests.delete(url)
 */
async function deleteTask(taskId) {
    try {
        const response = await fetch(`${API_BASE_URL}/tasks/${taskId}`, {
            method: 'DELETE'
        });
        
        if (!response.ok) throw new Error('Failed to delete task');
        showNotification('Task deleted!', 'success');
        return await response.json();
    } catch (error) {
        console.error('Error deleting task:', error);
        showNotification('Failed to delete task', 'error');
        throw error;
    }
}

/**
 * Fetch statistics from backend
 */
async function fetchStats() {
    try {
        const response = await fetch(`${API_BASE_URL}/stats`);
        if (!response.ok) throw new Error('Failed to fetch stats');
        const data = await response.json();
        AppState.stats = data;
        return data;
    } catch (error) {
        console.error('Error fetching stats:', error);
        return AppState.stats;
    }
}

/**
 * Fetch weather data
 */
async function fetchWeather() {
    try {
        const response = await fetch(`${API_BASE_URL}/weather`);
        if (!response.ok) throw new Error('Failed to fetch weather');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching weather:', error);
        return null;
    }
}

// ========================================
// UI UPDATE FUNCTIONS - DOM Manipulation
// ========================================

/**
 * Render tasks to the DOM
 * Python equivalent: Building HTML string and inserting it
 */
function renderTasks(tasks = AppState.tasks) {
    const taskList = document.getElementById('taskList');
    
    // Filter tasks based on current filter
    let filteredTasks = tasks;
    if (AppState.currentFilter !== 'all') {
        if (AppState.currentFilter === 'completed') {
            filteredTasks = tasks.filter(task => task.completed);
        } else {
            filteredTasks = tasks.filter(task => 
                task.category === AppState.currentFilter && !task.completed
            );
        }
    }
    
    // If no tasks, show empty state
    if (filteredTasks.length === 0) {
        taskList.innerHTML = `
            <div class="empty-state">
                <h3>No tasks found</h3>
                <p>Add a task above to get started!</p>
            </div>
        `;
        return;
    }
    
    // Build task HTML - like Python f-strings but for HTML
    taskList.innerHTML = filteredTasks.map(task => `
        <div class="task-item ${task.completed ? 'completed' : ''}" data-task-id="${task.id}">
            <div class="task-checkbox" onclick="handleCompleteTask('${task.id}')"></div>
            
            <div class="task-content">
                <div class="task-title">${escapeHtml(task.title)}</div>
                <div class="task-meta">
                    <span class="task-category">${getCategoryIcon(task.category)} ${task.category}</span>
                    <span class="task-priority ${task.priority}">${getPriorityIcon(task.priority)} ${task.priority}</span>
                    <span class="task-date">${formatDate(task.created_at)}</span>
                </div>
            </div>
            
            <div class="task-actions">
                <button class="task-btn delete" onclick="handleDeleteTask('${task.id}')" title="Delete task">
                    🗑️
                </button>
            </div>
        </div>
    `).join('');
}

/**
 * Update statistics display
 */
function updateStats(stats = AppState.stats) {
    document.getElementById('totalTasks').textContent = stats.total || 0;
    document.getElementById('completedTasks').textContent = stats.completed || 0;
    document.getElementById('activeTasks').textContent = stats.active || 0;
    document.getElementById('completionRate').textContent = `${stats.completion_rate || 0}%`;
}

/**
 * Update weather widget
 */
function updateWeather(weatherData) {
    const weatherWidget = document.getElementById('weatherWidget');
    
    if (!weatherData || weatherData.error) {
        weatherWidget.innerHTML = '<span class="weather-temp">Weather unavailable</span>';
        return;
    }
    
    const { temperature, condition, location } = weatherData;
    weatherWidget.innerHTML = `
        <span class="weather-temp">
            ${getWeatherIcon(condition)} ${temperature} - ${condition} in ${location}
        </span>
    `;
}

// ========================================
// EVENT HANDLERS - User Interactions
// ========================================

/**
 * Handle form submission for new task
 */
async function handleAddTask(event) {
    event.preventDefault(); // Prevent page reload
    
    // Get form values - like input() in Python
    const title = document.getElementById('taskTitle').value.trim();
    const category = document.getElementById('taskCategory').value;
    const priority = document.getElementById('taskPriority').value;
    
    // Validation
    if (!title || !category || !priority) {
        showNotification('Please fill in all fields', 'error');
        return;
    }
    
    // Create task object
    const taskData = {
        title: title,
        category: category,
        priority: priority
    };
    
    try {
        // Add to backend
        await addTask(taskData);
        
        // Refresh data
        await refreshData();
        
        // Clear form
        document.getElementById('taskForm').reset();
        
    } catch (error) {
        console.error('Failed to add task:', error);
    }
}

/**
 * Handle task completion
 */
async function handleCompleteTask(taskId) {
    try {
        await completeTask(taskId);
        await refreshData();
    } catch (error) {
        console.error('Failed to complete task:', error);
    }
}

/**
 * Handle task deletion
 */
async function handleDeleteTask(taskId) {
    // Confirm deletion - like Python's input() for confirmation
    if (!confirm('Are you sure you want to delete this task?')) {
        return;
    }
    
    try {
        await deleteTask(taskId);
        await refreshData();
    } catch (error) {
        console.error('Failed to delete task:', error);
    }
}

/**
 * Handle filter button clicks
 */
function handleFilterClick(filter) {
    // Update state
    AppState.currentFilter = filter;
    
    // Update UI - remove 'active' from all, add to clicked
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    event.target.classList.add('active');
    
    // Re-render tasks with new filter
    renderTasks();
}

// ========================================
// UTILITY FUNCTIONS - Helpers
// ========================================

/**
 * Refresh all data from backend
 */
async function refreshData() {
    try {
        // Fetch all data in parallel - like asyncio.gather() in Python
        const [tasks, stats] = await Promise.all([
            fetchTasks(),
            fetchStats()
        ]);
        
        // Update UI
        renderTasks(tasks);
        updateStats(stats);
        
    } catch (error) {
        console.error('Error refreshing data:', error);
    }
}

/**
 * Show notification to user
 */
function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem 2rem;
        background: ${type === 'success' ? '#10b981' : '#ef4444'};
        color: white;
        border-radius: 0.5rem;
        box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1);
        z-index: 1000;
        animation: slideIn 0.3s ease;
    `;
    
    document.body.appendChild(notification);
    
    // Remove after 3 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

/**
 * Escape HTML to prevent XSS attacks
 */
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

/**
 * Get category icon
 */
function getCategoryIcon(category) {
    const icons = {
        work: '💼',
        personal: '🏠',
        shopping: '🛒'
    };
    return icons[category] || '📝';
}

/**
 * Get priority icon
 */
function getPriorityIcon(priority) {
    const icons = {
        high: '🔴',
        medium: '🟡',
        low: '🟢'
    };
    return icons[priority] || '⚪';
}

/**
 * Get weather icon
 */
function getWeatherIcon(condition) {
    const lowerCondition = condition.toLowerCase();
    if (lowerCondition.includes('sun') || lowerCondition.includes('clear')) return '☀️';
    if (lowerCondition.includes('cloud')) return '☁️';
    if (lowerCondition.includes('rain')) return '🌧️';
    if (lowerCondition.includes('snow')) return '❄️';
    return '🌤️';
}

/**
 * Format date for display
 */
function formatDate(dateString) {
    const date = new Date(dateString);
    const now = new Date();
    const diffTime = Math.abs(now - date);
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    
    if (diffDays === 0) return 'Today';
    if (diffDays === 1) return 'Yesterday';
    if (diffDays < 7) return `${diffDays} days ago`;
    return date.toLocaleDateString();
}

// ========================================
// INITIALIZATION - App Startup
// ========================================

/**
 * Initialize the application
 * This runs when the page loads
 */
async function initApp() {
    console.log('🚀 TaskMasterPro initializing...');
    
    // Set up event listeners
    setupEventListeners();
    
    // Load initial data
    await refreshData();
    
    // Load weather
    const weather = await fetchWeather();
    if (weather) updateWeather(weather);
    
    console.log('✅ TaskMasterPro ready!');
}

/**
 * Set up all event listeners
 */
function setupEventListeners() {
    // Form submission
    const taskForm = document.getElementById('taskForm');
    taskForm.addEventListener('submit', handleAddTask);
    
    // Filter buttons - Event delegation pattern from Day 6!
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const filter = e.target.dataset.filter;
            handleFilterClick(filter);
        });
    });
    
    console.log('✅ Event listeners attached');
}

// ========================================
// START THE APP
// ========================================

// Wait for DOM to be ready, then initialize
// This is like Python's if __name__ == '__main__':
document.addEventListener('DOMContentLoaded', initApp);

console.log('📝 TaskMasterPro loaded, waiting for DOM...');
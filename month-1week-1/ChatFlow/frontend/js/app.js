/**
 * CHATFLOW 2.0 - REAL-TIME CHAT WITH AUTHENTICATION
 * Frontend: Socket.IO Client + Authentication + Chat Logic + Emojis
 */

// ========================================
// CONFIGURATION & STATE
// ========================================

// API Configuration
const API_BASE_URL = 'http://localhost:5000';

// Socket.IO connection (will connect after login)
let socket = null;

// Application State
const AppState = {
    username: null,
    userData: null,
    isAuthenticated: false,
    isConnected: false,
    messages: [],
    onlineUsers: []
};

// DOM Elements - Auth Screen
const authScreen = document.getElementById('authScreen');
const chatScreen = document.getElementById('chatScreen');
const loginTab = document.getElementById('loginTab');
const registerTab = document.getElementById('registerTab');
const loginForm = document.getElementById('loginForm');
const registerForm = document.getElementById('registerForm');

// DOM Elements - Login Form
const loginUsername = document.getElementById('loginUsername');
const loginPassword = document.getElementById('loginPassword');
const loginButton = document.getElementById('loginButton');
const loginError = document.getElementById('loginError');

// DOM Elements - Register Form
const registerUsername = document.getElementById('registerUsername');
const registerPassword = document.getElementById('registerPassword');
const registerConfirmPassword = document.getElementById('registerConfirmPassword');
const registerButton = document.getElementById('registerButton');
const registerError = document.getElementById('registerError');

// DOM Elements - Chat Screen
const currentUsername = document.getElementById('currentUsername');
const currentUserAvatar = document.getElementById('currentUserAvatar');
const userCount = document.getElementById('userCount');
const onlineUsersList = document.getElementById('onlineUsersList');
const messagesContainer = document.getElementById('messagesContainer');
const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');
const notificationToast = document.getElementById('notificationToast');
const notificationText = document.getElementById('notificationText');

// ========================================
// EMOJI PICKER FUNCTIONALITY
// ========================================

/**
 * Emoji collections by category
 */
const EMOJIS = {
    smileys: [
        '😀', '😃', '😄', '😁', '😆', '😅', '🤣', '😂',
        '🙂', '🙃', '😉', '😊', '😇', '🥰', '😍', '🤩',
        '😘', '😗', '😚', '😙', '😋', '😛', '😜', '🤪',
        '😝', '🤑', '🤗', '🤭', '🤫', '🤔', '🤐', '🤨',
        '😐', '😑', '😶', '😏', '😒', '🙄', '😬', '🤥',
        '😌', '😔', '😪', '🤤', '😴', '😷', '🤒', '🤕',
        '🤢', '🤮', '🤧', '🥵', '🥶', '😵', '🤯', '🤠',
        '🥳', '😎', '🤓', '🧐', '😕', '😟', '🙁', '☹️'
    ],
    gestures: [
        '👍', '👎', '👊', '✊', '🤛', '🤜', '🤞', '✌️',
        '🤟', '🤘', '👌', '🤏', '👈', '👉', '👆', '👇',
        '☝️', '✋', '🤚', '🖐️', '🖖', '👋', '🤙', '💪',
        '🦾', '✍️', '🙏', '🦶', '🦵', '👂', '🦻', '👃',
        '🧠', '🦷', '🦴', '👀', '👁️', '👅', '👄', '💋',
        '🩸', '👶', '👧', '🧒', '👦', '👩', '🧑', '👨'
    ],
    hearts: [
        '❤️', '🧡', '💛', '💚', '💙', '💜', '🖤', '🤍',
        '🤎', '💔', '❣️', '💕', '💞', '💓', '💗', '💖',
        '💘', '💝', '💟', '☮️', '✝️', '☪️', '🕉️', '☸️',
        '✡️', '🔯', '🕎', '☯️', '☦️', '🛐', '⛎', '♈',
        '♉', '♊', '♋', '♌', '♍', '♎', '♏', '♐',
        '♑', '♒', '♓', '🆔', '⚛️', '🉑', '☢️', '☣️'
    ],
    objects: [
        '🎉', '🎊', '🎈', '🎁', '🏆', '🥇', '🥈', '🥉',
        '⚽', '⚾', '🥎', '🏀', '🏐', '🏈', '🏉', '🎾',
        '🥏', '🎳', '🏏', '🏑', '🏒', '🥍', '🏓', '🏸',
        '🥊', '🥋', '🥅', '⛳', '⛸️', '🎣', '🤿', '🎽',
        '🎿', '🛷', '🥌', '🎯', '🪀', '🪁', '🎱', '🔮',
        '🪄', '🧿', '🎮', '🕹️', '🎰', '🎲', '🧩', '🧸'
    ]
};

/**
 * Current emoji category
 */
let currentEmojiCategory = 'smileys';

/**
 * Toggle emoji picker visibility
 */
function toggleEmojiPicker() {
    const emojiPicker = document.getElementById('emojiPicker');
    const isHidden = emojiPicker.classList.contains('hidden');
    
    if (isHidden) {
        emojiPicker.classList.remove('hidden');
        renderEmojis(currentEmojiCategory);
    } else {
        emojiPicker.classList.add('hidden');
    }
}

/**
 * Show specific emoji category
 */
function showEmojiCategory(category) {
    currentEmojiCategory = category;
    
    // Update active category button
    document.querySelectorAll('.emoji-category').forEach(btn => {
        btn.classList.remove('active');
    });
    event.target.classList.add('active');
    
    // Render emojis for this category
    renderEmojis(category);
}

/**
 * Render emojis for selected category
 */
function renderEmojis(category) {
    const emojiGrid = document.getElementById('emojiGrid');
    const emojis = EMOJIS[category] || EMOJIS.smileys;
    
    emojiGrid.innerHTML = '';
    
    emojis.forEach(emoji => {
        const button = document.createElement('button');
        button.className = 'emoji-item';
        button.textContent = emoji;
        button.onclick = () => insertEmoji(emoji);
        emojiGrid.appendChild(button);
    });
}

/**
 * Insert emoji into message input
 */
function insertEmoji(emoji) {
    const input = messageInput;
    const startPos = input.selectionStart;
    const endPos = input.selectionEnd;
    const currentValue = input.value;
    
    // Insert emoji at cursor position
    const newValue = currentValue.substring(0, startPos) + 
                     emoji + 
                     currentValue.substring(endPos);
    
    input.value = newValue;
    
    // Move cursor after emoji
    const newCursorPos = startPos + emoji.length;
    input.setSelectionRange(newCursorPos, newCursorPos);
    
    // Focus back on input
    input.focus();
    
    // Close emoji picker
    toggleEmojiPicker();
}

// ========================================
// AUTHENTICATION FUNCTIONS
// ========================================

/**
 * Switch between login and register tabs
 */
function switchAuthTab(tab) {
    if (tab === 'login') {
        loginTab.classList.add('active');
        registerTab.classList.remove('active');
        loginForm.classList.add('active');
        registerForm.classList.remove('active');
        clearAuthErrors();
    } else {
        registerTab.classList.add('active');
        loginTab.classList.remove('active');
        registerForm.classList.add('active');
        loginForm.classList.remove('active');
        clearAuthErrors();
    }
}

/**
 * Clear authentication error messages
 */
function clearAuthErrors() {
    loginError.textContent = '';
    registerError.textContent = '';
}

/**
 * Handle user login
 */
async function handleLogin() {
    const username = loginUsername.value.trim();
    const password = loginPassword.value;
    
    loginError.textContent = '';
    
    if (!username || !password) {
        loginError.textContent = 'Please enter username and password';
        return;
    }
    
    loginButton.disabled = true;
    loginButton.textContent = 'Logging in...';
    
    try {
        const response = await fetch(`${API_BASE_URL}/api/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });
        
        const data = await response.json();
        
        if (data.success) {
            AppState.username = username;
            AppState.userData = data.user;
            AppState.isAuthenticated = true;
            
            localStorage.setItem('chatflow_username', username);
            localStorage.setItem('chatflow_user_data', JSON.stringify(data.user));
            
            showNotification(data.message, 'success');
            connectToChat();
            
        } else {
            loginError.textContent = data.message;
        }
        
    } catch (error) {
        console.error('Login error:', error);
        loginError.textContent = 'Connection error. Please try again.';
    } finally {
        loginButton.disabled = false;
        loginButton.textContent = 'Login';
    }
}

/**
 * Handle user registration
 */
async function handleRegister() {
    const username = registerUsername.value.trim();
    const password = registerPassword.value;
    const confirmPassword = registerConfirmPassword.value;
    
    registerError.textContent = '';
    
    if (!username || !password || !confirmPassword) {
        registerError.textContent = 'Please fill in all fields';
        return;
    }
    
    if (username.length < 3) {
        registerError.textContent = 'Username must be at least 3 characters';
        return;
    }
    
    if (password.length < 6) {
        registerError.textContent = 'Password must be at least 6 characters';
        return;
    }
    
    if (password !== confirmPassword) {
        registerError.textContent = 'Passwords do not match';
        return;
    }
    
    registerButton.disabled = true;
    registerButton.textContent = 'Creating account...';
    
    try {
        const response = await fetch(`${API_BASE_URL}/api/register`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });
        
        const data = await response.json();
        
        if (data.success) {
            showNotification(data.message + ' Please login.', 'success');
            switchAuthTab('login');
            loginUsername.value = username;
            loginPassword.focus();
            
            registerUsername.value = '';
            registerPassword.value = '';
            registerConfirmPassword.value = '';
            
        } else {
            registerError.textContent = data.message;
        }
        
    } catch (error) {
        console.error('Registration error:', error);
        registerError.textContent = 'Connection error. Please try again.';
    } finally {
        registerButton.disabled = false;
        registerButton.textContent = 'Create Account';
    }
}

/**
 * Handle user logout
 */
function handleLogout() {
    if (socket) {
        socket.disconnect();
        socket = null;
    }
    
    AppState.username = null;
    AppState.userData = null;
    AppState.isAuthenticated = false;
    AppState.isConnected = false;
    AppState.messages = [];
    AppState.onlineUsers = [];
    
    localStorage.removeItem('chatflow_username');
    localStorage.removeItem('chatflow_user_data');
    
    messagesContainer.innerHTML = '';
    onlineUsersList.innerHTML = '';
    
    chatScreen.classList.remove('active');
    authScreen.classList.add('active');
    
    loginPassword.value = '';
    
    showNotification('Logged out successfully', 'success');
}
// ========================================
// CHAT CONNECTION FUNCTIONS
// ========================================

/**
 * Connect to chat with Socket.IO
 */
function connectToChat() {
    socket = io(API_BASE_URL, {
        transports: ['websocket', 'polling']
    });
    
    setupSocketHandlers();
    
    authScreen.classList.remove('active');
    chatScreen.classList.add('active');
    
    currentUsername.textContent = AppState.username;
    currentUserAvatar.style.backgroundColor = AppState.userData.avatar_color;
    currentUserAvatar.textContent = AppState.username.charAt(0).toUpperCase();
    
    messageInput.focus();
}

/**
 * Setup Socket.IO event handlers
 */
function setupSocketHandlers() {
    socket.on('connect', () => {
        console.log('🟢 Connected to ChatFlow server!');
        AppState.isConnected = true;
        
        socket.emit('user_login', {
            username: AppState.username
        });
        
        socket.emit('get_online_users');
    });
    
    socket.on('disconnect', () => {
        console.log('🔴 Disconnected from server');
        AppState.isConnected = false;
        addSystemMessage('Connection lost. Trying to reconnect...');
    });
    
    socket.on('message', (data) => {
        console.log('📨 Message from server:', data);
    });
    
    socket.on('user_joined', (data) => {
        console.log('👤 User joined:', data.username);
        
        userCount.textContent = `${data.user_count} user${data.user_count !== 1 ? 's' : ''} online`;
        
        if (data.username !== AppState.username) {
            addSystemMessage(`${data.username} joined the chat`);
        }
        
        socket.emit('get_online_users');
    });
    
    socket.on('user_left', (data) => {
        console.log('👋 User left:', data.username);
        
        userCount.textContent = `${data.user_count} user${data.user_count !== 1 ? 's' : ''} online`;
        
        addSystemMessage(`${data.username} left the chat`);
        
        socket.emit('get_online_users');
    });
    
    socket.on('new_message', (data) => {
        console.log('💬 New message:', data);
        
        const isOwnMessage = data.username === AppState.username;
        
        AppState.messages.push(data);
        
        addChatMessage(data, isOwnMessage);
    });
    
    socket.on('online_users_list', (data) => {
        console.log('👥 Online users:', data);
        AppState.onlineUsers = data.users;
        renderOnlineUsers();
    });
}

// ========================================
// MESSAGE HANDLING FUNCTIONS
// ========================================

/**
 * Handle sending message
 */
function handleSendMessage() {
    const messageText = messageInput.value.trim();
    
    if (!messageText) {
        return;
    }
    
    if (!AppState.isConnected) {
        showNotification('Not connected to chat', 'error');
        return;
    }
    
    socket.emit('send_message', {
        message: messageText
    });
    
    messageInput.value = '';
    
    messageInput.focus();
    
    console.log(`📤 Sent: ${messageText}`);
}

/**
 * Add system message to chat
 */
function addSystemMessage(text) {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message system';
    
    messageDiv.innerHTML = `
        <div class="message-bubble">
            ${escapeHtml(text)}
        </div>
    `;
    
    messagesContainer.appendChild(messageDiv);
    scrollToBottom();
}

/**
 * Add chat message to display
 */
function addChatMessage(data, isOwnMessage) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isOwnMessage ? 'user' : 'other'}`;
    
    const time = formatTime(data.timestamp);
    
    const avatarLetter = data.username.charAt(0).toUpperCase();
    
    messageDiv.innerHTML = `
        <div class="message-header">
            <div class="message-avatar" style="background-color: ${data.avatar_color}">
                ${avatarLetter}
            </div>
            <span class="message-username">${escapeHtml(data.username)}</span>
            <span class="message-time">${time}</span>
        </div>
        <div class="message-bubble">
            ${escapeHtml(data.text)}
        </div>
    `;
    
    messagesContainer.appendChild(messageDiv);
    scrollToBottom();
}

/**
 * Render online users list
 */
function renderOnlineUsers() {
    onlineUsersList.innerHTML = '';
    
    AppState.onlineUsers.forEach(user => {
        const userDiv = document.createElement('div');
        userDiv.className = 'online-user';
        
        const avatarLetter = user.username.charAt(0).toUpperCase();
        
        userDiv.innerHTML = `
            <div class="online-user-avatar" style="background-color: ${user.avatar_color}">
                ${avatarLetter}
            </div>
            <span class="online-user-name">${escapeHtml(user.username)}</span>
        `;
        
        onlineUsersList.appendChild(userDiv);
    });
}

// ========================================
// UTILITY FUNCTIONS
// ========================================

/**
 * Show notification toast
 */
function showNotification(message, type = 'info') {
    notificationText.textContent = message;
    notificationToast.className = `notification-toast ${type}`;
    
    setTimeout(() => {
        notificationToast.classList.remove('hidden');
    }, 100);
    
    setTimeout(() => {
        notificationToast.classList.add('hidden');
    }, 3100);
}

/**
 * Scroll messages to bottom
 */
function scrollToBottom() {
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

/**
 * Format timestamp for display
 */
function formatTime(isoString) {
    const date = new Date(isoString);
    const hours = date.getHours().toString().padStart(2, '0');
    const minutes = date.getMinutes().toString().padStart(2, '0');
    return `${hours}:${minutes}`;
}

/**
 * Escape HTML to prevent XSS
 */
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// ========================================
// EVENT LISTENERS
// ========================================

// Enter key in login username
loginUsername.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        loginPassword.focus();
    }
});

// Enter key in login password
loginPassword.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        handleLogin();
    }
});

// Enter key in register username
registerUsername.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        registerPassword.focus();
    }
});

// Enter key in register password
registerPassword.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        registerConfirmPassword.focus();
    }
});

// Enter key in register confirm password
registerConfirmPassword.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        handleRegister();
    }
});

// Enter key in message input
messageInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        handleSendMessage();
    }
});

// Close emoji picker when clicking outside
document.addEventListener('click', (e) => {
    const emojiPicker = document.getElementById('emojiPicker');
    const emojiButton = document.getElementById('emojiButton');
    
    if (emojiPicker && !emojiPicker.contains(e.target) && e.target !== emojiButton && !emojiButton.contains(e.target)) {
        if (!emojiPicker.classList.contains('hidden')) {
            emojiPicker.classList.add('hidden');
        }
    }
});

// ========================================
// INITIALIZATION
// ========================================

/**
 * Initialize application
 */
function initApp() {
    console.log('🚀 ChatFlow 2.0 initializing...');
    
    const savedUsername = localStorage.getItem('chatflow_username');
    const savedUserData = localStorage.getItem('chatflow_user_data');
    
    if (savedUsername && savedUserData) {
        AppState.username = savedUsername;
        AppState.userData = JSON.parse(savedUserData);
        AppState.isAuthenticated = true;
        
        console.log('📝 Found saved session, auto-connecting...');
        connectToChat();
    } else {
        authScreen.classList.add('active');
        loginUsername.focus();
    }
    
    console.log('✅ ChatFlow 2.0 ready!');
}

// Start the app when DOM is ready
document.addEventListener('DOMContentLoaded', initApp);

console.log('📝 ChatFlow 2.0 loaded, waiting for DOM...');
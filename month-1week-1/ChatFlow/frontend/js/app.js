/**
 * CHATFLOW - REAL-TIME CHAT APPLICATION
 * Frontend: Socket.IO Client + chat Logic
 */

// =========================================
// CONFIGURATION & STATE
// =========================================

// Connect to Socket.IO server
const socket = io('http://localhost:5000', {
    transports: ['websocket', 'polling']
});

// Application State
const AppState = {
    username: '',
    isConnected: false,
    messages: []
};

// DOM Elements 
const usernameScreen = document.getElementById('usernameScreen');
const chatScreen = document.getElementById('chatScreen');
const usernameInput = document.getElementById('usernameInput');
const joinButton = document.getElementById('joinButton');
const currentUsername = document.getElementById('currentUsername');
const messagesContainer = document.getElementById('messagesContainer');
const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');
const typingIndicator = document.getElementById('typingIndicator');

// ========================================
// SOCKET.IO EVENT HANDLERS
// ========================================

/**
 * Connection established
 */
socket.on('connect', () => {
    console.log('🟢 Connected to ChatFlow server!');
    AppState.isConnected = true;
    updateConnectionStatus(true);
});

/**
 * Connection lost
 */
socket.on('disconnect', () => {
    console.log('🔴 Disconnected from server');
    AppState.isConnected = false;
    updateConnectionStatus(false);
    addSystemMessage('Connection lost. Trying to reconnect...');
});

/**
 * Initial connection message from server
 */
socket.on('message', (data) => {
    console.log('📨 Message from server:', data);
    addSystemMessage(data.text);
});

/**
 * User joined notification
 */
socket.on('user_joined', (data) => {
    console.log('👤 User joined:', data.username);
    
    // Don't show notification for yourself
    if (data.username !== AppState.username) {
        addSystemMessage(`${data.username} joined the chat`);
    }
});

/**
 * New message received
 */
socket.on('new_message', (data) => {
    console.log('💬 New message:', data);
    
    // Determine if message is from current user
    const isOwnMessage = data.username === AppState.username;
    
    // Add to messages array
    AppState.messages.push(data);
    
    // Display message
    addChatMessage(data, isOwnMessage);
});

// ========================================
// UI EVENT HANDLERS
// ========================================

/**
 * Join chat button clicked
 */
joinButton.addEventListener('click', handleJoinChat);

/**
 * Enter key in username input
 */
usernameInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        handleJoinChat();
    }
});

/**
 * Send message button clicked
 */
sendButton.addEventListener('click', handleSendMessage);

/**
 * Enter key in message input
 */
messageInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        handleSendMessage();
    }
});

/**
 * Typing detection (optional feature)
 */
let typingTimeout;
messageInput.addEventListener('input', () => {
    clearTimeout(typingTimeout);
    
    // Emit typing event
    socket.emit('typing', { username: AppState.username });
    
    // Stop typing after 2 seconds of no input
    typingTimeout = setTimeout(() => {
        socket.emit('stop_typing', { username: AppState.username });
    }, 2000);
});

// ========================================
// MAIN FUNCTIONS
// ========================================

/**
 * Handle user joining chat
 */
function handleJoinChat() {
    const username = usernameInput.value.trim();
    
    // Validation
    if (!username) {
        alert('Please enter a username');
        return;
    }
    
    if (username.length < 2) {
        alert('Username must be at least 2 characters');
        return;
    }
    
    // Store username
    AppState.username = username;
    
    // Emit to server
    socket.emit('user_join', { username: username });
    
    // Switch screens
    usernameScreen.classList.remove('active');
    chatScreen.classList.add('active');
    
    // Update UI
    currentUsername.textContent = username;
    
    // Focus message input
    messageInput.focus();
    
    console.log(`✅ Joined as: ${username}`);
}

/**
 * Handle sending message
 */
function handleSendMessage() {
    const messageText = messageInput.value.trim();
    
    // Validation
    if (!messageText) {
        return;
    }
    
    // Emit to server
    socket.emit('send_message', {
        message: messageText
    });
    
    // Clear input
    messageInput.value = '';
    
    // Keep focus on input
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
    
    // Format timestamp
    const time = formatTime(data.timestamp);
    
    messageDiv.innerHTML = `
        <div class="message-header">
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
 * Update connection status indicator
 */
function updateConnectionStatus(isConnected) {
    const statusIndicators = document.querySelectorAll('.status-indicator');
    
    statusIndicators.forEach(indicator => {
        if (isConnected) {
            indicator.classList.add('online');
        } else {
            indicator.classList.remove('online');
        }
    });
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
// INITIALIZATION
// ========================================

/**
 * Initialize application
 */
function initApp() {
    console.log('🚀 ChatFlow initializing...');
    
    // Focus username input
    usernameInput.focus();
    
    console.log('✅ ChatFlow ready!');
}

// Start the app when DOM is ready
document.addEventListener('DOMContentLoaded', initApp);

console.log('📝 ChatFlow loaded, waiting for DOM...');
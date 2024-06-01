const messagesDiv = document.getElementById('messages');
const form = document.getElementById('message-form');
const input = document.getElementById('message-input');

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const message = input.value.trim();
    if (message !== '') {
        await sendMessage(message);
        input.value = '';
    }
});

const ws = new WebSocket(`ws://${window.location.host}/ws`);

ws.onmessage = (event) => {
    const message = document.createElement('div');
    message.textContent = event.data;
    messagesDiv.appendChild(message);
};

async function sendMessage(message) {
    ws.send(message);
}

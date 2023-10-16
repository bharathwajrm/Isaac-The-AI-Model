<script>
  document.addEventListener("DOMContentLoaded", function () {
    const chatContainer = document.querySelector(".chat-container");
    const chatInput = document.getElementById("chat-input");
    const sendBtn = document.getElementById("send-btn");

    function addMessage(message, isUser = false) {
      const chat = document.createElement("div");
      chat.classList.add("chat", isUser ? "outgoing" : "incoming");
      chat.innerHTML = `
        <div class="chat-content">
          <div class="chat-details">
            <img src="${isUser ? 'user.png' : 'AI.png'}" alt="Avatar">
            <p>${message}</p>
          </div>
        </div>
      `;
      chatContainer.appendChild(chat);
      chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    function sendMessage() {
      const userMessage = chatInput.value;
      addMessage(userMessage, true);

      // Send user message to the server for processing
      fetch("/chat", {
        method: "POST",
        body: new URLSearchParams({ user_message: userMessage }),
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
      })
        .then((response) => response.json())
        .then((data) => {
          const botResponse = data.bot;
          chatHistory = data.chat_history;

          addMessage(botResponse, false);
        });

      chatInput.value = "";
    }

    sendBtn.addEventListener("click", sendMessage);
    chatInput.addEventListener("keyup", function (event) {
      if (event.key === "Enter") {
        sendMessage();
      }
    });
  });
</script>
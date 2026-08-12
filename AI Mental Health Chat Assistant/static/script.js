async function sendMessage() {

    const input = document.getElementById("message");
    const chat = document.getElementById("chat");

    const message = input.value.trim();

    if (message === "") return;

    chat.innerHTML += `
        <div class="user">
            <b>You:</b> ${message}
        </div>
    `;

    const response = await fetch("/chat", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: message
        })

    });

    const data = await response.json();

    chat.innerHTML += `
        <div class="bot">
            <b>Bot:</b> ${data.reply}
        </div>
    `;

    input.value = "";

    chat.scrollTop = chat.scrollHeight;
}
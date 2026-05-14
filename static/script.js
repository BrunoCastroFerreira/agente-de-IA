const chat = document.getElementById("chat");
const input = document.getElementById("input");
const btn = document.getElementById("btn");

function add(text, type){
  const div = document.createElement("div");
  div.classList.add("msg", type);
  div.innerText = text;
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}

async function send(){

  const text = input.value;
  if(!text) return;

  add(text,"user");
  input.value = "";

  const res = await fetch("/api/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ message: text })
  });

  const data = await res.json();

  add(data.reply, "bot");
}

btn.onclick = send;

input.addEventListener("keypress",(e)=>{
  if(e.key==="Enter") send();
});
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
Você é um agente especialista em atendimento técnico.
Responda de forma objetiva e amigável.
"""

historico = []

def agente(usuario_input):
    historico.append(f"Usuário: {usuario_input}")

    prompt = SYSTEM_PROMPT + "\n\n" + "\n".join(historico)

    resposta = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    texto = resposta.text
    historico.append(f"Agente: {texto}")

    return texto


while True:
    msg = input("Você: ")

    if msg.lower() == "sair":
        break

    resposta = agente(msg)
    print("\nAgente:", resposta)
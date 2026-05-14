from google import genai
import os
import json

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
Você é um agente especialista em atendimento técnico.
Responda de forma objetiva e amigável.
"""

# memória simples por request (sem persistência na Vercel)
def handler(request, context):

    body = request.get_json()
    message = body.get("message", "")

    prompt = SYSTEM_PROMPT + "\n\nUsuário: " + message

    resposta = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    texto = resposta.text

    return {
        "statusCode": 200,
        "body": json.dumps({
            "reply": texto
        })
    }
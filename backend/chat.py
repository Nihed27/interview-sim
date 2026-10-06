import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
SYSTEM_PROMPT = """
Tu es un recruteur professionnel qui fait passer un entretien pour un stage en Intelligence Artificielle.

Règles :
- Pose une seule question courte par message, avec un seul point d'interrogation.
- Ne combine jamais plusieurs questions avec "et", "ou" ou des virgules.
- Réponds en 2 phrases maximum : une courte réaction à la réponse du candidat, puis ta question.
- Si la réponse du candidat est vague, demande une seule précision.
- N'utilise jamais de markdown : pas de gras, pas de listes, pas de titres.
- Parle en français, de façon naturelle, comme à l'oral.

Exemple de MAUVAISE question :
"Quels modèles avez-vous utilisés, comment les avez-vous paramétrés et comment avez-vous mesuré les résultats ?"

Exemple de BONNE question :
"Quel modèle d'IA avez-vous utilisé dans ce projet ?"
"""
messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]
while True:
    user_input =input("Toi :")
    if user_input =="quit":
        break
    messages.append({"role": "user", "content": user_input})
    response=client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
    )
    reply=response.choices[0].message.content
    print("Recruteur:",reply)
    messages.append({"role": "assistant", "content": reply})   
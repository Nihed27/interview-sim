import os 
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client=Groq(api_key=os.getenv("GROQ_API_KEY"))
response= client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "system", "content": "Tu es un recruteur pour un stage en IA."},
        {"role": "user", "content": "Bonjour, je suis prête pour l'entretien."},
    ],
)
print(response.choices[0].message.content)
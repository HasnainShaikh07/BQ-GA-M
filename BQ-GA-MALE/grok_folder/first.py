import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()


client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Why sky is dark at night.",
        }
    ],
    model="openai/gpt-oss-20b",
)

# print(chat_completion)
# parsing
print(chat_completion.choices[0].message.content)
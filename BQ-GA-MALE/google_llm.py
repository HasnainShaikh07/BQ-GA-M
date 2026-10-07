


from google import genai
import json
from dotenv import load_dotenv
import os
load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-flash-lite-latest",
    contents="Why sky is blue."
)
response_dict = response.model_dump()
# print(json.dumps(response_dict, indent=2, default=str))
print(response_dict["candidates"][0]["content"]["parts"][0]["text"])
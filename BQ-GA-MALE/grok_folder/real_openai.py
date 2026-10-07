
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

response = client.responses.create(
    input="Why sky is dark at night?",
    model="gpt-4.1-mini",
)


print(response.output_text)

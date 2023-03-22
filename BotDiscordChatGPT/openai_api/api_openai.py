import openai
import os 
from dotenv import load_dotenv
from typing import Any, Dict, List

load_dotenv()

openai.api_key = os.environ.get('OPENAI_API_KEY')

def get_chat_gpt_response(question: str) -> str:
    response_from_chat_gpt = openai.Image.create(
        prompt=question,
        n=1,
        size="512x512",
    )

    image_url = response_from_chat_gpt['data'][0]['url']

    return image_url
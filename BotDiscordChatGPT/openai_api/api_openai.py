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

'''
Para usar o chat gpt com perguntas e respostas, use o código abaixo:

def get_chat_gpt_response(question: str) -> str:
    response_from_chat_gpt = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        max_tokens=100,
    )

    if response_from_chat_gpt:
        choices: List[Dict[str, Any]] = response_from_chat_gpt.get("choices", None)
        if choices and len(choices) > 0:
            text: str = choices[0].get("text", None)
            return text
    return None
'''
'''prgrama para configurar chat gpt com discord'''
'''comando para instalar discord.py: pip install discord.py'''
'''comando para instalar dotenv: pip install python-dotenv'''
'''comando para instalar venv: pip install virtualenv'''
'''comando para criar env: python -m venv env'''
'''comando para entrar no env: .\env\Scripts\ activate'''
import os
from discord import Message
import discord
from discord.client import Client
from discord.flags import Intents
from dotenv import load_dotenv

from openai_api.api_openai import get_chat_gpt_response

load_dotenv()

bot_caller: str = "/gpt"

discord_token = os.environ.get('DISCORD_TOKEN')

class CustomDiscordClient(Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_message(self, message: Message):
        message_content: str = message.content
        if bot_caller in message_content:
            prompt: str = message_content.split(bot_caller)[1]
            print(prompt)
            chat_gpt_response: str = get_chat_gpt_response(question=prompt)
            if chat_gpt_response:
                await message.channel.send(chat_gpt_response)
Intents = Intents.default()
Intents.message_content = True
custom_discord_client = CustomDiscordClient = CustomDiscordClient(intents=Intents)


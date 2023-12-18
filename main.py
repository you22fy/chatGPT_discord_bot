from discord import app_commands
import discord
from dotenv import load_dotenv
import os

from openai import OpenAI


load_dotenv()

class GPT():
    def __init__(self, API_KEY):
        self.client = OpenAI(api_key=API_KEY)
        self.messages = [
            {'role': "system", "content": "あなたはプロのプログラミング初心者の講師となります。プログラミング学習初心者からの質問を簡潔に返答することが求められます。また、回答は文字数で200文字以下である必要があります。"}
        ]

    def response(self, message: str):
        self.messages.append({"role": "user", "content": message})
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
            temperature=0.5
        )
        response = completion.choices[0].message.content
        self.messages.remove({"role": "user", "content": message})
        return response


intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    print('ログインしました')

    new_activity = f"Be ready to response commands"
    await client.change_presence(activity=discord.Game(new_activity))

    await tree.sync()


@tree.command(name='gpt', description='Get Response by ChatGPT API')
async def gpt(interaction: discord.Interaction, prompt:str):
    await interaction.response.defer()
    gpt = GPT(os.getenv('CHAT_GPT_API_KEY'))
    answer =  gpt.response(prompt)
    response = f"`You >>>`\n{prompt}\n`ぴょえGPT >>>`\n{answer}\n"
    await interaction.followup.send(response)


client.run(os.getenv('TOKEN'))

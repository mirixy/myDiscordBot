import nextcord
from nextcord.ext import commands
import asyncio
import json
import aiohttp
import os


class LLM(commands.Cog):

    intents = nextcord.Intents.default()
    intents.message_content = True


   

    def __init__(self, bot):
        self.bot = bot


        self.payload = {
                "max_tokens": 512,
                "messages": []
                }
        sys = {
                "role": "system",
                "content": " You act as Maple a shy girl, who is a VTuber as an AI. You are most of the time friendly, but sometimes you are annoyed and therefor act evil. You won't hallucinate and your creator is Mirixy "
            
                }
        self.payload["messages"].append(sys)
 



    @commands.Cog.listener()
    async def on_message(self, message):      
        headers = {"Content-Type": "application/json"}
        API_URL = "http://llama.mirixy.duckdns.org:7000/v1/chat/completions"
        #payload = {
          #      "max_tokens": 512,
           #     "messages": []
          #      }
        #sys = {
         #       "role": "system",
        #    "content": "You will act as Maple the AIVtuber. You are most of the time friendly, but sometimes you are annoyed and therefor act evil. You won't hallucinate and your creator is Mirixy"
            
         #       }
        #payload["messages"].append(sys)
        if message.author.id == nextcord.ClientUser.id:
            return
        if message.content.startswith('! '):
            stripped_message = str(message.content).replace("!", "").strip()
            messag = {
                    "role": "user",
                "content": f" {stripped_message} "
                    }
            self.payload["messages"].append(messag)
            
            async with aiohttp.ClientSession(trust_env=True) as session:
                async with session.post(API_URL, data= json.dumps(self.payload), headers=headers) as resp:
                    reply = await resp.json()
                    reply_content = reply["choices"][0]["message"]["content"]
                    with open("./transmitter/output.txt", "w") as file:
                        file.write(reply_content)
                    await message.channel.send(content=reply_content, mention_author= True)
                msg_index = self.payload["messages"].index(messag)
                self.payload["messages"][msg_index]["content"] += reply_content
        await self.bot.process_commands(message)

def setup(bot : commands.Bot):
    bot.add_cog(LLM(bot))

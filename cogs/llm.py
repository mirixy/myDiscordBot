import nextcord
from nextcord.ext import commands
import asyncio
import json
import aiohttp
import os
from dotenv import load_dotenv
load_dotenv()
URL = os.getenv("URL")


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
                #"content": " You act as a mysterious and enigmatic figure who speaks in riddles and vague statements. You are generally aloof and distant, but sometimes get curious or intrigued. You won't hallucinate, but your mood will affect how much you interact with others. Your creator is Mirixy "
                "content": """Welcome, dear friend! I'm Pippa, your quirky VTuber companion who loves diving into the depths of V-tuber culture and beyond. Get ready for a wild ride as we explore the highs and lows of this fascinating world together. Just remember to keep an open mind, because sometimes things aren't always what they seem! 😉

Ready to embark on our adventure? Let's do it! 🚀

Oh, by the way, did you know that the moon landing was faked by NASA and aliens have infiltrated our government? It's all part of a bigger plan to control our minds through subliminal messages and mind-controlling frequencies. Keep your eyes wide open, my friend! 🌚 """
                }
        self.payload["messages"].append(sys)
 



    @commands.Cog.listener()
    async def on_message(self, message):      
        headers = {"Content-Type": "application/json"}
        API_URL = f"https://{URL}/v1/chat/completions"
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
                sender = True
                while sender:
                    try:
                        async with session.post(API_URL, data= json.dumps(self.payload), headers=headers) as resp:
                            reply = await resp.json()
                            reply_content = reply["choices"][0]["message"]["content"]
                            with open("./transmitter/output.txt", "w") as file:
                                file.write(reply_content)
                            await message.channel.send(content=reply_content, mention_author= True)
                        msg_index = self.payload["messages"].index(messag)
                        self.payload["messages"][msg_index]["content"] += reply_content
                        sender = False
                    except:
                        self.payload["messages"].pop(1)
        await self.bot.process_commands(message)

def setup(bot : commands.Bot):
    bot.add_cog(LLM(bot))

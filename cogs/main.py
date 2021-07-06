from urllib.parse import urlencode
from discord.ext.commands import Cog
from discord.ext.commands.core import command
import requests

class Session(requests.Session):
    pass

class Main(Cog,name='encode and decoder'):
    def __init__(self,bot):
        self.bot = bot
        self.session = Session()
    
    @command()
    async def base_64_encode(self,ctx,*, text):
        url = 'https://some-random-api.ml/base64?'+urlencode(
            {"encode":str(text)}
        )
        await ctx.send(self.session.get(url).json()['base64'])

    @command()
    async def base_64_decode(self,ctx,*, text):
        url = 'https://some-random-api.ml/base64?'+urlencode(
            {"decode":str(text)}
        )
        await ctx.send(self.session.get(url).json()['text'])
    
    @command()
    async def binary_encode(self,ctx,*,text):
        url = 'https://some-random-api.ml/binary?'+urlencode(
            {"text":str(text)}
        )
        await ctx.send(self.session.get(url).json()['binary'])
    @command()
    async def binary_decode(self,ctx,*,text):
        url = 'https://some-random-api.ml/binary?'+urlencode(
            {"decode":str(text)}
        )
        await ctx.send(self.session.get(url).json()['text'])

def setup(bot):
    bot.add_cog(Main(bot))
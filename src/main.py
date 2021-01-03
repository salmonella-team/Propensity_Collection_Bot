from typing import Pattern
import discord
from discord import channel
from discord.ext import commands
import settings
import re


bot = commands.Bot(command_prefix="/yashiro ")


@bot.event
async def on_ready():
    """
    bot起動 + 起動確認メッセージ送信
    """
    await bot.get_channel(int(settings.LAUNCH_NOTIFICATION)).send("起動")
    print("Launch OK")


@bot.command()
async def collect(ctx):
    """ 
    Tweetmessageを集める
    """

    # チャンネルの全メッセージを取得
    collect_channel = bot.get_channel(int(settings.COLLECTED_CHANNEL))
    collect_channel_message = await collect_channel.history(limit=1000).flatten()

    """
    Twitterの場合:https://twitter.com/XXXX/status/XXXXXXXXXX
    """

    # Twitter以外のメッセージを配列から消す
    pattern = "https\:\/\/twitter\.com\/[^\/]+\/status\/[0-9]+"
    messages = []
    for message in collect_channel_message:
        url = message.content
        url = re.match(pattern, url)
        if url:
            messages.append(url.group())
    # twitterでまず判別

    # 画像URLをすべて取得する

    # HTMLを発行

    #


bot.run(settings.DISCORD_TOKEN)

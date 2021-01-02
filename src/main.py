import discord
from discord.ext import commands
import settings

bot = commands.Bot(command_prefix="/yashiro ")

"""
やらないといけないこと
githubpagesでのルーティング方法
https://qiita.com/teinen_qiita/items/04522a76c239e9998856
今回はリポジトリのアレでなんかやる
"""

@bot.event
async def on_ready():
    """
    login + bot起動
    """
    await bot.get_channel(settings.LAUNCH_NOTIFICATION)
    print("Launch OK")

@bot.command()
async def collect():
    """
    Tweetmessageを集める
    """

    # チャンネルの全メッセージを取得

    # ツイートが画像ツイートか判別

    # 画像URLをすべて取得する

    # HTMLを発行

    # gistにPush





bot.run(settings.DISCORD_TOKEN)
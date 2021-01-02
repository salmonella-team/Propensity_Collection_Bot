import discord
from discord.ext import commands
import settings

bot = commands.Bot(command_prefix="/yashiro ")


@bot.event
async def on_ready():
    """
    bot起動 + 起動確認メッセージ送信
    """
    await bot.get_channel(int(settings.LAUNCH_NOTIFICATION)).send("起動")
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

    #


bot.run(settings.DISCORD_TOKEN)

from discord.ext import commands
from jinja2 import Template
import tweepy

import re

import settings


bot = commands.Bot(command_prefix="/yashiro ")
template = Template("{{ embedded_tweet  }}")

# Tweepyの準備
auth = tweepy.OAuthHandler(settings.TW_CONSUMER_KEY,
                           settings.TW_CONSUMER_SECRET)
auth.set_access_token(settings.TW_ACCESS_TOKEN,
                      settings.TW_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


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

    # 埋め込みAPIの取得(ページがなかったときの例外処理がまだ)
    embedded_tweets = []
    for message in messages:
        embedded_tweets.append(api.get_oembed(message))
    print(embedded_tweets)

    # print(template.render(embedded_tweet=embedded_tweet['html']))

    # JinjaでHTML作成

    # 画像URLをすべて取得する

    # HTMLを発行


bot.run(settings.DISCORD_TOKEN)

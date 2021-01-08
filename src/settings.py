import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
COLLECTED_CHANNEL = os.environ.get("COLLECTED_CHANNEL")
LAUNCH_NOTIFICATION = os.environ.get("LAUNCH_NOTIFICATION")
TW_CONSUMER_KEY = os.environ.get("TW_CONSUMER_KEY")
TW_CONSUMER_SECRET = os.environ.get("TW_CONSUMER_SECRET")
TW_ACCESS_TOKEN = os.environ.get("TW_ACCESS_TOKEN")
TW_ACCESS_TOKEN_SECRET = os.environ.get("TW_ACCESS_TOKEN_SECRET")
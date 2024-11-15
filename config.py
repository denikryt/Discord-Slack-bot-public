import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
SIGNING_SECRET = os.environ.get('SIGNING_SECRET')
TOKEN_DISCORD = os.environ.get('TOKEN_DISCORD')
MONGO_DB = os.environ.get('MONGO_DB')

SLACK_CHANNEL_GENERAL = os.environ.get('SLACK_CHANNEL_GENERAL')
SLACK_CHANNEL_RANDOM = os.environ.get('SLACK_CHANNEL_RANDOM')
SLACK_CHANNEL_DISCORD = os.environ.get('SLACK_CHANNEL_DISCORD')
SLACK_CHANNEL_MADE_IN_HACKLAB = os.environ.get('SLACK_CHANNEL_MADE_IN_HACKLAB')

DISCORD_CHANNEL_GENERAL = os.environ.get('DISCORD_CHANNEL_GENERAL')
DISCORD_CHANNEL_RANDOM = os.environ.get('DISCORD_CHANNEL_RANDOM')
DISCORD_CHANNEL_MADE_IN_HACKLAB = os.environ.get('DISCORD_CHANNEL_MADE_IN_HACKLAB')

SLACK_CHANNEL_TEST = os.environ.get('SLACK_CHANNEL_TEST')
DISCORD_CHANNEL_TEST = os.environ.get('DISCORD_CHANNEL_TEST')

SLACK_CHANNELS_DICT = {
    SLACK_CHANNEL_GENERAL:DISCORD_CHANNEL_GENERAL,
    SLACK_CHANNEL_RANDOM:DISCORD_CHANNEL_RANDOM,
    SLACK_CHANNEL_MADE_IN_HACKLAB:DISCORD_CHANNEL_MADE_IN_HACKLAB,
    SLACK_CHANNEL_TEST:DISCORD_CHANNEL_TEST
    }

DISCORD_CHANNELS_DICT = {
    DISCORD_CHANNEL_GENERAL:SLACK_CHANNEL_GENERAL,
    DISCORD_CHANNEL_RANDOM:SLACK_CHANNEL_RANDOM,
    DISCORD_CHANNEL_MADE_IN_HACKLAB:SLACK_CHANNEL_MADE_IN_HACKLAB,
    DISCORD_CHANNEL_TEST:SLACK_CHANNEL_TEST
    }

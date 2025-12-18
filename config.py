import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN","")
    API_ID = int(os.environ.get("API_ID","26375665"))
    API_HASH = os.environ.get("API_HASH","568839157ce65f4d3a91647f022b6737")
    AUTH_USER = os.environ.get('AUTH_USERS', '7547625729').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "[𝐒нɑᎥ𝚝ɑη](https://t.me/aaajaeooooobot)"





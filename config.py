import os
import re
from youtube_dl import YoutubeDL

class Config:
    APP_ID = int(os.environ.get("APP_ID", ''))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    START_MSG = os.environ.get("START_MSG", "<b>Hi {},\nIam A Song A Song Downloader Bot Exclusively Made For TG - Musics 🎶\nJoin My Group & See What Can I Do 😎")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/77e633996de605520a03f.jpg")
    OWNER = os.environ.get("OWNER", "TG_MusicsChat") 
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}

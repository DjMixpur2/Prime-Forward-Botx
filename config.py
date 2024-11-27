import datetime
from os import environ 

class Config:
    API_ID = environ.get("API_ID", "12850056")
    API_HASH = environ.get("API_HASH", "15564ec4a1a2cbef87c99a9aa9e40b34")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8178732396:AAEd104z69Wv0xQel_fgdWONINLHbKRBRIg") 
    BOT_SESSION = environ.get("BOT_SESSION", "Prime-Forward-Botx") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://renamebot:renamebot@cluster0.av4ze.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '770434685').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001933509863'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "https://t.me/Prime_Botz") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")
    PORT = environ.get('PORT', '8080')
   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []

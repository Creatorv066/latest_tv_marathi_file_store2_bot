import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "22787559"))
  API_HASH = os.environ.get("API_HASH", "e771139d8f3d4ae57f663ad049bbb710")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "7731772319:AAFJsDMmBRgN2T6tXV3nJ9KHOqOrGWcON34")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "latesttvshow_File_store_bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002117171789"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "publicearn.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "9a696c4ea657a9791396336c3d1d84fafe02eb74")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "1562792211"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Cluster0:Cluster0@cluster0.at9o8xi.mongodb.net/?appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001988223746")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001881381645"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 💡FɪʟᴇSᴛᴏʀᴇBᴏᴛ💡]────⍟
│
├🤖 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├📝 Language: [Python 3](https://www.python.org)
│
├🧰 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 🥰 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
👨‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [𝐋𝐓𝐒](https://t.me/Developerltr_bot)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/Developerltr_bot)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

👨‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:- @Developerltr_bot

ℹ️ How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""

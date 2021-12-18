from pyrogram import *
from pyrogram.types import *
import requests
# ====================================================================
app = Client("MrTak",config_file="config.ini")
# ====================================================================
ADMINID = "@MrTakDev"
# ====================================================================
Keyboard = ReplyKeyboardMarkup(
    [
        ["👤 Contact us 👤","ℹ️ Information ℹ️"]

    ],resize_keyboard=True
)
# ====================================================================
@app.on_message(filters.command("start"))
async def Start(client, message):
    await message.reply_text(f"""سلام <b> {message.from_user.mention} </b> عزیز 😃🔥
به ربات فینگیلیش به فارسی خوش آمدید 🤓""",reply_markup=Keyboard,parse_mode="html")
# ====================================================================
async def Information(client, message):
    await message.reply_text(f"""
`┌┬` __User info__
`│├` First Name:  `{message.from_user.first_name}`
`│├` Last Name:  `{message.from_user.last_name}`
`│├` Username:  `@{message.from_user.username}`
`│├` ID:  `{message.from_user.id}` """,reply_markup=Keyboard,parse_mode="markdown")
# ====================================================================
async def Contact_us(client, message):
    await message.reply_text(f"""👤 اگر پیشنهادی انتقادی یا حرفی یا اگر باگی در ربات هست میتونید از ایدی زیر استفاده کنید و مطرح کنید 😃🔥
🆔 ** {ADMINID} **""",reply_markup=Keyboard,parse_mode="markdown")
# ====================================================================
@app.on_message()
async def Fingilish(client, message):
    Text = message.text
    if Text == "👤 Contact us 👤":
        await Contact_us(client, message)
    elif Text == "ℹ️ Information ℹ️":
        await Information(client, message)
    URL = f"https://api.codebazan.ir/fintofa/?text={Text}"
    request =  requests.get(URL).json()
    Fingilish = dict(request)
    await message.reply_text(Fingilish["result"])
# ====================================================================
app.run()
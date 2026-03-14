from pyrogram import Client, filters
from pyrogram.enums import ChatAction
from config import API_ID, API_HASH, BOT_TOKEN
from iro import get_iro_reply

app = Client(
    "IR-O_Chatbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.text & ~filters.command())
async def chat_handler(client, message):
    await client.send_chat_action(message.chat.id, ChatAction.TYPING)
    reply = get_ai_reply(message.text)
    await message.reply_text(reply)

print("🤖 Desi Chatbot running...")
app.run()

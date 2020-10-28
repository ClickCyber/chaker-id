from pyrogram import Filters, InlineQueryResultArticle, Client
from pyrogram import InputTextMessageContent, InlineKeyboardMarkup
from pyrogram import InlineKeyboardButton
from apps.algo import id_chaker

apps = Client('config/Session',
              api_id=1,
              api_hash='b6b154c3707471f5339bd661645ed3d6',
              bot_token='1292354229:AAFCqtLRBAtgYiWBaYTrhfXieHLRJlqjypI')

@apps.on_message(Filters.command('start'))
def start(client, message):
    apps.send_message(message.chat.id, 
    f'{message.chat.first_name} ברוכים הבאים', 
    reply_markup=InlineKeyboardMarkup(
        [
    [InlineKeyboardButton('יוצר 👨🏻‍💻', url='t.me/writeXcode'), InlineKeyboardButton('קוד מקור 📝', url='https://github.com/ClickCyber/chaker-id')],
    [InlineKeyboardButton(' 🆔 בדוק מספר ת.ז 🆔', switch_inline_query_current_chat='')]
    ]))

@apps.on_inline_query()
def inline(client, message):
    if id_chaker(message.query) == True:
        message.answer(
        results=[InlineQueryResultArticle("מספר תעודת זהות נמצא  ! ✔️",
        InputTextMessageContent(f"מספר תעןדת זהות {message.query} תקין "))])
    else:
        message.answer(
        results=[InlineQueryResultArticle("מספר תעודת זהות לא נמצא ! ❌",
        InputTextMessageContent(f"מספר תעודת זהות {message.query} לא מצתט"))])

apps.run()

import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from config import BOT_TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

reply_keyboard = [['Русский язык', 'Математика профиль'],]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


async def start(update, context):
    await update.message.reply_text(
        "Выберите нужный вам предмет",
        reply_markup=markup
    )

async def start(update, context):
    text = update.message.text
    if text == "Русский язык":
        await update.message.reply_text(
            "Выберите нужный вам предмет",
            reply_markup=markup
        )


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT, start))

    application.run_polling()
if __name__ == '__main__':
    main()
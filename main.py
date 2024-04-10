import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler, ConversationHandler, ContextTypes, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, Update
from config import BOT_TOKEN

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logger = logging.getLogger(__name__)



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Русский яызк"],["Математика профиль"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)

    await update.message.reply_text("Выберите предмет:", reply_markup=reply_markup)

async def back_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    await query.answer()
    await start(query, context)


async def math(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("№1", callback_data="1"), InlineKeyboardButton("№2", callback_data="2")],
        [InlineKeyboardButton("№3", callback_data="3"), InlineKeyboardButton("№4", callback_data="4")],
        [InlineKeyboardButton("№5", callback_data="5"), InlineKeyboardButton("№6", callback_data="6")],
        [InlineKeyboardButton("№7", callback_data="7"), InlineKeyboardButton("№8", callback_data="8")],
        [InlineKeyboardButton("№9", callback_data="9"), InlineKeyboardButton("№10", callback_data="10")],
        [InlineKeyboardButton("№11", callback_data="11"), InlineKeyboardButton("№12", callback_data="12")],
        [InlineKeyboardButton("№13", callback_data="13"), InlineKeyboardButton("№14", callback_data="14")],
        [InlineKeyboardButton("№15", callback_data="15"), InlineKeyboardButton("№16", callback_data="16")],
        [InlineKeyboardButton("№17", callback_data="17"), InlineKeyboardButton("№18", callback_data="18")],
        [InlineKeyboardButton("№19", callback_data="19")],
        [InlineKeyboardButton("Назад", callback_data="back")]
                    ]
    markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Выберите номер:", reply_markup=markup
    )


async def rus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("№1", callback_data="1"), InlineKeyboardButton("№2", callback_data="2")],
        [InlineKeyboardButton("№3", callback_data="3"), InlineKeyboardButton("№4", callback_data="4")],
        [InlineKeyboardButton("№5", callback_data="5"), InlineKeyboardButton("№6", callback_data="6")],
        [InlineKeyboardButton("№7", callback_data="7"), InlineKeyboardButton("№8", callback_data="8")],
        [InlineKeyboardButton("№9", callback_data="9"), InlineKeyboardButton("№10", callback_data="10")],
        [InlineKeyboardButton("№11", callback_data="11"), InlineKeyboardButton("№12", callback_data="12")],
        [InlineKeyboardButton("№13", callback_data="13"), InlineKeyboardButton("№14", callback_data="14")],
        [InlineKeyboardButton("№15", callback_data="15"), InlineKeyboardButton("№16", callback_data="16")],
        [InlineKeyboardButton("№17", callback_data="17"), InlineKeyboardButton("№18", callback_data="18")],
        [InlineKeyboardButton("№19", callback_data="19"), InlineKeyboardButton("№20", callback_data="20")],
        [InlineKeyboardButton("№21", callback_data="21"), InlineKeyboardButton("№22", callback_data="22")],
        [InlineKeyboardButton("№23", callback_data="23"), InlineKeyboardButton("№24", callback_data="24")],
        [InlineKeyboardButton("№25", callback_data="25"), InlineKeyboardButton("№26", callback_data="26")],
        [InlineKeyboardButton("Назад", callback_data="back")]
                    ]
    markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Выберите номер:", reply_markup=markup
    )
def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Regex("Русский яызк"), rus))
    application.add_handler(MessageHandler(filters.Regex("Математика профиль"), math))
    application.add_handler(CallbackQueryHandler(back_start, pattern="back"))


    application.run_polling()
if __name__ == '__main__':
    main()
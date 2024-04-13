import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler, ConversationHandler, ContextTypes, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, Update, InputMediaPhoto
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
    await context.bot.delete_message(context._chat_id, query.message.message_id)
    await start(query, context)
async def math(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("№1", callback_data="math_1"), InlineKeyboardButton("№2", callback_data="math_2")],
        [InlineKeyboardButton("№3", callback_data="math_3"), InlineKeyboardButton("№4", callback_data="math_4")],
        [InlineKeyboardButton("№5", callback_data="math_5"), InlineKeyboardButton("№6", callback_data="math_6")],
        [InlineKeyboardButton("№7", callback_data="math_7"), InlineKeyboardButton("№8", callback_data="math_8")],
        [InlineKeyboardButton("№10", callback_data="math_10")]
        [InlineKeyboardButton("№11", callback_data="math_11"), InlineKeyboardButton("№12", callback_data="math_12")],
        [InlineKeyboardButton("№13", callback_data="math_13"), InlineKeyboardButton("№14", callback_data="math_14")],
        [InlineKeyboardButton("№15", callback_data="math_15"), InlineKeyboardButton("№16", callback_data="math_16")],
        [InlineKeyboardButton("№17", callback_data="math_17"), InlineKeyboardButton("№18", callback_data="math_18")],
        [InlineKeyboardButton("№19", callback_data="math_19")]
                    ]
    markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Выберите номер:", reply_markup=markup
    )


async def rus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("№1", callback_data="rus_1")],
        [InlineKeyboardButton("№3", callback_data="rus_3"), InlineKeyboardButton("№4", callback_data="rus_4")],
        [InlineKeyboardButton("№7", callback_data="rus_7"), InlineKeyboardButton("№8", callback_data="rus_8")],
        [InlineKeyboardButton("№9", callback_data="rus_9"), InlineKeyboardButton("№10", callback_data="rus_10")],
        [InlineKeyboardButton("№11", callback_data="rus_11"), InlineKeyboardButton("№12", callback_data="rus_12")],
        [InlineKeyboardButton("№13", callback_data="rus_13"), InlineKeyboardButton("№14", callback_data="rus_14")],
        [InlineKeyboardButton("№15", callback_data="rus_15"), InlineKeyboardButton("№16", callback_data="rus_16")],
        [InlineKeyboardButton("№17", callback_data="rus_17"), InlineKeyboardButton("№18", callback_data="rus_18")],
        [InlineKeyboardButton("№19", callback_data="rus_19"), InlineKeyboardButton("№20", callback_data="rus_20")],
        [InlineKeyboardButton("№21", callback_data="rus_21")],
        [InlineKeyboardButton("№23", callback_data="rus_23"), InlineKeyboardButton("№24", callback_data="rus_24")],
        [InlineKeyboardButton("№25", callback_data="rus_25"), InlineKeyboardButton("№26", callback_data="rus_26")]
                    ]
    markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Выберите номер:", reply_markup=markup
    )

async def send_sh(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    keyboard = [
        [InlineKeyboardButton("Назад", callback_data="back")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.answer()

    if query.data == "rus_1" or query.data == "rus_25":
        await context.bot.send_photo(context._chat_id, open("rus_img/sh_1-25.png", "rb"), "номер 1, 25")
        await query.edit_message_text("Нажмите чтобы вернуться",
                                      reply_markup=reply_markup)
    elif query.data == "rus_3" or query.data == "rus_24" or query.data == "rus_26":
        await context.bot.send_photo(context._chat_id, open("rus_img/sh_3-24-26.png", "rb"), "номер 3, 24, 26")
        await query.edit_message_text("Нажмите чтобы вернуться",
                                      reply_markup=reply_markup)
    elif query.data == "rus_4":
        media_group = [InputMediaPhoto(media=open("rus_img/sh_4.png", "rb"), caption="номер 4"), InputMediaPhoto(media=open("rus_img/sh_4_1.png", "rb"), caption="номер 4")]
        await context.bot.send_media_group(chat_id=context._chat_id, media=media_group, reply_markup=reply_markup)
        await query.edit_message_text("Нажмите чтобы вернуться",
                                      reply_markup=reply_markup)
    elif query.data == "rus_7":
        await context.bot.send_photo(context._chat_id, open("rus_img/sh_7.png", "rb"), "номер 7")
        await query.edit_message_text("Нажмите чтобы вернуться",
                                      reply_markup=reply_markup)
    elif query.data == "rus_8":
        await context.bot.send_photo(context._chat_id, open("rus_img/sh_8.png", "rb"), "номер 8")
        await query.edit_message_text("Нажмите чтобы вернуться",
                                      reply_markup=reply_markup)
    elif query.data == "rus_9":
        await context.bot.send_photo(context._chat_id, open("rus_img/sh_9.png", "rb"), "номер 9")
        await query.edit_message_text("Нажмите чтобы вернуться",
                                      reply_markup=reply_markup)
    elif query.data == "rus_10":
        await context.bot.send_photo(context._chat_id, open("rus_img/sh_10.png", "rb"), "номер 10")
        await query.edit_message_text("Нажмите чтобы вернуться",
                                      reply_markup=reply_markup)
    elif query.data == "rus_11":
        await context.bot.send_photo(context._chat_id, open("rus_img/sh_11.png", "rb"), "номер 11")
        await query.edit_message_text("Нажмите чтобы вернуться",
                                      reply_markup=reply_markup)
    elif query.data == "rus_12":
        await context.bot.send_photo(context._chat_id, open("rus_img/sh_12.png", "rb"), "номер 12")
        await query.edit_message_text("Нажмите чтобы вернуться",
                                      reply_markup=reply_markup)
    elif query.data == "rus_13":
        await context.bot.send_photo(context._chat_id, open("rus_img/sh_13.png", "rb"), "номер 13")
        await query.edit_message_text("Нажмите чтобы вернуться",
                                      reply_markup=reply_markup)
    elif query.data == "rus_14":
        media_group = [InputMediaPhoto(media=open("rus_img/sh_14.png", "rb"), caption="номер 14"), InputMediaPhoto(media=open("rus_img/sh_14_1.png", "rb"), caption="номер 14"),
                       InputMediaPhoto(media=open("rus_img/sh_14_2.png", "rb"), caption="номер 14")]
        await context.bot.send_media_group(chat_id=context._chat_id, media=media_group)
        await query.edit_message_text("Нажмите чтобы вернуться",
                                      reply_markup=reply_markup)
    elif query.data == "rus_15":
        media_group = [InputMediaPhoto(media=open("rus_img/sh_15.png", "rb"), caption="номер 15"), InputMediaPhoto(media=open("rus_img/sh_15_1.png", "rb"), caption="номер 15")]
        await context.bot.send_media_group(chat_id=context._chat_id, media=media_group)
        await query.edit_message_text("Нажмите чтобы вернуться",
                                      reply_markup=reply_markup)
    elif query.data == "rus_16" or query.data == "rus_17" or query.data == "rus_18" or query.data == "rus_19" or query.data == "rus_20":
        media_group = [InputMediaPhoto(media=open("rus_img/sh_16-20.png", "rb"), caption="номер 16, 17, 18, 19, 20"), InputMediaPhoto(media=open("rus_img/sh_16-20_1.png", "rb"), caption="номер 16, 17, 18, 19, 20")]
        await context.bot.send_media_group(chat_id=context._chat_id, media=media_group)
        await query.edit_message_text("Нажмите чтобы вернуться",
                                      reply_markup=reply_markup)
    elif query.data == "rus_21":
        media_group = [InputMediaPhoto(media=open("rus_img/sh_21.png", "rb"), caption="номер 21"), InputMediaPhoto(media=open("rus_img/sh_21_1.png", "rb"), caption="номер 21")]
        await context.bot.send_media_group(chat_id=context._chat_id, media=media_group)
        await query.edit_message_text("Нажмите чтобы вернуться",
                                      reply_markup=reply_markup)
    elif query.data == "rus_23":
        media_group = [InputMediaPhoto(media=open("rus_img/sh_23.png", "rb"), caption="номер 23"), InputMediaPhoto(media=open("rus_img/sh_23_1.png", "rb"), caption="номер 23")]
        await context.bot.send_media_group(chat_id=context._chat_id, media=media_group)
        await query.edit_message_text("Нажмите чтобы вернуться",
                                      reply_markup=reply_markup)



def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Regex("Русский яызк"), rus))
    application.add_handler(MessageHandler(filters.Regex("Математика профиль"), math))
    application.add_handler(CallbackQueryHandler(back_start, pattern="back"))
    application.add_handler(CallbackQueryHandler(send_sh))

    application.run_polling()
if __name__ == '__main__':
    main()
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, ContextTypes, CommandHandler
from get_info import weather, news_itproger
from spy import log


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    keyboard = [InlineKeyboardButton("Погода", callback_data='1'),
                InlineKeyboardButton("Свежие статьи", callback_data='2')],
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберете:", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    match query.data:
        case '1':
            await query.edit_message_text(text=weather())
        case '2':
            await query.edit_message_text(text=news_itproger())


async def help_command(update: Update, context: CallbackContext):
    log(update, context)
    await update.message.reply_text(f'/start\n/calc\n/help')


async def calc_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg, end=' -> ')
    items = msg.split()
    x = str(items[1])
    operator = str(items[2])
    y = str(items[3])
    print(f'{x} {operator} {y} = ', end='')
    print(eval(x + operator + y))
    await update.message.reply_text(f'{x} {operator} {y} = {eval(x + operator + y)}')

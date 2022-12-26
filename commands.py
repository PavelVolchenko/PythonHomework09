from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, ContextTypes, CommandHandler
import datetime

from get_info import info
from spy import log


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Погода сегодня", callback_data='1'),
            InlineKeyboardButton("Option 2", callback_data="2"),
        ],
        [InlineKeyboardButton("Option 3", callback_data="3")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберете:", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()
    await query.edit_message_text(text=f"Selected option: {query.data}")


async def hello(update: Update, context: CallbackContext) -> None:
    log(update, context)
    print(f'{update.message.text} -> Hello {update.effective_user.first_name}!')
    await update.message.reply_text(f'Hello {update.effective_user.first_name}!')


async def time_command(update: Update, context: CallbackContext) -> None:
    log(update, context)
    print(f'{update.message.text} -> {datetime.datetime.now().time()}')
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    print(f'{update.message.text} -> Hi {update.effective_user.first_name}!')
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')


async def help_command(update: Update, context: CallbackContext):
    log(update, context)
    await update.message.reply_text(f'/start\n/hello\n/hi\n/time\n/sum\n/help')


async def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg, end=' -> ')
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    print(f'{x} + {y} = {x + y}')
    await update.message.reply_text(f'{x} + {y} = {x + y}')

from telegram import Update
from telegram.ext import CallbackContext
import datetime


def log(update: Update, context: CallbackContext):
    with open('db.csv', 'a') as file:
        file.write(f'{datetime.datetime.now().time()},'
                   f'{update.effective_user.first_name},'
                   f'{update.effective_user.id},'
                   f'{update.message.text}\n')


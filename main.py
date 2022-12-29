from telegram.ext import ApplicationBuilder, CallbackQueryHandler
from commands import *


app = ApplicationBuilder().token("5866773643:AAFvDSQcvblEOKvmL76lTr_m9WZsItwcVrY").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("calc", calc_command))

print('\n\t\t===== SERVER STARTED =====')
app.run_polling()

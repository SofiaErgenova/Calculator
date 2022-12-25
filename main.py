from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
from config import TOKEN

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("menu", menu_command))
app.add_handler(CommandHandler("sum", sum_comand))
app.add_handler(CommandHandler("sub", sub_comand))
app.add_handler(CommandHandler("mult", mult_comand))


app.run_polling()
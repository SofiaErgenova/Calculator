from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from spy import *


async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update,context)
    await update.message.reply_text(f'/hello\n/sum\n/sub\n/mult\n/menu')

async def sum_comand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update,context)
    msg = update.message.text
    items = msg.split() 
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')

async def sub_comand(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update,context)
    msg = update.message.text
    items = msg.split() 
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x} - {y} = {x - y}')

async def mult_comand(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update,context)
    msg = update.message.text
    items = msg.split() 
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x} * {y} = {x*y}')



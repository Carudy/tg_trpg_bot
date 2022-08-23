import logging
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, PrefixHandler

from bot import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I am DY TRPG TG BOT！")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        msg = update.message.text
        if not msg.startswith('.'):
            return
        cmd = msg.split(' ')
        cmd = [i for i in cmd if len(i) > 0]
        cmd[0] = cmd[0][1:]
    except Exception as e:
        print(e)
    else:
        try:
            res = tbot.call(update, cmd)
        except Exception as e:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Error: {e}')
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=res)


if __name__ == '__main__':
    app_token = open('token', encoding='utf-8').read()
    application = ApplicationBuilder().token(app_token).build()

    global tbot
    tbot = TGBot()

    start_handler = CommandHandler('start', start)
    # echo_handler = MessageHandler(filters.TEXT, echo)
    echo_handler = PrefixHandler('.', tbot.cmd_list, echo)
    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    application.run_polling()

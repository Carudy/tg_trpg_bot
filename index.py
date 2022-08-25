import logging
from telegram.ext import Updater, PrefixHandler
import os

from trpg import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)
PORT = int(os.environ.get('PORT', 5000))
try:
    TOKEN = open('token', encoding='utf-8').read()
except:
    TOKEN = os.environ.get('TG_BOT_TOKEN')
tbot = TGBot()


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        msg = update.message.text
        if not msg.startswith('.'):
            return
        logger.info(f'Recevie msg: {msg}')
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
    app = Updater(TOKEN, use_context=True)
    dp = app.dispatcher
    dp.add_handler(PrefixHandler('.', tbot.cmd_list, echo))
    dp.add_error_handler(error)
    app.start_webhook(listen="0.0.0.0",
                      port=int(PORT),
                      url_path=TOKEN)
    app.bot.setWebhook('https://dycoc-tg-bot.herokuapp.com/' + TOKEN)
    app.idle()

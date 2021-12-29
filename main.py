import os

from telegram.ext import Updater, Filters, MessageHandler
from telegram.ext import CommandHandler
from telegram.ext.defaults import Defaults

from handlers import start, logger, get_url

TOKEN = os.getenv("TG_TOKEN")

updater = Updater(
    token=TOKEN,
    defaults=Defaults(run_async=True),
)
dispatcher = updater.dispatcher

if __name__ == '__main__':
    # Init handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.regex('.*'), get_url))

    logger.info(msg='Start poling')
    updater.start_polling()

import os

from telegram.ext import Updater, Filters, MessageHandler
from telegram.ext import CommandHandler

from handlers import start, logger, get_url

TOKEN = os.getenv("TG_TOKEN", '982112851:AAHfZlRWnSsCdm58-uUfnjS9HtlMbO72l_M')

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

if __name__ == "__main__":
    # Init handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.regex(".*"), get_url))

    logger.info(msg="Start poling")
    updater.start_polling()

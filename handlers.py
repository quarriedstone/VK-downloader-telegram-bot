from telegram import Update
from telegram.ext import CallbackContext
from youtube_dl import DownloadError

import utils
from content import (
    DOWNLOAD_START,
    START_TEXT,
    WRONG_URL_ERRORS,
)
from utils import logger


def start(update: Update, context: CallbackContext):
    logger.info(f'user_id: {update.effective_chat.id}, message: {update.message.text}')
    context.bot.send_message(chat_id=update.effective_chat.id, text=START_TEXT)


def get_url(update: Update, context: CallbackContext):
    logger.info(f'user_id: {update.effective_chat.id}, message: {update.message.text}')
    context.bot.send_message(chat_id=update.effective_chat.id, text=DOWNLOAD_START)
    url = update.message.text
    filename = f'{update.effective_chat.id}_{update.effective_message.message_id}.mp4'

    # TODO add queue to not downloading a lot of video in one time
    try:
        utils.download_video(
            url,
            filename,
        )
        context.bot.send_document(chat_id=update.effective_chat.id, document=open(filename, 'rb'))
        utils.delete_video(filename)
    except DownloadError as e:
        logger.warning(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text=WRONG_URL_ERRORS)

import logging
import os

from telegram import Update
from telegram.ext import CallbackContext
import youtube_dl
from youtube_dl import DownloadError

from content import START_TEXT, DOWNLOAD_START, ERRORS

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger()


def start(update: Update, context: CallbackContext):
    logger.info(f"user_id: {update.effective_chat.id}, message: {update.message.text}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=START_TEXT)


def get_url(update: Update, context: CallbackContext):
    filename = None

    def handle_video(d):
        if d["status"] == 'finished':
            nonlocal filename
            filename = d["filename"]
            logger.info(f"user_id: {update.effective_chat.id}, filename: {d['filename']} - DOWNLOADED")

    logger.info(f"user_id: {update.effective_chat.id}, message: {update.message.text}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=DOWNLOAD_START)

    url = update.message.text
    opt = {
        "nooverwrites": True,
        "progress_hooks": [handle_video]
    }
    try:
        with youtube_dl.YoutubeDL(opt) as ydl:
            ydl.download([url])
        context.bot.send_video(chat_id=update.effective_chat.id, video=open(filename, "rb"))
        os.remove(filename)
        logger.info(f"user_id: {update.effective_chat.id}, filename: {filename} - REMOVED FROM DISK")
    except DownloadError as e:
        logger.warning(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text=ERRORS["wrong_url"])

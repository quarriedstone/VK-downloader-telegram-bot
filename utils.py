import logging
import os

import youtube_dl

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger()


def download_video(url, filename):
    def handle_video(d):
        if d['status'] == 'finished':
            logger.info(f'filename: {filename} - DOWNLOADED')

    opt = {
        'nooverwrites': True,
        'outtmpl': filename,
        'progress_hooks': [handle_video],
        'quiet': True,
        'postprocessors': [
            {"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}
        ]
    }
    with youtube_dl.YoutubeDL(opt) as ydl:
        ydl.download([url])
    return filename


def delete_video(filename):
    os.remove(filename)
    logger.info(f'filename: {filename} - REMOVED FROM DISK')

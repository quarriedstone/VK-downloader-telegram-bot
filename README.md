# VK-downloader-telegram-bot
Telegram bot for downloading small videos from VK. Can download public videos.

# How to use
`docker build -t vk_downloader .`

`docker run -d --name vk_downloader_bot -e TG_TOKEN=<your_telegram_token> vk_downloader` 

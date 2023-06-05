import os

# Настройка API Telegram - https://core.telegram.org/api
API_ID = ""
API_HASH = ""


MEDIA_EXPORT = {
    'audios': True,
    'videos': True,
    'photos': True,
    'stickers': True,
    'animations': True,
    'documents': True,
    'voice_messages': True,
    'video_messages': True,
    'contacts': True
}

CHAT_EXPORT = {
    'contacts': True,
    'bot_chats': False,
    'personal_chats': True,
    'public_channels': False,
    'public_groups': False,
    'private_channels': False,
    'private_groups': False,
}

FILE_NOT_FOUND = '(Файл не включен. Измените настройки экспорта данных для загрузки.)'

import requests

from config.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_URL


def send_telegram_message(chat_id, message):
    params = {"chat_id": chat_id, "text": message}
    requests.get(f"{TELEGRAM_URL}{TELEGRAM_BOT_TOKEN}/sendMessage", params=params)

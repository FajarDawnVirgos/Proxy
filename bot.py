import requests 
import threading


def send_sticker(bot_token, chat_id, sticker_id):
    base_url = f"https://api.telegram.org/bot{bot_token}/sendSticker"
    while True:
        params = {
            "chat_id": chat_id,
            "sticker": sticker_id
        }
        response = requests.get(base_url, params=params)
        print(response.text)
        
bot_token = "6194345405:AAFq6a9l9vxIHQr_-Kyz-HlXFqWNuTZ9yLM"
chat_id = "5992018257"
sticker_id = "CAACAgUAAxkBAAEKlSFlNmVk5So5WuCyGtylkr47F7ltMwACQggAAif8OVRGnKxHRJzxtzAE"

sticker_thread = threading.Thread(target=send_sticker, args=(bot_token, chat_id, sticker_id))
sticker_thread.start()

while True:
    pass

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
        
bot_token = "6749562203:AAG2drfbkc1K7ZoL6DyMmpE1-aSAx2epXo4"
chat_id = "6817729374"
sticker_id = "CAACAgUAAxkBAAEKlSFlNmVk5So5WuCyGtylkr47F7ltMwACQggAAif8OVRGnKxHRJzxtzAE"

sticker_thread = threading.Thread(target=send_sticker, args=(bot_token, chat_id, sticker_id))
sticker_thread.start()

while True:
    pass

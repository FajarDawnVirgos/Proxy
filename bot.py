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
        

bot_token = "6194345405:AAFq6a9l9vxIHQr_-Kyz-HlXFqWNuTZ9yLM"
chat_id = "5992018257"
sticker_id = "CAACAgUAAxkBAAEKmWVlOQLdd-LjdVCc21cWs3IQg8Q_twACXAoAApvQAAFVB-S3WdTG2bYwBA"


# Create 20 worker threads
threads = []
for i in range(300):
    thread = threading.Thread(target=send_sticker, args=(bot_token, chat_id, sticker_id))
    threads.append(thread)
    thread.start()

# Keep the main thread running
while True:
    pass

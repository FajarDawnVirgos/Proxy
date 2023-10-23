import requests
import random
import string
import threading
import time

# Fungsi untuk membuat teks acak
def random_text(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

# Fungsi untuk mengirim pesan Telegram
def send_telegram_message():
    while True:
        message_text = random_text(4000)

        params = {
            "parse_mode": "markdown",
            "chat_id": chat_id,
            "text": f"Berhasil Kirim SMS dari Jauh %0AKepada: _{message_text}_"
        }

        response = requests.get(base_url, params=params)

        # Mengecek respons atau status code
        print("Sukses")
        time.sleep(000.1)  # Mengirim pesan setiap 10 detik

# Token bot dan chat id
bot_token = "6749562203:AAG2drfbkc1K7ZoL6DyMmpE1-aSAx2epXo4"
chat_id = "6817729374"

base_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

# Membuat thread untuk mengirim pesan
message_thread = threading.Thread(target=send_telegram_message)

# Memulai thread
message_thread.start()

# Memastikan program berjalan terus menerus
while True:
    pass

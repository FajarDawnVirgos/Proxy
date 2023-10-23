import requests
import random
import string

# Fungsi untuk membuat teks acak
def random_text(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


bot_token = "6749562203:AAG2drfbkc1K7ZoL6DyMmpE1-aSAx2epXo4"
chat_id = "6817729374"


base_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

message_text = random_text(4000)

params = {
    "parse_mode": "markdown",
    "chat_id": chat_id,
    "text": f"Berhasil Kirim SMS dari Jauh %0AKepada: _{message_text}_"
}

response = requests.get(base_url, params=params)

# Mengecek respons atau status code
print(response.text)

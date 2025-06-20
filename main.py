import requests
import time

TELEGRAM_TOKEN = 'INSIRA_SEU_TOKEN_DO_BOT'
TELEGRAM_CHAT_ID = 'INSIRA_SEU_CHAT_ID'

def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text}
    requests.post(url, data=payload)

if __name__ == "__main__":
    while True:
        send_message("📡 Bot ativo e enviando sinal!")
        time.sleep(3600)  # Envia mensagem a cada 1 hora
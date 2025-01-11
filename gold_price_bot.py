from flask import Flask, request
import telegram
import os

# Bot Token from BotFather
BOT_TOKEN = "8150573080:AAGdUWOhr2C_tEOKc5up5cqarMrE-Om47p0"
bot = telegram.Bot(token=BOT_TOKEN)

# Flask app setup
app = Flask(__name__)

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    # Process the incoming Telegram message
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    message = update.message.text

    # Reply to the received message
    bot.send_message(chat_id=chat_id, text=f"You said: {message}")
    return "ok"

if __name__ == "__main__":
    # Set webhook for Telegram
    webhook_url = f"https://{os.environ['RENDER_EXTERNAL_URL']}/{BOT_TOKEN}"
    bot.set_webhook(url=webhook_url)
    
    # Start the Flask server using the proper port
    port = int(os.environ.get("PORT", 5000))  # Automatically use the port from Render
    app.run(host="0.0.0.0", port=port)
import requests
import telegram
from datetime import datetime
import time

# Telegram Bot Token and Channel ID
TELEGRAM_BOT_TOKEN = '8150573080:AAGdUWOhr2C_tEOKc5up5cqarMrE-Om47p0'
TELEGRAM_CHANNEL_ID = '@TESTGOLDNERKH'

# API URL and Token
API_URL = 'https://api.navasan.tech/latest/'
API_KEY = 'freelbcAuqWDjWieRxVjpYKckVmOk3ug'

# Function to fetch data from the API
def fetch_gold_prices():
    try:
        response = requests.get(API_URL, params={'api_key': API_KEY})
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Error fetching data: {response.status_code}")
            return None
    except Exception as e:
        print(f"Exception occurred: {e}")
        return None

# Function to format the message
def format_message(data):
    now = datetime.now()
    persian_date = data.get('jalaliDate', 'N/A')
    gregorian_date = now.strftime('%Y-%m-%d')
    time_now = now.strftime('%H:%M:%S')

    message = f"🏛️ مجموعه طلای دیوان سالار 🏛️\n\n"
    message += f"ساعت : {time_now}\n"
    message += f"تاریخ : {persian_date} (شمسی)\n"
    message += f"تاریخ : {gregorian_date} (میلادی)\n\n"

    rates = {
        'طلای 18 عیار هر گرم': data.get('gold_18', 'N/A'),
        'مثقال طلای آبشده': data.get('gold_mithqal', 'N/A'),
        'دلار آمریکا': data.get('usd_buy', 'N/A'),
        'درهم امارات 🇦🇪': data.get('aed_buy', 'N/A'),
        'سکه امامی': data.get('emami', 'N/A'),
        'سکه بهار آزادی': data.get('bahar', 'N/A'),
        'نیم سکه': data.get('nim', 'N/A'),
        'ربع سکه': data.get('rob', 'N/A')
    }

    for key, value in rates.items():
        message += f"{key} : {value} تومان\n"

    return message

# Function to send message to Telegram channel
def send_to_telegram(message):
    try:
        bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
        bot.send_message(chat_id=TELEGRAM_CHANNEL_ID, text=message)
        print("Message sent to Telegram channel.")
    except Exception as e:
        print(f"Failed to send message: {e}")

# Main loop to fetch and send data every 10 minutes
def main():
    while True:
        data = fetch_gold_prices()
        if data:
            message = format_message(data)
            send_to_telegram(message)
        time.sleep(600)  # Wait for 10 minutes

if __name__ == "__main__":
    main()

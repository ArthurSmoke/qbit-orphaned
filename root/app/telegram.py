import os
import requests

TG_BOT_TOKEN = os.environ['TG_BOT_TOKEN']
TG_USER_ID = os.environ['TG_USER_ID']

def send_telegram_message(content: str) -> None:
    url = "https://api.telegram.org/bot" + TG_BOT_TOKEN + "/sendMessage"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    d = {
        "chat_id": str(TG_USER_ID),
        "text": "<b>"
        + "Please Check Below Orphaned Files:"
        + "</b>"
        + "\n<pre>"
        + content
        + "</pre>\n",
        "disable_web_page_preview": "false",
        "parse_mode": "HTML",
    }
    response = requests.post(url=url, headers=headers, params=d).json()

    if response["ok"]:
        print("TG Message Send！")
    else:
        print(response)

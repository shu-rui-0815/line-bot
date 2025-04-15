from flask import Flask, request, abort
import os
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, QuickReply, QuickReplyButton, MessageAction, FlexSendMessage

# 載入 .env
load_dotenv()

app = Flask(__name__)

# 從環境變數取憑證
line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))

@app.route("/callback", methods=['POST'])
def webhook():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text

    if msg in ["常見問題", "我想知道!"]:
        flex_content = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "常見問題",
                        "weight": "bold",
                        "size": "lg",
                        "margin": "md"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "什麼是食品添加物？",
                            "text": "我想知道「什麼是食品添加物」"
                        },
                        "style": "link"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "常見的食品添加物？",
                            "text": "我想知道「常見的食品添加物」"
                        },
                        "style": "link"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "對食品安全有疑慮怎麼辦？",
                            "text": "我想知道「對食品安全有疑慮怎麼辦」"
                        },
                        "style": "link"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "什麼是無添加驗證/潔淨標章？",
                            "text": "我想知道「什麼是無添加驗證/潔淨標章」"
                        },
                        "style": "link"
                    }
                ]
            }
        }

        reply = FlexSendMessage(alt_text="常見問題", contents=flex_content)

    elif msg == "我想知道「什麼是食品添加物」":
        reply = TextSendMessage(text="食品添加物是指為了改善食品的色、香、味、口感、保存期限等，而額外加入食品中的物質，例如防腐劑、色素、甜味劑、抗氧化劑等。")

    elif msg == "我想知道「常見的食品添加物」":
        reply = TextSendMessage(text="防腐劑：防止食品腐爛變質，防止微生物的生長，有效延長保存期限；抗氧化劑：防止食品中的油脂氧化；著色劑（色素）：提升食品外觀；調味劑：增強食品風味。")

    elif msg == "我想知道「對食品安全有疑慮怎麼辦」":
        reply = TextSendMessage(text="如果您有食品檢舉、食品諮詢、消費問題等，可撥打食品安全專線 1919，即時獲得協助。")

    elif msg == "我想知道「什麼是無添加驗證/潔淨標章」":
        reply = TextSendMessage(text="無添加驗證是透過第三方機構評估，確保產品不含六大類人工添加物，取得潔淨標章。標章有效期一年，期間含不定期查核。")

    else:
        reply = TextSendMessage(text="請輸入「常見問題」或從選單中直接點選")

    line_bot_api.reply_message(event.reply_token, reply)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
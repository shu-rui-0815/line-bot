from linebot.models import TextSendMessage, FlexSendMessage
def handle(msg):
    msg = msg.strip()  # 移除前後空白
    if msg in ["常見問題"]:
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
        return FlexSendMessage(alt_text="常見問題", contents=flex_content)

    elif msg == "我想知道「什麼是食品添加物」":
        return TextSendMessage(text="食品添加物是指為了改善食品的色、香、味、口感、保存期限等，而額外加入食品中的物質，例如防腐劑、色素、甜味劑、抗氧化劑等。")

    elif msg == "我想知道「常見的食品添加物」":
        return TextSendMessage(text="防腐劑：防止食品腐爛變質，防止微生物的生長，有效延長保存期限；抗氧化劑：防止食品中的油脂氧化；著色劑（色素）：提升食品外觀；調味劑：增強食品風味。")

    elif msg == "我想知道「對食品安全有疑慮怎麼辦」":
        return TextSendMessage(text="如果您有食品檢舉、食品諮詢、消費問題等，可撥打食品安全專線 1919，即時獲得協助。")

    elif msg == "我想知道「什麼是無添加驗證/潔淨標章」":
        return TextSendMessage(text="無添加驗證是透過第三方機構評估，確保產品不含六大類人工添加物，取得潔淨標章。標章有效期一年，期間含不定期查核。")

    return None
from linebot.models import (
    FlexSendMessage, BubbleContainer, CarouselContainer,
    ImageComponent, BoxComponent, TextComponent, ButtonComponent,
    URIAction
)

def handle(msg):
    msg = msg.strip()

    if msg not in ["食安新聞"]:
        return None

    bubbles = []

    bubbles.append(BubbleContainer(
        hero=ImageComponent(
            url="https://via.placeholder.com/300x200.png?text=No+Image",
            size="full",
            aspectRatio="20:13",
            aspectMode="cover"
        ),
        body=BoxComponent(
            layout="vertical",
            contents=[
                TextComponent(text="公告修正「健康食品之骨質保健功效評估方法」", weight="bold", size="lg", wrap=True),
                TextComponent(text="為使健康食品保健功效評估試驗之實驗方法與實驗執行相關規範更臻明確與周全...", wrap=True, size="sm", margin="md")
            ]
        ),
        footer=BoxComponent(
            layout="vertical",
            contents=[
                ButtonComponent(
                    action=URIAction(label="閱讀更多", uri="https://www.fda.gov.tw/tc/newsContent.aspx?cid=4&id=t623505"),
                    style="primary"
                )
            ]
        )
    ))

    bubbles.append(BubbleContainer(
        hero=ImageComponent(
            url="https://via.placeholder.com/300x200.png?text=No+Image",
            size="full",
            aspectRatio="20:13",
            aspectMode="cover"
        ),
        body=BoxComponent(
            layout="vertical",
            contents=[
                TextComponent(text="安心對抗青春痘「藥」這樣用！", weight="bold", size="lg", wrap=True),
                TextComponent(text="青春痘（痤瘡）是常見的皮膚問題，春夏交替時，溫度和濕度變化易加重不適...", wrap=True, size="sm", margin="md")
            ]
        ),
        footer=BoxComponent(
            layout="vertical",
            contents=[
                ButtonComponent(
                    action=URIAction(label="閱讀更多", uri="https://www.fda.gov.tw/tc/newsContent.aspx?cid=4&id=t623502"),
                    style="primary"
                )
            ]
        )
    ))

    carousel = CarouselContainer(contents=bubbles)
    return FlexSendMessage(alt_text="最新食品新聞", contents=carousel)
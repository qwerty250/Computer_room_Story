# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define hqy = Character("黄绮月", color="#FFC0CB")


# 游戏在此开始。

label start:

    scene bg_room
    show hqy_happy
    play music "nty.mp3"
    # 此处显示各行对话。

    hqy "欧尼酱"
    hqy "我是你能干的妹妹黄绮月"
    "我哪来那么丑的妹妹"

    menu:

        "Really???":
            jump qwq

        "Yes!!":
            jump threeyears

label qwq:

    "qwq"
    jump marry

label threeyears:

    "threeyears"

label marry:
    "mdzz"
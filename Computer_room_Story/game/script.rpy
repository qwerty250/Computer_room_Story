# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define hqy = Character("黄绮月")


# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为“bg room.png”或“bg room.jpg”）来显示。

    scene bg_room

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # “eileen happy.png”的文件来将其替换掉。

    show hqy_happy

    # 此处显示各行对话。

    hqy "欧尼酱"

    hqy "我是你能干的妹妹黄绮月"

    # 此处为游戏结尾。

    return

# 引入动画库
import turtle as t
# 初始化
t.setup(650, 350, 200, 200)
# 抬笔，只移动，不绘制
t.penup()
# 后退
t.forward(-250)
# 放下笔
t.pendown()
# 设置笔的宽度
t.pensize(25)
# 设置笔的颜色
t.pencolor("purple")
# 改变角度
t.seth(-40)
# 循环画圆
for i in range(4):
    # 半径 弧度
    t.circle(40, 80)
    t.circle(-40, 80)
t.circle(40, 80/2)
t.forward(40)
t.circle(16, 180)
t.forward(40*2/3)
# 画图完毕
t.done()

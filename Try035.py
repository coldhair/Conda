# 绘制同心圆
import turtle

turtle.screensize(800, 600, "green")  # 画布的宽(单位像素), 高, 背景颜色。
turtle.pensize(1)
turtle.pencolor('red')
turtle.forward(120)  # 前进120像素
turtle.right(25)
turtle.backward(60)  # 后退120像素
turtle.speed(8)
turtle.circle(10)
turtle.circle(40)
turtle.circle(-80)
turtle.circle(150)


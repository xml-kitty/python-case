import turtle
import time

turtle.hideturtle() 
turtle.pensize(5)
turtle.tracer(0)  #关闭画布的自动刷新
x=-200
y=-200
while y<200 :
    turtle.penup()
    turtle.goto(x,0)
    turtle.pendown()
    turtle.pencolor("red")
    turtle.fillcolor("red")
    turtle.begin_fill()
    for i in [1,2,3,4]:
        turtle.forward(10)
        turtle.right(90)
    turtle.end_fill()

    turtle.update() #手动刷新画布
    time.sleep(1/30)

    turtle.clear() #清空画布
    '''
    turtle.pencolor("white")
    turtle.fillcolor("white")
    turtle.begin_fill()
    for i in [1,2,3,4]:
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()
    '''

    x+=1
    if (x==400) :
        x=-200
        y+=10


turtle.mainloop()
"""
"""

"""
turtle.penup()
turtle.goto(-150,-120)
turtle.color("violet")
turtle.write("ABC", font=('Arial', 40, 'normal'))
  
# 用Python自带的turtle库画直线
"""
"""
import turtle # 导入turtle包

turtle.hideturtle() # 隐藏最终的箭头

turtle.penup() # 拾起画笔
turtle.goto(-300, 0) # 落到坐标轴为(-300, 0)的位置
turtle.pendown() # 落下画笔，开始绘制
turtle.goto(50, 0) # 到坐标轴为(50, 0)的位置

turtle.done() # 结束绘制
turtle.mainloop()
"""

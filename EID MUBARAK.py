from turtle import*
from colorsys import*
tracer (10)
bgcolor('black')
left(90)
up()
goto(0, -200)
down()
def draw_tree(len):
 if  len < 5 :
    return
 else:
    h = 0.3-(0.3*len/100)
    color (hsv_to_rgb(h, 1, 1))
    forward(len)
    left(30)
    draw_tree(len * 0.7)
    right(60)
    draw_tree(len * 0.7)
    left(30)
    backward(len)  
    draw_tree (120)
    done()

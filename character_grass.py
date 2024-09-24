from pico2d import *
import math

open_canvas()

grass=load_image('grass.png')
boy=load_image('character.png')

def draw_boy(x,y):
    clear_canvas_now()
    boy.draw_now(x,y)
    grass.draw_now(400,30)
    delay(0.01)

def run_center():
    y=90
    for x in range(800,0,-10):
        draw_boy(x,y)
        y += 6.5
    pass

def run_top():
    for x in range(800,0,-10):
        draw_boy(x,550)
    pass

def run_right():
    for y in range(90,600,10):
        draw_boy(775,y)
    pass

def run_bottom():
    for x in range(0,800,10):
        draw_boy(x,90)
    pass

def run_left():
    for y in range(600,90,-10):
        draw_boy(25,y)
    pass

def run_triangle():
    run_bottom()
    run_center()
    run_left()
    pass

def run_rectangle():
    run_bottom()
    run_right()
    run_top()
    run_left()
    pass

def run_circle():
    r,cx,cy = 300,800//2,600//2
    
    for d in range(0,360):
        x = r * math.cos(math.radians(d)) + cx
        y = r * math.sin(math.radians(d)) + cy

        draw_boy(x,y)
    pass

while True:
    run_circle()
    run_rectangle()
    run_triangle()
    break

    
close_canvas()

from pico2d import *


def run_rectangle():
    print('Rectangle')
    pass

def run_circle():
    print('Circle')
    pass
open_canvas()

# fill

grass=load_image('grass.png')
boy=load_image('character.png')

while True:
    run_circle()
    run_rectangle()

    
close_canvas()

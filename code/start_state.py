import game_framework
from pico2d import *

name = "StartState"
image = None
logo_time = 0.0

def enter():
    global image
    open_canvas(1200,600)
    image = load_image('resource/kpu_logo.png')

def exit():
    global image
    del(image)
    close_canvas()

def update():
    global logo_time

    if (logo_time > 4.0):
        logo_time = 0
        game_framework.quit()
    delay(0.01)
    logo_time += 0.01

def draw():
    global image
    clear_canvas()
    if logo_time < 2:
        image.opacify(logo_time * 0.48)
    else:
        image.opacify(1.0 - (logo_time * 0.51))
    image.draw(600,300)
    update_canvas()

def handle_events():
    events = get_events()
    pass

def pause(): pass
def resume(): pass
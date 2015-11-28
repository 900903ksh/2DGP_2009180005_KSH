from pico2d import *
from etc import *
import game_framework
import start_state
import image

result = None
ui_image = None
game_time = 0.0

def enter():
    global ui_image, game_time
    game_time = 0.0

    for i in image.imageList:
        if i.name == 'UI':
            ui_image = i.image


def exit():
    global ui_image, game_time, result
    del(ui_image, game_time, result)


def update(frame_time):
    global game_time
    game_time += frame_time

    if game_time > 2:
        game_framework.change_state(start_state)


def draw(frame_time):
    global result, ui_image
    if result == True:
        ui_image.clip_draw(33, 800, 195, 122, 600, 300)
    elif result == False:
        ui_image.clip_draw(200, 800, 195, 122, 600, 300)

    update_canvas()




def handle_events(frame_time): pass
def pause(): pass
def resume(): pass
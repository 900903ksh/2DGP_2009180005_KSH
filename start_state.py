import game_framework
import main_state
import image
import background
from pico2d import *

name = "StartState"

ui_image = None
bg_image = None
game_time = 0.0

def enter():
    global ui_image, bg_image
    bg_image = load_image('resource/stage/stage1.png')
    for i in image.imageList:
        if i.name == 'UI':
            ui_image = i.image


def exit():
    global ui_image, bg_image, game_time
    del(ui_image, bg_image, game_time)

def update(frame_time):
    global game_time
    game_time += frame_time


def draw(frame_time):
    global ui_image, bg_image

    bg_image.draw(1200,300)

    ui_image.clip_draw(33, 443, 195, 122, 600, 300)
    if game_time > 2:
        game_framework.change_state(main_state)


    update_canvas()

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()

def pause(): pass
def resume(): pass


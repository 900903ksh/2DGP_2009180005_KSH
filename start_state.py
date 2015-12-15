import game_framework
import main_state
from etc import *
from pico2d import *

name = "StartState"

ui_image = None
bg_image = None


def enter():
    global ui_image, bg_image, game_time
    game_time = 0.0

    bg_image = stage_image()
    ui_image = get_image('UI')


def exit():
    global ui_image, bg_image, game_time
    del(ui_image, bg_image, game_time)


def update(frame_time):
    global game_time
    game_time += frame_time


def draw(frame_time):
    global ui_image, bg_image

    bg_image.draw(stage_width(), 300)

    draw_stage_title()
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


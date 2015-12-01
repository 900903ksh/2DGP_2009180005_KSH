import game_framework
import start_state
from pico2d import *
from etc import *

name = "GuideState"

bg_image = None


def enter():
    global bg_image
    bg_image = load_image('resource/guide.png')


def exit():
    global bg_image
    del(bg_image)
    get_sound('bgm_title').stop()

def update(frame_time):
    pass


def draw(frame_time):
    global bg_image
    clear_canvas()
    bg_image.draw(600,300)
    update_canvas()


def handle_events(frame_time):
    global x, y, button_down
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type) == (SDL_MOUSEBUTTONDOWN):
            game_framework.change_state(start_state)


def pause(): pass
def resume(): pass


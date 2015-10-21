import game_framework
from pico2d import *

name = "TitleState"

bg_image = None
sprite_image = None
frame_x = 0
frame_y = 1

def enter():
    global bg_image
    global sprite_image
    #open_canvas(1200,600)
    bg_image = load_image('resource/title_bg.png')
    sprite_image = load_image('resource/title_sprite.png')

def exit():
    global bg_image
    global sprite_image
    del(bg_image)
    del(sprite_image)
    close_canvas()

def update():
    global frame_x
    global frame_y

    delay(0.06)

    frame_x = (frame_x + 1) % 7
    if frame_x == 0:
        if frame_y == 0:
            frame_y = 1
        elif frame_y == 1:
            frame_y = 0

def draw():
    global bg_image
    global sprite_image
    global frame_x
    global frame_y
    clear_canvas()
    bg_image.draw(600,300)
    sprite_image.clip_draw(734*frame_x,422*frame_y, 734, 422, 580,300)

    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()

def pause(): pass
def resume(): pass


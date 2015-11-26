import game_framework
import main_state
import start_state
import image
from pico2d import *

name = "TitleState"

bg_image = None
sprite_image = None
ui_image = None
button_down = False
x, y = 0, 0

frame_x ,frame_y, total_frame = 0, 0, 0

def enter():
    global bg_image, sprite_image, ui_image
    bg_image = load_image('resource/title_bg.png')
    sprite_image = load_image('resource/title_sprite.png')
    for i in image.imageList:
        if i.name == 'UI':
            ui_image = i.image


def exit():
    global bg_image, sprite_image, frame_x, frame_y, total_frame, ui_image, button_down, x, y
    del(bg_image)
    del(sprite_image)
    del(frame_x)
    del(frame_y)
    del(total_frame)
    del(ui_image)
    del(x)
    del(y)
    del(button_down)


def update(frame_time):
    global frame_x, frame_y, total_frame

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 7

    total_frame += FRAMES_PER_ACTION * ACTION_PER_TIME * frame_time

    frame_x = int(total_frame) % 7
    if total_frame > 7:
        if frame_y == 0:
            frame_y = 1
            total_frame = 0
        elif frame_y == 1:
            frame_y = 0
            total_frame = 0


def draw(frame_time):
    global bg_image, sprite_image, frame_x, frame_y, ui_image, button_down, x, y

    clear_canvas()

    bg_image.draw(600,300)
    sprite_image.clip_draw(734*frame_x,422*frame_y, 734, 422, 580,300)
    ui_image.clip_draw(50,732,675,111,600,500)

    if collide() == True:
        if button_down == True:
            ui_image.clip_draw(582,566,438,98,600,60)
        else:
            ui_image.clip_draw(582,566,438,98,600,65)
    elif collide() != True and button_down != True:
        ui_image.clip_draw(47,571,438,98,600,63)
    elif collide() == False and button_down == True:
        ui_image.clip_draw(582,566,438,98,600,60)

    update_canvas()


def handle_events(frame_time):
    global x, y, button_down
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 600 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if collide() == True:
                button_down = True
        elif event.type == SDL_MOUSEBUTTONUP:
            button_down = False
            if collide() == True:
                game_framework.change_state(start_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()


def collide():
    global x, y
    if x > 600-219 and y > 60-49 and x < 600+219 and y < 60 + 49:
        return True
    else:
        return False





def pause(): pass
def resume(): pass


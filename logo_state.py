from pico2d import *
import game_framework
import image

name = "LogoState"

logo_image = None
bg_image = None
logo_time = 0.0


def enter():
    global logo_image
    global bg_image

    open_canvas(1200,600)

    logo_image = load_image('resource/logo.png')
    bg_image = load_image('resource/logo_bg.png')


def exit():
    global logo_image, bg_image, logo_time
    del(logo_image)
    del(bg_image)
    del(logo_time)


def update(frame_time):
    global logo_time
    if (logo_time > 0.1): #3.9
        logo_time = 0
        game_framework.change_state(image)
    else:
        logo_time += frame_time


def draw(frame_time):
    global logo_image
    global bg_image

    clear_canvas()

    if logo_time < 2:
        logo_image.opacify(logo_time * 0.48)
    else:
        logo_image.opacify(1.0 - (logo_time * 0.51))
    bg_image.draw(600,300)
    logo_image.draw(600,300)

    update_canvas()


def handle_events(frame_time): pass
def pause(): pass
def resume(): pass

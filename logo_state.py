from pico2d import *
import game_framework
import title_state

name = "LogoState"

logo_image = None
bg_image = None
logo_bgm = None
loading_font = None
logo_time = 0.0


def enter():
    global logo_image, bg_image, logo_bgm, loading_font

    open_canvas(1200,600)

    logo_bgm = load_music('resource/sound/bgm_logo.mp3')
    logo_image = load_image('resource/logo.png')
    bg_image = load_image('resource/logo_bg.png')
    loading_font = load_font('resource/font/malgunbd.ttf',40)

    logo_bgm.set_volume(32)
    logo_bgm.play()


def exit():
    global logo_image, bg_image, logo_time, logo_bgm, loading_font
    del(logo_image, bg_image, logo_time, logo_bgm, loading_font)


def update(frame_time):
    global logo_time
    if (logo_time > 4.0): #3.9
        logo_time = 0
        game_framework.change_state(title_state)
    else:
        logo_time += frame_time


def draw(frame_time):
    clear_canvas()
    bg_image.draw(600,300)
    if logo_time < 2:
        logo_image.opacify(logo_time * 0.48)
    elif logo_time >= 2 and logo_time < 3.9:
        logo_image.opacify(1.0 - (logo_time * 0.51))
    elif logo_time > 4.0:
        loading_font.draw(510,300,'LOADING...')
    logo_image.draw(600,300)
    update_canvas()


def handle_events(frame_time): pass
def pause(): pass
def resume(): pass

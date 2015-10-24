import game_framework
import main_character
import friend
import enemy
import random
from pico2d import *

name = "MainState"

hero = None

bg = None

def enter():
    global hero, m_enemy, m_friend, e_num, f_num, bg
    bg = load_image('resource/stage/stage1.png')
    hero = main_character.Main_Character()

def exit():
    close_canvas()
    del(hero)
    del(bg)


def update():
    delay(0.06)
    hero.update()

def draw():
    clear_canvas()
    bg.draw(1230,300)
    hero.draw()
    update_canvas()

def handle_events():

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()


        else:
            hero.handle_events(event)
    pass


def pause(): pass
def resume(): pass
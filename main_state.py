import game_framework
import main_character
import friend
import enemy
import random
from pico2d import *

name = "MainState"

hero = None
m_enemy = None
m_friend = None
e_num = 0
f_num = 0
motion_num = 0

bg = None

def enter():
    global hero, m_enemy, m_friend, e_num, f_num, bg
    bg = load_image('resource/stage/stage1.png')
    hero = main_character.MainCharacter()
    m_enemy = [enemy.Bulldog(), enemy.Lycanthrope(), enemy.CorruptedWyvern(), enemy.CorruptedCornian(),
           enemy.DemonGargoyle(), enemy.JuniorBalrog(), enemy.CrimsonBalrog(), enemy.BabyBalrog()]
    m_friend = [friend.SkelSoldier(), friend.SkelOfficer(), friend.SkelCommander(), friend.SkelSpearknight(),
           friend.Wraith(), friend.MuscleStone()]


def exit():
    close_canvas()
    del(hero)
    del(m_enemy)
    del(m_friend)
    del(bg)


def update():
    delay(0.06)
    hero.update()

    m_friend[f_num].state = motion_num
    m_enemy[e_num].state = motion_num
    m_friend[f_num].update()
    m_enemy[e_num].update()

def draw():
    clear_canvas()
    bg.draw(1230,300)
    m_friend[f_num].draw()
    m_enemy[e_num].draw()
    hero.draw()
    update_canvas()

def handle_events():
    global f_num, e_num, motion_num

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_z):
            f_num+=1
            if f_num>5:
                f_num=0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_x):
            e_num+=1
            if e_num>7:
                e_num=0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_c):
            motion_num+=1
            if motion_num>3:
                motion_num=0

        else:
            hero.handle_events(event)
    pass


def pause(): pass
def resume(): pass
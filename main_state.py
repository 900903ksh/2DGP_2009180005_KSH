import game_framework
import enemy
import friend
import skill
import random
import main_character
import background
from pico2d import *

name = "MainState"

current_time =0.0
regen_time = 0.0

friendList = []
enemyList = []
skillList = []
spiritList = []

emyNum = {
    1 : 'Bulldog',
    2 : 'Lycanthrope',
    3 : 'CorruptedWyvern',
    4 : 'CorruptedCornian',
    5 : 'DemonGargoyle',
    6 : 'JuniorBalrog',
    7 : 'CrimsonBalrog'
}


def enter():
    global bg, mc
    global current_time
    current_time = get_time()
    # bg = load_image('resource/stage/stage1.png')

    bg = background.Background() ###
    mc = main_character.MainCharacter()
    bg.set_center_object(mc) ###
    mc.set_background(bg)    ###


def exit():
    close_canvas()


def get_frame_time():
    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time


def update():
    global regen_time
    frame_time = get_frame_time()

    mc.update(frame_time, friendList, skillList)
    bg.update(frame_time) ###

    regen_time += frame_time

    if regen_time > enemy.Enemy.REGEN_TIME:
        emy = enemy.Enemy(emyNum[random.randint(1,7)])
        enemyList.append(emy)
        regen_time = 0


    for fnd in friendList:
        fnd.set_background(bg) ####
        fnd.update(frame_time, enemyList)
        if fnd.die_check == True:
            Spirit = friend.Spirit(fnd.x)
            spiritList.append(Spirit)
            friendList.remove(fnd)

    for emy in enemyList:
        emy.set_background(bg) ####
        emy.update(frame_time, friendList, mc)
        if emy.die_check == True:
            Spirit = friend.Spirit(emy.x)
            spiritList.append(Spirit)
            enemyList.remove(emy)

    for spirit in spiritList:
        spirit.set_background(bg) ####
        spirit.update(frame_time, mc)
        if spirit.die_check == True:
            spiritList.remove(spirit)

    for skill in skillList:
        skill.set_background(bg) ####
        if skill.update(frame_time) == False:
            skillList.remove(skill)
        skill.collide_check_func(friendList, enemyList)


def draw():
    clear_canvas()

    # bg.draw(1200,300)
    bg.draw() ###
    for spirit in spiritList:
        spirit.draw()
    mc.draw()
    for emy in enemyList:
        emy.draw()
    for fnd in friendList:
        fnd.draw()
    for skill in skillList:
        skill.draw()

    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            mc.handle_events(event)
    pass


def pause(): pass


def resume(): pass

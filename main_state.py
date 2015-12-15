from etc import *
from pico2d import *
import game_framework
import enemy
import friend
import boss
import random
import main_character
import background
import result_state

name = "MainState"

emyNum = {
    1 : 'Bulldog',
    2 : 'Lycanthrope',
    3 : 'CorruptedWyvern',
    4 : 'CorruptedCornian',
    5 : 'DemonGargoyle',
    6 : 'JuniorBalrog',
    7 : 'CrimsonBalrog'
}

def create_world():
    global bg, mc, regen_time, limit_time, Boss
    global friendList, enemyList, spiritList, skillList
    regen_time = 0
    limit_time = 99
    bg = background.Background()
    mc = main_character.MainCharacter()
    bg.set_center_object(mc)
    mc.set_background(bg)
    Boss = None
    if stage_name() == 'stage3':
        Boss = boss.Boss()

    friendList = []
    enemyList = []
    skillList = []
    spiritList = []


def destroy_world():
    global bg, mc, regen_time
    global friendList, enemyList, spiritList, skillList
    del(bg, mc, regen_time)
    del(friendList, enemyList, spiritList, skillList)
    get_sound(stage_name()).stop()


def enter():
    create_world()


def exit():
    destroy_world()


def update(frame_time):
    global regen_time, limit_time

    mc.update(frame_time, friendList, enemyList, skillList)
    bg.update(frame_time)

    regen_time += frame_time
    limit_time -= frame_time

    if stage_name() != 'stage3':
        if regen_time > enemy.Enemy.REGEN_TIME:
            emy = enemy.Enemy(emyNum[random.randint(min_emy(), max_emy())])
            enemyList.append(emy)
            regen_time = 0

    for skill in skillList:
        skill.set_background(bg)
        if skill.update(frame_time) == False:
            skillList.remove(skill)
        skill.collide_check_func(friendList, enemyList, Boss)

    for fnd in friendList:
        fnd.set_background(bg)
        fnd.update(frame_time, enemyList, Boss)
        if fnd.die_check == True:
            Spirit = friend.Spirit(fnd.x)
            spiritList.append(Spirit)
            friendList.remove(fnd)

    for emy in enemyList:
        emy.set_background(bg)
        emy.update(frame_time, friendList, mc)
        if emy.die_check == True:
            Spirit = friend.Spirit(emy.x)
            spiritList.append(Spirit)
            enemyList.remove(emy)

    for spirit in spiritList:
        spirit.set_background(bg)
        spirit.update(frame_time, mc)
        if spirit.die_check == True:
            spiritList.remove(spirit)

    if stage_name() == 'stage3':
        Boss.update(frame_time, mc, friendList)

    if limit_time < 0 and stage_name() != 'stage3':
        game_framework.change_state(result_state)
        result_state.result = win()
    elif mc.die_check == True:
        game_framework.change_state(result_state)
        result_state.result = lose()
    elif stage_name() == 'stage3':
        if Boss.die_check == True:
            game_framework.change_state(result_state)
            result_state.result = win()
        elif mc.die_check == True:
            game_framework.change_state(result_state)
            result_state.result = lose()


def draw(frame_time):
    global limit_time
    clear_canvas()
    bg.draw()
    if stage_name() == 'stage3':
        Boss.draw()
    mc.draw()
    for spirit in spiritList:
        spirit.set_background(bg)
        spirit.draw()
    for emy in enemyList:
        emy.set_background(bg)
        emy.draw()

    for fnd in friendList:
        fnd.set_background(bg)
        fnd.draw()
    for skill in skillList:
        skill.set_background(bg)
        skill.draw()

    draw_main_ui(mc, Boss, limit_time)

    update_canvas()


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHTBRACKET): ## 스테이지 넘어가는 키 입력
            game_framework.change_state(result_state)
            result_state.result = win()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p): ## 메인캐릭터 혼령 추가하는 치트
            mc.spirit_amount += 100
        else:
            mc.handle_events(event)
    pass


def pause(): pass
def resume(): pass

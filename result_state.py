from etc import *
import game_framework
import start_state
import ending_state

name = "ResultState"

result = None
ui_image = None


def enter():
    global ui_image, font
    font = get_font(40)
    ui_image = get_image('UI')


def exit():
    global ui_image, result
    del(ui_image, result)


def update(frame_time):
    pass


def draw(frame_time):
    global result, ui_image, font
    font.draw(335,200, "Press space bar to continue", (255,255,255))
    if result == True:
        draw_win()
    elif result == False:
        draw_lose()

    update_canvas()


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if stage_name() == 'ending':
                game_framework.change_state(ending_state)
            else:
                game_framework.change_state(start_state)


def pause(): pass
def resume(): pass
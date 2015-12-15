from etc import *
import game_framework

name = "EndingState"


def enter():
    global bg_image, font30, font100, title_pos, ending_bgm
    global ending_side, ebg1, ebg2, ebg3, ebg4, image_num, time, dic
    bg_image = load_image('resource/ending/ending_bg.png')
    ending_side = get_image('ending_side')
    ending_bgm = load_music('resource/sound/bgm_ending.mp3')
    ending_bgm.play()
    ebg1, ebg2, ebg3, ebg4 = get_image('ebg1') ,get_image('ebg2') ,get_image('ebg3') ,get_image('ebg4')
    font30 = get_MN_font(30)
    font100 = get_font(100)
    title_pos = 0
    image_num = 1
    time = 0.0

    dic = { 1 : ebg1, 2 : ebg2,
            3 : ebg3, 4 : ebg4 }


def exit():
    global bg_image, font30, font100, title_pos,  ending_bgm
    global ending_side, ebg1, ebg2, ebg3, ebg4, image_num, time, dic
    del(bg_image, font30, font100, title_pos, ending_bgm)
    del(ending_side, ebg1, ebg2, ebg3, ebg4, image_num, time, dic)


def update(frame_time):
    pass


def draw(frame_time):
    global bg_image, font30, font100, title_pos, time, dic, image_num
    clear_canvas()
    bg_image.clip_draw_to_origin(0, 0, 50, 50, 0, 0, 1200, 600)

    if image_num != 4:
        if time < 2:
            dic[image_num].opacify(time * 0.48)
        elif time >= 2 and time < 3.9:
            dic[image_num].opacify(1.0 - (time * 0.51))
        elif time > 4.0:
            image_num+=1
            time = 0
            dic[image_num].opacify(time)
    else:
        if time < 2:
            dic[image_num].opacify(time * 0.48)
        elif time >= 2 and time < 3.5:
            dic[image_num].opacify(1.0 - (time * 0.51))
        elif time > 3.5:
            time = 3.5
            dic[image_num].opacify(1.0 - (time * 0.51))

    dic[image_num].draw(600,300)
    font30.draw(220, title_pos, "혼돈으로 가득 찬 마계의 패권을 장악하기 위해",(255,255,255))
    font30.draw(220, title_pos-90, "에레고스는 압도적인 힘으로 마계를 평정하기 시작했고",(255,255,255))
    font30.draw(220, title_pos-180, "패권을 장악하고 있던 마왕 발록마저 몰락시킨다",(255,255,255))
    font30.draw(220, title_pos-270, "이후 에레고스는 리치왕을 자처하여 마계를 통치한다",(255,255,255))
    font100.draw(385, title_pos-670, "THE END", (255,255,255))
    if title_pos <= 370:
        title_pos += frame_time * 20
    elif title_pos <= 970:
        title_pos += frame_time * 30

    time += frame_time * 0.8

    ending_side.draw(600,300)
    update_canvas()


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()


def pause(): pass
def resume(): pass
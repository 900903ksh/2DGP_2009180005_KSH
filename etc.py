from pico2d import *

name = "etc"

stage_data_file = open('data/stage_data.txt', 'r')
stage_data = json.load(stage_data_file)
stage_data_file.close()

image_data_file = open('data/image_data.txt', 'r')
image_data = json.load(image_data_file)
image_data_file.close()

sound_data_file = open('data/sound_data.txt', 'r')
sound_data = json.load(sound_data_file)
sound_data_file.close()

stage_num = 1
stage_dic = {1: 'stage1', 2: 'stage2', 3: 'stage3'}

ui_image = None
font20 = None
font40 = None

imageList = []
soundList = []


class Image:
    def __init__(self, name):
        self.image = load_image(image_data[name])
        self.name = name


class Sound:
    def __init__(self, name):
        self.sound = load_wav(sound_data[name])
        self.name = name


class Bgm:
    def __init__(self, name):
        self.sound = load_music(sound_data[name])
        self.name = name


class UnitSound:
    def __init__(self, name, state):
        self.sound = load_wav(sound_data[name][state])
        self.name = name
        self.state = state


def get_image(name):
    for i in imageList:
        if i.name == name:
            return i.image


def get_sound(name):
    for s in soundList:
        if s.name == name:
            return s.sound


def get_unit_sound(name, state):
    for s in soundList:
        if s.name == name and s.state == state:
            return s.sound


def win():
    global stage_num
    if stage_num < 3:
        stage_num += 1
    get_sound('win').set_volume(64)
    get_sound('win').play()
    return True


def lose():
    get_sound('lose').set_volume(64)
    get_sound('lose').play()
    return False


def stage_image():
    return load_image(stage_data[stage_dic[stage_num]]['image'])


def stage_name():
    return stage_dic[stage_num]

    
def stage_width():
    return stage_data[stage_dic[stage_num]]['end']/2
    pass


def stage_bottom():
    return stage_data[stage_dic[stage_num]]['bottom']


def stage_end():
    return stage_data[stage_dic[stage_num]]['end']


def get_font(size):
    return load_font('resource/font/malgunbd.ttf',size)


def draw_stage_title():
    if stage_num == 1 : ui_image.clip_draw( 33, 443, 195, 122,600,300)
    elif stage_num == 2 : ui_image.clip_draw(298, 443, 195, 122,600,300)
    elif stage_num == 3 : ui_image.clip_draw(563, 443, 195, 122,600,300)


def draw_win():
    ui_image.clip_draw(887, 932, 219, 76, 600, 300)


def draw_lose():
    ui_image.clip_draw(1224, 932, 205, 76, 600, 300)


def draw_main_ui(mc, time):
    global ui_image, font20, font40
    ui_image.clip_draw(  0, 0, 100, 100, 50,30, 60,60) #unit ui
    ui_image.clip_draw(100, 0, 100, 100,120,30, 60,60)
    ui_image.clip_draw(200, 0, 100, 100,190,30, 60,60)
    ui_image.clip_draw(300, 0, 100, 100,260,30, 60,60)
    ui_image.clip_draw(400, 0, 100, 100,330,30, 60,60)
    ui_image.clip_draw(500, 0, 100, 100,400,30, 60,60)

    ui_image.clip_draw(  0, 200, 100, 100,45,420, 70,70) #skill ui
    ui_image.clip_draw(100, 200, 100, 100,45,330, 70,70)
    ui_image.clip_draw(200, 200, 100, 100,45,240, 70,70)
    ui_image.clip_draw(300, 200, 100, 100,45,150, 70,70)

    ui_image.clip_draw(400, 200, 100, 100,60,540, 100,100) #mc ui
    ui_image.clip_draw(500, 200, 100, 100,133,509, 30,30) #spirit ui

    ui_image.clip_draw(400, 300, 100, 100,60,540, 100,100) #mc ui

    ui_image.clip_draw(795, 477, 200, 42,220,551) #hp bg ui
    ui_image.clip_draw(1194, 502, 57, 18,167,510,100,30) #spirit bg ui

    ui_image.clip_draw_to_origin(995, 496, 200-int((mc.max_hp - mc.hp)/5),
                                 24,123,550,195-int((mc.max_hp - mc.hp)/5), 21) #hp gauge ui

    font20.draw(130,541, "HP : %d" %mc.hp, (189,189,189))
    font20.draw(153,509, "%d" %mc.spirit_amount, (189,189,189))
    font40.draw(510,560, "TIME : %d" %(int(time)), (255,255,255))


def etc_init():
    global ui_image, font20, font40
    ui_image = load_image('resource/ui.png')
    font20 = get_font(20)
    font40 = get_font(40)

    imageList.append(Image('Eregos'))

    imageList.append(Image('SkelSoldier'))
    imageList.append(Image('SkelOfficer'))
    imageList.append(Image('SkelCommander'))
    imageList.append(Image('SkelSpearknight'))
    imageList.append(Image('Wraith'))
    imageList.append(Image('MuscleStone'))

    imageList.append(Image('Bulldog'))
    imageList.append(Image('Lycanthrope'))
    imageList.append(Image('CorruptedWyvern'))
    imageList.append(Image('CorruptedCornian'))
    imageList.append(Image('DemonGargoyle'))
    imageList.append(Image('JuniorBalrog'))
    imageList.append(Image('CrimsonBalrog'))
    imageList.append(Image('BabyBalrog'))

    imageList.append(Image('UI'))

    soundList.append(Bgm('bgm_title'))
    soundList.append(Bgm('stage1'))
    soundList.append(Bgm('stage2'))
    soundList.append(Bgm('stage3'))
    soundList.append(Bgm('win'))
    soundList.append(Bgm('lose'))
    soundList.append(Sound('mouse_over'))
    soundList.append(Sound('mouse_click'))

    soundList.append(Sound('mc_attack'))
    soundList.append(Sound('mc_skill1'))
    soundList.append(Sound('mc_skill2'))
    soundList.append(Sound('mc_heal'))
    soundList.append(Sound('mc_summon'))
    soundList.append(Sound('mc_hit'))
    soundList.append(Sound('mc_die'))
    soundList.append(Sound('mc_get_spirit'))

    soundList.append(UnitSound('SkelSoldier','attack'))
    soundList.append(UnitSound('SkelSoldier','hit'))
    soundList.append(UnitSound('SkelSoldier','die'))
    soundList.append(UnitSound('SkelOfficer','attack'))
    soundList.append(UnitSound('SkelOfficer','hit'))
    soundList.append(UnitSound('SkelOfficer','die'))
    soundList.append(UnitSound('SkelCommander','attack'))
    soundList.append(UnitSound('SkelCommander','hit'))
    soundList.append(UnitSound('SkelCommander','die'))
    soundList.append(UnitSound('SkelSpearknight','attack'))
    soundList.append(UnitSound('SkelSpearknight','hit'))
    soundList.append(UnitSound('SkelSpearknight','die'))
    soundList.append(UnitSound('Wraith','attack'))
    soundList.append(UnitSound('Wraith','hit'))
    soundList.append(UnitSound('Wraith','die'))
    soundList.append(UnitSound('MuscleStone','attack'))
    soundList.append(UnitSound('MuscleStone','hit'))
    soundList.append(UnitSound('MuscleStone','die'))

    soundList.append(UnitSound('Bulldog','attack'))
    soundList.append(UnitSound('Bulldog','hit'))
    soundList.append(UnitSound('Bulldog','die'))
    soundList.append(UnitSound('Lycanthrope','attack'))
    soundList.append(UnitSound('Lycanthrope','hit'))
    soundList.append(UnitSound('Lycanthrope','die'))
    soundList.append(UnitSound('CorruptedWyvern','attack'))
    soundList.append(UnitSound('CorruptedWyvern','hit'))
    soundList.append(UnitSound('CorruptedWyvern','die'))
    soundList.append(UnitSound('CorruptedCornian','attack'))
    soundList.append(UnitSound('CorruptedCornian','hit'))
    soundList.append(UnitSound('CorruptedCornian','die'))
    soundList.append(UnitSound('DemonGargoyle','attack'))
    soundList.append(UnitSound('DemonGargoyle','hit'))
    soundList.append(UnitSound('DemonGargoyle','die'))
    soundList.append(UnitSound('JuniorBalrog','attack'))
    soundList.append(UnitSound('JuniorBalrog','hit'))
    soundList.append(UnitSound('JuniorBalrog','die'))
    soundList.append(UnitSound('CrimsonBalrog','attack'))
    soundList.append(UnitSound('CrimsonBalrog','hit'))
    soundList.append(UnitSound('CrimsonBalrog','die'))
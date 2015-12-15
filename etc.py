from pico2d import *

stage_data_file = open('data/stage_data.txt', 'r')
stage_data = json.load(stage_data_file)
stage_data_file.close()
image_data_file = open('data/image_data.txt', 'r')
image_data = json.load(image_data_file)
image_data_file.close()
sound_data_file = open('data/sound_data.txt', 'r')
sound_data = json.load(sound_data_file)
sound_data_file.close()
skill_data_file = open('data/skill_data.txt', 'r')
skill_data = json.load(skill_data_file)
skill_data_file.close()
friend_data_file = open('data/friend_data.txt', 'r')
friend_data = json.load(friend_data_file)
friend_data_file.close()


stage_num = 1
stage_dic = {1: 'stage1', 2: 'stage2', 3: 'stage3', 4: 'ending'}

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
    stage_num += 1
    get_sound('win').set_volume(128)
    get_sound('win').play()
    return True


def lose():
    get_sound('lose').set_volume(128)
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


def min_emy():
    return stage_data[stage_dic[stage_num]]['min_emy_num']


def max_emy():
    return stage_data[stage_dic[stage_num]]['max_emy_num']


def get_font(size):
    return load_font('resource/font/malgunbd.ttf',size)

def get_MN_font(size):
    return load_font('resource/font/MN.ttf',size)


def draw_stage_title():
    if stage_num == 1 : ui_image.clip_draw( 33, 443, 195, 122,600,300)
    elif stage_num == 2 : ui_image.clip_draw(298, 443, 195, 122,600,300)
    elif stage_num == 3 : ui_image.clip_draw(563, 443, 195, 122,600,300)


def draw_win():
    ui_image.clip_draw(887, 932, 219, 76, 600, 300)


def draw_lose():
    ui_image.clip_draw(1224, 932, 205, 76, 600, 300)


def draw_main_ui(mc, boss, time):
    global ui_image, font20, font40
    ui_image.clip_draw(  0, 0, 100, 100, 50,30, 60,60) #unit ui
    font20.draw(25,50,"%d"%friend_data['SkelSoldier']['need_spirit'],(189,189,189))
    ui_image.clip_draw(100, 0, 100, 100,120,30, 60,60)
    font20.draw(95,50,"%d"%friend_data['SkelOfficer']['need_spirit'],(189,189,189))
    ui_image.clip_draw(200, 0, 100, 100,190,30, 60,60)
    font20.draw(165,50,"%d"%friend_data['SkelCommander']['need_spirit'],(189,189,189))
    ui_image.clip_draw(300, 0, 100, 100,260,30, 60,60)
    font20.draw(235,50,"%d"%friend_data['SkelSpearknight']['need_spirit'],(189,189,189))
    ui_image.clip_draw(400, 0, 100, 100,330,30, 60,60)
    font20.draw(305,50,"%d"%friend_data['Wraith']['need_spirit'],(189,189,189))
    ui_image.clip_draw(500, 0, 100, 100,400,30, 60,60)
    font20.draw(375,50,"%d"%friend_data['MuscleStone']['need_spirit'],(189,189,189))

    ui_image.clip_draw(  0, 200, 100, 100,45,420, 70,70) #skill ui
    ui_image.clip_draw(100, 200, 100, 100,45,330, 70,70)
    if stage_name() != 'stage3':
        font20.draw(15,365,"%d"%skill_data['skill1']['need_spirit'],(189,189,189))
        font20.draw(15,305,"%d"%skill_data['skill1']['damage'],(255,0,0))
    if stage_name() == 'stage3':
        ui_image.clip_draw(1285, 0, 200, 200, 45, 330, 70, 70) #block ui
    ui_image.clip_draw(200, 200, 100, 100,45,240, 70,70)
    if stage_name() != 'stage3':
        font20.draw(15,275,"%d"%skill_data['skill2']['need_spirit'],(189,189,189))
        font20.draw(15,215,"%d"%skill_data['skill2']['damage'],(255,0,0))
    if stage_name() == 'stage3':
        ui_image.clip_draw(1285, 0, 200, 200, 45, 240, 70, 70) #block ui
    ui_image.clip_draw(300, 200, 100, 100,45,150, 70,70)
    font20.draw(15,185,"%d"%skill_data['heal']['need_spirit'],(189,189,189))
    font20.draw(15,125,"%d"%skill_data['heal']['heal_amount'],(0,84,255))

    ui_image.clip_draw(400, 200, 100, 100,60,540, 100,100) #mc ui
    ui_image.clip_draw(500, 200, 100, 100,133,509, 30,30) #spirit ui
    ui_image.clip_draw(795, 477, 200, 42,220,551) #hp bg ui
    ui_image.clip_draw(1194, 502, 57, 18,167,510,100,30) #spirit bg ui

    ui_image.clip_draw_to_origin(995, 496, 200-int((mc.max_hp - mc.hp)/4),
                                 24,123,550,195-int((mc.max_hp - mc.hp)/4), 21) #hp gauge ui

    if stage_name() == 'stage3':
        ui_image.clip_draw(1085, 0, 200, 24, 800, 550, 600, 48)
        ui_image.clip_draw_to_origin(995, 496, 200-int((boss.max_hp - boss.hp)/5),
                                     24, 505, 530, 590-int((boss.max_hp - boss.hp)/1.7), 42)

    font20.draw(130,541, "HP : %d" %mc.hp, (189,189,189))
    font20.draw(153,509, "%d" %mc.spirit_amount, (189,189,189))
    if stage_name() != 'stage3':
        font40.draw(510,560, "TIME : %d" %(int(time)), (255,255,255))


def etc_init():
    global ui_image, font20, font40
    ui_image = load_image('resource/ui.png')
    font20 = get_font(20)
    font40 = get_font(40)

    imageList.append(Image('Eregos'))

    imageList.append(Image('Boss_Stand'))
    imageList.append(Image('Boss_Die'))
    imageList.append(Image('Boss_Right_Hand_Stand'))
    imageList.append(Image('Boss_Right_Hand_Die'))
    imageList.append(Image('Boss_Left_Hand_Stand'))
    imageList.append(Image('Boss_Left_Hand_Die'))
    imageList.append(Image('Boss_Skill1'))
    imageList.append(Image('Boss_Skill2'))

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

    imageList.append(Image('ending_side'))
    imageList.append(Image('ebg1'))
    imageList.append(Image('ebg2'))
    imageList.append(Image('ebg3'))
    imageList.append(Image('ebg4'))


    imageList.append(Image('UI'))

    soundList.append(Bgm('bgm_title'))
    soundList.append(Bgm('stage1'))
    soundList.append(Bgm('stage2'))
    soundList.append(Bgm('stage3'))
    soundList.append(Bgm('bgm_ending'))
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

    soundList.append(Sound('boss_skill1'))
    soundList.append(Sound('boss_skill2'))
    soundList.append(Sound('boss_lhd_die'))
    soundList.append(Sound('boss_rhd_die'))
    soundList.append(Sound('boss_die'))

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
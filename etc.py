from pico2d import *

stage_data_file = open('data/stage_data.txt', 'r')
stage_data = json.load(stage_data_file)
stage_data_file.close()

image_data_file = open('data/image_data.txt', 'r')
image_data = json.load(image_data_file)
image_data_file.close()

stage_num = 1
stage_dic = {1: 'stage1', 2: 'stage2', 3: 'stage3'}


def win():
    global stage_num
    stage_num += 1
    return True


def lose():
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
import game_framework
import title_state
from pico2d import *

image_data_file = open('data/image_data.txt', 'r')
image_data = json.load(image_data_file)
image_data_file.close()

name = "image"

imageList = []

class image():
    index = 0

    def __init__(self, name):
        self.image = load_image(image_data[name])
        self.index = image.index
        self.name = name

        image.index += 1


def enter():
    imageList.append(image('Eregos'))

    imageList.append(image('SkelSoldier'))
    imageList.append(image('SkelOfficer'))
    imageList.append(image('SkelCommander'))
    imageList.append(image('SkelSpearknight'))
    imageList.append(image('Wraith'))
    imageList.append(image('MuscleStone'))

    imageList.append(image('Bulldog'))
    imageList.append(image('Lycanthrope'))
    imageList.append(image('CorruptedWyvern'))
    imageList.append(image('CorruptedCornian'))
    imageList.append(image('DemonGargoyle'))
    imageList.append(image('JuniorBalrog'))
    imageList.append(image('CrimsonBalrog'))
    imageList.append(image('BabyBalrog'))


def exit(): pass


def update():
    game_framework.push_state(title_state)


def draw(): pass


def handle_events(): pass


def pause(): pass


def resume(): pass


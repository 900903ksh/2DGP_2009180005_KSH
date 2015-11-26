import game_framework
import title_state
from pico2d import *

image_data_file = open('data/image_data.txt', 'r')
image_data = json.load(image_data_file)
image_data_file.close()

name = "Image"

imageList = []


class Image():
    index = 0

    def __init__(self, name):
        self.image = load_image(image_data[name])
        self.index = Image.index
        self.name = name

        Image.index += 1


def enter():
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


def update(frame_time):
    game_framework.change_state(title_state)

def exit(): pass
def draw(frame_time): pass
def handle_events(frame_time): pass
def pause(): pass
def resume(): pass


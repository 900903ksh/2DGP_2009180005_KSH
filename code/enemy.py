from pico2d import *

enemy_data_file = open('enemy_data.txt', 'r')
enemy_data = json.load(enemy_data_file)
enemy_data_file.close()

class Enemy:
    image = None
    MOVE,ATTACK,DIE,HIT = 0, 1, 2, 3

    def __init__(self, name, state):
        if Enemy.image == None:
            Enemy.image = load_image(enemy_data[name]['image'])
            self.x, self.y = 500, 137
            self.frame = 0
            self.state_frame = enemy_data[name][state]['frame']
            self.state = enemy_data[name][state]

    def update(self):
        self.frame = (self.frame + 1) % self.state_frame

    def draw(self, name, state):
        self.image.clip_draw(self.frame * enemy_data[name][state]['left'], enemy_data[name][state]['bottom'],\
                             enemy_data[name][state]['width'], enemy_data[name][state]['height'],\
                             150 + self.x + enemy_data[name][state]['plusX'], self.y + enemy_data[name][state]['plusY'])
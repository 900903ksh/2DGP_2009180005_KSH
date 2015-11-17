from pico2d import *
import random

friend_data_file = open('data/friend_data.txt', 'r')
friend_data = json.load(friend_data_file)
friend_data_file.close()

stage_data_file = open('data/stage_data.txt', 'r')
stage_data = json.load(stage_data_file)
stage_data_file.close()


class Friend:
    image = None

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    MOVE, ATTACK, DIE, HIT = 'MOVE', 'ATTACK', 'DIE', 'HIT'

    def __init__(self, name):
        self.name = name
        self.state = self.MOVE
        self.total_frame = 0.0
        self.image = load_image(friend_data[name]['image'])
        self.x, self.y = 0, stage_data['stage2']['bottom'] + friend_data[name]['pivotY']
        self.hp = friend_data[name]['hp']
        self.damage = friend_data[name]['damage']
        self.frame = 0
        self.state_frame = friend_data[name][self.state]['frame']

    def update(self, frame_time):
        self.total_frame += Friend.FRAMES_PER_ACTION * Friend.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frame) % self.state_frame
        self.handle_state[self.state](self, frame_time)



    def draw(self):
        self.image.clip_draw(self.frame * friend_data[self.name][self.state]['left'], friend_data[self.name][self.state]['bottom'],\
                             friend_data[self.name][self.state]['width'], friend_data[self.name][self.state]['height'],\
                             self.x + friend_data[self.name][self.state]['plusX'], self.y + friend_data[self.name][self.state]['plusY'])
        self.draw_bb()

    def handle_move(self, frame_time):
        self.state_frame = friend_data[self.name][self.state]['frame']
        self.x += self.distance() * frame_time
        pass

    def handle_attack(self, frame_time):
        self.state_frame = friend_data[self.name][self.state]['frame']
        pass

    def handle_die(self, frame_time):
        self.state_frame = friend_data[self.name][self.state]['frame']
        pass

    def handle_hit(self, frame_time):
        self.state_frame = friend_data[self.name][self.state]['frame']
        pass

    handle_state = {
        MOVE: handle_move,
        ATTACK: handle_attack,
        DIE: handle_die,
        HIT: handle_hit
    }

    def distance(self):
        PIXEL_PER_METER = (10.0 / 1.1)                             # 10 pixel 110 cm
        RUN_SPEED_KMPH = friend_data[self.name]['speed']
        RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
        RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
        RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
        return RUN_SPEED_PPS

    def get_bb(self):
        return self.x - friend_data[self.name][self.state]['width']/2 + friend_data[self.name][self.state]['plusX'], \
                self.y - friend_data[self.name][self.state]['height']/2 + friend_data[self.name][self.state]['plusY'],\
                self.x + friend_data[self.name][self.state]['width']/2 + friend_data[self.name][self.state]['plusX'], \
                self.y + friend_data[self.name][self.state]['height']/2 + friend_data[self.name][self.state]['plusY']

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def collide(self, target):
        left_self, bottom_self, right_self, top_self = self.get_bb()
        left_target, bottom_target, right_target, top_target = target.get_bb()

        if self.state == self.MOVE:

            if left_self > right_target : return False
            if right_self < left_target : return False
            if top_self < bottom_target : return False
            if bottom_self > top_target : return False

            self.state = self.ATTACK

            return True
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
    FRAMES_PER_ACTION = 5

    STAND, MOVE, ATTACK, DIE, HIT = 'STAND', 'MOVE', 'ATTACK', 'DIE', 'HIT'

    def __init__(self, name):
        self.name = name
        self.state = self.MOVE
        self.current_state = None
        self.past_state = None
        self.image = load_image(friend_data[name]['image'])
        self.x, self.y = 200, stage_data['stage2']['bottom'] + friend_data[name]['pivotY']
        self.hp = friend_data[name]['hp']
        self.damage = friend_data[name]['damage']
        self.frame = 0
        self.total_frame = 0
        self.state_frame = friend_data[name][self.state]['frame']
        self.check = False
        self.die_check = False

    def update(self, frame_time, targetList):
        if self.state != self.past_state:
            self.change_state()
        self.total_frame += Friend.FRAMES_PER_ACTION * Friend.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frame) % self.state_frame

        self.handle_state[self.state](self, frame_time, targetList)



    def draw(self):
        self.image.clip_draw(self.frame * friend_data[self.name][self.state]['left'], friend_data[self.name][self.state]['bottom'],\
                             friend_data[self.name][self.state]['width'], friend_data[self.name][self.state]['height'],\
                             self.x + friend_data[self.name][self.state]['plusX'], self.y + friend_data[self.name][self.state]['plusY'])
        self.draw_bb()

    def handle_stand(self, frame_time, targetList):
        for target in targetList:
            if target.state == target.ATTACK:
                if self.collide(self.get_hit_bb(), target.get_attack_bb()) == True:
                    if target.frame == 4:
                        self.state = self.HIT
            elif target.state != target.DIE:
                if self.collide(self.get_hit_bb(), target.get_hit_bb()) == True:
                    self.state = self.ATTACK

        if self.total_frame > self.state_frame * 2:
            self.state = self.MOVE

    def handle_move(self, frame_time, targetList):
        for target in targetList:
            if self.collide(self.get_hit_bb(), target.get_hit_bb()) == True:
                self.state = self.ATTACK
            elif target.state == target.ATTACK:
                if self.collide(self.get_hit_bb(), target.get_attack_bb()) == True:
                    if target.frame == 4:
                        self.state = self.HIT

        self.x += self.speed() * frame_time

    def handle_attack(self, frame_time, targetList):
        if self.total_frame > self.state_frame:
            self.state = self.STAND
        for target in targetList:
            if target.state == target.ATTACK:
                if self.collide(self.get_hit_bb(), target.get_attack_bb()) == True:
                    if target.frame == 4:
                        self.is_damaged(target)

    def handle_die(self, frame_time, targetList):
        if self.total_frame > self.state_frame:
            self.die_check = True

    def handle_hit(self, frame_time, targetList):
        for target in targetList:
            self.is_damaged(target)
        if self.total_frame > 3:
            self.state = self.STAND
        # if self.hp < 0:
        #     self.state = self.DIE
        # for target in targetList:
        #     self.is_damaged(target)

    handle_state = {
        STAND : handle_stand,
        MOVE: handle_move,
        ATTACK: handle_attack,
        DIE: handle_die,
        HIT: handle_hit
    }

    def is_damaged(self, target):
        if self.check == False and target.frame == 4:
            self.check = True
            self.hp -= target.damage
            print("%f"%self.hp)
        elif self.check == True and target.frame > 5:
            self.check = False
        if self.hp <= 0:
            self.state = self.DIE

    def change_state(self):
        self.state_frame = friend_data[self.name][self.state]['frame']
        self.total_frame = 0.0
        self.past_state = self.state
        pass

    def speed(self):
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

    def get_hit_bb(self):
        return self.x - friend_data[self.name]['MOVE']['width']/2 + friend_data[self.name]['MOVE']['plusX'], \
                self.y - friend_data[self.name]['MOVE']['height']/2 + friend_data[self.name]['MOVE']['plusY'],\
                self.x + friend_data[self.name]['MOVE']['width']/2 + friend_data[self.name]['MOVE']['plusX'], \
                self.y + friend_data[self.name]['MOVE']['height']/2 + friend_data[self.name]['MOVE']['plusY']

    def get_attack_bb(self):
        return self.x - friend_data[self.name]['ATTACK']['width']/2 + friend_data[self.name]['ATTACK']['plusX'], \
                self.y - friend_data[self.name]['ATTACK']['height']/2 + friend_data[self.name]['ATTACK']['plusY'],\
                self.x + friend_data[self.name]['ATTACK']['width']/2 + friend_data[self.name]['ATTACK']['plusX'], \
                self.y + friend_data[self.name]['ATTACK']['height']/2 + friend_data[self.name]['ATTACK']['plusY']

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def collide(self, a, b):
        left_self, bottom_self, right_self, top_self = a
        left_target, bottom_target, right_target, top_target = b

        if left_self > right_target : return False
        if right_self < left_target : return False
        if top_self < bottom_target : return False
        if bottom_self > top_target : return False

        return True

    def hit_collide(self, target):
        left_self, bottom_self, right_self, top_self = self.get_hit_bb()
        left_target, bottom_target, right_target, top_target = target.get_hit_bb()

        if left_self > right_target : return False
        if right_self < left_target : return False
        if top_self < bottom_target : return False
        if bottom_self > top_target : return False

        return True

    def attack_collide(self, target):
        left_self, bottom_self, right_self, top_self = self.get_hit_bb()
        left_target, bottom_target, right_target, top_target = target.get_attack_bb()

        if left_self > right_target : return False
        if right_self < left_target : return False
        if top_self < bottom_target : return False
        if bottom_self > top_target : return False

        return True
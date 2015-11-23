from pico2d import *
import image
import random

enemy_data_file = open('data/enemy_data.txt', 'r')
enemy_data = json.load(enemy_data_file)
enemy_data_file.close()

stage_data_file = open('data/stage_data.txt', 'r')
stage_data = json.load(stage_data_file)
stage_data_file.close()


class Enemy:
    image = None

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    REGEN_TIME = 0

    STAND, MOVE, ATTACK, DIE, HIT = 'STAND', 'MOVE', 'ATTACK', 'DIE', 'HIT'

    def __init__(self, name):
        self.name = name
        self.state = self.STAND
        self.hp = enemy_data[name]['hp']
        self.damage = enemy_data[name]['damage']
        for i in image.imageList:
            if i.name == name:
                self.image = i.image
        self.type = enemy_data[name]['type']
        self.x, self.y = 1700, stage_data['stage1']['bottom'] + enemy_data[name]['pivotY']
        self.game_time, self.frame, self.total_frame = 0, 0, 0
        self.state_frame = enemy_data[name][self.state]['frame']
        self.attack_frame = enemy_data[self.name]['attack_frame']
        self.past_state = None
        self.current_state = None
        self.die_check = False
        self.collide_check = False
        self.attack_check = False
        self.hit_check = False
        self.target_name = None
        self.target_index = None
        self.effect_on = False
        self.effect_frame, self.effect_total_frame, self.target_effect_frame, self.effect_pos = 0, 0, 0, 0
        self.effect_left, self.effect_right, self.effect_width, self.effect_height = 0, 0, 0, 0
        self.effect_image = None

        Enemy.REGEN_TIME = enemy_data[name]['regen_time']

    def update(self, frame_time, targetList,mc):
        self.change_state()
        self.collide_check_func(targetList, mc)
        self.game_time += frame_time
        self.total_frame += Enemy.FRAMES_PER_ACTION * Enemy.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frame) % self.state_frame
        self.handle_state[self.state](self, frame_time, targetList, mc)
        if self.effect_on == True:
            self.effect_total_frame += Enemy.FRAMES_PER_ACTION * Enemy.ACTION_PER_TIME * frame_time
            self.effect_frame = int(self.effect_total_frame) % self.target_effect_frame

    def draw(self):
        self.image.clip_draw(self.frame * enemy_data[self.name][self.state]['left'], enemy_data[self.name][self.state]['bottom'],
                             enemy_data[self.name][self.state]['width'], enemy_data[self.name][self.state]['height'],
                             self.x - self.bg.window_left + enemy_data[self.name][self.state]['plusX'], self.y + enemy_data[self.name][self.state]['plusY'])
                            ###- self.bg.window_left
        if self.effect_on == True:
            if self.effect_image != None:
                self.effect_image.clip_draw(self.effect_frame * self.effect_left, self.effect_right, self.effect_width,
                                            self.effect_height, self.x - self.bg.window_left, stage_data['stage1']['bottom'] + self.effect_pos)
                                            ###- self.bg.window_left
                if self.effect_total_frame >= self.target_effect_frame:
                    self.effect_frame = 0
                    self.effect_total_frame = 0
                    self.effect_on = False

    def handle_stand(self, frame_time, targetList, mc):
        if self.past_state == self.ATTACK:
            if self.game_time > enemy_data[self.name]['attack_delay']:
                if self.collide_check == True:
                    self.state = self.ATTACK
                    self.attack_check = True
                elif self.collide_check == False:
                    self.state = self.MOVE
            elif self.hit_check == True:
                self.state = self.HIT
        else:
            if self.collide_check == True:
                    self.state = self.ATTACK
                    self.attack_check = True
            elif self.hit_check == True:
                self.state = self.HIT
            elif self.collide_check == False:
                self.state = self.MOVE

    def handle_move(self, frame_time, targetList, mc):
        if self.hit_check == True:
            self.state = self.HIT
        elif self.collide_check == True:
            self.state = self.ATTACK
            self.attack_check = True
        else:
            self.x -= self.speed() * frame_time

    def handle_attack(self, frame_time, targetList, mc):
        # self.hit_check = False
        if self.total_frame >= self.state_frame:
            self.state = self.STAND
            self.collide_check = False
        elif self.frame == self.attack_frame and self.attack_check == True:
            if self.target_name == 'mc':
                mc.hit(self.damage, self.get_effect())
                self.attack_check = False
                return
            elif targetList != []:
                if self.target_index < len(targetList):
                    if self.target_name == targetList[self.target_index].name:
                        targetList[self.target_index].hit(self.damage, self.get_effect())
                        self.attack_check = False

    def handle_die(self, frame_time, targetList, mc):
        if self.total_frame >= self.state_frame:
            self.die_check = True

    def handle_hit(self, frame_time, targetList, mc):
        self.x += frame_time * 30
        if self.game_time > 0.3:
            self.state = self.past_state
            self.hit_check = False

    handle_state = {
        STAND : handle_stand,
        MOVE: handle_move,
        ATTACK: handle_attack,
        DIE: handle_die,
        HIT: handle_hit
    }
    
    def hit(self, damage, effect):
        self.effect_on = True
        self.effect_left, self.effect_right, self.effect_width, self.effect_height,\
        self.target_effect_frame, self.effect_pos, self.effect_image = effect
        self.hp -= damage
        if self.hp <= 0:
            self.state = self.DIE
        else:
            self.hit_check = True

    def skill_hit(self, damage):
        self.hp -= damage
        self.state = self.HIT
        if self.hp <= 0:
            self.state = self.DIE

    def change_state(self):
        if self.state != self.current_state:
            self.past_state = self.current_state
            self.current_state = self.state
            self.state_frame = enemy_data[self.name][self.state]['frame']
            self.total_frame = 0.0
            self.game_time = 0.0

    def speed(self):
        PIXEL_PER_METER = (10.0 / 1.1)
        RUN_SPEED_KMPH = enemy_data[self.name]['speed']
        RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
        RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
        RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
        return RUN_SPEED_PPS

    def get_hit_bb(self):
        return self.x - enemy_data[self.name]['hit_bb_left'], \
                self.y - enemy_data[self.name]['hit_bb_bottom'],\
                self.x + enemy_data[self.name]['hit_bb_right'], \
                self.y + enemy_data[self.name]['hit_bb_height']

    def get_attack_bb(self):
        if self.type == 'long_distance':
            return self.x - enemy_data[self.name]['hit_bb_left'] - enemy_data[self.name]['attack_distance'], \
                    self.y - enemy_data[self.name]['hit_bb_bottom'],\
                    self.x + enemy_data[self.name]['hit_bb_right'], \
                    self.y + enemy_data[self.name]['hit_bb_height']
        else:
            return self.x - enemy_data[self.name]['hit_bb_left'], \
                    self.y - enemy_data[self.name]['hit_bb_bottom'],\
                    self.x + enemy_data[self.name]['hit_bb_right'], \
                    self.y + enemy_data[self.name]['hit_bb_height']

    def get_effect(self):
        return enemy_data[self.name]['EFFECT']['left'],\
                enemy_data[self.name]['EFFECT']['bottom'],\
                enemy_data[self.name]['EFFECT']['width'],\
                enemy_data[self.name]['EFFECT']['height'],\
                enemy_data[self.name]['EFFECT']['frame'],\
                enemy_data[self.name]['EFFECT']['pos'], self.image

    def collide(self, self_bb, target_bb):
        left_self, bottom_self, right_self, top_self = self_bb
        left_target, bottom_target, right_target, top_target = target_bb

        if left_self > right_target : return False
        if right_self < left_target : return False
        if top_self < bottom_target : return False
        if bottom_self > top_target : return False

        return True

    def collide_check_func(self, targetList, mc):
        if self.collide_check == False:
            if self.collide(self.get_attack_bb(), mc.get_bb()) == True:
                self.collide_check = True
                self.target_name = 'mc'
                return
            for target in targetList:
                if target.state != target.DIE:
                    if self.collide(self.get_attack_bb(), target.get_hit_bb()) == True:
                        if target.state != target.DIE:
                            self.target_name = target.name
                            self.target_index = targetList.index(target)
                            self.collide_check = True
                            return

    def set_background(self, bg):  ###
        self.bg = bg



from pico2d import *
from etc import *
import random

friend_data_file = open('data/friend_data.txt', 'r')
friend_data = json.load(friend_data_file)
friend_data_file.close()


class Friend:
    image = None

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    STAND, MOVE, ATTACK, DIE, HIT, REGEN = 'STAND', 'MOVE', 'ATTACK', 'DIE', 'HIT', 'REGEN'

    def __init__(self, name, x_pos):
        self.name = name
        self.state = self.REGEN
        self.hp = friend_data[name]['hp']
        self.damage = friend_data[name]['damage']
        self.image = get_image(name)
        self.type = friend_data[name]['type']
        self.x, self.y = x_pos, stage_bottom() + friend_data[name]['pivotY']
        self.game_time, self.frame, self.total_frame = 0, 0, 0
        self.state_frame = friend_data[name][self.state]['frame']
        self.attack_frame = friend_data[self.name]['attack_frame']
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
        self.attack_sound = get_unit_sound(name, 'attack')
        self.attack_sound_check = False
        self.hit_sound = get_unit_sound(name, 'hit')
        self.die_sound = get_unit_sound(name, 'die')
        self.die_sound_check = False
        self.font = get_font(20)

    def update(self, frame_time, targetList, boss):
        self.change_state()
        self.collide_check_func(targetList, boss)
        self.game_time += frame_time
        self.total_frame += Friend.FRAMES_PER_ACTION * Friend.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frame) % self.state_frame
        self.handle_state[self.state](self, frame_time, targetList, boss)
        if self.effect_on == True:
            self.effect_total_frame += Friend.FRAMES_PER_ACTION * Friend.ACTION_PER_TIME * frame_time
            self.effect_frame = int(self.effect_total_frame) % self.target_effect_frame


    def draw(self):
        sx = self.x - self.bg.window_left

        self.image.clip_draw(self.frame * friend_data[self.name][self.state]['left'], friend_data[self.name][self.state]['bottom'],
                             friend_data[self.name][self.state]['width'], friend_data[self.name][self.state]['height'],
                             sx + friend_data[self.name][self.state]['plusX'], self.y + friend_data[self.name][self.state]['plusY'])
        if self.effect_on == True:
            if self.effect_image != None:
                self.effect_image.clip_draw(self.effect_frame * self.effect_left, self.effect_right, self.effect_width,
                                            self.effect_height, sx, stage_bottom() + self.effect_pos)
                if self.effect_total_frame >= self.target_effect_frame:
                    self.effect_frame = 0
                    self.effect_total_frame = 0
                    self.effect_on = False

        self.font.draw(sx, self.y + friend_data[self.name]['hit_bb_height'],"%d"%self.hp,(0,84,255))

    def handle_regen(self, frame_time, targetList, boss):
        if self.total_frame >= self.state_frame:
            self.state = self.STAND

    def handle_stand(self, frame_time, targetList, boss):
        if self.past_state == self.ATTACK:
            if self.game_time > friend_data[self.name]['attack_delay']:
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

    def handle_move(self, frame_time, targetList, boss):
        if self.hit_check == True:
            self.state = self.HIT
        elif self.collide_check == True:
            self.state = self.ATTACK
            self.attack_check = True
        else:
            self.x += self.speed() * frame_time
            self.x = clamp(0, self.x, self.bg.w)

    def handle_attack(self, frame_time, targetList, boss):
        if self.attack_sound_check == False:
            self.attack_sound.play()
            self.attack_sound_check = True
        if self.total_frame >= self.state_frame:
            self.state = self.STAND
            self.collide_check = False
            self.attack_sound_check = False
        elif self.frame == self.attack_frame and self.attack_check == True:
            if targetList != []:
                if self.target_index < len(targetList):
                    if self.target_name == targetList[self.target_index].name:
                        targetList[self.target_index].hit(self.damage, self.get_effect())
                        self.attack_check = False
            if boss != None:
                boss.hit(self.damage, self.get_effect())
                self.attack_check = False


    def handle_die(self, frame_time, targetList, boss):
        if self.die_sound_check == False:
            self.die_sound.play()
            self.die_sound_check = True
        if self.total_frame >= self.state_frame:
            self.die_check = True

    def handle_hit(self, frame_time, targetList, boss):
        self.x -= frame_time * 30
        if self.game_time > 0.3:
            self.state = self.past_state
            self.hit_check = False

    handle_state = {
        REGEN : handle_regen,
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
        if self.hp >= 0:
            self.hit_sound.play()
        if self.hp <= 0:
            self.hp = 0
            self.state = self.DIE
        else:
            self.hit_check = True

    def skill_hit(self, damage):
        self.hp -= damage
        self.state = self.HIT
        if self.hp <= 0:
            self.hp = 0
            self.state = self.DIE

    def change_state(self):
        if self.state != self.current_state:
            self.past_state = self.current_state
            self.current_state = self.state
            self.state_frame = friend_data[self.name][self.state]['frame']
            self.total_frame = 0.0
            self.game_time = 0.0

    def speed(self):
        PIXEL_PER_METER = (10.0 / 1.1)
        RUN_SPEED_KMPH = friend_data[self.name]['speed']
        RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
        RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
        RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
        return RUN_SPEED_PPS

    def get_hit_bb(self):
            return self.x - friend_data[self.name]['hit_bb_left'], \
                    self.y - friend_data[self.name]['hit_bb_bottom'],\
                    self.x + friend_data[self.name]['hit_bb_right'], \
                    self.y + friend_data[self.name]['hit_bb_height']

    def get_attack_bb(self):
        if self.type == 'long_distance':
            return self.x - friend_data[self.name]['hit_bb_left'], \
                    self.y - friend_data[self.name]['hit_bb_bottom'],\
                    self.x + friend_data[self.name]['hit_bb_right'] + friend_data[self.name]['attack_distance'], \
                    self.y + friend_data[self.name]['hit_bb_height']
        else:
            return self.x - friend_data[self.name]['hit_bb_left'], \
                    self.y - friend_data[self.name]['hit_bb_bottom'],\
                    self.x + friend_data[self.name]['hit_bb_right'], \
                    self.y + friend_data[self.name]['hit_bb_height']

    def get_effect(self):
        return friend_data[self.name]['EFFECT']['left'],\
                friend_data[self.name]['EFFECT']['bottom'],\
                friend_data[self.name]['EFFECT']['width'],\
                friend_data[self.name]['EFFECT']['height'],\
                friend_data[self.name]['EFFECT']['frame'],\
                friend_data[self.name]['EFFECT']['pos'], self.image

    def collide(self, self_bb, target_bb):
        left_self, bottom_self, right_self, top_self = self_bb
        left_target, bottom_target, right_target, top_target = target_bb

        if left_self > right_target : return False
        if right_self < left_target : return False
        if top_self < bottom_target : return False
        if bottom_self > top_target : return False

        return True

    def collide_check_func(self, targetList, boss):
        if self.collide_check == False:
            self.min_distance = 2000
            for target in targetList:
                if target.state != target.DIE:
                    if self.collide(self.get_attack_bb(), target.get_hit_bb()) == True:
                        if self.min_distance > target.x - self.x:
                            self.min_distance = target.x - self.x
                            self.target_name = target.name
                            self.target_index = targetList.index(target)
                            self.collide_check = True
            if boss != None and boss.state != boss.DIE:
                if self.collide(self.get_attack_bb(), boss.return_bb()) == True:
                    self.collide_check = True


    def set_background(self, bg):
        self.bg = bg


class Spirit:
    image = None
    MOVE_LEFT, MOVE_RIGHT, DIE_LEFT, DIE_RIGHT = 'MOVE_LEFT', 'MOVE_RIGHT', 'DIE_LEFT', 'DIE_RIGHT'

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    PIXEL_PER_METER = (10.0 / 1.1)
    RUN_SPEED_KMPH = friend_data['Spirit']['speed']
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self, xpos):
        self.center = xpos
        self.x, self.y = xpos, stage_bottom() + friend_data['Spirit']['pivotY']
        if random.randint(0,1) == 0:
            self.state = self.MOVE_LEFT
        else:
            self.state = self.MOVE_RIGHT
        self.frame = 0
        self.total_frame = 0
        self.state_frame = friend_data['Spirit'][self.state]['frame']
        self.die_check = False
        if Spirit.image == None:
            Spirit.image = load_image(friend_data['Spirit']['image'])

    def update(self, frame_time, mc):
        self.total_frame += Friend.FRAMES_PER_ACTION * Friend.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frame) % self.state_frame
        self.handle_state[self.state](self, frame_time)
        if self.state != self.DIE_LEFT and self.state != self.DIE_RIGHT:
            if self.collide(mc) == True:
                mc.absorb_spirit()
                if self.state == self.MOVE_LEFT:
                    self.state = self.DIE_LEFT
                    self.total_frame = 0
                elif self.state == self.MOVE_RIGHT:
                    self.state = self.DIE_RIGHT
                    self.total_frame = 0

    def draw(self):
        sx = self.x - self.bg.window_left

        self.image.clip_draw(self.frame * friend_data['Spirit'][self.state]['left'], friend_data['Spirit'][self.state]['bottom'],
                             friend_data['Spirit'][self.state]['width'], friend_data['Spirit'][self.state]['height'],
                             sx + friend_data['Spirit'][self.state]['plusX'], self.y + friend_data['Spirit'][self.state]['plusY'])

    def get_bb(self):
            return self.x - friend_data['Spirit']['bb_left'], \
                    self.y - friend_data['Spirit']['bb_bottom'],\
                    self.x + friend_data['Spirit']['bb_right'], \
                    self.y + friend_data['Spirit']['bb_height']

    def collide(self, mc):
        left_self, bottom_self, right_self, top_self = self.get_bb()
        left_target, bottom_target, right_target, top_target = mc.get_bb()

        if left_self > right_target : return False
        if right_self < left_target : return False
        if top_self < bottom_target : return False
        if bottom_self > top_target : return False

        return True

    def handle_move_left(self, frame_time):
        self.x -= self.RUN_SPEED_PPS * frame_time
        if self.x < self.center - friend_data['Spirit']['move_range']/2:
            self.state = self.MOVE_RIGHT

    def handle_move_right(self, frame_time):
        self.x += self.RUN_SPEED_PPS * frame_time
        self.x = clamp(0, self.x, self.bg.w)
        if self.x > self.center + friend_data['Spirit']['move_range']/2:
            self.state = self.MOVE_LEFT

    def handle_die_left(self, frame_time):
        if self.total_frame >= self.state_frame:
            self.die_check = True

    def handle_die_right(self, frame_time):
        if self.total_frame >= self.state_frame:
            self.die_check = True

    handle_state = {
        MOVE_LEFT  : handle_move_left,
        MOVE_RIGHT : handle_move_right,
        DIE_LEFT   : handle_die_left,
        DIE_RIGHT  : handle_die_right
    }

    def set_background(self, bg):
        self.bg = bg
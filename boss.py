from pico2d import *
from etc import *

boss_data_file = open('data/boss_data.txt', 'r')
boss_data = json.load(boss_data_file)
boss_data_file.close()


class Boss:
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    NORMAL, INJURY, FATAL, DIE, SKILL1, SKILL2 = 'NORMAL', 'INJURY', 'FATAL', 'DIE', 'SKILL1', 'SKILL2'

    def __init__(self):
        self.stand_image = get_image('Boss_Stand')
        self.die_image = get_image('Boss_Die')
        self.right_stand_image = get_image('Boss_Right_Hand_Stand')
        self.right_die_image = get_image('Boss_Right_Hand_Die')
        self.left_stand_image = get_image('Boss_Left_Hand_Stand')
        self.left_die_image = get_image('Boss_Left_Hand_Die')
        self.skill1_image = get_image('Boss_Skill1')
        self.skill2_image = get_image('Boss_Skill2')
        self.skill1_sound = get_sound('boss_skill1')
        self.skill2_sound = get_sound('boss_skill2')
        self.lhand_die_sound = get_sound('boss_lhd_die')
        self.rhand_die_sound = get_sound('boss_rhd_die')
        self.die_sound = get_sound('boss_die')
        self.state = self.NORMAL
        self.body_state = 'BODY_STAND'
        self.lhand_state = 'LHAND_STAND'
        self.rhand_state = 'RHAND_STAND'
        self.hp = boss_data['hp']
        self.max_hp = boss_data['hp']
        self.body_xframe, self.body_yframe, self.body_total_frame = 0, 0, 0
        self.Rhand_xframe, self.Rhand_yframe, self.Rhand_total_frame = 0, 2, 0
        self.Lhand_xframe, self.Lhand_yframe, self.Lhand_total_frame = 0, 2, 0
        self.stand_times = 0
        self.skill_turn = True
        self.die_check = False
        self.for_mc_damage = boss_data['for_mc_damage']
        self.for_unit_damage = boss_data['for_unit_damage']
        self.effect_on = False
        self.effect_frame, self.effect_total_frame, self.target_effect_frame, self.effect_pos = 0, 0, 0, 0
        self.effect_left, self.effect_right, self.effect_width, self.effect_height = 0, 0, 0, 0
        self.effect_image = None

    def update(self, frame_time, mc, targetList):
        self.body_update(frame_time, mc, targetList)
        if self.state != self.DIE:
            self.right_hand_update(frame_time)
            self.left_hand_update(frame_time)
            self.skill_change()
            if self.effect_on == True:
                self.effect_total_frame += Boss.FRAMES_PER_ACTION * Boss.ACTION_PER_TIME * frame_time
                self.effect_frame = int(self.effect_total_frame) % self.target_effect_frame

    def draw(self):
        global ypos
        self.body_draw()
        if self.state != self.DIE:
            self.right_hand_draw()
            self.left_hand_draw()
        if self.effect_on == True:
            if self.state == self.NORMAL: ypos = boss_data['left_hand_bb']['l'] + 20
            else: ypos = boss_data['lower_body_bb']['l'] + 20
            if self.effect_image != None:
                self.effect_image.clip_draw(self.effect_frame * self.effect_left, self.effect_right, self.effect_width,
                                            self.effect_height, ypos, stage_bottom() + self.effect_pos)
                if self.effect_total_frame >= self.target_effect_frame:
                    self.effect_frame = 0
                    self.effect_total_frame = 0
                    self.effect_on = False

    def body_update(self, frame_time, mc, targetList):
        self.body_total_frame += Boss.FRAMES_PER_ACTION * Boss.ACTION_PER_TIME * frame_time
        if self.state == self.DIE:
            self.body_state = 'BODY_DIE'
            self.body_xframe = int(self.body_total_frame) % boss_data[self.body_state]['xframe']
            if self.body_total_frame >= boss_data[self.body_state]['xframe'] and self.body_yframe==2:
                self.body_yframe = 1
                self.body_total_frame = 0
            elif self.body_total_frame >= boss_data[self.body_state]['xframe'] and self.body_yframe==1:
                self.body_yframe = 0
                self.body_total_frame = 0
            elif self.body_total_frame >= boss_data[self.body_state]['xframe'] and self.body_yframe==0:
                self.die_check = True

        elif self.body_state == 'BODY_STAND':
            self.body_xframe = int(self.body_total_frame) % boss_data[self.body_state]['xframe']
            if self.body_total_frame >= boss_data[self.body_state]['xframe'] and self.body_yframe==0:
                self.body_yframe = 1
                self.body_total_frame = 0
            elif self.body_total_frame >= boss_data[self.body_state]['xframe'] and self.body_yframe==1:
                self.body_yframe = 0
                self.body_total_frame = 0
                self.stand_times += 1
                print(self.stand_times)

        elif self.body_state == 'SKILL1' or self.body_state == 'SKILL2':
            self.body_xframe = int(self.body_total_frame) % boss_data[self.body_state]['xframe']
            if self.body_total_frame >= boss_data[self.body_state]['xframe'] and self.body_yframe==2:
                if self.body_state == 'SKILL2':
                    self.target_attack(mc, targetList)
                self.body_yframe = 1
                self.body_total_frame = 0
            elif self.body_total_frame >= boss_data[self.body_state]['xframe'] and self.body_yframe==1:
                if self.body_state == 'SKILL1':
                    self.target_attack(mc, targetList)
                self.body_yframe = 0
                self.body_total_frame = 0
            elif self.body_total_frame >= boss_data[self.body_state]['xframe'] and self.body_yframe==0:
                self.body_yframe = 1
                self.body_total_frame = 0
                self.body_state = 'BODY_STAND'

    def body_draw(self):
        image = None
        if self.body_state == 'BODY_STAND':
            image = self.stand_image
        elif self.body_state == 'SKILL1':
            image = self.skill1_image
        elif self.body_state == 'SKILL2':
            image = self.skill2_image
        elif self.body_state == 'BODY_DIE':
            image = self.die_image
        image.clip_draw(boss_data[self.body_state]['left']*self.body_xframe,
                        boss_data[self.body_state]['bottom']*self.body_yframe,
                        boss_data[self.body_state]['width'], boss_data[self.body_state]['height'],
                        boss_data[self.body_state]['xpos'], boss_data[self.body_state]['ypos'])

    def right_hand_update(self, frame_time):
        self.Rhand_total_frame += Boss.FRAMES_PER_ACTION * Boss.ACTION_PER_TIME * frame_time
        self.Rhand_xframe = int(self.Rhand_total_frame)% boss_data[self.rhand_state]['xframe']
        if self.state != self.NORMAL and self.state != self.INJURY:
            if self.Rhand_total_frame >= boss_data[self.rhand_state]['xframe'] and self.Rhand_yframe == 2:
                self.Rhand_yframe -= 1
                self.Rhand_total_frame = 0
            elif self.Rhand_total_frame >= boss_data[self.rhand_state]['xframe2'] and self.Rhand_yframe == 1:
                self.Rhand_yframe -= 1
                self.Rhand_total_frame = 0
            elif self.Rhand_total_frame >= boss_data[self.rhand_state]['xframe3'] and self.Rhand_yframe == 0:
                self.Rhand_xframe = boss_data[self.rhand_state]['xframe3'] - 1

    def right_hand_draw(self):
        image = None
        if self.state == self.NORMAL or self.state == self.INJURY:
            image = self.right_stand_image
        else:
            image = self.right_die_image
        image.clip_draw(boss_data[self.rhand_state]['left']*self.Rhand_xframe,
                        boss_data[self.rhand_state]['bottom']*self.Rhand_yframe,
                        boss_data[self.rhand_state]['width'], boss_data[self.rhand_state]['height'],
                        boss_data[self.rhand_state]['xpos'], boss_data[self.rhand_state]['ypos'])

    def left_hand_update(self, frame_time):
        self.Lhand_total_frame += Boss.FRAMES_PER_ACTION * Boss.ACTION_PER_TIME * frame_time
        self.Lhand_xframe = int(self.Lhand_total_frame)% boss_data[self.lhand_state]['xframe']
        if self.state != self.NORMAL:
            if self.Lhand_total_frame >= boss_data[self.lhand_state]['xframe'] and self.Lhand_yframe == 2:
                self.Lhand_yframe -= 1
                self.Lhand_total_frame = 0
            elif self.Lhand_total_frame >= boss_data[self.lhand_state]['xframe2'] and self.Lhand_yframe == 1:
                self.Lhand_yframe -= 1
                self.Lhand_total_frame = 0
            elif self.Lhand_total_frame >= boss_data[self.lhand_state]['xframe3'] and self.Lhand_yframe == 0:
                self.Lhand_xframe = boss_data[self.lhand_state]['xframe3'] - 1

    def left_hand_draw(self):
        image = None
        if self.state == self.NORMAL:
            image = self.left_stand_image
        else:
            image = self.left_die_image
        image.clip_draw(boss_data[self.lhand_state]['left']*self.Lhand_xframe,
                        boss_data[self.lhand_state]['bottom']*self.Lhand_yframe,
                        boss_data[self.lhand_state]['width'], boss_data[self.lhand_state]['height'],
                        boss_data[self.lhand_state]['xpos'], boss_data[self.lhand_state]['ypos'])

    def left_hand_bb(self):
        return boss_data['left_hand_bb']['l'], boss_data['left_hand_bb']['b'],\
                boss_data['left_hand_bb']['r'], boss_data['left_hand_bb']['h']

    def lower_body_bb(self):
        return boss_data['lower_body_bb']['l'], boss_data['lower_body_bb']['b'],\
                boss_data['lower_body_bb']['r'], boss_data['lower_body_bb']['h']

    def upper_body_bb(self):
        return boss_data['upper_body_bb']['l'], boss_data['upper_body_bb']['b'],\
                boss_data['upper_body_bb']['r'], boss_data['upper_body_bb']['h']

    def return_bb(self):
        if self.state == self.NORMAL:
            return self.left_hand_bb()
        else:
            return self.lower_body_bb()

    def hit(self, damage, effect):
        self.effect_on = True
        self.effect_left, self.effect_right, self.effect_width, self.effect_height,\
        self.target_effect_frame, self.effect_pos, self.effect_image = effect
        self.hp -= damage
        if self.hp < self.max_hp*0.7 and self.hp >= self.max_hp*0.3 and self.state == self.NORMAL:
            self.state = self.INJURY
            self.lhand_state = 'LHAND_DIE'
            self.lhand_die_sound.play()
            self.Lhand_total_frame = 0
        elif self.hp < self.max_hp*0.3 and self.hp > 0 and self.state == self.INJURY:
            self.state = self.FATAL
            self.rhand_state = 'RHAND_DIE'
            self.rhand_die_sound.play()
            self.Rhand_total_frame = 0
        elif self.hp <= 0:
            self.body_yframe = 2
            self.state = self.DIE
            self.die_sound.play()

    def skill_change(self):
        global nom1, nom2
        if self.state == self.NORMAL: nom1, nom2 = 5, 4
        elif self.state == self.INJURY: nom1, nom2 = 3, 2
        elif self.state == self.FATAL: nom1, nom2 = 1, 1

        if self.stand_times >= nom1 and self.skill_turn == True:
            self.body_state = self.SKILL1
            self.skill1_sound.play()
            self.skill_turn = False
            self.stand_times = 0
            self.body_total_frame = 0
            self.body_yframe = 2
        elif self.stand_times >= nom2 and self.skill_turn == False:
            self.body_state = self.SKILL2
            self.skill2_sound.play()
            self.skill_turn = True
            self.stand_times = 0
            self.body_total_frame = 0
            self.body_yframe = 2

    def target_attack(self, mc, targetList):
        mc.skill_hit(self.for_mc_damage)
        for target in targetList:
            target.skill_hit(self.for_unit_damage)

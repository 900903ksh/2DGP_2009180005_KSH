from pico2d import *
from etc import *

boss_data_file = open('data/boss_data.txt', 'r')
boss_data = json.load(boss_data_file)
boss_data_file.close()


class Boss:
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    NORMAL, INJURY, FATAL, DIE = 0,1,2,3
    SKILL1, SKILL2 = 4,5

    def __init__(self):
        self.stand_image = get_image('Boss_Stand')
        self.right_stand_image = get_image('Boss_Right_Hand_Stand')
        self.right_die_image = get_image('Boss_Right_Hand_Die')
        self.left_stand_image = get_image('Boss_Left_Hand_Stand')
        self.left_die_image = get_image('Boss_Left_Hand_Die')
        self.skill1_image = get_image('Boss_Skill1')
        self.skill2_image = get_image('Boss_Skill2')
        self.state = self.NORMAL
        self.body_state = 'BODY_STAND'
        self.lhand_state = 'LHAND_STAND'
        self.rhand_state = 'RHAND_STAND'
        self.hp = boss_data['hp']
        self.max_hp = boss_data['hp']
        self.body_xframe, self.body_yframe, self.body_total_frame = 0, 0, 0
        self.Rhand_xframe, self.Rhand_yframe, self.Rhand_total_frame = 0, 2, 0
        self.Lhand_xframe, self.Lhand_yframe, self.Lhand_total_frame = 0, 2, 0

    def update(self, frame_time):
        self.body_update(frame_time)
        self.right_hand_update(frame_time)
        self.left_hand_update(frame_time)
        pass

    def draw(self):
        self.body_draw()
        self.right_hand_draw()
        self.left_hand_draw()
        draw_rectangle(*self.left_hand_bb())
        draw_rectangle(*self.lower_body_bb())
        draw_rectangle(*self.upper_body_bb())
        pass

    def body_update(self, frame_time):
        self.body_total_frame += Boss.FRAMES_PER_ACTION * Boss.ACTION_PER_TIME * frame_time
        if self.body_state == 'BODY_STAND':
            self.body_xframe = int(self.body_total_frame) % boss_data[self.body_state]['xframe']
            if self.body_total_frame >= boss_data[self.body_state]['xframe'] and self.body_yframe==0:
                self.body_yframe = 1
                self.body_total_frame = 0
            elif self.body_total_frame >= boss_data[self.body_state]['xframe'] and self.body_yframe==1:
                self.body_yframe = 0
                self.body_total_frame = 0

        elif self.body_state == 'SKILL1' or self.body_state == 'SKILL2':
            self.body_xframe = int(self.body_total_frame) % boss_data[self.body_state]['xframe']
            if self.body_total_frame >= boss_data[self.body_state]['xframe'] and self.body_yframe==2:
                self.body_yframe = 1
                self.body_total_frame = 0
            elif self.body_total_frame >= boss_data[self.body_state]['xframe'] and self.body_yframe==1:
                self.body_yframe = 0
                self.body_total_frame = 0
            elif self.body_total_frame >= boss_data[self.body_state]['xframe'] and self.body_yframe==0:
                self.body_yframe = 2
                self.body_total_frame = 0

    def body_draw(self):
        image = None
        if self.body_state == 'BODY_STAND':
            image = self.stand_image
        elif self.body_state == 'SKILL1':
            image = self.skill1_image
        elif self.body_state == 'SKILL2':
            image = self.skill2_image
        image.clip_draw(boss_data[self.body_state]['left']*self.body_xframe,
                        boss_data[self.body_state]['bottom']*self.body_yframe,
                        boss_data[self.body_state]['width'], boss_data[self.body_state]['height'],
                        boss_data[self.body_state]['xpos'], boss_data[self.body_state]['ypos'])

    def right_hand_update(self, frame_time):
        self.Rhand_total_frame += Boss.FRAMES_PER_ACTION * Boss.ACTION_PER_TIME * frame_time
        self.Rhand_xframe = int(self.Rhand_total_frame)% boss_data[self.rhand_state]['xframe']
        if self.state != self.NORMAL and self.state != self.INJURY:
            self.rhand_state = 'RHAND_DIE'
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
            self.lhand_state = 'LHAND_DIE'
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

    def hit(self, damage):
        self.hp -= damage
        print(self.hp)
        if self.hp < self.max_hp*0.7 and self.hp >= self.max_hp*0.3:
            self.state = self.INJURY
        if self.hp < self.max_hp*0.3 and self.hp > 0:
            self.state = self.FATAL
        if self.hp <= 0:
            self.state = self.DIE

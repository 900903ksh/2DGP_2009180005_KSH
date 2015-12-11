from pico2d import *

skill_data_file = open('data/skill_data.txt', 'r')
skill_data = json.load(skill_data_file)
skill_data_file.close()


class Attack:
    image = None

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    def __init__(self, xpos, ypos):
        if Attack.image == None:
            Attack.image = load_image(skill_data['attack']['image'])
        self.damage = skill_data['attack']['damage']
        self.frame = 0
        self.total_frame = 0
        self.skill_frame = skill_data['attack']['draw']['frame']
        self.x = xpos + skill_data['attack']['draw']['xpos']
        self.y = ypos + skill_data['attack']['draw']['ypos']
        self.attack_frame = skill_data['attack']['attack_frame']
        self.attack_check = True

    def set_background(self, bg):
        self.bg = bg

    def update(self, frame_time):
        self.total_frame += Attack.FRAMES_PER_ACTION * Attack.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frame) % self.skill_frame
        if self.total_frame >= skill_data['attack']['limit_frame']:
            return False

    def draw(self):
        sx = self.x - self.bg.window_left

        self.image.clip_draw(self.frame * skill_data['attack']['draw']['left'], skill_data['attack']['draw']['bottom'],
                             skill_data['attack']['draw']['width'], skill_data['attack']['draw']['height'],
                             sx, self.y + skill_data['attack']['draw']['ypos'])

    def get_bb(self):
        return self.x - skill_data['attack']['attack_range_left'],\
                self.y - skill_data['attack']['attack_range_bottom'],\
                self.x + skill_data['attack']['attack_range_right'],\
                self.y + skill_data['attack']['attack_range_height']

    def collide(self, target_bb):
        left_self, bottom_self, right_self, top_self = self.get_bb()
        left_target, bottom_target, right_target, top_target = target_bb

        if left_self > right_target : return False
        if right_self < left_target : return False
        if top_self < bottom_target : return False
        if bottom_self > top_target : return False

        return True

    def collide_check_func(self, friendList, enemyList, boss):
        if self.attack_check == True:
            if self.total_frame >= self.attack_frame:
                for emy in enemyList:
                    if self.collide(emy.get_hit_bb()) == True:
                        emy.skill_hit(self.damage)
                if boss != None and boss.state != boss.DIE:
                    if self.collide(boss.left_hand_bb()) == True or self.collide(boss.upper_body_bb()) == True or self.collide(boss.lower_body_bb()) == True:
                        boss.hit(self.damage, self.get_effect())

                self.attack_check = False

    def get_effect(self):
        return skill_data['attack']['EFFECT']['left'],\
                skill_data['attack']['EFFECT']['bottom'],\
                skill_data['attack']['EFFECT']['width'],\
                skill_data['attack']['EFFECT']['height'],\
                skill_data['attack']['EFFECT']['frame'],\
                skill_data['attack']['EFFECT']['pos'], self.image


class Skill1:
    image = None

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    SUMMON, ATTACK, DIE = 0, 1, 2

    def __init__(self, xpos, ypos):
        if Skill1.image == None:
            Skill1.image = load_image(skill_data['skill1']['image'])
        self.damage = skill_data['skill1']['damage']
        self.frame = 0
        self.state = self.SUMMON
        self.total_frame = 0
        self.skill_frame = skill_data['skill1']['draw']['frame']
        self.x = skill_data['skill1']['draw']['xpos'] + xpos
        self.y = skill_data['skill1']['draw']['ypos'] + ypos
        self.attack_frame = skill_data['skill1']['attack_frame']
        self.attack_check = True

    def set_background(self, bg):
        self.bg = bg

    def update(self, frame_time):
        self.total_frame += Skill1.FRAMES_PER_ACTION * Skill1.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frame) % self.skill_frame
        if self.total_frame >= self.skill_frame:
            self.total_frame = 0
            self.state += self.ATTACK
        if self.state == self.DIE:
            return False

    def draw(self):
        self.image.clip_draw(self.frame * skill_data['skill1']['draw']['left'],
                             self.state * skill_data['skill1']['draw']['bottom'],
                             skill_data['skill1']['draw']['width'], skill_data['skill1']['draw']['height'],
                             self.x - self.bg.window_left, self.y,
                             skill_data['skill1']['draw']['xsize'], skill_data['skill1']['draw']['ysize'])

    def get_bb(self):
        return self.x - skill_data['skill1']['attack_range_left'],\
                self.y - skill_data['skill1']['attack_range_bottom'],\
                self.x + skill_data['skill1']['attack_range_right'],\
                self.y + skill_data['skill1']['attack_range_height']

    def collide(self, target_bb):
        left_self, bottom_self, right_self, top_self = self.get_bb()
        left_target, bottom_target, right_target, top_target = target_bb

        if left_self > right_target : return False
        if right_self < left_target : return False
        if top_self < bottom_target : return False
        if bottom_self > top_target : return False

        return True

    def collide_check_func(self, friendList, enemyList, boss):
        if self.attack_check == True:
            if self.state == self.ATTACK:
                if self.total_frame >= self.attack_frame:
                    for fnd in friendList:
                        if self.collide(fnd.get_hit_bb()) == True:
                            fnd.skill_hit(self.damage)
                    for emy in enemyList:
                        if self.collide(emy.get_hit_bb()) == True:
                            emy.skill_hit(self.damage)
                    self.attack_check = False


class Skill2:
    image = None

    SUMMON, ATTACK, DIE = 'SUMMON', 'ATTACK', 'DIE'

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    def __init__(self, xpos, ypos):
        if Skill2.image == None:
            Skill2.image = load_image(skill_data['skill2']['image'])
        self.damage = skill_data['skill2']['damage']
        self.frame = 0
        self.total_frame = 0
        self.state = self.SUMMON
        self.skill_frame = skill_data['skill2'][self.state]['frame']
        self.x = skill_data['skill2'][self.state]['xpos'] + xpos
        self.y = ypos
        self.attack_frame = skill_data['skill2']['attack_frame']
        self.attack_check = True

    def set_background(self, bg):
        self.bg = bg

    def update(self, frame_time):
        self.total_frame += Skill2.FRAMES_PER_ACTION * Skill2.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frame) % self.skill_frame
        if self.total_frame >= self.skill_frame:
            if self.state == self.SUMMON:
                self.state = self.ATTACK
            elif self.state == self.ATTACK:
                self.state = self.DIE
            elif self.state == self.DIE:
                return False
            self.total_frame = 0
            self.skill_frame = skill_data['skill2'][self.state]['frame']

    def draw(self):
        self.image.clip_draw(self.frame * skill_data['skill2'][self.state]['left'], skill_data['skill2'][self.state]['bottom'],
                             skill_data['skill2'][self.state]['width'], skill_data['skill2'][self.state]['height'],
                             self.x - self.bg.window_left, self.y + skill_data['skill2'][self.state]['ypos'], ###
                             skill_data['skill2'][self.state]['xsize'], skill_data['skill2'][self.state]['ysize'])

    def get_bb(self):
        return self.x - skill_data['skill2']['attack_range_left'],\
                self.y - skill_data['skill2']['attack_range_bottom'],\
                self.x + skill_data['skill2']['attack_range_right'],\
                self.y + skill_data['skill2']['attack_range_height']

    def collide(self, target_bb):
        left_self, bottom_self, right_self, top_self = self.get_bb()
        left_target, bottom_target, right_target, top_target = target_bb

        if left_self > right_target : return False
        if right_self < left_target : return False
        if top_self < bottom_target : return False
        if bottom_self > top_target : return False

        return True

    def collide_check_func(self, friendList, enemyList, boss):
        if self.attack_check == True:
            if self.state == self.ATTACK:
                if self.total_frame >= self.attack_frame:
                    for fnd in friendList:
                        if self.collide(fnd.get_hit_bb()) == True:
                            fnd.skill_hit(self.damage)
                    for emy in enemyList:
                        if self.collide(emy.get_hit_bb()) == True:
                            emy.skill_hit(self.damage)
                    self.attack_check = False


class Heal:
    image = None

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    def __init__(self, xpos, ypos):
        if Heal.image == None:
            Heal.image = load_image(skill_data['heal']['image'])
        self.heal_amount = skill_data['heal']['heal_amount']
        self.frame = 0
        self.total_frame = 0
        self.skill_frame = skill_data['heal']['draw']['frame']
        self.x = xpos
        self.y = ypos + skill_data['heal']['draw']['ypos']

    def set_background(self, bg):
        self.bg = bg

    def update(self, frame_time):
        self.total_frame += Skill1.FRAMES_PER_ACTION * Skill1.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frame) % self.skill_frame
        if self.total_frame >= skill_data['heal']['limit_frame']:
            return False

    def draw(self):
        self.image.clip_draw(self.frame * skill_data['heal']['draw']['left'], skill_data['heal']['draw']['bottom'],
                             skill_data['heal']['draw']['width'], skill_data['heal']['draw']['height'],
                             self.x - self.bg.window_left, self.y,
                             skill_data['heal']['draw']['xsize'], skill_data['heal']['draw']['ysize'])

    def collide_check_func(self, friendList, enemyList, boss):
        pass

from pico2d import *

skill_data_file = open('data/skill_data.txt', 'r')
skill_data = json.load(skill_data_file)
skill_data_file.close()

class Skill1:
    image = None

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    def __init__(self, xpos):
        if Skill1.image == None:
            Skill1.image = load_image(skill_data['skill1']['image'])
        self.damage = skill_data['skill1']['damage']
        self.x_frame = 0
        self.y_frame = 0
        self.total_frame = 0
        self.skill_frame = skill_data['skill1']['draw']['frame']
        self.x = xpos

    def update(self, frame_time):
        self.total_frame += Skill1.FRAMES_PER_ACTION * Skill1.ACTION_PER_TIME * frame_time
        self.x_frame = int(self.total_frame) % self.skill_frame
        if self.total_frame >= self.skill_frame:
            self.total_frame = 0
            self.y_frame += 1
        if self.y_frame == 2:
            return False


    def draw(self):
        self.image.clip_draw(self.x_frame * skill_data['skill1']['draw']['left'],
                             self.y_frame * skill_data['skill1']['draw']['bottom'],
                             skill_data['skill1']['draw']['width'], skill_data['skill1']['draw']['height'],
                             skill_data['skill1']['draw']['xpos']+self.x, skill_data['skill1']['draw']['ypos'],
                             skill_data['skill1']['draw']['xsize'], skill_data['skill1']['draw']['ysize'])


class Skill2:
    image = None

    SUMMON, ATTACK, DIE = 'SUMMON', 'ATTACK', 'DIE'

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    def __init__(self, xpos):
        if Skill2.image == None:
            Skill2.image = load_image(skill_data['skill2']['image'])
        self.damage = skill_data['skill2']['damage']
        self.frame = 0
        self.total_frame = 0
        self.state = self.SUMMON
        self.skill_frame = skill_data['skill2'][self.state]['frame']
        self.x = xpos

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
                             skill_data['skill2'][self.state]['xpos']+self.x, skill_data['skill2'][self.state]['ypos'],
                             skill_data['skill2'][self.state]['xsize'], skill_data['skill2'][self.state]['ysize'])
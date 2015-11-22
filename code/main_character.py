from pico2d import *
import image
import skill
import friend

mc_data_file = open('data/main_character_data.txt', 'r')
mc_data = json.load(mc_data_file)
mc_data_file.close()

friend_data_file = open('data/friend_data.txt', 'r')
friend_data = json.load(friend_data_file)
friend_data_file.close()

skill_data_file = open('data/skill_data.txt', 'r')
skill_data = json.load(skill_data_file)
skill_data_file.close()

stage_data_file = open('data/stage_data.txt', 'r')
stage_data = json.load(stage_data_file)
stage_data_file.close()

class MainCharacter:
    image = None

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    PIXEL_PER_METER = (10.0 / 1.1)                             # 10 pixel 110 cm
    RUN_SPEED_KMPH = 50
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    STAND_RIGHT, STAND_LEFT, MOVE_RIGHT, MOVE_LEFT = 'STAND_RIGHT', 'STAND_LEFT', 'MOVE_RIGHT', 'MOVE_LEFT'
    SKILL1, SKILL2, ATTACK, SUMMON, HEAL = 'SKILL1', 'SKILL2', 'ATTACK', 'SUMMON', 'HEAL'
    DIE_RIGHT, DIE_LEFT, HIT_RIGHT, HIT_LEFT = 'DIE_RIGHT', 'DIE_LEFT', 'HIT_RIGHT', 'HIT_LEFT'

    def __init__(self):
        self.state = self.STAND_RIGHT
        self.hp = mc_data['hp']
        self.damage = mc_data['damage']
        self.spirit = mc_data['spirit']
        for i in image.imageList:
            if i.name == 'Eregos':
                self.image = i.image
        self.x, self.y = 200, stage_data['stage1']['bottom'] + mc_data['pivotY']

        self.game_time = 0

        self.frame = 0
        self.total_frame = 0
        self.state_frame = mc_data[self.state]['frame']

        self.past_state = None
        self.current_state = None
        self.key_lock = False
        self.left_key_pressed = False
        self.right_key_pressed = False
        self.summon_name = False
        self.summon_check = False
        self.skill_check = False

    def update(self, frame_time, friendList, skillList):
        self.change_state()
        self.total_frame += MainCharacter.FRAMES_PER_ACTION * MainCharacter.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frame) % self.state_frame
        self.state_frame = mc_data[self.state]['frame']
        self.handle_state[self.state](self, frame_time, friendList, skillList)
        if self.spirit < 0: self.spirit = 0

    def draw(self):
        self.image.clip_draw(self.frame * mc_data[self.state]['left'], mc_data[self.state]['bottom'],
                             mc_data[self.state]['width'], mc_data[self.state]['height'],
                             self.x + mc_data[self.state]['plusX'], self.y + mc_data[self.state]['plusY'])

        # draw_rectangle(*self.get_bb())

    def handle_events(self,event):
        if self.key_lock == False:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                self.state = self.MOVE_RIGHT
                self.right_key_pressed = True
            elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
                self.right_key_pressed = False
                if self.state in (self.MOVE_RIGHT,):
                    self.state = self.STAND_RIGHT

            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                self.left_key_pressed = True
                self.state = self.MOVE_LEFT
            elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
                self.left_key_pressed = False
                if self.state in (self.MOVE_LEFT,):
                    self.state = self.STAND_LEFT

            elif (event.type, event.key) in ((SDL_KEYDOWN, SDLK_1), (SDL_KEYDOWN, SDLK_2), (SDL_KEYDOWN, SDLK_3),
                                             (SDL_KEYDOWN, SDLK_4), (SDL_KEYDOWN, SDLK_5), (SDL_KEYDOWN, SDLK_6)):
                if event.key == SDLK_1: self.summon_name = 'SkelSoldier'
                elif event.key == SDLK_2: self.summon_name = 'SkelOfficer'
                elif event.key == SDLK_3: self.summon_name = 'SkelCommander'
                elif event.key == SDLK_4: self.summon_name = 'SkelSpearknight'
                elif event.key == SDLK_5: self.summon_name = 'Wraith'
                elif event.key == SDLK_6: self.summon_name = 'MuscleStone'

                if self.spirit >= friend_data[self.summon_name]['need_spirit']:
                    self.spirit -= friend_data[self.summon_name]['need_spirit']
                    print(self.spirit)
                    self.summon_check = True
                    self.state = self.SUMMON
                    self.key_lock_func()

            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
                self.state = self.ATTACK
                self.key_lock_func()

            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
                if self.spirit >= skill_data['skill1']['need_spirit']:
                    self.spirit -= skill_data['skill1']['need_spirit']
                    self.skill_check = True
                    self.state = self.SKILL1
                    self.key_lock_func()

            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_w):
                if self.spirit >= skill_data['skill2']['need_spirit']:
                    self.spirit -= skill_data['skill2']['need_spirit']
                    self.skill_check = True
                    self.state = self.SKILL2
                    self.key_lock_func()

            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_e):
                if self.spirit >= skill_data['heal']['need_spirit']:
                    self.spirit -= skill_data['heal']['need_spirit']
                    self.skill_check = True
                    self.state = self.HEAL
                    self.key_lock_func()

        elif self.key_lock == True:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                self.right_key_pressed = True
            elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
                self.right_key_pressed = False
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                self.left_key_pressed = True
            elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
                self.left_key_pressed = False

    def handle_stand_right(self, frame_time, friendList, skillList):
        pass

    def handle_stand_left(self, frame_time, friendList, skillList):
        pass

    def handle_move_right(self, frame_time, friendList, skillList):
        self.x += self.RUN_SPEED_PPS * frame_time

    def handle_move_left(self, frame_time, friendList, skillList):
        self.x -= self.RUN_SPEED_PPS * frame_time

    def handle_skill1(self, frame_time, friendList, skillList):
        if self.skill_check == True:
            Skill = skill.Skill1(self.x, stage_data['stage1']['bottom'])
            skillList.append(Skill)
            self.skill_check = False
        if self.total_frame > self.state_frame:
            self.next_state()

    def handle_skill2(self, frame_time, friendList, skillList):
        if self.skill_check == True:
            Skill = skill.Skill2(self.x, stage_data['stage1']['bottom'])
            skillList.append(Skill)
            self.skill_check = False
        if self.total_frame > self.state_frame:
            self.next_state()

    def handle_heal(self, frame_time, friendList, skillList):
        if self.skill_check == True:
            Skill = skill.Heal(self.x, self.y)
            skillList.append(Skill)
            self.hp += Skill.heal_amount
            if self.hp > mc_data['hp']:
                self.hp = mc_data['hp']
            self.skill_check = False
        if self.total_frame > self.state_frame:
            self.next_state()

    def handle_attack(self, frame_time, friendList, skillList):
        if self.total_frame > self.state_frame:
            self.next_state()

    def handle_summon(self, frame_time, friendList, skillList):
        if self.summon_check == True:
            Friend = friend.Friend(self.summon_name, self.x + 150) ## self.x + 200 소환 위치
            friendList.append(Friend)
            self.summon_check = False
        if self.total_frame > self.state_frame:
            self.next_state()

    def handle_die_right(self, frame_time, friendList, skillList):
        pass

    def handle_die_left(self, frame_time, friendList, skillList):
        pass

    def handle_hit_right(self, frame_time, friendList, skillList):
        self.next_state()
        pass

    def handle_hit_left(self, frame_time, friendList, skillList):
        self.next_state()
        pass

    def absorb_spirit(self):
        self.spirit += 10

    handle_state = {
        STAND_RIGHT : handle_stand_right,
        STAND_LEFT  : handle_stand_left,
        MOVE_RIGHT  : handle_move_right,
        MOVE_LEFT   : handle_move_left,
        SKILL1      : handle_skill1,
        SKILL2      : handle_skill2,
        HEAL        : handle_heal,
        ATTACK      : handle_attack,
        SUMMON      : handle_summon,
        DIE_RIGHT   : handle_die_right,
        DIE_LEFT    : handle_die_left,
        HIT_RIGHT   : handle_hit_right,
        HIT_LEFT    : handle_hit_left
    }

    def change_state(self):
        if self.state != self.current_state:
            self.past_state = self.current_state
            self.current_state = self.state
            self.state_frame = mc_data[self.state]['frame']
            self.total_frame = 0.0
            self.game_time = 0.0

    def get_bb(self):
        return self.x - mc_data['bb_left'], self.y - mc_data['bb_bottom'],\
                self.x + mc_data['bb_right'], self.y + mc_data['bb_height']

    def key_lock_func(self):
        self.key_lock = True

    def next_state(self):
        if self.right_key_pressed == True:
            self.state = self.MOVE_RIGHT
        elif self.left_key_pressed == True:
            self.state = self.MOVE_LEFT
        else:
            self.state = self.STAND_RIGHT

        self.key_lock = False



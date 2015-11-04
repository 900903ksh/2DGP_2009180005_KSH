from pico2d import *


class SkelSoldier:
    image = None
    MOVE,ATTACK,DIE,HIT = 0, 1, 2, 3

    def __init__(self):
        if SkelSoldier.image == None:
            SkelSoldier.image = load_image('resource/friend/Fnd1_SkelSoldier.png')
            self.x, self.y = 150, 135
            self.frame = 0
            self.state = self.MOVE

    def update(self):
        if self.state == self.MOVE:
            self.state_frame = 4
            #self.x += 7
        elif self.state == self.ATTACK:
            self.state_frame = 8
        elif self.state == self.DIE:
            self.state_frame = 6
        elif self.state == self.HIT:
            self.state_frame = 1

        self.frame = (self.frame + 1) % self.state_frame

    def draw(self):
        if self.state == self.MOVE:
            self.image.clip_draw(self.frame * 95, 470, 95, 110, 300 + self.x , self.y)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 109, 350, 109, 120, 300 + self.x+8, self.y+6)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 95, 240, 95, 110, 300 + self.x, self.y-3)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 110, 120, 110, 120, 300 + self.x+6, self.y+8)


class SkelOfficer:
    image = None
    MOVE,ATTACK,DIE,HIT = 0, 1, 2, 3

    def __init__(self):
        if SkelOfficer.image == None:
            SkelOfficer.image = load_image('resource/friend/Fnd2_SkelOfficer.png')
            self.x, self.y = 150, 145
            self.frame = 0
            self.state = self.MOVE

    def update(self):
        if self.state == self.MOVE:
            self.state_frame = 4
            #self.x += 7
        elif self.state == self.ATTACK:
            self.state_frame = 8
        elif self.state == self.DIE:
            self.state_frame = 6
        elif self.state == self.HIT:
            self.state_frame = 1

        self.frame = (self.frame + 1) % self.state_frame

    def draw(self):
        if self.state == self.MOVE:
            self.image.clip_draw(self.frame * 95, 490, 95, 115, 300 + self.x , self.y)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 109, 370, 109, 120, 300 + self.x+8, self.y+3)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 100, 250, 100, 120, 300 + self.x+2, self.y-4)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 110, 120, 110, 120, 300 + self.x+6, self.y)


class SkelCommander:
    image = None
    MOVE,ATTACK,DIE,HIT = 0, 1, 2, 3

    def __init__(self):
        if SkelCommander.image == None:
            SkelCommander.image = load_image('resource/friend/Fnd3_SkelCommander.png')
            self.x, self.y = 150, 158
            self.frame = 0
            self.state = self.MOVE

    def update(self):
        if self.state == self.MOVE:
            self.state_frame = 4
            #self.x += 7
        elif self.state == self.ATTACK:
            self.state_frame = 12
        elif self.state == self.DIE:
            self.state_frame = 11
        elif self.state == self.HIT:
            self.state_frame = 1

        self.frame = (self.frame + 1) % self.state_frame

    def draw(self):
        if self.state == self.MOVE:
            self.image.clip_draw(self.frame * 140, 600, 140, 155, 300 + self.x , self.y)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 160, 445, 160, 155, 300 + self.x+20, self.y)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 157, 280, 157, 165, 300 + self.x-24, self.y+1)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 160, 125, 160, 165, 300 + self.x+1, self.y+13)

class SkelSpearknight:
    image = None
    MOVE,ATTACK,DIE,HIT = 0, 1, 2, 3

    def __init__(self):
        if SkelSpearknight.image == None:
            SkelSpearknight.image = load_image('resource/friend/Fnd4_SkelSpearknight.png')
            self.x, self.y = 150, 150
            self.frame = 0
            self.state = self.MOVE

    def update(self):
        if self.state == self.MOVE:
            self.state_frame = 4
            #self.x += 7
        elif self.state == self.ATTACK:
            self.state_frame = 8
        elif self.state == self.DIE:
            self.state_frame = 10
        elif self.state == self.HIT:
            self.state_frame = 1

        self.frame = (self.frame + 1) % self.state_frame

    def draw(self):
        if self.state == self.MOVE:
            self.image.clip_draw(self.frame * 155, 605, 155, 120, 300 + self.x , self.y)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 460, 475, 460, 120, 300 + self.x+81, self.y-1)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 215, 260, 215, 155, 300 + self.x-32, self.y+17)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 155, 120, 155, 120, 300 + self.x+1, self.y-1)


class Wraith:
    image = None
    MOVE,ATTACK,DIE,HIT,REGEN = 0, 1, 2, 3, 4

    def __init__(self):
        if Wraith.image == None:
            Wraith.image = load_image('resource/friend/Fnd5_Wraith.png')
            self.x, self.y = 150, 145
            self.frame = 0
            self.state = self.MOVE

    def update(self):
        if self.state == self.MOVE:
            self.state_frame = 6
            #self.x += 7
        elif self.state == self.ATTACK:
            self.state_frame = 12
        elif self.state == self.DIE:
            self.state_frame = 7
        elif self.state == self.HIT:
            self.state_frame = 1
        elif self.state == self.REGEN:
            self.state_frame = 9

        self.frame = (self.frame + 1) % self.state_frame

    def draw(self):
        if self.state == self.MOVE:
            self.image.clip_draw(self.frame * 96, 625, 96, 100, 300 + self.x , self.y)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 124, 525, 124, 100, 300 + self.x+11, self.y+2)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 90, 415, 90, 110, 300 + self.x+14, self.y)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 110, 305, 110, 110, 300 + self.x+6, self.y+4)
        elif self.state == self.REGEN:
            self.image.clip_draw(self.frame * 170, 0, 170, 175, 300 + self.x+11, self.y)


class MuscleStone:
    image = None
    MOVE,ATTACK,DIE,HIT = 0, 1, 2, 3

    def __init__(self):
        if MuscleStone.image == None:
            MuscleStone.image = load_image('resource/friend/Fnd6_MuscleStone.png')
            self.x, self.y = 150, 152
            self.frame = 0
            self.state = self.MOVE

    def update(self):
        if self.state == self.MOVE:
            self.state_frame = 6
            #self.x += 7
        elif self.state == self.ATTACK:
            self.state_frame = 15
        elif self.state == self.DIE:
            self.state_frame = 6
        elif self.state == self.HIT:
            self.state_frame = 1

        self.frame = (self.frame + 1) % self.state_frame

    def draw(self):
        if self.state == self.MOVE:
            self.image.clip_draw(self.frame * 144, 590, 144, 130, 300 + self.x , self.y)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 153, 440, 153, 145, 300 + self.x+2, self.y+5)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 170, 320, 170, 120, 300 + self.x, self.y-20)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 180, 190, 180, 130, 300 + self.x-20, self.y)

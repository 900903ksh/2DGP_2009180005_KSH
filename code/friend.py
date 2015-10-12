from pico2d import *

running = None

class Friend_1:
    image = None
    MOVE,ATTACK,DIE,HIT = 0, 1, 2, 3

    def __init__(self):
        if Friend_1.image == None:
            Friend_1.image = load_image('resource/friend/friend1.png')
            self.x, self.y = 0, 0
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
            self.image.clip_draw(self.frame * 95, 470, 95, 110, 300 + self.x , 205)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 109, 350, 109, 120, 300 + self.x+8, 205+6)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 95, 240, 95, 110, 300 + self.x, 205-3)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 110, 120, 110, 120, 300 + self.x+6, 205+8)


class Friend_2:
    image = None
    MOVE,ATTACK,DIE,HIT = 0, 1, 2, 3

    def __init__(self):
        if Friend_2.image == None:
            Friend_2.image = load_image('resource/friend/friend2.png')
            self.x, self.y = 0, 0
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
            self.image.clip_draw(self.frame * 95, 490, 95, 115, 300 + self.x , 205)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 109, 370, 109, 120, 300 + self.x+8, 205+3)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 100, 250, 100, 120, 300 + self.x+2, 205-4)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 110, 120, 110, 120, 300 + self.x+6, 205)


class Friend_3:
    image = None
    MOVE,ATTACK,DIE,HIT = 0, 1, 2, 3

    def __init__(self):
        if Friend_3.image == None:
            Friend_3.image = load_image('resource/friend/friend3.png')
            self.x, self.y = 0, 0
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
            self.image.clip_draw(self.frame * 140, 600, 140, 155, 300 + self.x , 205)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 160, 445, 160, 155, 300 + self.x+20, 205)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 157, 280, 157, 165, 300 + self.x-24, 205+1)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 160, 125, 160, 165, 300 + self.x+1, 205+13)

class Friend_4:
    image = None
    MOVE,ATTACK,DIE,HIT = 0, 1, 2, 3

    def __init__(self):
        if Friend_4.image == None:
            Friend_4.image = load_image('resource/friend/friend4.png')
            self.x, self.y = 0, 0
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
            self.image.clip_draw(self.frame * 155, 605, 155, 120, 300 + self.x , 205)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 460, 475, 460, 120, 300 + self.x+81, 205-1)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 215, 260, 215, 155, 300 + self.x-32, 205+17)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 155, 120, 155, 120, 300 + self.x+1, 205-1)


class Friend_5:
    image = None
    MOVE,ATTACK,DIE,HIT,REGEN = 0, 1, 2, 3, 4

    def __init__(self):
        if Friend_5.image == None:
            Friend_5.image = load_image('resource/friend/friend5.png')
            self.x, self.y = 0, 0
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
            self.image.clip_draw(self.frame * 96, 625, 96, 100, 300 + self.x , 205)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 124, 525, 124, 100, 300 + self.x+11, 205+2)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 90, 415, 90, 110, 300 + self.x+14, 205)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 110, 305, 110, 110, 300 + self.x+6, 205+4)
        elif self.state == self.REGEN:
            self.image.clip_draw(self.frame * 170, 0, 170, 175, 300 + self.x+11, 205)


class Friend_6:
    image = None
    MOVE,ATTACK,DIE,HIT = 0, 1, 2, 3

    def __init__(self):
        if Friend_6.image == None:
            Friend_6.image = load_image('resource/friend/friend6.png')
            self.x, self.y = 0, 0
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
            self.image.clip_draw(self.frame * 144, 590, 144, 130, 300 + self.x , 205)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 153, 440, 153, 145, 300 + self.x+2, 205+5)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 170, 320, 170, 120, 300 + self.x, 205-20)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 180, 190, 180, 130, 300 + self.x-20, 205)

from pico2d import *

class Enemy_1:
    image = None
    MOVE,ATTACK,DIE,HIT = 0, 1, 2, 3

    def __init__(self):
        if Enemy_1.image == None:
            Enemy_1.image = load_image('resource/enemy/enemy1.png')
            self.x, self.y = 0, 0
            self.frame = 0
            self.state = self.MOVE

    def update(self):
        if self.state == self.MOVE:
            self.state_frame = 8
            #self.x += 7
        elif self.state == self.ATTACK:
            self.state_frame = 11
        elif self.state == self.DIE:
            self.state_frame = 5
        elif self.state == self.HIT:
            self.state_frame = 1

        self.frame = (self.frame + 1) % self.state_frame

    def draw(self):
        if self.state == self.MOVE:
            self.image.clip_draw(self.frame * 121, 468, 121, 100, 300 + self.x , 205)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 142, 333, 142, 135, 300 + self.x-5, 205+16)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 140, 228, 140, 100, 300 + self.x+5, 205-6)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 130, 128, 130, 100, 300 + self.x, 205-4)

class Enemy_2:
    image = None
    MOVE,ATTACK,DIE,HIT = 0, 1, 2, 3

    def __init__(self):
        if Enemy_2.image == None:
            Enemy_2.image = load_image('resource/enemy/enemy2.png')
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
            self.state_frame = 8
        elif self.state == self.HIT:
            self.state_frame = 1

        self.frame = (self.frame + 1) % self.state_frame

    def draw(self):
        if self.state == self.MOVE:
            self.image.clip_draw(self.frame * 182, 725, 182, 190, 300 + self.x , 205)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 401, 485, 401, 240, 300 + self.x-80, 205+28)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 264, 305, 264, 170, 300 + self.x-63, 205-10)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 190, 115, 190, 190, 300 + self.x-6, 205-1)


class Enemy_3:
    image = None
    MOVE,ATTACK,DIE,HIT = 0, 1, 2, 3

    def __init__(self):
        if Enemy_3.image == None:
            Enemy_3.image = load_image('resource/enemy/enemy3.png')
            self.x, self.y = 0, 0
            self.frame = 0
            self.state = self.MOVE

    def update(self):
        if self.state == self.MOVE:
            self.state_frame = 6
            #self.x += 7
        elif self.state == self.ATTACK:
            self.state_frame = 18
        elif self.state == self.DIE:
            self.state_frame = 5
        elif self.state == self.HIT:
            self.state_frame = 1

        self.frame = (self.frame + 1) % self.state_frame

    def draw(self):
        if self.state == self.MOVE:
            self.image.clip_draw(self.frame * 198, 743, 198, 190, 300 + self.x, 205)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 280, 543, 280, 190, 300 + self.x - 33, 205 - 2)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 194, 323, 194, 210, 300 + self.x - 2, 205 - 9)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 190, 133, 190, 190, 300 + self.x + 12, 205)

class Enemy_4:
    image = None
    MOVE,ATTACK,DIE,HIT = 0, 1, 2, 3

    def __init__(self):
        if Enemy_4.image == None:
            Enemy_4.image = load_image('resource/enemy/enemy4.png')
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
            self.state_frame = 6
        elif self.state == self.HIT:
            self.state_frame = 1

        self.frame = (self.frame + 1) % self.state_frame

    def draw(self):
        if self.state == self.MOVE:
            self.image.clip_draw(self.frame * 191, 732, 191, 190, 300 + self.x, 205)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 301, 532, 301, 200, 300 + self.x + 12, 205 - 9)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 220, 322, 220, 200, 300 + self.x + 14, 205 + 6)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 210, 122, 210, 200, 300 + self.x + 18, 205 + 2)

class Enemy_5:
    image = None
    MOVE,ATTACK,DIE,HIT = 0, 1, 2, 3

    def __init__(self):
        if Enemy_5.image == None:
            Enemy_5.image = load_image('resource/enemy/enemy5.png')
            self.x, self.y = 0, 0
            self.frame = 0
            self.state = self.MOVE

    def update(self):
        if self.state == self.MOVE:
            self.state_frame = 7
            #self.x += 7
        elif self.state == self.ATTACK:
            self.state_frame = 18
        elif self.state == self.DIE:
            self.state_frame = 13
        elif self.state == self.HIT:
            self.state_frame = 1

        self.frame = (self.frame + 1) % self.state_frame

    def draw(self):
        if self.state == self.MOVE:
            self.image.clip_draw(self.frame * 133, 697, 133, 140, 300 + self.x, 205)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 307, 497, 307, 200, 300 + self.x - 10, 205 + 15)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 175, 347, 175, 140, 300 + self.x + 21, 205 - 3)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 160, 197, 160, 140, 300 + self.x + 22, 205 + 3)

class Enemy_6:
    image = None
    MOVE,ATTACK,DIE,HIT = 0, 1, 2, 3

    def __init__(self):
        if Enemy_6.image == None:
            Enemy_6.image = load_image('resource/enemy/enemy6.png')
            self.x, self.y = 0, 0
            self.frame = 0
            self.state = self.MOVE

    def update(self):
        if self.state == self.MOVE:
            self.state_frame = 5
            #self.x += 7
        elif self.state == self.ATTACK:
            self.state_frame = 4
        elif self.state == self.DIE:
            self.state_frame = 3
        elif self.state == self.HIT:
            self.state_frame = 1

        self.frame = (self.frame + 1) % self.state_frame

    def draw(self):
        if self.state == self.MOVE:
            self.image.clip_draw(self.frame * 195, 835, 195, 180, 300 + self.x, 205)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 211, 645, 211, 190, 300 + self.x - 5, 205 + 6)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 255, 465, 255, 180, 300 + self.x + 9, 205 - 1)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 190, 280, 190, 180, 300 + self.x + 14, 205 - 2)


class Enemy_7:
    image = None
    MOVE,ATTACK,DIE,HIT = 0, 1, 2, 3

    def __init__(self):
        if Enemy_7.image == None:
            Enemy_7.image = load_image('resource/enemy/enemy7.png')
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
            self.image.clip_draw(self.frame * 322, 1382, 322, 330, 300 + self.x, 205)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 322, 1052, 322, 330, 300 + self.x - 2, 205 + 1)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 170, 652, 170, 395, 300 + self.x + 7, 205 - 9)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 180, 327, 180, 320, 300 + self.x + 16, 205 - 5)


class Enemy_Bonus:
    image = None
    MOVE,DIE,HIT = 0, 1, 2

    def __init__(self):
        if Enemy_Bonus.image == None:
            Enemy_Bonus.image = load_image('resource/enemy/enemy_bonus.png')
            self.x, self.y = 0, 0
            self.frame = 0
            self.state = self.MOVE

    def update(self):
        if self.state == self.MOVE:
            self.state_frame = 8
        elif self.state == self.DIE:
            self.state_frame = 14
        elif self.state == self.HIT:
            self.state_frame = 1

        self.frame = (self.frame + 1) % self.state_frame

    def draw(self):
        if self.state == self.MOVE:
            self.image.clip_draw(self.frame * 102, 230, 102, 100, 300 + self.x, 205)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 145, 100, 145, 120, 300 + self.x + 11, 205 - 11)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 110, 0, 110, 100, 300 + self.x + 1, 205 - 1)
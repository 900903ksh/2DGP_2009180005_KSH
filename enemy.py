from pico2d import *


class Bulldog:
    image = None
    MOVE,ATTACK,DIE,HIT = 0, 1, 2, 3

    def __init__(self):
        if Bulldog.image == None:
            Bulldog.image = load_image('resource/enemy/Emy1_Bulldog.png')
            self.x, self.y = 500, 137
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
            self.image.clip_draw(self.frame * 121, 468, 121, 100, 300 + self.x , self.y)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 142, 333, 142, 135, 300 + self.x-5, self.y+16)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 140, 228, 140, 100, 300 + self.x+5, self.y-6)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 130, 128, 130, 100, 300 + self.x, self.y-4)


class Lycanthrope:
    image = None
    MOVE,ATTACK,DIE,HIT = 0, 1, 2, 3

    def __init__(self):
        if Lycanthrope.image == None:
            Lycanthrope.image = load_image('resource/enemy/Emy2_Lycanthrope.png')
            self.x, self.y = 500, 185
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
            self.image.clip_draw(self.frame * 182, 725, 182, 190, 300 + self.x , self.y)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 401, 485, 401, 240, 300 + self.x-80, self.y+28)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 264, 305, 264, 170, 300 + self.x-63, self.y-10)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 190, 115, 190, 190, 300 + self.x-6, self.y-1)


class CorruptedWyvern:
    image = None
    MOVE,ATTACK,DIE,HIT = 0, 1, 2, 3

    def __init__(self):
        if CorruptedWyvern.image == None:
            CorruptedWyvern.image = load_image('resource/enemy/Emy3_CorruptedWyvern.png')
            self.x, self.y = 500, 188
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
            self.image.clip_draw(self.frame * 198, 743, 198, 190, 300 + self.x, self.y)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 280, 543, 280, 190, 300 + self.x - 33, self.y - 2)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 194, 323, 194, 210, 300 + self.x - 2, self.y - 9)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 190, 133, 190, 190, 300 + self.x + 12, self.y)


class CorruptedCornian:
    image = None
    MOVE,ATTACK,DIE,HIT = 0, 1, 2, 3

    def __init__(self):
        if CorruptedCornian.image == None:
            CorruptedCornian.image = load_image('resource/enemy/Emy4_CorruptedCornian.png')
            self.x, self.y = 500, 184
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
            self.image.clip_draw(self.frame * 191, 732, 191, 190, 300 + self.x, self.y)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 301, 532, 301, 200, 300 + self.x + 12, self.y - 9)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 220, 322, 220, 200, 300 + self.x + 14, self.y + 6)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 210, 122, 210, 200, 300 + self.x + 18, self.y + 2)


class DemonGargoyle:
    image = None
    MOVE,ATTACK,DIE,HIT = 0, 1, 2, 3

    def __init__(self):
        if DemonGargoyle.image == None:
            DemonGargoyle.image = load_image('resource/enemy/Emy5_DemonGargoyle.png')
            self.x, self.y = 500, 162
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
            self.image.clip_draw(self.frame * 133, 697, 133, 140, 300 + self.x, self.y)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 307, 497, 307, 200, 300 + self.x - 10, self.y + 15)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 175, 347, 175, 140, 300 + self.x + 21, self.y - 3)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 160, 197, 160, 140, 300 + self.x + 22, self.y + 3)


class JuniorBalrog:
    image = None
    MOVE,ATTACK,DIE,HIT = 0, 1, 2, 3

    def __init__(self):
        if JuniorBalrog.image == None:
            JuniorBalrog.image = load_image('resource/enemy/Emy6_JuniorBalrog.png')
            self.x, self.y = 500, 180
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
            self.image.clip_draw(self.frame * 195, 835, 195, 180, 300 + self.x, self.y)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 211, 645, 211, 190, 300 + self.x - 5, self.y + 6)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 255, 465, 255, 180, 300 + self.x + 9, self.y - 1)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 190, 280, 190, 180, 300 + self.x + 14, self.y - 2)


class CrimsonBalrog:
    image = None
    MOVE,ATTACK,DIE,HIT = 0, 1, 2, 3

    def __init__(self):
        if CrimsonBalrog.image == None:
            CrimsonBalrog.image = load_image('resource/enemy/Emy7_CrimsonBalrog.png')
            self.x, self.y = 500, 260
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
            self.image.clip_draw(self.frame * 322, 1382, 322, 330, 300 + self.x, self.y)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 322, 1052, 322, 330, 300 + self.x - 2, self.y + 1)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 170, 652, 170, 395, 300 + self.x + 7, self.y - 9)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 180, 327, 180, 320, 300 + self.x + 16, self.y - 5)


class BabyBalrog:
    image = None
    MOVE,DIE,HIT = 0, 1, 2

    def __init__(self):
        if BabyBalrog.image == None:
            BabyBalrog.image = load_image('resource/enemy/EmyBonus_BabyBalrog.png')
            self.x, self.y = 500, 145
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
            self.image.clip_draw(self.frame * 102, 230, 102, 100, 300 + self.x, self.y)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 145, 100, 145, 120, 300 + self.x + 11, self.y - 11)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 110, 0, 110, 100, 300 + self.x + 1, self.y - 1)
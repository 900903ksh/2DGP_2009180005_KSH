from pico2d import *

class Main_Character:
    STAND_RIGHT, STAND_LEFT, MOVE_RIGHT, MOVE_LEFT, MOTION1, MOTION2, MOTION3, MOTION4, \
    MOTION5, DIE_RIGHT, DIE_LEFT, HIT_RIGHT, HIT_LEFT = 0,1,2,3,4,5,6,7,8,9,10,11,12
    def __init__(self):
        self.image=load_image('resource/friend/main_character_0.png')
        self.x, self.y = 0, 0
        self.frame = 0
        self.state = self.STAND_RIGHT

    def update(self):
        if self.state == self.MOVE_RIGHT:
            self.x += 7
        if self.state == self.MOVE_LEFT:
            self.x -= 7
        if self.state == self.STAND_RIGHT or self.state == self.MOVE_RIGHT\
            or self.state == self.STAND_LEFT or self.state == self.MOVE_LEFT:
            self.state_frame = 8
        elif self.state == self.MOTION1 or self.state == self.MOTION2:
            self.state_frame = 13
        elif self.state == self.MOTION3:
            self.state_frame = 9
        elif self.state == self.MOTION4 or self.state == self.MOTION5:
            self.state_frame = 12
        elif self.state == self.DIE_RIGHT or self.state == self.DIE_LEFT:
            self.state_frame = 9
        elif self.state == self.HIT_RIGHT or self.state == self.HIT_LEFT:
            self.state_frame = 1

        self.frame = (self.frame + 1) % self.state_frame

    def draw(self):
        if self.state == self.STAND_RIGHT or self.state == self.MOVE_RIGHT:
            self.image.clip_draw(self.frame * 204, 3760, 204, 287, 300 + self.x, 205)
        elif self.state == self.STAND_LEFT or self.state == self.MOVE_LEFT:
            self.image.clip_draw(self.frame * 204, 3463, 204, 287, 300 + self.x, 205)
        elif self.state == self.MOTION1:
            self.image.clip_draw(self.frame * 404, 3093, 404, 365, 300 + self.x + 50, 205 + 39)
        elif self.state == self.MOTION2:
            self.image.clip_draw(self.frame * 335, 2735, 335, 348, 300 + self.x + 14, 205 + 37)
        elif self.state == self.MOTION3:
            self.image.clip_draw(self.frame * 265, 2409, 265, 316, 300 + self.x + 35, 205 + 14)
        elif self.state == self.MOTION4:
            self.image.clip_draw(self.frame * 277, 2053, 277, 341, 300 + self.x - 16, 205 + 36)
        elif self.state == self.MOTION5:
            self.image.clip_draw(self.frame * 281, 1746, 281, 297, 300 + self.x - 18, 205 + 14)
        elif self.state == self.DIE_RIGHT:
            self.image.clip_draw(self.frame * 338, 1402, 338, 334, 300 + self.x - 26, 205 + 21)
        elif self.state == self.DIE_LEFT:
            self.image.clip_draw(self.frame * 338, 1058, 338, 334, 300 + self.x + 26, 205 + 21)
        elif self.state == self.HIT_RIGHT:
            self.image.clip_draw(self.frame * 255, 761, 255, 287, 300 + self.x - 26, 205 + 21)
        elif self.state == self.HIT_LEFT:
            self.image.clip_draw(self.frame * 255, 464, 255, 287, 300 + self.x + 26, 205 + 21)

    def handle_events(self):
        global running

        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                running = False
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                running = False
            elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
                self.state = self.STAND_RIGHT
            elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
                self.state = self.STAND_LEFT
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                self.state = self.MOVE_RIGHT
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                self.state = self.MOVE_LEFT
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
                self.state = self.MOTION1
                self.frame = 0
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_w):
                self.state = self.MOTION2
                self.frame = 0
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_e):
                self.state = self.MOTION3
                self.frame = 0
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_r):
                self.state = self.MOTION4
                self.frame = 0
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_t):
                self.state = self.MOTION5
                self.frame = 0
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
                self.state = self.DIE_RIGHT
                self.frame = 0
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_s):
                self.state = self.DIE_LEFT
                self.frame = 0
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_d):
                self.state = self.HIT_RIGHT
                self.frame = 0
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_f):
                self.state = self.HIT_LEFT
                self.frame = 0




open_canvas()
hero = Main_Character()

running = True

while running:
    hero.handle_events()


    clear_canvas()
    hero.update()
    hero.draw()
    update_canvas()

    delay(0.07)

close_canvas()


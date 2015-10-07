from pico2d import *

class Main_Character:
    global dir
    global move
    LEFT_MOVE, RIGHT_MOVE = 0, 1

    def __init__(self):
        self.image_r = load_image('resource/friend/m_stand_r.png')
        self.image_l = load_image('resource/friend/m_stand_l.png')
        self.x, self.y = 0, 0
        self.frame = 0
        self.state = self.RIGHT_MOVE

    def update(self):
        self.frame = (self.frame +1) % 8
        if dir == 1:
            self.state = self.RIGHT_MOVE
        elif dir == -1:
            self.state = self.LEFT_MOVE
        self.x = move

    def draw(self):
        if self.state == self.RIGHT_MOVE:
            self.image_r.clip_draw(self.frame * 204, 0, 204, 295, 300 + self.x, 200, 204, 295)
        elif self.state == self.LEFT_MOVE:
            self.image_l.clip_draw(self.frame * 204, 0, 204, 295, 300 + self.x, 200, 204, 295)

def handle_events():
    global running
    global dir
    global move

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

        if event.type == SDL_KEYDOWN or event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                    dir = 1
                    move += 10
            elif event.key == SDLK_LEFT:
                dir = -1
                move -= 10

dir = 1
move = 0
push = False

open_canvas()

hero = Main_Character()

running = True

while running:
    handle_events()

    hero.update()

    clear_canvas()

    hero.draw()
    update_canvas()

    delay(0.05)

close_canvas()


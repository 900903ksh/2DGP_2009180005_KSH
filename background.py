from pico2d import *
import ui

class Background:
    def __init__(self):
        self.image = load_image('resource/stage/stage1.png')
        self.speed = 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.ui = ui.UI(0)

    def set_center_object(self, mc):
        self.center_object = mc

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, 0, self.canvas_width, self.canvas_height, 0, 0)
        self.ui.draw()


    def update(self, frame_time):
        self.window_left = clamp(0, int(self.center_object.x) - self.canvas_width//2, self.w - self.canvas_width)
        self.ui.update(frame_time)


    def handle_event(self, event):
        pass
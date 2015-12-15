from etc import *


class Background:
    def __init__(self):
        self.image = stage_image()
        self.speed = 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

        get_sound(stage_name()).repeat_play()

    def set_center_object(self, mc):
        self.center_object = mc

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, 0, self.canvas_width, self.canvas_height, 0, 0)

    def update(self, frame_time):
        self.window_left = clamp(0, int(self.center_object.x) - self.canvas_width//2, self.w - self.canvas_width)

    def handle_event(self, event):
        pass
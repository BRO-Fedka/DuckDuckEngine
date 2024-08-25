import pygame
import math


class Circle:
    def __init__(self, world, x, y, z, color=(255, 0, 0), r=1):
        self.world = world
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.cl = color

    def calc_scr_pos(self, offset_x=0, offset_y=0):
        dx = (self.world.camera.x - self.x)
        dy = (self.world.camera.y - self.y)
        sin = math.sin(self.world.camera.dir / 180 * math.pi)
        cos = math.cos(self.world.camera.dir / 180 * math.pi)
        # +(poly[_][1]*cos*320)+(poly[_][0]*320*sin)  | +(poly[_][1]*sin*320)-(poly[_][0]*cos*320)
        return (self.world.game.w / 2 + (dy * cos + sin * dx) * self.world.camera.zoom + offset_x,
                self.world.game.h / 2 + (
                            - dy * sin * self.world.camera.vert_cos + cos * dx * self.world.camera.vert_cos - (
                                self.z - self.world.camera.z) * self.world.camera.vert_sin) * self.world.camera.zoom + offset_y)

    def draw(self):
        pygame.draw.circle(self.world.game.screen, self.cl, self.calc_scr_pos(), self.r * self.world.camera.zoom)

    def update(self): pass

    def calc_position_in_draw_queue(self):
        dx = (self.world.camera.x - self.x)
        dy = (self.world.camera.y - self.y)
        sin = math.sin(self.world.camera.dir / 180 * math.pi)
        cos = math.cos(self.world.camera.dir / 180 * math.pi)
        return - dy * sin + cos * dx + self.z

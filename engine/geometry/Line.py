import math
import pygame
from engine.geometry.Point import Point


class Line:
    def __init__(self, world, p1, p2, color=(255, 0, 0), width=3):
        self.p1 = p1
        self.p2 = p2
        self.world = world
        self.w = width
        self.cl = color

    def draw(self):
        # deg = lookat(self.p2.calc_scr_pos()[0]-self.p1.calc_scr_pos()[0],self.p2.calc_scr_pos()[1]-self.p1.calc_scr_pos()[1])
        # cossin = abs(math.cos(deg/180*math.pi))+abs(math.sin(deg/180*math.pi))
        pygame.draw.line(self.world.game.screen, self.cl, self.p1.calc_scr_pos(), self.p2.calc_scr_pos(),
                     math.ceil(self.w * self.world.camera.zoom))  # w * cossin
        pygame.draw.circle(self.world.game.screen, self.cl, self.p1.calc_scr_pos(1, 1),
                       math.ceil(self.w / 2 * self.world.camera.zoom))
        pygame.draw.circle(self.world.game.screen, self.cl, self.p2.calc_scr_pos(1, 1),
                       math.ceil(self.w / 2 * self.world.camera.zoom))
        self.p1.draw()
        self.p2.draw()

    def update(self): pass

    def calc_position_in_draw_queue(self):
        p = Point(self.world, (self.p1.x + self.p2.x) / 2, (self.p1.y + self.p2.y) / 2, (self.p1.z + self.p2.z) / 2)

        return p.calc_position_in_draw_queue()

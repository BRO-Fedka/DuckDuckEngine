from engine.geometry.Point import Point
import pygame


class aLine:
    def __init__(self, world, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.world = world

    def update(self): pass

    def draw(self):
        pygame.draw.aaline(self.world.game.screen, (255, 0, 255), self.p1.calc_scr_pos(), self.p2.calc_scr_pos())

    def calc_position_in_draw_queue(self):
        p = Point(self.world, (self.p1.x + self.p2.x) / 2, (self.p1.y + self.p2.y) / 2, (self.p1.z + self.p2.z) / 2)

        return p.calc_position_in_draw_queue()

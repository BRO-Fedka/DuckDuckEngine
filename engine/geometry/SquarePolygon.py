from engine.geometry.Point import Point
from engine.base.Vector3D import Vector3D
import pygame
from typing import List
from engine.geometry.Base import Base


class SquarePolygon(Base):
    instances: List = []

    def __init__(self, world, p1, p2, p3, p4, color):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.world = world
        self.cl = color
        self.instances.append(self)

    def draw(self):
        def take0(val):
            return val[0]

        a = Vector3D(self.p3.x - self.p2.x, self.p3.y - self.p2.y, self.p3.z - self.p2.z)
        b = Vector3D(self.p1.x - self.p2.x, self.p1.y - self.p2.y, self.p1.z - self.p2.z)
        c = Vector3D(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x)
        cam_vec = Vector3D(self.world.camera.surf_cos, self.world.camera.surf_sin, -self.world.camera.vert_cos)
        c_cam = c.x * cam_vec.x + c.y * cam_vec.y + c.z * cam_vec.z
        cos = c_cam / c.module() / cam_vec.module()
        cos = abs(cos)
        color = (0, 0, int(cos * 255))
        pygame.draw.polygon(self.world.game.screen, color,
                            [self.p1.calc_scr_pos(), self.p2.calc_scr_pos(), self.p3.calc_scr_pos(),
                             self.p4.calc_scr_pos()])

        self.p1.draw()
        self.p2.draw()
        self.p3.draw()
        self.p4.draw()

    def update(self): pass

    def calc_position_in_draw_queue(self):
        p = Point(self.world, (self.p1.x + self.p2.x + self.p3.x + self.p4.x) / 4,
                  (self.p1.y + self.p2.y + self.p3.y + self.p4.y) / 4,
                  (self.p1.z + self.p2.z + self.p3.z + self.p4.z) / 4)

        return p.calc_position_in_draw_queue()

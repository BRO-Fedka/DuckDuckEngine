from random import *
from engine import *


class Duck:
    def __init__(self, world, x, y, z, name):
        self.name = name
        self.dinamic_object = DinamicObject2D(self, 10, 20)
        self.gravity_object = GravityObject(self, 10)
        self.world = world
        self.x = x
        self.y = y
        self.z = z
        self.dir = 0
        self.target_dir = 0
        self.p = Point(self.world, x, y, z)
        self.p_neck = Point(self.world, x + math.cos(self.dir / 180 * math.pi) * 13,
                            y + math.sin(self.dir / 180 * math.pi) * 12, z)
        self.p_ass = Point(self.world, x - math.cos(self.dir / 180 * math.pi) * 13,
                           y - math.sin(self.dir / 180 * math.pi) * 12, z)
        self.body = Line(self.world, self.p_neck, self.p_ass, (255, 255, 255), 20)
        # Circle(self.world, x + math.cos(self.dir / 180 * math.pi) * 20, y + math.sin(self.dir / 180 * math.pi) * 20, 40,
        #        (255, 255, 255), 10)
        self.head = Head(self.world, x + math.cos(self.dir / 180 * math.pi) * 20,
                         y + math.sin(self.dir / 180 * math.pi) * 20, z, self, 20)
        self.neck = Line(self.world, self.p_neck, self.head, (255, 255, 255), 16)
        self.world.game.objects[name + ".body"] = self.body
        self.world.game.objects[name + ".head"] = self.head
        self.world.game.objects[name + ".neck"] = self.neck
        self.left_leg = Leg(self.world, random() * 30 - 15, random() * 30 - 15, 0, self, -6)
        self.right_leg = Leg(self.world, random() * 30 - 15, random() * 30 - 15, 0, self, 6)
        self.world.game.objects[name + ".left_leg"] = self.left_leg
        self.world.game.objects[name + ".right_leg"] = self.right_leg
        # self.rleg_deg = 0
        # self.lleg_deg = 0

    def update(self):
        self.left_leg.update()
        self.right_leg.update()
        # self.dir += (self.target_dir - self.dir)*0.05
        self.p_neck.x = self.x + math.cos(self.dir / 180 * math.pi) * 12
        self.p_neck.y = self.y + math.sin(self.dir / 180 * math.pi) * 12
        self.p_neck.z = self.z + 20
        self.p_ass.x = self.x - math.cos(self.dir / 180 * math.pi) * 12
        self.p_ass.y = self.y - math.sin(self.dir / 180 * math.pi) * 12
        self.p_ass.z = self.z + 20
        self.head.x = self.x + math.cos(self.dir / 180 * math.pi) * 18
        self.head.y = self.y + math.sin(self.dir / 180 * math.pi) * 18
        self.head.z = self.z + 30
        self.p.x = self.x
        self.p.y = self.y
        self.p.z = self.z
        # self.left_leg.x = self.x + math.sin(self.dir/180*math.pi) * 4
        # self.right_leg.x = self.x - math.sin(self.dir / 180 * math.pi) * 4
        # self.left_leg.y = self.y - math.cos(self.dir / 180 * math.pi)*4
        # self.right_leg.y = self.y + math.cos(self.dir / 180 * math.pi) * 4
        self.dinamic_object.update()
        self.gravity_object.update()
        # if self.dinamic_object.ismoving:
        #     speed = self.dinamic_object.v.module()
        #     self.rleg_deg += speed
        #     self.lleg_deg += speed
        #     self.right_leg.z = math.sin(self.rleg_deg)*3+3
        #     self.left_leg.z = math.sin(self.lleg_deg)*3+3
        # else:
        #     self.right_leg.z = 0
        #     self.left_leg.z = 0

    def draw(self):
        self.p.draw()
        # print(self.p.calc_scr_pos())

    def calc_position_in_draw_queue(self):
        return self.p.calc_position_in_draw_queue()


class Leg:
    def __init__(self, world, x, y, z, parent, leg_offset=4):
        self.parent = parent
        self.world = world
        self.leg_offset = leg_offset
        self.x = x
        self.y = y
        self.z = z
        self.target_x = x
        self.target_y = y
        self.target_z = z
        self.p = Circle(self.world, x, y, 0, (255, 128, 0), 4)

    def update(self):
        self.target_z = self.parent.z
        self.x += (self.target_x - self.x) * 0.2
        self.y += (self.target_y - self.y) * 0.2
        self.z += (self.target_z - self.z) * 0.2
        self.p.x = self.x
        self.p.y = self.y
        self.p.z = self.z
        # print(math.sqrt((self.parent.x-self.x)**2 + (self.parent.y -self.y)**2))
        if math.sqrt((self.parent.x - self.x) ** 2 + (self.parent.y - self.y) ** 2) > 20 + random() * 6 - 3:
            self.target_x = self.parent.x - math.cos(
                self.parent.dinamic_object.v.dir() / 180 * math.pi) * 20 + math.sin(
                self.parent.dinamic_object.v.dir() / 180 * math.pi) * self.leg_offset
            self.target_y = self.parent.y + math.sin(
                self.parent.dinamic_object.v.dir() / 180 * math.pi) * 20 - math.cos(
                self.parent.dinamic_object.v.dir() / 180 * math.pi) * self.leg_offset
            # print("!!!")

    def draw(self):
        self.p.draw()
        # print(self.p.calc_scr_pos())

    def calc_position_in_draw_queue(self):
        return self.p.calc_position_in_draw_queue()


class Head:
    def __init__(self, world, x, y, z, parent, head_offset):
        self.parent = parent
        self.world = world
        self.target_head_offset = head_offset
        self.head_offset = head_offset
        self.x = x
        self.y = y
        self.z = z
        self.p = Circle(self.world, x, y, z + 40, (255, 255, 255), 10)
        self.beak = Circle(self.world, x, y, z + 40, (255, 128, 0), 4)
        self.left_eye = Circle(self.world, x, y, z + 40, (0, 0, 0), 2)
        self.right_eye = Circle(self.world, x, y, z + 40, (0, 0, 0), 2)
        self.world.game.objects[self.parent.name + ".beck"] = self.beak
        self.world.game.objects[self.parent.name + ".left_eye"] = self.left_eye
        self.world.game.objects[self.parent.name + ".right_eye"] = self.right_eye

    def update(self):
        self.x = self.parent.x + math.cos(self.parent.dir / 180 * math.pi) * self.head_offset
        self.y = self.parent.y + math.sin(self.parent.dir / 180 * math.pi) * self.head_offset
        self.z = self.parent.z + 35
        self.beak.x = self.x + math.cos(self.parent.dir / 180 * math.pi) * 12
        self.beak.y = self.y + math.sin(self.parent.dir / 180 * math.pi) * 12
        self.beak.z = self.z - 2
        self.left_eye.x = self.x + math.cos((self.parent.dir - 25) / 180 * math.pi) * 10
        self.left_eye.y = self.y + math.sin((self.parent.dir - 25) / 180 * math.pi) * 10
        self.left_eye.z = self.z + 3
        self.right_eye.x = self.x + math.cos((self.parent.dir + 25) / 180 * math.pi) * 10
        self.right_eye.y = self.y + math.sin((self.parent.dir + 25) / 180 * math.pi) * 10
        self.right_eye.z = self.z + 3
        self.p.x = self.x
        self.p.y = self.y
        self.p.z = self.z
        # print("!!!")

    def draw(self):
        self.p.draw()
        # print(self.p.calc_scr_pos())

    def calc_position_in_draw_queue(self):
        return self.p.calc_position_in_draw_queue()

    def calc_scr_pos(self, offset_x=0, offset_y=0):
        return self.p.calc_scr_pos(offset_x, offset_y)

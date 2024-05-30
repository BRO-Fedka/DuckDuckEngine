import math
from random import  *
from engine import *
class Duck:
    def __init__(self,world,x,y,z,name):
        self.name = name
        self.dinamic_object = DinamicObject2D(self)
        self.world = world
        self.x = x
        self.y = y
        self.z = z
        self.dir = 0
        self.target_dir = 0
        self.p = Point(self.world,x,y,z)
        self.p_neck = Point(self.world,x+math.cos(self.dir/180*math.pi)*13,y+math.sin(self.dir/180*math.pi)*12,z)
        self.p_ass = Point(self.world,x-math.cos(self.dir/180*math.pi)*13,y-math.sin(self.dir/180*math.pi)*12,z)
        self.body = Line(self.world,self.p_neck,self.p_ass,(255,255,255),20)
        self.head = Circle(self.world,x+math.cos(self.dir/180*math.pi)*20,y+math.sin(self.dir/180*math.pi)*20,40,(255,255,255),10)
        self.neck = Line(self.world, self.p_neck, self.head, (255, 255, 255), 16)
        self.world.game.objects[name+".body"] = self.body
        self.world.game.objects[name + ".head"] = self.head
        self.world.game.objects[name + ".neck"] = self.neck
        self.left_leg = Leg(self.world,random()*30-15,random()*30-15,0,self,-6)
        self.right_leg = Leg(self.world,random()*30-15,random()*30-15,0,self,6)
        self.world.game.objects[name + ".left_leg"] = self.left_leg
        self.world.game.objects[name + ".right_leg"] = self.right_leg
        # self.rleg_deg = 0
        # self.lleg_deg = 0
    def update(self):
        self.left_leg.update()
        self.right_leg.update()
        # self.dir += (self.target_dir - self.dir)*0.05
        self.p_neck.x = self.x+math.cos(self.dir/180*math.pi)*12
        self.p_neck.y = self.y+math.sin(self.dir/180*math.pi)*12
        self.p_neck.z = self.z+20
        self.p_ass.x = self.x-math.cos(self.dir/180*math.pi)*12
        self.p_ass.y = self.y-math.sin(self.dir/180*math.pi)*12
        self.p_ass.z = self.z+20
        self.head.x = self.x + math.cos(self.dir/180*math.pi)*18
        self.head.y = self.y + math.sin(self.dir/180*math.pi)*18
        self.head.z = self.z+30
        self.p.x = self.x
        self.p.y = self.y
        self.p.z = self.z
        # self.left_leg.x = self.x + math.sin(self.dir/180*math.pi) * 4
        # self.right_leg.x = self.x - math.sin(self.dir / 180 * math.pi) * 4
        # self.left_leg.y = self.y - math.cos(self.dir / 180 * math.pi)*4
        # self.right_leg.y = self.y + math.cos(self.dir / 180 * math.pi) * 4
        self.dinamic_object.update()
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
    def __init__(self,world,x,y,z,parent,leg_offset= 4):
        self.parent = parent
        self.world = world
        self.leg_offset = leg_offset
        self.x = x
        self.y = y
        self.z = z
        self.target_x = x
        self.target_y = y
        self.p = Circle(self.world,x,y,0,(255,128,0),3)
    def update(self):
        self.x += (self.target_x-self.x) * 0.2
        self.y += (self.target_y - self.y) * 0.2
        self.p.x = self.x
        self.p.y = self.y
        # print(math.sqrt((self.parent.x-self.x)**2 + (self.parent.y -self.y)**2))
        if math.sqrt((self.parent.x-self.x)**2 + (self.parent.y -self.y)**2) > 20+ random()*6-3:
            self.target_x =self.parent.x - math.cos(self.parent.dinamic_object.v.dir() / 180 * math.pi)*20 + math.sin(self.parent.dinamic_object.v.dir() / 180 * math.pi)*self.leg_offset
            self.target_y =self.parent.y + math.sin(self.parent.dinamic_object.v.dir() / 180 * math.pi)*20 - math.cos(self.parent.dinamic_object.v.dir() / 180 * math.pi)*self.leg_offset
            # print("!!!")
    def draw(self):
        self.p.draw()
        # print(self.p.calc_scr_pos())
    def calc_position_in_draw_queue(self):
        return self.p.calc_position_in_draw_queue()
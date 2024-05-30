import math
import pygame as pg
def lookat(x,y):
 if x == 0:
  x = 0.0001
 angle = -math.atan((y / x)) / ( math.pi / 180)
 # if y != abs(y):
 #  angle =  angle + 360
 if x != abs(x):
  angle =  angle + 180
 return angle+180
class Game:
    def __init__(self,setup ,loop):
        self.FPS = 60
        pg.init()
        self.w = 600
        self.h = 400
        self.bg_color = (0,0,0)
        self.screen = pg.display.set_mode((self.w, self.h))
        self.clock = pg.time.Clock()
        self.__vars = {}
        self.cameras = {}
        self.stages = {}
        self.i_active_stage = None
        self.i_active_camera = None
        self.objects = {}
        setup(self)
        pg.display.update()
        while True:
            self.clock.tick(self.FPS)
            loop(self)
            self.cameras[self.i_active_camera].update()
            self.stages[self.i_active_stage].update()
            self.update()
            self.draw()
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    exit()

            pg.display.update()
    def __getitem__(self, item):
        return self.__vars[item]
    def __setitem__(self, key, value):
        self.__vars[key] = value
    def update(self):
        for obj in self.objects.keys():
            self.objects[obj].update()
    def draw(self):
        self.screen.fill(self.bg_color)
        draw_queue = []
        for obj in self.objects.keys():
            draw_queue.append((obj,self.objects[obj].calc_position_in_draw_queue()))

        def takeSecond(elem):
            return elem[ 1]
        draw_queue.sort(key=takeSecond)
        for couple in draw_queue:
            obj = couple [0]
            self.objects[obj].draw()

class World:
    def __init__(self,game):
        self.game = game

        self.camera = None
    def update(self):
        pass
class Camera:
    def __init__(self,world,x,y,dir,vert_dir = 45):
        self.speed_cof = 0.1
        self.world = world
        self.tracked_object = None
        world.camera = self
        self.x = x
        self.zoom = 1
        self.y = y
        self.dir = dir
        self.vert_dir = vert_dir
        self.target_x = x

        self.target_y = y
        self.target_dir = dir
        self.target_vert_dir = vert_dir
        self.surf_cos = math.cos(dir/180*math.pi)
        self.surf_sin = math.sin(dir/180*math.pi)
        self.vert_cos = math.cos(vert_dir / 180 * math.pi)
        self.vert_sin = math.sin(vert_dir/180*math.pi)
        self.update()
    def update(self):
        if not self.tracked_object is None:
            self.target_x = self.tracked_object.x
            self.target_y = self.tracked_object.y
        self.x += (self.target_x-self.x) * self.speed_cof
        self.y += (self.target_y - self.y) * self.speed_cof
        self.dir += (self.target_dir-self.dir) * self.speed_cof
        self.vert_dir += (self.target_vert_dir-self.vert_dir)* self.speed_cof
        if (self.dir != self.target_dir) or (self.vert_dir != self.target_vert_dir):
            self.surf_cos = math.cos(self.dir / 180 * math.pi)
            self.surf_sin = math.sin(self.dir / 180 * math.pi)
            self.vert_cos = math.cos(self.vert_dir / 180 * math.pi)
            self.vert_sin = math.sin(self.vert_dir / 180 * math.pi)
        if round (self.dir ) == round(self.target_dir):
            self.dir = self.target_dir


class Point:
    def __init__(self,world,x,y,z,visible = False):
        self.world = world
        self.x = x
        self.y = y
        self.z = z
        self.visible = visible
    def calc_scr_pos(self,offset_x =0, offset_y = 0):
        dx = (self.world.camera.x - self.x)
        dy = (self.world.camera.y - self.y)
        sin = math.sin(self.world.camera.dir/180*math.pi)
        cos = math.cos(self.world.camera.dir/180*math.pi)
        # +(poly[_][1]*cos*320)+(poly[_][0]*320*sin)  | +(poly[_][1]*sin*320)-(poly[_][0]*cos*320)
        return (self.world.game.w/2+ (dy*cos+sin*dx)*self.world.camera.zoom+offset_x,self.world.game.h/2+(- dy*sin*self.world.camera.vert_cos+cos*dx*self.world.camera.vert_cos-self.z*self.world.camera.vert_sin)*self.world.camera.zoom+offset_y)
    def draw(self):
        if self.visible:
            pg.draw.circle(self.world.game.screen, (255,0,0), self.calc_scr_pos(), 3)

    def update(self): pass
    def calc_position_in_draw_queue(self):
        dx = (self.world.camera.x - self.x)
        dy = (self.world.camera.y - self.y)
        sin = math.sin(self.world.camera.dir/180*math.pi)
        cos = math.cos(self.world.camera.dir/180*math.pi)
        return (- dy*sin+cos*dx+self.z)

class aLine:
    def __init__(self,world,p1,p2):
        self.p1 = p1
        self.p2 = p2
        self.world = world

    def update(self): pass
    def draw(self):
        pg.draw.aaline(self.world.game.screen, (255,0,255),self.p1.calc_scr_pos(),self.p2.calc_scr_pos())
    def calc_position_in_draw_queue(self):
        p = Point(self.world,(self.p1.x+self.p2.x)/2,(self.p1.y+self.p2.y)/2,(self.p1.z+self.p2.z)/2)

        return p.calc_position_in_draw_queue()

class Line:
    def __init__(self,world,p1,p2,color = (255,0,0),width = 3):
        self.p1 = p1
        self.p2 = p2
        self.world = world
        self.w = width
        self.cl = color
    def draw(self):
        # deg = lookat(self.p2.calc_scr_pos()[0]-self.p1.calc_scr_pos()[0],self.p2.calc_scr_pos()[1]-self.p1.calc_scr_pos()[1])
        # cossin = abs(math.cos(deg/180*math.pi))+abs(math.sin(deg/180*math.pi))
        pg.draw.line(self.world.game.screen, self.cl ,self.p1.calc_scr_pos(),self.p2.calc_scr_pos(),math.ceil(self.w*self.world.camera.zoom)) # w * cossin
        pg.draw.circle(self.world.game.screen, self.cl,self.p1.calc_scr_pos(1,1),math.ceil(self.w/2*self.world.camera.zoom))
        pg.draw.circle(self.world.game.screen, self.cl, self.p2.calc_scr_pos(1,1), math.ceil(self.w / 2*self.world.camera.zoom))
        self.p1.draw()
        self.p2.draw()
    def update(self):pass
    def calc_position_in_draw_queue(self):
        p = Point(self.world,(self.p1.x+self.p2.x)/2,(self.p1.y+self.p2.y)/2,(self.p1.z+self.p2.z)/2)

        return p.calc_position_in_draw_queue()
class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def module(self):
        return math.sqrt(self.x**2+self.y**2)
    def dir(self):
        return lookat(self.x,self.y)
    def __add__(self, other):

        return Vector2D(self.x+other.x,self.y+other.y)
    def __sub__(self, other):
        return Vector2D(self.x-other.x,self.y-other.y)
    def __truediv__(self, other):
        return Vector2D(self.x/other,self.y/other)
    def __mul__(self, other):
        return Vector2D(self.x*other,self.y*other)
    def __str__(self): return f'({self.x};{self.y})'
class DinamicObject2D:
    def __init__(self,parent,m = 1,friction_cof = 5):
        self.m = m
        self.ismoving = False
        self.parent = parent
        self.friction_cof = friction_cof
        self.a = Vector2D(0,0)
        self.v = Vector2D(0,0)
        self.Fres = Vector2D(0,0)
    def update (self):
        # print(self.a,self.v)

        self.a = self.Fres/self.m
        self.v = self.v + self.a*(1/self.parent.world.game.FPS)
        self.parent.x += self.v.x
        self.parent.y += self.v.y
        if self.v.x > 0.1 or self.v.y > 0.1:
            self.ismoving = True
        else : self.ismoving  =False
        self.Fres = Vector2D(0,0)
        self.Fres = self.Fres-self.v*self.friction_cof

class Circle:
    def __init__(self,world,x,y,z,color = (255,0,0),r = 1):
        self.world = world
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.cl = color
    def calc_scr_pos(self,offset_x =0, offset_y = 0):
        dx = (self.world.camera.x - self.x)
        dy = (self.world.camera.y - self.y)
        sin = math.sin(self.world.camera.dir/180*math.pi)
        cos = math.cos(self.world.camera.dir/180*math.pi)
        # +(poly[_][1]*cos*320)+(poly[_][0]*320*sin)  | +(poly[_][1]*sin*320)-(poly[_][0]*cos*320)
        return (self.world.game.w/2+ (dy*cos+sin*dx)*self.world.camera.zoom+offset_x,self.world.game.h/2+(- dy*sin*self.world.camera.vert_cos+cos*dx*self.world.camera.vert_cos-self.z*self.world.camera.vert_sin)*self.world.camera.zoom+offset_y)
    def draw(self):
            pg.draw.circle(self.world.game.screen, self.cl, self.calc_scr_pos(), self.r)

    def update(self): pass
    def calc_position_in_draw_queue(self):
        dx = (self.world.camera.x - self.x)
        dy = (self.world.camera.y - self.y)
        sin = math.sin(self.world.camera.dir/180*math.pi)
        cos = math.cos(self.world.camera.dir/180*math.pi)
        return (- dy*sin+cos*dx+self.z)

from engine.base import Vector2D


class DinamicObject2D:
    def __init__(self, parent, m=1, friction_cof=5):
        self.m = m
        self.ismoving = False
        self.parent = parent
        self.friction_cof = friction_cof
        self.a = Vector2D(0, 0)
        self.v = Vector2D(0, 0)
        self.Fres = Vector2D(0, 0)

    def update(self):
        # print(self.a,self.v)

        self.a = self.Fres / self.m
        self.v = self.v + self.a * (1 / self.parent.world.game.FPS)
        self.parent.x += self.v.x
        self.parent.y += self.v.y
        if self.v.x > 0.1 or self.v.y > 0.1:
            self.ismoving = True
        else:
            self.ismoving = False
        self.Fres = Vector2D(0, 0)
        self.Fres = self.Fres - self.v * self.friction_cof


G = 30


class GravityObject:
    def __init__(self, parent, m=1):
        self.m = m
        self.ismoving = False
        self.parent = parent
        self.a = 0
        self.v = 0
        self.Fres = 0

    def update(self):
        # print(self.a,self.v)

        self.a = self.Fres / self.m - G
        self.v = self.v + self.a * (1 / self.parent.world.game.FPS)
        self.parent.z += self.v
        if self.parent.z < 0:
            self.parent.z = 0
            self.v = 0
        if self.v > 0.1:
            self.ismoving = True
        else:
            self.ismoving = False
        self.Fres = 0

import pygame


class Game:
    def empty(self, e=None,*args):
        pass

    def __init__(self, setup, loop):
        self.FPS = 60
        pygame.init()
        self.w = 1500
        self.h = 1000
        self.on_motion = self.empty
        self.bg_color = (0, 0, 0)
        self.screen = pygame.display.set_mode((self.w, self.h))
        self.clock = pygame.time.Clock()
        self.__vars = {}
        self.cameras = {}
        self.stages = {}
        self.mouse_hold = {1: False, 2: False, 3: False, 4: False, 5: False, }
        self.i_active_stage = None
        self.i_active_camera = None
        self.objects = {}
        setup(self)
        pygame.display.update()

        while True:
            self.clock.tick(self.FPS)
            loop(self)
            self.cameras[self.i_active_camera].update()
            self.stages[self.i_active_stage].update()
            self.update()
            self.draw()
            self.mouse_hold[4] = False
            self.mouse_hold[5] = False
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()
                if i.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_hold[i.button] = True
                if i.type == pygame.MOUSEBUTTONUP:
                    self.mouse_hold[i.button] = False
                if i.type == pygame.MOUSEMOTION:
                    self.on_motion(i, self)

            pygame.display.update()

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
            draw_queue.append((obj, self.objects[obj].calc_position_in_draw_queue()))

        def takeSecond(elem):
            return elem[1]

        draw_queue.sort(key=takeSecond)
        for couple in draw_queue:
            obj = couple[0]
            self.objects[obj].draw()

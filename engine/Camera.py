import math


class Camera:
    def __init__(self, world, x, y, z, dir, vert_dir=45):
        self.speed_cof = 0.1
        self.world = world
        self.tracked_object = None
        world.camera = self
        self.x = x
        self.zoom = 1
        self.target_zoom = 1
        self.y = y
        self.z = z
        self.dir = dir
        self.vert_dir = vert_dir
        self.target_x = x
        self.target_z = z
        self.target_y = y
        self.target_dir = dir
        self.target_vert_dir = vert_dir
        self.surf_cos = math.cos(dir / 180 * math.pi)
        self.surf_sin = math.sin(dir / 180 * math.pi)
        self.vert_cos = math.cos(vert_dir / 180 * math.pi)
        self.vert_sin = math.sin(vert_dir / 180 * math.pi)
        self.update()

    def update(self):
        if not self.tracked_object is None:
            self.target_x = self.tracked_object.x
            self.target_y = self.tracked_object.y
            self.target_z = self.tracked_object.z
        self.zoom += (self.target_zoom - self.zoom) * self.speed_cof
        self.x += (self.target_x - self.x) * self.speed_cof
        self.y += (self.target_y - self.y) * self.speed_cof
        self.z += (self.target_z - self.z) * self.speed_cof
        self.dir += (self.target_dir - self.dir) * self.speed_cof
        self.vert_dir += (self.target_vert_dir - self.vert_dir) * self.speed_cof
        if (self.dir != self.target_dir) or (self.vert_dir != self.target_vert_dir):
            self.surf_cos = math.cos(self.dir / 180 * math.pi)
            self.surf_sin = math.sin(self.dir / 180 * math.pi)
            self.vert_cos = math.cos(self.vert_dir / 180 * math.pi)
            self.vert_sin = math.sin(self.vert_dir / 180 * math.pi)
        if round(self.dir) == round(self.target_dir):
            self.dir = self.target_dir

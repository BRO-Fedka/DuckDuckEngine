import keyboard


from duck import *
from engine import *
import keyboard as kb
MOVE_POWER = 50
JUMP_POWER = 5000
def on_motion(e,game):
    if game.mouse_hold[2]:
        game.cameras["Player"].target_dir += e.rel[0]/2
        game.cameras["Player"].target_vert_dir -= e.rel[1] / 2
        if game.cameras["Player"].target_vert_dir < 0: game.cameras["Player"].target_vert_dir = 0
        if game.cameras["Player"].target_vert_dir > 75: game.cameras["Player"].target_vert_dir = 75

    # if e.buttons == 4:
    #     game.cameras["Player"].target_zoom /= 1.1
    # elif e. buttons == 5:
    #     game.cameras["Player"].target_zoom *= 1.1
def jump(e,game):
    if game.objects["Duck"].z == 0:
        game.objects["Duck"].gravity_object.Fres = JUMP_POWER
    # print("KOKF")
def setup(game):
    keyboard.on_press_key('space',lambda e: jump(e,game))
    game.on_motion = on_motion
    game.bg_color = (128,255,128)
    game.stages["World"] = World(game)
    game.cameras["Player"] = Camera(game.stages["World"],0,0,0,0)
    game.objects["Duck"] = Duck(game.stages["World"], 0, 0, 0, "Duck")
    game.cameras["Player"].tracked_object = game.objects["Duck"]
    game.i_active_camera = "Player"
    game.i_active_stage = "World"
    game.objects["Point0"] = Point(game.stages["World"],100,100,0)
    game.objects["Point1"] = Point(game.stages["World"],-100, -100, 0)
    game.objects["Point2"] = Point(game.stages["World"],100,-100,0)
    game.objects["Point3"] = Point(game.stages["World"],-100, 100, 0)
    game.objects["Point0_"] = Point(game.stages["World"],100,100,100)
    game.objects["Point1_"] = Point(game.stages["World"],-100, -100,100)
    game.objects["Point2_"] = Point(game.stages["World"],100,-100,100)
    game.objects["Point3_"] = Point(game.stages["World"],-100, 100,100)
    game.objects["Poly0"] = SquarePolygon(game.stages["World"],game.objects["Point0"],game.objects["Point2"],game.objects["Point1_"],game.objects["Point3_"], (0,0,255))
    game.objects["Poly1"] = SquarePolygon(game.stages["World"], game.objects["Point0"], game.objects["Point2"],
                                         game.objects["Point2_"], game.objects["Point0_"], (0, 0, 255))
    game.objects["Line02"] = Line(game.stages["World"], game.objects["Point0"], game.objects["Point2"],(200,200,200),20)
    game.objects["Line13"] = aLine(game.stages["World"], game.objects["Point1"], game.objects["Point3"])
    game.objects["Line30"] = aLine(game.stages["World"], game.objects["Point3"], game.objects["Point0"])
    game.objects["Line21"] = aLine(game.stages["World"], game.objects["Point2"], game.objects["Point1"])
    game.objects["Line02_"] = aLine(game.stages["World"], game.objects["Point0_"], game.objects["Point2_"])
    game.objects["Line13_"] = aLine(game.stages["World"], game.objects["Point1_"], game.objects["Point3_"])
    game.objects["Line30_"] = aLine(game.stages["World"], game.objects["Point3_"], game.objects["Point0_"])
    game.objects["Line21_"] = aLine(game.stages["World"], game.objects["Point2_"], game.objects["Point1_"])

    game.objects["Line0"] = aLine(game.stages["World"], game.objects["Point0"], game.objects["Point0_"])
    game.objects["Line1"] = aLine(game.stages["World"], game.objects["Point1"], game.objects["Point1_"])
    game.objects["Line2"] = Line(game.stages["World"], game.objects["Point2"], game.objects["Point2_"],(200,200,200),20)
    game.objects["Line3"] = aLine(game.stages["World"], game.objects["Point3"], game.objects["Point3_"])
def loop(game):
    kp_y= 0
    kp_x = 0
    k_vector = Vector2D(0,0)
    # if keyboard.is_pressed("space"):

    mx,my = pg.mouse.get_pos()
    dx,dy = mx-game.w/2,my-game.h/2
    if math.sqrt(dx**2+dy**2) > 100:
        game.objects["Duck"].dinamic_object.Fres = game.objects["Duck"].dinamic_object.Fres + Vector2D(math.sin((-game.objects["Duck"].dir+90)/180*math.pi),math.cos((-game.objects["Duck"].dir+90)/180*math.pi))*MOVE_POWER
    game.objects["Duck"].dir = -game.cameras["Player"].dir + lookat(dx,dy/game.cameras["Player"].vert_cos)+90
    # if kp_y == 1 and kp_x == 1:

        # print("DF")
        # print(k_vector)
        # k_vector = k_vector / (2**0.5)


    # if keyboard.is_pressed("left"):
    #     game.cameras["Player"].target_dir+= 1
    # if keyboard.is_pressed("right"):
    #     game.cameras["Player"].target_dir -= 1
    # if keyboard.is_pressed("down"):
    #     game.cameras["Player"].target_vert_dir+= 1
    # if keyboard.is_pressed("up"):
    #     game.cameras["Player"].target_vert_dir -= 1
    if game.mouse_hold[4]:
        game.cameras["Player"].target_zoom*= 1.1
    if game.mouse_hold[5]:
        game.cameras["Player"].target_zoom /= 1.1



if __name__ == '__main__':
    game = Game(setup,loop)


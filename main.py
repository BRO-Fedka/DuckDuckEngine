import keyboard


from duck import *
from engine import *
import keyboard as kb
MOVE_POWER = 10
def setup(game):
    game.bg_color = (128,255,128)
    game.stages["World"] = World(game)
    game.cameras["Player"] = Camera(game.stages["World"],0,0,0)
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
    if keyboard.is_pressed("w"):
        kp_y += 1
        k_vector = k_vector - Vector2D(-game.cameras["Player"].surf_cos,game.cameras["Player"].surf_sin)*MOVE_POWER
    if keyboard.is_pressed("s"):
        kp_y += 1
        k_vector = k_vector + Vector2D(-game.cameras["Player"].surf_cos,game.cameras["Player"].surf_sin)*MOVE_POWER
    if keyboard.is_pressed("a"):
        kp_x += 1
        k_vector = k_vector + Vector2D(game.cameras["Player"].surf_sin,game.cameras["Player"].surf_cos)*MOVE_POWER
    if keyboard.is_pressed("d"):
        kp_x += 1
        k_vector = k_vector - Vector2D(game.cameras["Player"].surf_sin,game.cameras["Player"].surf_cos)*MOVE_POWER
    mx,my = pg.mouse.get_pos()

    game.objects["Duck"].dir = -game.cameras["Player"].dir + lookat((mx-game.w/2),(my-game.h/2)/game.cameras["Player"].vert_cos)+90
    if kp_y == 1 and kp_x == 1:

        # print("DF")
        # print(k_vector)
        k_vector = k_vector / (2**0.5)

    game.objects["Duck"].dinamic_object.Fres = game.objects["Duck"].dinamic_object.Fres + k_vector
    if keyboard.is_pressed("left"):
        game.cameras["Player"].target_dir+= 1
    if keyboard.is_pressed("right"):
        game.cameras["Player"].target_dir -= 1
    if keyboard.is_pressed("down"):
        game.cameras["Player"].target_vert_dir+= 1
    if keyboard.is_pressed("up"):
        game.cameras["Player"].target_vert_dir -= 1
    if keyboard.is_pressed("+"):
        game.cameras["Player"].zoom*= 1.1
    if keyboard.is_pressed("-"):
        game.cameras["Player"].zoom /= 1.1



if __name__ == '__main__':
    game = Game(setup,loop)

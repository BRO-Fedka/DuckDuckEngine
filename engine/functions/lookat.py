import math


def lookat(x, y):
    if x == 0:
        x = 0.0001
    angle = -math.atan((y / x)) / (math.pi / 180)
    # if y != abs(y):
    #  angle =  angle + 360
    if x != abs(x):
        angle = angle + 180
    return angle + 180

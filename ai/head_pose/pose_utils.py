import math


def calculate_angle(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y

    return math.degrees(math.atan2(dy, dx))
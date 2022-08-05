import math


def distance_2points(x1, y1, x2, y2):
    dist = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
    x = math.sqrt(dist)
    y = dist
    return x, y


ans = distance_2points(-4, 1, 2, -1)
print(ans)

ans1 = distance_2points(0, 0, 3, 3)
print(ans1)

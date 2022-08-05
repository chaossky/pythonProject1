import math

diameter=2
polygon=6
side=1

n=10
for i in range(n):
    polygon = polygon * 2
    side = ( 2 - ( 4 - side**2 ) **.5 ) **.5
    pi = side * polygon / diameter
    print(polygon, ":", pi, math.pi-pi)
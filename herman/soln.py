import math 
r = int(input())
print(math.pi * r**2)
def distance(x1, y1, x2, y2):
    return (abs(x1-x2) + abs(y1-y2))
print(distance(0, 0, r, 0))
print(math.pi * distance(0, 0, r, 0)**2)

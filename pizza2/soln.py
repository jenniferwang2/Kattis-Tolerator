import math 
radius, crust = map(int, input().split())
def area(rad):
    return math.pi*rad**2

print(f"{area(radius - crust)/area(radius) * 100}")
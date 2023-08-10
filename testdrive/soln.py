a, b, c = map(int, input().split())
#figure out if its going up or down initially
up = True 
if b > a:
    up = True
else:
    up = False
turned = False
if up: #checking for turning requires two cases: 
    if b > c: 
        print("turned")
        turned = True 
elif not up: 
    if c > b: 
        print("turned")
        turned = True
if not turned: #acceleration takes absolute distance between the points
    if abs(a-b) == abs(c-b):
        print("cruised")
    elif abs(b-a) > abs(c-b):
        print("braked")
    else:
        print("accelerated")
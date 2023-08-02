m, a, b, c = map(int, input().split())
if (a + b + c) / m > 2: #condition that checks if we need to get to round 3, which would mean that a item is choosen by everyone
    print("impossible")
else:
    print("possible")
n = int(input())
for i in range(n):
    sums, difference = map(int, input().split())
    b = (sums - difference)/2 
    a = sums - b
    if a < 0 or b <0:
        print("impossible")
    else:
        print(int(a), int(b))
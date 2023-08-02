a, b, c, n = map(int, input().split())
if 0 in [a, b, c]:
    print("NO")
elif n < 3: #needs less than 3 questions contradiciting needed 1 of each type
    print("NO")
#have at least 1 problem for each
elif a + b + c >= n: #total is at least or more than requirement
    print("YES")
#case where there are at least 1 of each, but there arent' enough for the requirement
else:
    print("NO")
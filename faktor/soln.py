A, I = map(int, input().split())
n = A * I #min briberies
while n/A > I - 1:
        n = n - 1
print(n + 1)


x = int(input()) #amount you can use each month
n = int(input()) #number of months 
leftover = 0
for i in range(n):
    m = int(input()) #used
    leftover += x - m
print(leftover + x)
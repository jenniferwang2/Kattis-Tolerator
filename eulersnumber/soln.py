import math

n = int(input())
euler = 1/math.factorial(0)
factorial_cache = math.factorial(0) #default cache
for i in range(1, n + 1 ):
    factorial_cache = factorial_cache*i #update cache to new factorial
    term = 1/factorial_cache
    euler += term
print(euler)

with open("output.txt", "w") as file:
    file.write(str(euler) + "\n")
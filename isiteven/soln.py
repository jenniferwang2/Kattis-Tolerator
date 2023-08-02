# n, power = map(int, input().split())
# factors = []
# for i in range(n):
#     factors.append(int(input()))

# total_factors_of_two = sum(factor % 2 == 0 for factor in factors)
# if total_factors_of_two >= power and power > 0:
#     print("1")
# else:
#     print("0")

# n, power = map(int, input().split())
# product = 1
# for i in range(n):
#     factor = int(input())
#     product *= factor

# last_n_digits = product % (10 ** power)
# is_divisible = last_n_digits % (2 ** power) == 0

# if is_divisible:
#     print("1")
# else:
#     print("0")

n, power = map(int, input().split())
factors = []
count = 0

for i in range(n):
    factor = int(input())
    while factor % 2 == 0:
        factor //= 2
        count += 1

if count >= power:
    print("1")
else:
    print("0")


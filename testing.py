# # n = int(input())
# # for i in range(n):
# #     sums, difference = map(int, input().split())
# #     b = (sums - difference)/2 
# #     a = sums - b
# #     if a < 0 or b <0:
# #         print("impossible")
# #     else:
# #         print(a, b)

# string = input()
# if string == "OCT 31" or string == "DEC 25":
#     print("yup")
# else:
#     print("nope")

# str = [*input()]
# curr = str[0]
# output = str[0]
# for char in str[1:]:
#     if char != curr: #keep new unique character
#         output += char
#     curr = char
# print(output)

# import math

# n = int(input())  # Input the number to check for primality

# # Initialize array to store results
# array = [True] * (10 ** 8)

# for i in range(2, int(math.sqrt(10 ** 18))):
#     if array[i]:
#         for j in range(i * i, 10 ** 18 + 1, i):
#             array[j] = False

# # Check if n-th index is True
# if array[n]:
#     print("YES")
# else:
#     print("NO")

import math
n = int(input())
output = ""
get_l = [""] * 45
for _ in range(n):
    word = input()
    for index, letter in enumerate(word):
        get_l[index] += letter
for i in range(45):
    position = get_l[i]
    if position != "":
        avg = 0
        for letter in position:
            number = ord(letter)
            avg += number
        avg = math.floor(avg/len(position))
        new = chr(avg)
        output += new
print(output)
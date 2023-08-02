# a = input()
# b = input()
# c = input()
# d = input() 
# e = input()
# n = 0
# for i in [a, b, c, d, e]:
#     if "FBI" in i:
#         print([a, b, c, d, e].index(i) + 1, end=" ") 
#         n += 1
# if n == 0:
#     print("HE GOT AWAY!")

inputs = []
for i in range(5):
    inputs.append(input())
indicies = []
for i, input in enumerate(inputs, start = 1): #gos through the list and it's associated indexes, starting with 1, avoid issue of index finding first instance multiple times
    if "FBI" in input:
        indicies.append(i)
if indicies:
    print(*indicies, end=" ")
else: 
    print("HE GOT AWAY!")
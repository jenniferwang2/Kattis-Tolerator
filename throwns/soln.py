# n, k = map(int, input().split())
# stack = []
# lst = input().split()

# backtracked = True
# for item in lst: 

#     if item == "undo": #if need undo, do next time by backtrack = False
#         backtracked = False

#     elif backtracked == False: 
#         for i in range(int(item)):
#             stack.pop()
#         backtracked = True

#     else: #no backtrack, is integer
#         item = int(item)
#         # if item % n == 0: #turn no move
#         #     stack.append(0)
#         # elif item > 5: 
#         #     stack.append(item % n)
#         if item >= 5: 
#             stack.append(item % n)
#         elif item < 5: 
#                 stack.append(5 - abs((-1) * item % n))
# print(sum(stack) % n)
# Read the number of bags
n = int(input())

# Initialize a list to store the candy counts for each type
candy_counts = [0] * 11  # Assuming candy types are in the range -10 to 10

# Read each bag's data and update candy counts
for _ in range(n):
    bag_data = list(map(int, input().split()))
    k = bag_data[0]  # Number of candy types
    for i in range(1, k * 2 + 1, 2):
        candy_type = abs(bag_data[i])
        candy_count = bag_data[i + 1]
        candy_counts[candy_type] += candy_count

# Calculate the total positive candy count
total_positive_candy = 0
for i in range(1, 11):
    if candy_counts[i] > 0:
        total_positive_candy += candy_counts[i]

# Print the result
print(total_positive_candy)

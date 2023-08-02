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


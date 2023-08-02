stack = []
for i in [*input()]:
    if i != "<":
        stack.append(i)
    else:
        stack.pop() 
print("".join(stack))
OPEN = ["(", "[", "{"]
CLOSE = [")", "]", "}"]

length = int(input())
str = input() 

#tracking invalid deliminators to return first invalid bracket
first = ""
first_idx = 0
invalid_count = 0
found = False

stack = []
for pos, char in enumerate(str):
    
    if char in OPEN: 
        stack.append(char)

    elif char in CLOSE: 
        if not stack: # automatically not valid if stack empty
            if not found:
                first = char
                found = True
                first_idx = pos
            invalid_count += 1
        else:
            if OPEN.index(stack[-1]) == CLOSE.index(char): 
                stack.pop()
            else: # no matching open bracket
                if not found:
                    first = char
                    found = True
                    first_idx = pos
                invalid_count += 1

if invalid_count == 0:
    print("ok so far")
else:
    print(first, first_idx)


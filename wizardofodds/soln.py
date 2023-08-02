import math
n, b = map(int, input().split())
def log_base_2(x):
    result = math.log2(x)
    return result
guesses = log_base_2(n)
if guesses > b: 
    print("Your wish is granted!")
else:
    print("Your wish is granted!")
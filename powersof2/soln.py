import math

def count_powers_of_two(x, y):
    # Create the string representation of 10^x
    num_str = '1' + '0' * x
    
    count = 0
    power = 1
    while True:
        # Calculate the next power of 2^y
        power_str = str(power)
        if len(power_str) > len(num_str):
            break
        count += num_str.count(power_str)
        
        # Calculate the next power of 2^y by multiplying the current power
        power *= 2**y

    return count
# usage
x, y = map(int, input().split())

print(count_powers_of_two(x, y))

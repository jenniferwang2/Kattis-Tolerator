from math import floor

def find_minimum_rock_size(desired_sizes):
    max_desired_size = max(desired_sizes)
    min_rock_size = max_desired_size

    while min_rock_size > 1:
        min_rock_size = floor(min_rock_size / 2)

    return min_rock_size

# Take user input for desired rock sizes
n = input()
desired_sizes = input().split()
desired_sizes = [int(size) for size in desired_sizes]

minimum_size = find_minimum_rock_size(desired_sizes)

print("The minimum rock size to use is", minimum_size)

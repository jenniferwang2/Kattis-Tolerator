# Read the number of bags
n = int(input())

# Initialize a dictionary to store the candy counts for each type
candy_counts = {}

# Read each bag's data and update candy counts
for _ in range(n):
    bag_data = list(map(int, input().split()))
    k = bag_data[0]  # Number of candy types
    for i in range(1, k * 2 + 1, 2):
        candy_type = abs(bag_data[i])
        candy_count = bag_data[i + 1]
        if candy_type in candy_counts:
            candy_counts[candy_type] += candy_count
        else:
            candy_counts[candy_type] = candy_count

# Calculate the maximum amount of candy after considering cancellations
max_total_candies = 0
for candy_type in candy_counts.keys():
    if -candy_type in candy_counts:
        max_total_candies += max(candy_counts[candy_type] + candy_counts[-candy_type], 0)
    else:
        max_total_candies += max(candy_counts[candy_type], 0)

# Print the result
print(max_total_candies)

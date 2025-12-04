import itertools

# Function to check if a number is even
is_even = lambda x: x % 2 == 0

# Dataset of customer IDs visiting the store on consecutive days
day1_visitors = [101, 102, 105, 107, 109, 110]
day2_visitors = [102, 104, 105, 108, 110, 111]
day3_visitors = [103, 105, 106, 107, 110, 112]

# Find visitors who came on at least two different days
all_combinations = list(itertools.product([1, 2, 3], repeat=2))
day_pairs = [(a, b) for a, b in all_combinations if a < b]

frequent_visitors = set()
for day1, day2 in day_pairs:
    if day1 == 1 and day2 == 2:
        common = set(day1_visitors) & set(day2_visitors)
    elif day1 == 1 and day2 == 3:
        common = set(day1_visitors) & set(day3_visitors)
    else:  # day1 == 2 and day2 == 3
        common = set(day2_visitors) & set(day3_visitors)
    frequent_visitors.update(common)

# Filter out even visitor IDs
filtered_items = [visitor for visitor in frequent_visitors if not is_even(visitor)]

# Count unique visitors after filtering
unique_count = len(set(filtered_items))

print(f"Result: {unique_count}")
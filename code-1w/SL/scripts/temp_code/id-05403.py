from collections import defaultdict, Counter

# Irrelevant frequency map for distraction
default_freq = defaultdict(int)
for char in 'abracadabra':
    default_freq[char] += 1

# Decoy statistical computation with no impact
decoy_array = [x ** 2 - x for x in range(10)]
decoy_mean = sum(decoy_array) / len(decoy_array)

# Real data pipeline starts
raw_data = [i for i in range(-15, 25) if i % 3 != 0]

# Apply transformation with red herring condition
transformed_data = []
for val in raw_data:
    temp_val = abs(val) * 2
    if temp_val > 30:  # Misleading threshold check (not used later)
        temp_val -= 10
    transformed_data.append(temp_val)

# Bit manipulation decoy chain
bitmask = 0b101010
masked_values = [v ^ bitmask for v in transformed_data[:5]]
unused_result = sum(bitmask << i for i in range(3))

# Logical filtering with multiple distractions
valid_flags = []
for v in transformed_data:
    flag = True
    if v % 7 == 0:
        flag = False
    if v < 10:
        flag = False
    # Another misleading short-circuit block
    if v % 4 == 0 and v > 100:
        flag = True  # Dead code
    valid_flags.append(flag)

# Actual filtering uses a subset of logic above but not exactly
# The real filter reuses only 'v >= 10' and 'v % 7 != 0'
filtered_data = [transformed_data[i] for i in range(len(transformed_data)) if valid_flags[i]]

# Decoy dictionary aggregation (distractor)
data_stats = {}
data_stats['max'] = max(transformed_data)
data_stats['min'] = min(transformed_data)
data_stats['range'] = data_stats['max'] - data_stats['min']

# Critical statement — answer derived here
filtered_sum = sum(filtered_data)

# More red herrings below this line
lambda_offset = lambda x: x + 5
offset_sum = lambda_offset(filtered_sum)

# Unused recursive function to increase nesting depth
def useless_recursive(n):
    if n <= 1:
        return 1
    return n + useless_recursive(n - 2)

_ = useless_recursive(10)

# Final output
print(f"Result: {filtered_sum}")
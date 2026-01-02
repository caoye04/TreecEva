def analyze_pattern(sequence):
    count_pairs = 0
    for i in range(len(sequence) - 1):
        if sequence[i] == sequence[i + 1]:
            count_pairs += 1
    return count_pairs

sequence_data = [3, 3, 5, 7, 7, 7, 2, 2, 8, 1]

# Irrelevant transformation (distractor)
transformed = [x ** 2 for x in sequence_data if x % 2 == 0]

# Semi-relevant preprocessing: normalize odd numbers
normalized_odds = [x / 2 for x in sequence_data if x % 2 == 1]

# Enumerate with index tracking (used later)
indexed_data = list(enumerate(sequence_data))
processed_values = []
for idx, val in indexed_data:
    if idx % 2 == 0:
        processed_values.append(val + idx)
    else:
        processed_values.append(val - 1)

# Compute frequency map (some distraction here)
frequency_map = {}
for num in sequence_data:
    frequency_map[num] = frequency_map.get(num, 0) + 1

unique_count = len(frequency_map)

# Set operations: find distinct transitions
shifts = set()
for i in range(len(sequence_data) - 1):
    shifts.add((sequence_data[i], sequence_data[i + 1]))

# Slice middle portion for analysis
mid_slice = sequence_data[2:8]

# Threshold logic with zip and slicing
baseline = [4, 6, 5, 7, 3, 5]
thresholds = [a - 1 for a in baseline]

paired_comparison = list(zip(mid_slice, thresholds))

valid_window = 0
for val, thresh in paired_comparison:
    if val >= thresh:
        valid_window += 1

# Helper function with recursion (simple)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Unused helper (dead code path - distractor)
def rolling_average(lst, window=3):
    averages = []
    for i in range(len(lst) - window + 1):
        avg = sum(lst[i:i+window]) / window
        averages.append(avg)
    return averages

# Core scoring logic
sum_primary = sum(processed_values)
penalty = analyze_pattern(sequence_data)
effective_length = len([x for x in processed_values if x > 3])

# Final computation uses enumerate result and threshold comparison
intermediate_metric = valid_window * unique_count

# Key line: final_score depends on multiple derived values
final_score = (sum_primary - penalty) + (intermediate_metric // 2)

# Print result as required
print(f"Result: {final_score}")
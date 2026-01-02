import itertools

def analyze_pattern(sequence):
    frequency_map = {x: sequence.count(x) for x in set(sequence)}
    max_freq = max(frequency_map.values())
    modes = [k for k, v in frequency_map.items() if v == max_freq]
    return modes[0] if len(modes) == 1 else min(modes)

# Simulated sensor readings with noise filtering
data_stream = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
threshold = 4

# Irrelevant transformation (distractor)
doubled_values = [x * 2 for x in data_stream if x > 2]
filtered_data = [x for x in data_stream if x >= threshold]

# State tracking variables (some unused later)
count_high = 0
running_total = 0
for val in filtered_data:
    if val > 5:
        count_high += 1
    running_total += val

# Multiple assignment and distractor state
snapshot = (len(filtered_data), sum(filtered_data), count_high)
size, total, peaks = snapshot

# Advanced processing with list comprehension and set operations
even_components = {x for x in data_stream if x % 2 == 0}
odd_shifted = [(x + 1) for x in data_stream if x % 2 == 1]
combined_pool = list(even_components) + odd_shifted

# Process through windowing (simulated analysis)
windows = [combined_pool[i:i+3] for i in range(0, len(combined_pool)-2, 3)]
processed_data = []
for window in windows:
    processed_data.append(analyze_pattern(window))

# Secondary irrelevant metric (dead computation path)
avg_window_sum = sum([sum(w) for w in windows]) / len(windows) if windows else 0

# Core logic chain leading to final result
def calculate_performance_metric(data):
    if not data:
        return 0
    
    # Use of itertools to generate permutations (partial use - increases complexity)
    perms = list(itertools.permutations(data[:2]))  # Only use first two elements
    perm_count = len(perms)
    
    base_value = sum(data) * perm_count
    adjustment = abs(data[0] - data[-1]) if len(data) > 1 else 0
    
    # Final computation involving multiple prior values
    score = base_value - adjustment
    return score

# Misleading intermediate calculation (not used)
temp_diagnostic = len(even_components) * peaks

# Key execution point
final_score = calculate_performance_metric(processed_data)

print(f"Result: {final_score}")
def analyze_pattern(sequence):
    count_pairs = 0
    for i in range(len(sequence) - 1):
        if sequence[i] < sequence[i + 1]:
            count_pairs += 1
    return count_pairs

sequence = [3, 7, 2, 8, 1, 9, 4, 6]

# Irrelevant transformation (distractor)
shifted = [x % 5 for x in sequence]
duplicate_check = set(shifted)

# Semi-relevant preprocessing
index_map = {val: idx for idx, val in enumerate(sequence)}
ranked = sorted(sequence, reverse=True)

# Weight assignment using slicing and zip
sliced_ranks = ranked[1:6]
weights = [i * 0.1 for i in range(1, len(sliced_ranks) + 1)]
paired_weights = list(zip(sliced_ranks, weights))

# Another distractor: unused helper function
def compute_magnitude(vec):
    return sum(x ** 2 for x in vec) ** 0.5

# Data transformation with enumerate and distraction
adjusted = []
for idx, val in enumerate(sequence):
    adjustment = (idx % 3) * 0.1
    adjusted.append(val + adjustment if val % 2 == 0 else val - adjustment)

# Create temp_data using slicing and filtering
filtered = [x for x in adjusted if x > 4.5]
temp_data = filtered[:4]

# Dummy state tracking (irrelevant)
counter_log = []
for step in range(3):
    counter_log.append(len(counter_log) + step * 2)

# Core computation
sum_temp = sum(temp_data)
avg_temp = sum_temp / len(temp_data) if temp_data else 0

# Final calculation depending on multiple paths
def calculate_final(data, w):
    base = 0
    for i, v in enumerate(data):
        base += v * w[i % len(w)]
    # Additional logic with conditional offset
    if len(data) >= 3:
        max_val = max(data)
        min_val = min(data)
        spread_penalty = (max_val - min_val) * 0.2
        base -= spread_penalty
    return int(base + 0.5)  # Round to nearest integer

final_score = calculate_final(temp_data, weights)
print(f"Result: {final_score}")
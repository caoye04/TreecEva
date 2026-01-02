def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    count = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i-1] < sequence[i] > sequence[i+1]:
            count += 1
    return count

raw_input = [3, 7, 4, 8, 2, 9, 1, 5, 6]

# Preprocessing phase with distractor transformations
temp_transform = [x * 2 for x in raw_input if x % 2 == 1]
offset_map = {i: val % 4 for i, val in enumerate(raw_input)}
shifted_vals = [raw_input[i] + offset_map[i] for i in range(len(raw_input))]

# Actual relevant processing path
filtered_data = [x for x in raw_input if x > 4]
sorted_data = sorted(filtered_data, reverse=True)
processed_data = sorted_data[:len(sorted_data)//2] if len(sorted_data) > 2 else sorted_data

# Secondary analysis with red herring computation
max_peak = analyze_pattern(shifted_vals)
useless_aggregate = sum([i * v for i, v in enumerate(shifted_vals) if i % 3 == 0]) / (len(shifted_vals) or 1)

# Core scoring logic
primary_weight = len(processed_data) * 1.5
secondary_weight = min(processed_data) if processed_data else 0
dynamic_factor = 2 if sum(processed_data) > 15 else 1.5

intermediate_score = primary_weight + secondary_weight
penalty = 0
if len(temp_transform) > 3:
    penalty += 2.5
if max_peak < 3:
    penalty += 1.0

final_score = int((intermediate_score * dynamic_factor) - penalty)

# Distractor block - dead code path
if False:
    backup_scores = {"alt": sum(shifted_vals), "fallback": len(temp_transform)}
    final_score = backup_scores["alt"] // 3

Result: final_score
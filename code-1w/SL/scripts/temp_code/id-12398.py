def calculate_adjusted_sum(data):
    base_sum = sum(x for x in data if x > 0)
    adjustment = len([x for x in data if x % 2 == 0])
    temp_result = base_sum + adjustment * 0.5
    
    # Distractor: irrelevant statistical calculation
    mean_val = sum(data) / len(data) if data else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in data) / len(data) if data else 0
    unused_flag = variance_proxy > 100
    
    # Real logic step: apply conditional penalty
    penalty = 0
    if any(x < 0 for x in data):
        penalty = 3
    
    return temp_result - penalty

# Simulate sensor readings with noise filtering
raw_readings = [12, -5, 8, 0, 15, -3, 4]
filtered_readings = [x if x >= 0 else 0 for x in raw_readings]

# Secondary processing path - partially irrelevant
status_flags = [1 if x > 10 else 0 for x in raw_readings]
activation_count = sum(status_flags)

# Main data processing chain
processed_data = []
for i, val in enumerate(raw_readings):
    if val != 0:
        processed_data.append(val + i)
    else:
        processed_data.append(0)

# Additional distraction: string-based tagging (unused)
tags = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
label_map = dict(zip(tags, raw_readings))
relevant_labels = [k for k, v in label_map.items() if v > 5]

# Lambda-based transformation (semi-relevant)
index_boost = list(map(lambda idx_val: idx_val[0] * 0.1, enumerate(processed_data)))

# Final computation step
final_score = calculate_adjusted_sum(processed_data)

# Output result as required
print(f"Target result: {final_score}")
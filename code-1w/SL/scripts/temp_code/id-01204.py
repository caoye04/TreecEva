def calculate_final_score(data, weight_map):
    total = 0
    base_offset = len(data) % 3
    temp_result = []
    
    # Irrelevant pre-processing (distractor)
    outlier_flags = [x > 50 for x in data]
    valid_count = sum(1 for flag in outlier_flags if not flag)
    scaling_factor = 1.0 if valid_count == 0 else 100 / (valid_count + 1)
    
    # Real processing begins
    weighted_values = []
    for i, val in enumerate(data):
        weight = weight_map.get(i, 0.5)
        adjusted = val * weight
        weighted_values.append(adjusted)
    
    # Use of lambda and zip (required feature)
    capped_values = list(map(lambda x: min(x, 25), weighted_values))
    indexed_pairs = list(zip(range(len(capped_values)), capped_values))
    
    # Secondary adjustment with modular arithmetic
    for idx, value in indexed_pairs:
        if idx % 2 == 0:
            total += value + (idx % 7)
        else:
            total -= value % 4
    
    # Dead code path (distractor)
    secondary_sum = 0
    for item in temp_result:  # Never populated
        secondary_sum += item * 2
    
    # Final computation
    final_adjustment = base_offset * scaling_factor
    return int(total - final_adjustment)

# Main execution
raw_inputs = [12, 18, 27, 33, 14, 8, 21]
weights = {0: 1.2, 1: 0.8, 2: 1.5, 3: 0.9, 6: 1.1}

# Preprocessing step with enumerate and set operations (required features)
processed_data = []
duplicate_tracker = set()
for index, value in enumerate(raw_inputs):
    shifted = value ^ 3  # Bitwise XOR as simple transformation
    if shifted in duplicate_tracker:
        continue
    duplicate_tracker.add(shifted)
    if index % 2 == 0:
        processed_data.append(shifted + index)
    else:
        processed_data.append(shifted - (index % 3))

# Extraneous function call with no effect (distractor)
def analyze_distribution(vals):
    mean_val = sum(vals) / len(vals)
    variance = sum((v - mean_val) ** 2 for v in vals) / len(vals)
    return variance

_ = analyze_distribution(raw_inputs)  # Unused result

# Key statement
final_score = calculate_final_score(processed_data, weights)
print(f"Result: {final_score}")
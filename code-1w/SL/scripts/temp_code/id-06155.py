from itertools import combinations

def analyze_sequence(seq):
    # Irrelevant transformation: convert to uppercase (has no effect on numbers)
    seq_str = ''.join(map(str, seq))
    padded_seq = [x + 1 for x in seq]  # Distractor: modified but unused

    # Actual relevant logic: find all pairs with sum > 10
    valid_pairs_count = 0
    for a, b in combinations(seq, 2):
        if (a + b) > 10:
            valid_pairs_count += 1

    return valid_pairs_count

def transform_readings(readings):
    # Normalize readings by z-score (distractor computation)
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    std_dev = variance ** 0.5
    z_scores = [(x - mean_val) / std_dev for x in readings]  # Unused normalization

    # Relevant: apply threshold filter
    filtered = [x for x in readings if x >= mean_val]
    return filtered

def calculate_optimal_yield(data):
    base_accum = 0
    temp_shift = 0

    # Complex control flow with nesting
    for i, val in enumerate(data):
        if i % 2 == 0:
            base_accum += val * (i + 1)
            # Case conversion red herring
            status_flag = "ACTIVE" if val > 0 else "INACTIVE"
            status_flag = status_flag.lower()  # Irrelevant string op
        else:
            # Nested condition with misleading bitwise op
            temp_shift |= (val & 3)
            base_accum -= (val // 2)

    # Additional semi-relevant manipulation
    adjustment_factor = len(data) // 3
    final_yield = base_accum - temp_shift + adjustment_factor

    return final_yield

# Main execution
sensor_inputs = [4, 7, 2, 9, 5, 8]
dummy_labels = ['A', 'B', 'C', 'D', 'E']

# Dead code path: never used
mapped_names = [name.upper() for name in dummy_labels]
mapped_names.reverse()

# Step 1: Analyze sequence (returns count of valid pairs)
pair_analysis = analyze_sequence(sensor_inputs)

# Step 2: Transform sensor readings
processed_data = transform_readings(sensor_inputs)

# Step 3: Calculate yield based on processed data
final_yield = calculate_optimal_yield(processed_data)

print(f"Result: {final_yield}")
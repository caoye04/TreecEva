def calculate_final_score(data):
    # Irrelevant transformation (distractor)
    temp_offsets = [x % 7 for x in range(len(data))]
    adjusted_values = []

    for i, val in enumerate(data):
        if i % 2 == 0:
            adjusted_values.append(val * 1.5 + 2)
        else:
            adjusted_values.append(val - 1)

    # Semi-relevant filtering (some values are used later)
    filtered = list(filter(lambda x: x > 5, adjusted_values))

    # Red herring computation with dead-end variable
    outlier_check = sum(1 for x in adjusted_values if x < 0)
    scaling_factor = 1.0
    if len(filtered) > 3:
        scaling_factor = 0.9

    # Core logic hidden among distractions
    base_total = sum(filtered)
    penalty = 0
    for idx, (orig, adj) in enumerate(zip(data, adjusted_values)):
        if adj > orig and idx in [i for i in range(0, len(data), 3)]:
            penalty += 1

    intermediate_score = base_total - penalty * 2.5

    # Secondary distraction: unused set operation
    unique_caps = set([chr(int(x)) for x in data if 65 <= x <= 90])
    case_shift_warning = len(unique_caps) > 0  # never used

    # Final score calculation - depends on filtered sum and penalty
    final_normalization = intermediate_score * scaling_factor
    return round(final_normalization, 4)

# Initial dataset (simulated sensor readings)
data_stream = [4, 8, 6, 12, 3, 9, 11]

# Simulate preprocessing: convert to integer codes based on case rules
case_mapping = {c: ord(c.lower()) for c in 'ABCDEF'}
offset_signal = [case_mapping.get(chr(x), x) for x in data_stream if x in range(65, 71)]

# Main processing pipeline
processed_data = []
for val in data_stream:
    processed_data.append(val + 2)

# Key statement
final_score = calculate_final_score(processed_data)

print(f"Target result: {final_score}")
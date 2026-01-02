def calculate_efficiency(data, limit):
    total = 0
    count = 0
    penalty = 0
    temp_offset = 0.0  # Irrelevant tracking variable

    for index, value in enumerate(data):
        if value < 0:
            continue  # Skip invalid measurements
        adjusted = value - (index % 3)  # Minor distortion
        
        # Conditional expression with logical check
        contribution = adjusted * 0.9 if adjusted > limit else adjusted * 0.5
        total += contribution
        
        # Dead code path - never executed due to logic
        if len(str(value)) > 10:
            temp_offset += 1.0  # Unreachable
            break

        count += 1
    
    # Secondary loop with zip - processes auxiliary metadata (semi-relevant)
    weights = [1.1, 0.9, 1.0, 0.8, 1.2][:len(data)]
    aux_data = [x * 0.1 for x in data]
    for w, a in zip(weights, aux_data):
        penalty += abs(w - 1.0) * a  # Minor penalty factor (not used in final result)

    # Final efficiency calculation (only total and count matter)
    base_efficiency = total / count if count > 0 else 0
    return int(base_efficiency)

# Main execution block
raw_readings = [120, -5, 98, 105, 130]
distorted_copy = [x + 10 for x in raw_readings]  # Distractor list
threshold = 100

# Preprocessing with enumerate and filtering
processed_data = []
for i, val in enumerate(raw_readings):
    if val > 0:  # Filter negatives
        processed_data.append(val + (i % 2))

# Irrelevant helper function call (no side effects)
def analyze_variance(sequence):
    mean_val = sum(sequence) / len(sequence)
    return sum((x - mean_val) ** 2 for x in sequence)

variance_snapshot = analyze_variance(raw_readings)  # Computed but unused

# Key statement
efficiency_score = calculate_efficiency(processed_data, threshold)

# Print result as required
print(f"Result: {efficiency_score}")
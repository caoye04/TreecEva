def calculate_final_score(raw_data, limits):
    # Initialize various tracking variables
    temp_values = []
    outlier_count = 0
    normalized = {}
    adjustment_factor = 0.85
    base_reference = 100

    # Irrelevant pre-processing: simulate data calibration
    calibration_sequence = [i ** 0.5 for i in range(1, 6)]
    dummy_offset = sum(calibration_sequence) / len(calibration_sequence)

    # Main processing loop with filtering and transformation
    for key, value in raw_data.items():
        if value < limits['min']:
            outlier_count += 1
            temp_values.append(limits['min'])
        elif value > limits['max']:
            outlier_count += 1
            temp_values.append(limits['max'])
        else:
            temp_values.append(value)

        # Compute normalized value (semi-relevant but not used directly)
        normalized[key] = (value - limits['min']) / (limits['max'] - limits['min'] + 1e-9)

    # Secondary pass: compute rolling adjustment (distractor)
    adjustments = []
    for i in range(len(temp_values)):
        if i > 0:
            change = temp_values[i] - temp_values[i-1]
            adjustments.append(change * adjustment_factor)

    # Critical computation: weighted contribution based on position
    weighted_sum = 0.0
    for idx, val in enumerate(temp_values):
        weight = 0.9 ** idx  # higher weight for earlier elements
        weighted_sum += weight * val

    # Simulate confidence score (irrelevant)
    confidence = len(temp_values) / (outlier_count + 1) if outlier_count > 0 else len(temp_values)

    # Final aggregation using fixed formula
    raw_total = sum(temp_values)
    penalty = 2 * outlier_count
    final_score = int((weighted_sum + raw_total) / 2 - penalty)

    return final_score

# Input data setup
data = {
    'sensor_A': 45,
    'sensor_B': 120,
    'sensor_C': 67,
    'sensor_D': 210,
    'sensor_E': 88,
    'sensor_F': 3,
    'sensor_G': 150
}

thresholds = {
    'min': 10,
    'max': 200
}

# Dead code path - never executed but looks important
if __name__ == "__main__":
    print("Debug mode inactive")

# Actual execution
temp_result = [x * 2 for x in data.values() if x > 50]  # distractor list comprehension
distorted_map = {k: v * v for k, v in data.items()}  # unused dictionary operation

final_score = calculate_final_score(data, thresholds)
print(f"Target result: {final_score}")
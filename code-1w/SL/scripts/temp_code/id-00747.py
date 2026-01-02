def calculate_final_score(data, weights):
    # Initialize tracking variables
    base_sum = 0
    adjustment_factor = 1.0
    temp_result = []
    outlier_count = 0  # distractor: not used in final logic

    # Process each data entry with index tracking
    for i, (key, value) in enumerate(data.items()):
        weighted_val = value * weights[i % len(weights)]
        squared_dev = (value - 5) ** 2  # distractor computation

        if i % 3 == 0:
            base_sum += weighted_val * 0.9
        elif i % 3 == 1:
            base_sum += weighted_val * 1.05
        else:
            base_sum += weighted_val * 1.1

        temp_result.append(squared_dev)  # stored but unused later

    # Additional red herring: complex conditional that doesn't affect output
    if len(temp_result) > 5 and sum(temp_result) > 100:
        adjustment_factor *= 0.95
    else:
        adjustment_factor *= 1.0

    # Real adjustment based on key count (only relevant part)
    if len(data) >= 6:
        adjustment_factor = 1.2
    else:
        adjustment_factor = 0.8

    # Secondary distraction: nested loop over zipped data
    cumulative_noise = 0
    for a, b in zip(temp_result, temp_result[1:]):
        cumulative_noise += abs(a - b) * 0.01  # minor irrelevant accumulation

    # Final score calculation
    raw_score = base_sum * adjustment_factor
    final_score = int(round(raw_score))

    # Distractor: dead code path
    if False:
        final_score -= 100

    return final_score

# Main execution
if __name__ == '__main__':
    data = {
        'sensor_A1': 4.2,
        'sensor_B2': 6.8,
        'sensor_C3': 5.1,
        'sensor_D4': 3.9,
        'sensor_E5': 7.0,
        'sensor_F6': 5.5
    }
    weights = [0.8, 1.1, 0.9, 1.2]

    intermediate_total = sum(data.values()) * 0.1  # irrelevant precomputation
    scaling_hint = 2.0 if intermediate_total > 3.0 else 1.5  # unused hint

    final_score = calculate_final_score(data, weights)
    print(f"Result: {final_score}")
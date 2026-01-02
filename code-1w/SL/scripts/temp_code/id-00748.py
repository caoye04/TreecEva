def calculate_final_score(raw_data, limits):
    # Preprocessing: filter valid entries based on multiple criteria
    valid_entries = [x for x in raw_data if x > limits['min'] and x < limits['max']]

    # Irrelevant transformation: unused string manipulation
    status_labels = ['valid' if x >= 50 else 'low' for x in raw_data]
    label_summary = ''.join(status_labels).upper().replace('LOW', 'L').count('L')

    # Distractor: complex but unused lambda with set operation
    transform = lambda s: {y % 10 for y in s if y > 30}
    dummy_set = transform(raw_data)

    # Semi-relevant computation: normalize values within range
    normalized = [(x - limits['min']) / (limits['max'] - limits['min']) for x in valid_entries]

    # Additional distraction: sorting and reversing that isn't used
    sorted_vals = sorted(normalized, reverse=True)
    reversed_copy = sorted_vals[::-1]

    # Core logic: apply weighted scoring using a subset of processed data
    weights = [0.8, 1.2, 1.0, 0.9]  # Weight per quartile
    weighted_sum = 0.0
    for i, val in enumerate(normalized[:4]):  # Only first four contribute
        weighted_sum += val * weights[i % len(weights)]

    # Final adjustment using length of original data (modulates score)
    adjustment_factor = len(raw_data) % 7
    final_score = int((weighted_sum * 100) + adjustment_factor)

    return final_score


# Input data and parameters
data_set = [23, 45, 56, 67, 78, 89, 12, 34, 50, 61]
thresholds = {'min': 20, 'max': 80}

# Execution point of interest
final_score = calculate_final_score(data_set, thresholds)
print(f"Result: {final_score}")
from collections import defaultdict

# Simulate sensor data processing with noise filtering and weighted aggregation
def preprocess_data(raw):
    processed = []
    noise_floor = 0.1
    for val in raw:
        if abs(val) > noise_floor:  # Filter near-zero noise
            processed.append(abs(val) ** 0.5)
    return processed

# Misleading helper: not actually used in final computation
def legacy_normalize(arr):
    total = sum(arr)
    return [x / total for x in arr] if total else arr

# Core calculation with distractor variables
def calculate_final_score(data, weights):
    temp_results = defaultdict(float)
    intermediate_log = []
    adjustment_factor = 1.75  # Unused red herring
    decay_rate = 0.9  # Distractor

    # Weighted accumulation using dictionary
    for i, (val, weight) in enumerate(zip(data, weights)):
        weighted_val = val * weight
        temp_results[f'entry_{i}'] = weighted_val
        intermediate_log.append(weighted_val ** 0.5)

    # Real computation path
    base_sum = sum(temp_results.values())
    penalty = 0
    for v in temp_results.values():
        if v > 5:
            penalty += 0.5  # Small penalty for high values

    # Secondary adjustment based on count
    count_bonus = len(data) * 0.2

    # Final formula
    score = base_sum - penalty + count_bonus

    # Dead code branch (never reached due to logic)
    if False and adjustment_factor > 2:
        score *= decay_rate

    return score

# Main execution
if __name__ == '__main__':
    raw_sensor_readings = [0.05, -4.2, 6.8, -0.03, 3.1, 7.4, 2.2]
    config_weights = [0.8, 1.2, 1.0, 0.5, 1.1, 0.9, 1.3]

    # Preprocess the data
    cleaned = preprocess_data(raw_sensor_readings)

    # Irrelevant list comprehension (distractor)
    squared_cleaned = [x**2 for x in cleaned if x > 1]

    # Key statement
    final_score = calculate_final_score(cleaned, config_weights)

    # Print result as required
    print(f"Target result: {final_score}")
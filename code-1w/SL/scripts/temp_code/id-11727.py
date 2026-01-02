import itertools

def main():
    # Simulated sensor readings with noise
    raw_readings = [12.5, 13.0, 11.8, 14.2, 13.7, 12.9, 13.1]
    noise_offset = [0.1, -0.2, 0.3, -0.1, 0.0, 0.2, -0.3]
    adjusted_readings = [raw_readings[i] + noise_offset[i] for i in range(len(raw_readings))]

    # Filter out any readings below threshold (not actually used later)
    filtered_readings = [r for r in adjusted_readings if r > 12.5]

    # Apply moving average smoothing (distractor computation)
    smoothed = []
    for i in range(1, len(adjusted_readings) - 1):
        smoothed.append((adjusted_readings[i-1] + adjusted_readings[i] + adjusted_readings[i+1]) / 3)

    # Normalize readings to baseline (semi-relevant)
    baseline = sum(adjusted_readings) / len(adjusted_readings)
    normalized = [x / baseline for x in adjusted_readings]

    # Simulate multi-sensor fusion using itertools (relevant)
    sensor_ids = ['S1', 'S2', 'S3']
    timestamps = [100, 101, 102]
    combinations = list(itertools.product(sensor_ids, timestamps))
    fusion_count = len(combinations)  # Used later

    # Process data: apply weighting and aggregation
    weights = [0.8, 1.0, 0.9, 1.1, 0.95, 0.85, 1.05]
    weighted_sum = sum(normalized[i] * weights[i] for i in range(len(normalized)))
    avg_weighted = weighted_sum / len(weights)

    # Secondary distraction: simulate calibration drift adjustment
    drift_compensation = 0.0
    for step in range(5):
        drift_compensation += 0.01 * (step + 1)
    calibrated_avg = avg_weighted - drift_compensation  # Not used

    # Prepare processed data structure
    processed_data = {
        'values': normalized,
        'count': fusion_count,
        'aggregate': avg_weighted,
        'meta': {'version': '2.1', 'calibrated': False}
    }

    final_score = calculate_final_score(processed_data)
    print(f"Result: {final_score}")


def calculate_final_score(data):
    base_score = data['aggregate'] * 100
    multiplier = data['count']  # from itertools product
    penalty = 0

    # Apply penalty based on value distribution
    for v in data['values']:
        if v < 0.9 or v > 1.1:
            penalty += 2

    # Red herring: unused conditional branch
    if data['meta']['calibrated']:
        base_score *= 1.1

    result = base_score - penalty * 5
    return int(result)

if __name__ == '__main__':
    main()
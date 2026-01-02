import itertools

# Simulate sensor readings with noise and calibration offsets
def main():
    raw_readings = [104, 95, 115, 87, 93, 120, 102]
    calibration_factor = 0.92
    noise_offsets = [0.5, -0.3, 0.7, -0.4, 0.2, -0.6, 0.1]

    # Apply calibration and noise correction
    corrected = [reading * calibration_factor for reading in raw_readings]
    adjusted_readings = [corrected[i] + noise_offsets[i] for i in range(len(corrected))]

    # Normalize readings to baseline (mean-centered)
    mean_value = sum(adjusted_readings) / len(adjusted_readings)
    normalized_readings = [x - mean_value for x in adjusted_readings]

    # Outlier suppression: cap values beyond 1.5 sigma
    variance = sum(x ** 2 for x in normalized_readings) / len(normalized_readings)
    std_dev = variance ** 0.5
    capped_readings = [max(-1.5 * std_dev, min(1.5 * std_dev, x)) for x in normalized_readings]

    # Scale to 0-1 range using min-max scaling
    min_val = min(capped_readings)
    max_val = max(capped_readings)
    scaled_values = [(x - min_val) / (max_val - min_val) if max_val != min_val else 0 for x in capped_readings]

    # Weight assignment using decay pattern
    weights = [0.8 ** i for i in range(len(scaled_values))]
    total_weight = sum(weights)
    weights = [w / total_weight for w in weights]  # Normalize weights

    # Dummy transformation - irrelevant to final result
    transformed_pairs = list(itertools.combinations(scaled_values, 2))
    pair_sums = [a + b for a, b in transformed_pairs]
    avg_pair_sum = sum(pair_sums) / len(pair_sums) if pair_sums else 0

    # Irrelevant secondary metric
    rolling_avg = 0
    for i in range(1, len(scaled_values)):
        rolling_avg += abs(scaled_values[i] - scaled_values[i-1])
    rolling_avg /= len(scaled_values) - 1 if len(scaled_values) > 1 else 1

    # Core aggregation function
    def compute_aggregate(values, weights):
        return sum(v * w for v, w in zip(values, weights))

    final_score = compute_aggregate(scaled_values, weights)
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()
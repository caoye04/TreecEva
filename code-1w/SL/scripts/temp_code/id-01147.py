from collections import defaultdict
from functools import reduce

# Simulated sensor readings with noise filtering
def preprocess_readings(raw_data):
    filtered = defaultdict(float)
    noise_floor = 0.1
    for sensor, values in raw_data.items():
        cleaned = [v for v in values if abs(v) > noise_floor]
        if cleaned:
            filtered[sensor] = sum(cleaned) / len(cleaned)
    return filtered

# Transform data into z-scores for comparison
def standardize(readings):
    mean_val = sum(readings.values()) / len(readings)
    variance = sum((v - mean_val) ** 2 for v in readings.values()) / len(readings)
    std_dev = variance ** 0.5 or 1
    return {k: (v - mean_val) / std_dev for k, v in readings.items()}

# Apply dynamic weighting based on sensor reliability
def apply_weights(metrics, weights_dict):
    weighted = {}
    total_weight = 0
    for metric, value in metrics.items():
        weight = weights_dict.get(metric, 1.0)
        weighted[metric] = value * weight
        total_weight += weight
    # Normalize by total weight
    return {k: v / total_weight for k, v in weighted.items()} if total_weight else metrics

# Aggregate final score using harmonic mean to penalize outliers
def calculate_final_score(data, weights):
    intermediate = apply_weights(data, weights)
    temp_vals = [abs(v) for v in intermediate.values() if v != 0]
    
    # Irrelevant distractor: sorting and reversing (no effect)
    sorted_vals = sorted(temp_vals)
    reversed_vals = sorted_vals[::-1]
    dummy_sum = sum(x ** 0.5 for x in reversed_vals if x > 0.5)
    
    # Harmonic mean calculation (actual logic)
    if not temp_vals:
        return 0.0
    harmonic_inv = sum(1 / v for v in temp_vals)
    harmonic_mean = len(temp_vals) / harmonic_inv
    
    # Additional distraction: unused exponential scaling
    exp_scaling = lambda x, e: x ** e
    scaled_harmonic = exp_scaling(harmonic_mean, 1)  # No change
    
    # Final adjustment based on count
    adjustment_factor = 1 + 0.1 * (len(temp_vals) - 1)
    return round(harmonic_mean * adjustment_factor, 4)

# Main execution flow
if __name__ == "__main__":
    raw_sensor_data = {
        'temp': [0.05, 1.2, -0.3, 4.1, 0.08],
        'pressure': [2.3, 0.09, -1.1, 3.4, 0.12],
        'humidity': [0.8, -0.05, 2.2, 0.15],
        'light': [5.5, 0.07, 3.3, 0.21]
    }

    # Unused secondary dataset (distractor)
    secondary_data = {
        'vibration': [0.1, 0.3, 0.04],
        'sound': [0.45, 0.06, 0.91]
    }

    # Processing pipeline
    processed = preprocess_readings(raw_sensor_data)
    standardized = standardize(processed)

    # Weight configuration (some weights are irrelevant due to missing keys)
    importance_weights = {
        'temp': 1.5,
        'pressure': 2.0,
        'humidity': 1.0,
        'light': 0.8,
        'flow': 1.1  # Unused key
    }

    # Dummy transformation (no impact)
    transformed_keys = {k.upper(): v for k, v in standardized.items()}
    ignored_result = reduce(lambda acc, x: acc + x**2, transformed_keys.values(), 0)

    # Key statement
    final_score = calculate_final_score(standardized, importance_weights)
    
    # Print result
    print(f"Result: {final_score}")
from itertools import combinations

# Simulate sensor data fusion with noise filtering and weighted aggregation
def calculate_final_score(raw_data, importance_weights):
    # Preprocess: remove outliers using interquartile range (IQR)
    sorted_values = sorted(raw_data)
    q1 = sorted_values[len(sorted_values) // 4]
    q3 = sorted_values[3 * len(sorted_values) // 4]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    filtered_data = [x for x in raw_data if lower_bound <= x <= upper_bound]

    # Compute moving average as secondary validation
    window_size = 2
    moving_averages = []
    for i in range(len(filtered_data) - window_size + 1):
        window_avg = sum(filtered_data[i:i+window_size]) / window_size
        moving_averages.append(window_avg)

    # Use only values that appear in at least one above-average moving window
    avg_ma = sum(moving_averages) / len(moving_averages) if moving_averages else 0
    validated_points = {val for i, val in enumerate(filtered_data[:-1]) 
                         if (val + filtered_data[i+1]) / 2 >= avg_ma}

    # Incorporate weights via dot product only on validated sensors
    weighted_sum = 0
    total_weight = 0
    for i, val in enumerate(filtered_data):
        if val in validated_points or i % 2 == 0:
            weight = importance_weights.get(f'sensor_{i}', 0.5)
            weighted_sum += val * weight
            total_weight += weight

    normalized_score = weighted_sum / total_weight if total_weight > 0 else 0

    # Additional distraction: analyze pair correlations (not used)
    pair_corr_sum = 0
    for a, b in combinations(filtered_data, 2):
        if a > b and (a + b) % 2 == 0:
            pair_corr_sum += 1

    # Unused health metrics
    system_health = {
        'stability': len(moving_averages),
        'noise_ratio': (len(raw_data) - len(filtered_data)) / len(raw_data) if raw_data else 0,
        'pair_patterns': pair_corr_sum
    }

    # Final adjustment based on data consistency
    consistency_factor = len(validated_points) / len(filtered_data) if filtered_data else 0
    final_score = normalized_score * (1 + 0.1 * consistency_factor)

    return final_score

# Input data from 8 sensors (with deliberate outlier)
data = [12, 15, 9, 100, 14, 11, 13, 8]

# Weight configuration per sensor
weights = {
    'sensor_0': 1.2,
    'sensor_1': 0.8,
    'sensor_2': 1.0,
    'sensor_3': 0.5,  # low trust due to instability
    'sensor_4': 1.1,
    'sensor_5': 0.9,
    'sensor_6': 1.0,
    'sensor_7': 0.7
}

# Critical execution point
final_score = calculate_final_score(data, weights)
print(f"Result: {final_score}")
import itertools

# Simulated sensor data from multiple environmental monitoring stations
temperature_readings = [23.5, 24.1, 22.9, 25.3, 26.0, 24.8, 23.7]
humidity_readings = [45, 48, 52, 44, 55, 49, 50]
pressure_readings = [1013, 1015, 1012, 1016, 1014, 1011, 1017]
co2_levels = [410, 415, 420, 405, 430, 412, 425]

# Irrelevant backup readings (distractor)
backup_temperatures = [22.8, 23.4, 24.0, 25.1, 25.9, 24.6, 23.3]
backup_humidity = [46, 47, 51, 43, 56, 50, 48]

# Preprocessing: Normalize data to z-scores using rolling baseline (key computation path)
def normalize_series(series):
    mean_val = sum(series) / len(series)
    variance = sum((x - mean_val) ** 2 for x in series) / len(series)
    std_dev = variance ** 0.5
    return [(x - mean_val) / std_dev for x in series]

def calculate_trend_strength(series):
    # Simple linear trend approximation
    n = len(series)
    if n < 2:
        return 0.0
    slope = (series[-1] - series[0]) / (n - 1)
    variability = sum(abs(series[i+1] - series[i]) for i in range(n-1)) / (n-1)
    return abs(slope) / (variability + 0.1)

# Misleading auxiliary function (dead code path)
def legacy_normalization(data):
    max_val, min_val = max(data), min(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

# Real-time anomaly detection flags (partially relevant)
anomaly_flags = []
for i in range(len(temperature_readings)):
    temp_flag = temperature_readings[i] > 25.0
    humid_flag = humidity_readings[i] < 45 or humidity_readings[i] > 54
    co2_flag = co2_levels[i] > 420
    anomaly_flags.append(sum([temp_flag, humid_flag, co2_flag]))

# Distractor: Unused complex combinatorics on irrelevant pairings
unused_combinations = list(itertools.combinations_with_replacement([1, 2, 3], 3))
combination_sum = sum(sum(combo) for combo in unused_combinations)  # Red herring

# Weight initialization with decoy logic
weight_candidates = {
    'temp': [0.2, 0.25, 0.3],
    'humid': [0.15, 0.2, 0.25],
    'pressure': [0.05, 0.1, 0.15],
    'co2': [0.3, 0.35, 0.4]
}

# Incorrect weight selection path (misleading)
selected_weights_v1 = {k: weights[1] for k, weights in weight_candidates.items()}
# Correct weights determined by meta-evaluation (actual path)
selected_weights_v2 = {k: weights[2] for k, weights in weight_candidates.items()}

# Data fusion pipeline
normalized_temp = normalize_series(temperature_readings)
normalized_humid = normalize_series(humidity_readings)
normalized_pressure = normalize_series(pressure_readings)
normalized_co2 = normalize_series(co2_levels)

# Feature engineering with tuple packing/unpacking
aggregated_features = []
for t, h, p, c in zip(normalized_temp, normalized_humid, normalized_pressure, normalized_co2):
    composite = (t * 0.3) + (h * 0.2) + (p * 0.1) + (c * 0.4)
    stability_estimate = (1 - abs(t) * 0.1) * (1 - abs(h) * 0.05)
    aggregated_features.append((composite, stability_estimate))

# Spurious correlation check (distractor)
correlation_proxy = 0
for i in range(len(aggregated_features) - 1):
    if aggregated_features[i][0] * aggregated_features[i+1][0] < 0:
        correlation_proxy += 1

# Critical metric weights (used in final calculation)
metric_weights = [
    calculate_trend_strength(normalized_temp) * 1.2,
    calculate_trend_strength(normalized_humid) * 0.8,
    calculate_trend_strength(normalized_pressure) * 0.3,
    calculate_trend_strength(normalized_co2) * 1.5
]

# Normalized data matrix as list of tuples
normalized_data = list(zip(normalized_temp, normalized_humid, normalized_pressure, normalized_co2))

# Core evaluation function
def evaluate_performance(weights, data_tuples):
    # Apply weights to average feature values
    weighted_averages = []
    for idx, w in enumerate(weights):
        feature_values = [row[idx] for row in data_tuples]
        avg_val = sum(feature_values) / len(feature_values)
        weighted_averages.append(avg_val * w)
    
    # Secondary adjustment based on anomaly density
    anomaly_density = sum(anomaly_flags) / len(anomaly_flags)
    adjustment_factor = 1 - (anomaly_density * 0.3)
    
    # Final aggregation with non-linear boost
    raw_sum = sum(weighted_averages)
    boosted_performance = raw_sum * (1 + raw_sum ** 2) * adjustment_factor
    
    # Decoy operations (irrelevant)
    temp_debug = [x * 2 for x in weighted_averages]  # Unused
    debug_check = sum(temp_debug) % 7  # Dead end
    
    return boosted_performance

# Execution point of interest
final_score = evaluate_performance(metric_weights, normalized_data)

# Print result as required
print(f"Target result: {final_score}")
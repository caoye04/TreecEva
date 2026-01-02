import math

# Simulate sensor data with noise and valid readings
data_points = [
    (1.2, 3.5, 0.7), (2.1, -1.0, 0.9), (3.3, 4.2, 1.1),
    (4.0, 2.8, 0.6), (5.5, 6.1, 1.3), (6.2, 5.9, 0.8),
    (7.0, 7.2, 1.0), (8.1, 8.0, 1.4)
]

# Irrelevant baseline constants for distraction
temperature_bias = 0.3
pressure_floor = 101.3
altitude_reference = 500

# Preprocessing: extract only high-confidence readings (quality > 0.8)
valid_readings = [r for r in data_points if r[2] > 0.8]

# Misleading intermediate transformation - not used in final result
transformed = list(map(lambda x: (x[0]**1.1, x[1]**0.95, x[2]), valid_readings))

# Extract time and value series for analysis
time_series = [point[0] for point in valid_readings]
value_series = [point[1] for point in valid_readings]

# Compute moving average over window size 3 for smoothing
def moving_average(series, window=3):
    if len(series) < window:
        return series[:]
    avg = [(sum(series[i:i+window]) / window) for i in range(len(series) - window + 1)]
    return avg

smoothed_values = moving_average(value_series)

# Secondary distraction: analyze time deltas (not directly used)
time_deltas = [time_series[i+1] - time_series[i] for i in range(len(time_series)-1)]
avg_time_delta = sum(time_deltas) / len(time_deltas) if time_deltas else 0

# Core metric computation
peak_value = max(value_series)
base_trend = sum(smoothed_values) / len(smoothed_values) if smoothed_values else 0
drift = abs(peak_value - base_trend)

# Efficiency model based on stability and growth
stability_factor = 1 / (1 + drift * 0.1)
growth_potential = math.log(peak_value + 1)

# Final processing function
def process_metrics(raw_data):
    # Local slicing distraction
    segment = raw_data[1:6:2]  # Skips and subsets
    temp_weights = [math.sin(x[0] * 0.1) for x in segment]
    unused_total = sum(temp_weights)
    
    # Actual relevant logic
    valid_subset = [d for d in raw_data if d[2] > 0.85]  # Stricter filter
    if not valid_subset:
        return 0
    
    values = [v[1] for v in valid_subset]
    if len(values) < 2:
        score = values[0] if values else 0
    else:
        # Use lambda to compute weighted impact
        weights = list(map(lambda i: 0.5 + i * 0.1, range(len(values))))
        total_weight = sum(weights[:len(values)])
        weighted_sum = sum(val * weights[i] for i, val in enumerate(values))
        score = weighted_sum / total_weight
    
    # Apply logarithmic scaling
    return math.log(score + 10) if score > -10 else 0

# Execute main logic
final_output = process_metrics(data_points)

# Key tracking variable
efficiency_score = round(final_output * 1000) / 10.0

# Output result
print(f"Target result: {efficiency_score}")
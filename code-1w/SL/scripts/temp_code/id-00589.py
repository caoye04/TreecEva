from collections import defaultdict
import math

# Simulate sensor data aggregation and weighted scoring with noise filtering
def collect_sensor_readings():
    raw_readings = [12, 15, 10, 8, 23, 14, 18, 7]
    timestamps = [1, 2, 3, 4, 5, 6, 7, 8]
    
    # Misleading transformation (not used in final score)
    squared_noise = [x**2 for x in raw_readings if x < 10]
    offset_correction = sum(squared_noise) / len(squared_noise) if squared_noise else 0
    
    # Relevant data structure
    sensor_map = defaultdict(list)
    for t, val in zip(timestamps, raw_readings):
        sensor_map[t % 3].append(val)
    
    processed = []
    for key in sensor_map:
        if sensor_map[key]:
            avg_val = sum(sensor_map[key]) / len(sensor_map[key])
            processed.append(avg_val)
    
    return processed

# Filter outliers using a lambda (used later)
filter_outliers = lambda data, threshold: [x for x in data if abs(x - sum(data)/len(data)) < threshold]

# Secondary distraction: simulate calibration drift (unused)
def apply_calibration_drift(readings):
    drift = 0.1
    calibrated = []
    for i, val in enumerate(readings):
        calibrated.append(val + drift * i)  # This function is never called
    return calibrated

# Main processing pipeline
def calculate_final(data, weight_vec):
    # Unnecessary intermediate computation
    squared_sums = sum(x**2 for x in data)
    temp_shift = math.sin(len(data)) * 0.5
    
    # Actual relevant logic
    filtered = filter_outliers(data, 5.0)
    weighted_sum = sum(val * weight_vec[i] for i, val in enumerate(filtered))
    norm_factor = sum(weight_vec[:len(filtered)])
    
    # Dead code branch (never executes due to data size)
    if len(data) > 20:
        extra_bonus = 100
        weighted_sum += extra_bonus
    
    mean_weighted = weighted_sum / norm_factor if norm_factor != 0 else 0
    
    # Another distraction variable
    entropy_proxy = -sum(math.log(abs(x) + 1e-5) for x in weight_vec)
    
    return int(round(mean_weighted * 10))  # Final transformation

# Execution flow
data_chunk = collect_sensor_readings()

# Unused but plausible-looking preprocessing
sorted_data = sorted(data_chunk, reverse=True)
delta_rates = [sorted_data[i] - sorted_data[i+1] for i in range(len(sorted_data)-1)]

# Weight vector for scoring (critical input)
weights = [0.1, 0.3, 0.4, 0.2]

# Key statement
final_score = calculate_final(data_chunk, weights)

print(f"Result: {final_score}")
from itertools import combinations
from math import log

# Simulate sensor data processing with noise filtering and flow calculation
def preprocess_readings(raw_readings):
    filtered = [x for x in raw_readings if x > 0]
    normalized = [x / sum(filtered) for x in filtered]
    scaled = [int(x * 1000) for x in normalized]
    return scaled

# Identify anomalous patterns using combination analysis
def detect_anomalies(data):
    anomaly_score = 0
    for combo in combinations(data, 3):
        if sum(combo) > 1500:  # arbitrary threshold
            anomaly_score += 1
    return anomaly_score  # unused but adds cognitive load

# Transform data through multiple stages
def transform_sequence(seq):
    shifted = [(x >> 2) for x in seq]  # bitwise shift
    diff_series = [shifted[i+1] - shifted[i] for i in range(len(shifted)-1)]
    smoothed = [round((diff_series[i] + diff_series[i-1]) / 2) 
                for i in range(1, len(diff_series))]
    return smoothed + [sum(smoothed)]

# Main flow calculation based on transformed inputs
def calculate_net_flow(flow_points, cutoff):
    total_in = 0
    total_out = 0
    temp_buffer = []
    
    for val in flow_points:
        if val > cutoff:
            total_in += val
        else:
            total_out += val
        temp_buffer.append(abs(val - cutoff))
    
    # Secondary adjustment based on buffer statistics
    avg_dev = sum(temp_buffer) / len(temp_buffer)
    adjustment = int(avg_dev ** 0.5)
    net = (total_in - total_out) - adjustment
    
    return net

# Simulated system state
raw_sensor_data = [120, -5, 230, 45, 89, 0, 301, 150, 75, 200]
baseline_reference = 85

# Step 1: Preprocess to remove invalid readings
processed_data = preprocess_readings(raw_sensor_data)

# Step 2: Detect anomalies (result not used, distractor)
anomaly_count = detect_anomalies(processed_data)

# Step 3: Transform sequence through multi-stage pipeline
transformed_data = transform_sequence(processed_data)

# Step 4: Compute dynamic threshold based on derived stats
length_flag = len(transformed_data) > 5
threshold = baseline_reference if length_flag else 50

# Step 5: Calculate final flux using core logic
final_flux = calculate_net_flow(transformed_data, threshold)

# Output result
print(f"Result: {final_flux}")
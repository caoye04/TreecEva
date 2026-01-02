from collections import defaultdict
from itertools import combinations

# Simulate sensor data streams with timestamped readings
def generate_flow_data():
    timestamps = list(range(10))
    raw_readings = [23, 45, 12, 67, 34, 89, 23, 56, 78, 34]
    flow_data = defaultdict(float)
    
    for t, val in zip(timestamps, raw_readings):
        flow_data[t] = val * 1.05  # Apply calibration factor
    
    return flow_data

# Identify anomalous fluctuation pairs above a delta
def detect_spike_pairs(data, delta):
    spike_markers = []
    values = list(data.values())
    for i in range(len(values) - 1):
        if abs(values[i+1] - values[i]) > delta:
            spike_markers.append((i, i+1))
    return spike_markers

# Misleading function: appears relevant but unused in final calculation
def compute_variance(lst):
    mean = sum(lst) / len(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

# Core logic to calculate system equilibrium score
def calculate_equilibrium(data, threshold):
    values = list(data.values())
    
    # Step 1: Smooth data with moving average (window size = 2)
    smoothed = [(values[i] + values[i+1]) / 2 for i in range(len(values)-1)]
    smoothed.append(values[-1])  # Retain last value
    
    # Step 2: Count how many values are above threshold
    above_threshold_count = sum(1 for v in smoothed if v > threshold)
    
    # Step 3: Compute weighted balance score
    total_weight = 0
    for i, val in enumerate(smoothed):
        if val > threshold:
            total_weight += val * 0.1
        else:
            total_weight -= val * 0.05
    
    # Step 4: Adjust score based on trend consistency
    increasing_trend = 0
    for i in range(len(smoothed) - 1):
        if smoothed[i+1] > smoothed[i]:
            increasing_trend += 1
        elif smoothed[i+1] < smoothed[i]:
            increasing_trend -= 1
    
    # Final equilibrium score computation
    base_score = above_threshold_count * 100
    adjustment = total_weight + (increasing_trend * 5)
    final_score = base_score + adjustment
    
    # Irrelevant intermediate transformation (dead computation)
    temp_map = {i: final_score / (i+1) for i in range(1, 5)}
    scaling_factor = 1.0
    for k, v in temp_map.items():
        scaling_factor *= (v % 100) / 100
    
    return int(final_score)  # Deterministic integer result

# Main execution block
flow_data = generate_flow_data()
threshold = 50.0

# Dead code path: never executed but adds distraction
if __debug__:
    debug_info = [len(flow_data), min(flow_data.values()), max(flow_data.values())]
    redundant_sum = sum(debug_info)

# Generate spike markers (computed but not used in final score)
spike_pairs = detect_spike_pairs(flow_data, 20)
spike_count_proxy = len(spike_pairs) * 10  # Unused variable

# Key statement
equilibrium_score = calculate_equilibrium(flow_data, threshold)

# Print final result as required
print(f"Result: {equilibrium_score}")
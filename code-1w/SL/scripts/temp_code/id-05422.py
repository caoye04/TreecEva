from collections import defaultdict

# Simulate sensor data stream with temporal weights
def generate_flow_data():
    raw_readings = [12, 15, 10, 8, 23, 16, 9, 11, 14, 18]
    timestamps = list(range(10))
    weighted_flow = defaultdict(float)
    
    for i, val in enumerate(raw_readings):
        weighted_flow[timestamps[i]] = val * (0.9 ** i)  # Exponential decay weighting
    
    return dict(weighted_flow)

# Misleading auxiliary function that computes unrelated statistic
def compute_variance(data):
    n = len(data)
    if n == 0:
        return 0.0
    mean = sum(data) / n
    squared_diffs = [(x - mean) ** 2 for x in data]
    return sum(squared_diffs) / n

# Auxiliary distraction: analyze pattern cycles (not used in final result)
def detect_cycles(sequence, max_cycle_len=3):
    for length in range(1, max_cycle_len + 1):
        if len(sequence) >= 2 * length:
            first = sequence[-2*length:-length]
            second = sequence[-length:]
            if first == second:
                return length
    return None

# Core logic: calculate equilibrium score based on stable window deviations
def calculate_equilibrium(flow_dict, threshold):
    values = list(flow_dict.values())
    adjustments = []
    
    for i in range(1, len(values)):
        diff = abs(values[i] - values[i-1])
        if diff < threshold:
            adjustments.append(values[i] * 0.1)
        else:
            adjustments.append(-values[i] * 0.05)
    
    cumulative_shift = 0
    for adj in adjustments:
        cumulative_shift += adj
    
    # Introduce irrelevant intermediate normalization
    if cumulative_shift != 0:
        normalized_shift = cumulative_shift / (1 + abs(cumulative_shift))
    else:
        normalized_shift = 0
    
    # Final equilibrium formula
    base_magnitude = sum(v * 0.1 for v in values)
    equilibrium = base_magnitude + cumulative_shift
    
    return round(equilibrium, 4)

# Main execution block
flow_data = generate_flow_data()

# Distractor variables: unused cycle analysis
readings_only = list(flow_data.values())
cycle_detected = detect_cycles(readings_only)
variance_metric = compute_variance(readings_only)
scaling_factor = 1.0 if cycle_detected else 0.8

threshold = 2.5

# Key statement
equilibrium_score = calculate_equilibrium(flow_data, threshold)

# Tracking variable state for debugging (irrelevant to result)
status_log = []
if equilibrium_score > 10:
    status_log.append('HIGH')
elif equilibrium_score > 5:
    status_log.append('MEDIUM')
else:
    status_log.append('LOW')

# Output the target result
print(f"Result: {equilibrium_score}")
from collections import defaultdict
from itertools import combinations

# Simulate sensor data flow with decay patterns
def generate_decay_sequence(length, factor):
    return [int(100 * (factor ** i)) for i in range(length)]

# Misleading helper: analyzes peaks but not used in final logic
def analyze_peaks(data, limit=50):
    peak_count = 0
    for i in range(1, len(data) - 1):
        if data[i] > data[i-1] and data[i] > data[i+1] and data[i] < limit:
            peak_count += 1
    return peak_count

# Auxiliary function to compute moving average (distractor)
def moving_average(seq, window=3):
    if len(seq) < window:
        return [0]
    return [sum(seq[i:i+window]) // window for i in range(len(seq) - window + 1)]

# Core logic: detects equilibrium state based on deviation thresholds
def detect_equilibrium(flow_data, thresholds):
    base_ref = flow_data[0]
    deviation_counts = defaultdict(int)
    
    # Primary analysis loop
    for i, val in enumerate(flow_data):
        diff = abs(val - base_ref)
        if diff <= thresholds['low']:
            deviation_counts['stable'] += 1
        elif diff <= thresholds['medium']:
            deviation_counts['moderate'] += 1
        else:
            deviation_counts['high'] += 1
    
    # Compute equilibrium score: stable ratio adjusted by sequence length
    total = len(flow_data)
    stable_ratio = deviation_counts['stable'] / total
    modifier = 1 + (deviation_counts['moderate'] * 0.1) - (deviation_counts['high'] * 0.3)
    return int(stable_ratio * modifier * 100)

# Initialize parameters
sensor_sequence = generate_decay_sequence(12, 0.88)
threshold_map = {
    'low': 8,
    'medium': 15,
    'high': 25
}

# Dead code path - never called
if False:
    smoothed_data = moving_average(sensor_sequence, 4)
    noise_level = sum(smoothed_data) % 7

# Extract sub-sequence for processing (removes transient phase)
processed_flow = sensor_sequence[3:]

# Compute auxiliary metrics (unused)
baseline_avg = sum(processed_flow[:4]) / 4
peak_frequency = analyze_peaks(processed_flow, limit=45)

# Key computation point
equilibrium_score = detect_equilibrium(processed_flow, threshold_map)

# Print result for evaluation
print(f"Result: {equilibrium_score}")
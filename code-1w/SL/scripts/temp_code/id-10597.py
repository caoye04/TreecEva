import math

# Simulated sensor readings with noise and metadata
data_stream = [
    {'value': 12.5, 'status': 'active', 'timestamp': '2023-05-01T10:00:00'},
    {'value': 8.7, 'status': 'inactive', 'timestamp': '2023-05-01T10:01:00'},
    {'value': 14.2, 'status': 'active', 'timestamp': '2023-05-01T10:02:00'},
    {'value': 6.1, 'status': 'active', 'timestamp': '2023-05-01T10:03:00'},
    {'value': 9.8, 'status': 'active', 'timestamp': '2023-05-01T10:04:00'},
    {'value': 11.3, 'status': 'inactive', 'timestamp': '2023-05-01T10:05:00'},
    {'value': 13.9, 'status': 'active', 'timestamp': '2023-05-01T10:06:00'}
]

# Irrelevant constants for distraction (dead code paths)
CALIBRATION_FACTOR = 0.987
MAX_BUFFER_SIZE = 256
DEBUG_MODE = False
TEMP_OFFSET = -2.1

# Distractor function – never called but looks important
def normalize_signal(x):
    return [val * 0.5 for val in x if val > 0]

# Another decoy function with misleading name
def compute_entropy(data):
    entropy = 0.0
    for d in data:
        if isinstance(d['value'], float) and d['value'] > 0:
            entropy -= d['value'] * math.log(d['value'])
    return entropy

# Real processing begins here
active_only = [entry for entry in data_stream if entry['status'] == 'active']

# Extract values and timestamps separately
raw_values = [d['value'] for d in active_only]
timestamps = [d['timestamp'] for d in active_only]

# Convert timestamps to minute-of-day for analysis (unused later)
minute_of_day = []
for ts in timestamps:
    hour, minute = int(ts[11:13]), int(ts[14:16])
    minute_of_day.append(hour * 60 + minute)

# Apply arbitrary filtering based on substring in timestamp (distractor logic)
day_filter = [ts for ts in timestamps if '02' in ts or '06' in ts]
filtered_indices = [i for i, ts in enumerate(timestamps) if ts in day_filter]

# Actual relevant subset: only values at filtered indices
preliminary_data = [raw_values[i] for i in filtered_indices]

# Introduce string-based transformation as per requirement (string methods)
temp_strings = [f"{val:.1f}" for val in preliminary_data]
length_counts = {len(s.strip()): s.count('.') for s in temp_strings}

# Set operation to satisfy language-specific feature (set operations)
unique_chars = set()
for s in temp_strings:
    unique_chars.update(set(s))
non_digit_chars = unique_chars - set('0123456789')
num_special = len(non_digit_chars)

# Define threshold using distracting formula
base_threshold = sum(preliminary_data) / len(preliminary_data)
threshold = base_threshold - (num_special * 0.1)

# Core logic: detect anomalies above dynamic threshold
anomalies = [v for v in raw_values if v > threshold]

# Accumulate deviation from mean
mean_val = sum(raw_values) / len(raw_values)
deviation_sum = sum(abs(v - mean_val) for v in anomalies)

# Main processing function
def process_signals(signal_list, thresh):
    # Nested logic with multiple steps
    high_signals = [s for s in signal_list if s > thresh]
    squared_devs = [(s - thresh) ** 2 for s in high_signals]
    
    # Red herring: complex weight map that isn't fully used
    weights = {}
    for i, sd in enumerate(squared_devs):
        if i % 2 == 0:
            weights[i] = math.cos(sd / (thresh + 1))
        else:
            weights[i] = math.sin(sd / (thresh + 1))
    
    # Only even-indexed weights are actually used
    effective_weights = [weights[i] for i in range(0, len(weights), 2) if i in weights]
    
    # Final computation chain
    total_power = sum(high_signals)
    weight_factor = sum(effective_weights) if effective_weights else 1.0
    adjustment = weight_factor * (deviation_sum + len(anomalies))
    result = total_power - adjustment
    
    # Additional distraction: unused recursive helper
    def smooth(x, depth=0):
        if depth >= 2 or x <= 1:
            return x
        return smooth(x / 2, depth + 1) + smooth(x / 3, depth + 1)
    
    return int(round(result))

# Filter data again for final input
filtered_data = [v for v in raw_values if str(v).find('3') == -1 or v > 10]

# Critical execution point
final_output = process_signals(filtered_data, threshold)

print(f"Target result: {final_output}")
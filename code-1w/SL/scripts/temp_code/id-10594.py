from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and auxiliary metadata
timestamps = [1001, 1002, 1003, 1004, 1005]
sensor_readings = [3.2, -1.4, 4.8, 2.1, -0.9]
noise_floor = 0.5
baseline_offset = 2.0

# Irrelevant auxiliary data (distractor)
device_logs = [
    {'event': 'power_on', 'code': 200},
    {'event': 'calibrate', 'code': 301},
    {'event': 'idle', 'code': 100}
]

event_counter = defaultdict(int)
for log in device_logs:
    event_counter[log['event']] += 1

# Misleading intermediate transformation (dead path)
transformed_logs = []
for entry in device_logs:
    if 'cal' in entry['event']:
        transformed_logs.append(math.log(abs(entry['code']) + 1))

# Core signal processing chain
filtered_readings = []
for val in sensor_readings:
    if abs(val) > noise_floor:
        filtered_readings.append(val + baseline_offset)

# Apply windowing function (relevant)
window_weights = [0.2, 0.5, 1.0, 0.5, 0.2]
weighted_sum = sum(filtered_readings[i] * window_weights[i] for i in range(len(filtered_readings)))

# Bit manipulation red herring (irrelevant but plausible)
status_flag = 0b101010
mask = 0b111100
masked_status = status_flag & mask
shifted = masked_status >> 2
checksum = bin(shifted).count('1')

# Data aggregation with Counter (partially relevant)
reading_signs = ['positive' if x >= 0 else 'negative' for x in filtered_readings]
sign_distribution = Counter(reading_signs)

# Decoy function that looks important but unused
def compute_entropy(values):
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log(p) for p in probs)

# Real processing begins here — tuple unpacking and assignment
data_packet = (timestamps, filtered_readings)
times, corrected_values = data_packet

# Lambda-based transformation chain (key step)
process_chain = [
    lambda x: x ** 2,
    lambda x: x + 1.5,
    lambda x: math.sqrt(x)
]

cumulative = 0
for val in corrected_values:
    temp = val
    for func in process_chain:
        temp = func(temp)
    cumulative += temp

# Secondary processing branch with misleading correlation
aggregate_metrics = {}
aggregate_metrics['peak'] = max(corrected_values)
aggregate_metrics['skew'] = (3 * (sum(corrected_values) / len(corrected_values) - aggregate_metrics['peak'])) / (sum((x - sum(corrected_values)/len(corrected_values))**2 for x in corrected_values)/len(corrected_values))**0.5 if corrected_values else 0

# Destructuring assignment with dummy variables
_, _, main_component, _, _ = corrected_values

# Signal analysis function (uses lambda indirectly)
def analyze_signal(data):
    if not data:
        return 0.0
    
    # Local distractor: character counting in debug mode
    debug_tag = "DIAGNOSTIC_MODE_ACTIVE"
    char_count = sum(1 for c in debug_tag if c in 'AEIOU')
    
    # Actual computation path
    squared_chain = list(map(lambda x: ((x ** 3) / 2.0), data))
    base_result = sum(squared_chain) / len(squared_chain)
    
    # Conditional adjustment based on sign distribution (real logic)
    if sign_distribution['positive'] > sign_distribution['negative']:
        base_result *= 1.1
    else:
        base_result *= 0.9
    
    # Final adjustment using cumulative from earlier
    final_score = base_result + (cumulative / 100)
    
    return final_score

# Processed data construction (red herring list)
auxiliary_data = [math.sin(t) for t in timestamps]
processed_data = [x - baseline_offset for x in filtered_readings]

# Critical execution point
final_diagnostic = analyze_signal(processed_data)

print(f"Result: {final_diagnostic}")
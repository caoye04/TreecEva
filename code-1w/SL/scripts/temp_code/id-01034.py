from collections import defaultdict
import math

# Simulated sensor data aggregation (irrelevant preprocessing)
sensor_feeds = {
    'temp': [23.5, 24.1, 22.9, 25.0, 23.8],
    'pressure': [101.3, 100.7, 102.1, 99.8, 100.5],
    'humidity': [45, 47, 44, 50, 46]
}

# Irrelevant transformation: normalize unrelated metrics
def normalize(values):
    min_val, max_val = min(values), max(values)
    return [(v - min_val) / (max_val - min_val) for v in values]

def compute_entropy(data):
    total = sum(data)
    if total == 0:
        return 0.0
    return -sum((x / total) * math.log2(x / total) if x > 0 else 0 for x in data)

# Dead function - never called
def analyze_anomaly_pattern(seq):
    anomalies = []
    for i in range(1, len(seq)):
        if abs(seq[i] - seq[i-1]) > 1.0:
            anomalies.append(i)
    return anomalies

# Misleading intermediate diagnostic (red herring)
baseline_score = sum(len(feed) for feed in sensor_feeds.values()) * 0.75

# Core processing chain begins here
log_data = [
    {'event': 'read', 'value': 128, 'flags': 0b1010},
    {'event': 'write', 'value': 64, 'flags': 0b1100},
    {'event': 'read', 'value': 32, 'flags': 0b1010},
    {'event': 'exec', 'value': 16, 'flags': 0b0110},
    {'event': 'write', 'value': 8, 'flags': 0b1110}
]

# Bit manipulation analysis (partially relevant)
flag_counter = defaultdict(int)
for entry in log_data:
    flag_counter['high_bit'] += (entry['flags'] >> 3) & 1
    flag_counter['mid_bit'] += (entry['flags'] >> 2) & 1
    flag_counter['low_and'] += entry['flags'] & 3

# Decoy aggregation with string methods (distractor)
event_types = ''.join(entry['event'] for entry in log_data)
fragment_count = event_types.count('read') + event_types.count('write')

# Unused lambda (dead code path)
validate_entry = lambda e: e['value'] > 0 and len(e['event']) > 0

# Real processing starts: filter and transform based on bit conditions
active_masks = []
for entry in log_data:
    if (entry['flags'] & 0b1100) == 0b1100:  # High two bits set
        active_masks.append(entry['value'])

# Secondary condition: only those with alternating bit pattern in lower nibble
cleaned_values = []
for val in active_masks:
    lower_nibble = val & 0xF
    if ((lower_nibble >> 3) ^ ((lower_nibble >> 2) & 1) ^ ((lower_nibble >> 1) & 1) ^ (lower_nibble & 1)) == 1:
        cleaned_values.append(val)

# Accumulate using mathematical sequence
accum = 0
for i, v in enumerate(cleaned_values):
    accum += v * (2 ** i)  # Exponential weighting

# System threshold derived from irrelevant entropy of pressure
pressure_entropy = compute_entropy(sensor_feeds['pressure'])
system_threshold = int(pressure_entropy * 10)  # ~20

# Key logic: conditional offset based on flag patterns
offset = 0
if flag_counter['high_bit'] > 2:
    offset += 5
if flag_counter['mid_bit'] % 3 == 0:
    offset -= 2

# Final metric computation (core answer path)
base_metric = accum + offset
adjustment_factor = len([e for e in log_data if 'r' in e['event']])  # read events
final_diagnostic = base_metric * adjustment_factor - system_threshold

# Output result
print(f"Result: {final_diagnostic}")
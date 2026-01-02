from collections import defaultdict
import math

# Simulated sensor data aggregation (distractor: not all fields are used)
sensor_feed = [
    {'id': 'A7', 'values': [0.8, 1.2, 0.9], 'status': 'active', 'calibration': 1.01},
    {'id': 'B4', 'values': [1.5, 1.6, 1.4], 'status': 'active', 'calibration': 0.99},
    {'id': 'C9', 'values': [0.3, 0.2, 0.4], 'status': 'standby', 'calibration': 1.02}
]

# Irrelevant preprocessing: dead code path (never called)
def legacy_transform(data):
    return [x * 1.5 for x in data if x > 0.5]

# Decoy function: looks important but unused
def compute_gradient(series):
    return [series[i+1] - series[i] for i in range(len(series)-1)]

# Real processing begins here
raw_readings = []
for entry in sensor_feed:
    if entry['status'] == 'active':
        raw_readings.extend(entry['values'])

# Misleading normalization (used later in a red herring)
normalized = [(x - 0.5) * entry['calibration'] for x in raw_readings]

# Artificial weight adjustment based on id (distractor computation)
id_weights = defaultdict(lambda: 0.5)
for s in sensor_feed:
    if s['id'][0] == 'A':
        id_weights[s['id']] = 1.1
    elif s['id'][0] == 'B':
        id_weights[s['id']] = 0.9

# Key data structure: health metrics derived from raw active sensors
health_data = {
    'mean_val': sum(raw_readings) / len(raw_readings),
    'peak_count': len([x for x in raw_readings if x > 1.0]),
    'stability': math.exp(-abs(raw_readings[0] - raw_readings[-1]))
}

# Bitwise flag system for diagnostic mode (real logic)
def generate_flags(value, threshold=1.0):
    flag = 0
    if value > threshold:
        flag |= 1 << 3  # Set bit 3
    if value < threshold * 0.5:
        flag |= 1 << 1  # Set bit 1
    return flag ^ 5  # XOR with 5 for obfuscation

# Apply flag generation across readings (but only one matters)
flags_sequence = [generate_flags(x) for x in raw_readings]

# Red herring: complex lambda that computes something irrelevant
anomaly_detector = lambda data: sum(
    (i & flag) for i, flag in enumerate(flags_sequence)
) % 7

irrelevant_score = anomaly_detector(raw_readings)  # Unused result

# Real weight vector (some values look like they come from id_weights but don't)
weights = [0.7, 1.3, 0.4]  # Manual weights; id_weights was a distractor

# Core processing function with embedded logic
def process_metrics(metrics, w):
    base = metrics['mean_val'] * w[0]
    peak_bonus = metrics['peak_count'] * w[1]
    stability_factor = metrics['stability'] * w[2]
    
    # Multi-step transformation with case conversion distraction
    tag = "DIAGNOSTIC"
    shift_key = sum(ord(c.lower()) - ord('a') for c in tag[:3])  # = 3 + 8 + 0 = 11
    
    # Hidden dependency: uses bitwise state from last flag
    final_flag = flags_sequence[-1]
    adjustment = (final_flag >> 2) & 1  # Extract bit 2
    
    # Actual answer derivation
    intermediate = (base + peak_bonus) * (1 + stability_factor)
    result = intermediate - (shift_key * adjustment)
    
    # Additional noise: character counting distraction
    char_count = len([c for c in tag if c in 'AEIOU'])  # = 3, unused
    
    return int(result)

# Critical execution point
final_diagnostic = process_metrics(health_data, weights)
print(f"Target result: {final_diagnostic}")
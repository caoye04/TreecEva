from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation (distractor structure)
sensor_readings = {
    'temp': [23.4, 24.1, 22.9, 25.0, 23.8],
    'pressure': [1013, 1011, 1015, 1009, 1012],
    'humidity': [45, 47, 50, 44, 60]
}

# Irrelevant preprocessing: normalize unrelated metrics (red herring)
normalized = {}
for key, values in sensor_readings.items():
    mean_val = sum(values) / len(values)
    normalized[key] = [round((v - mean_val) / mean_val * 100, 2) for v in values]

# Decoy function: looks important but unused in final path
def analyze_trend(data):
    trend_score = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_score += 1
        elif data[i] < data[i-1]:
            trend_score -= 1
    return abs(trend_score)

# Unused diagnostic flags (dead code path)
flag_codes = defaultdict(int)
flag_codes['OVERHEAT'] = 1 << 5
flag_codes['LOW_PRESS'] = 1 << 4
flag_codes['HUMIDITY_SPIKE'] = 1 << 3

# Simulated event log with irrelevant events (distractor data)
event_log = [
    {'type': 'calibration', 'value': 0.98},
    {'type': 'noise_spike', 'value': None},
    {'type': 'data_drop', 'value': 0},
    {'type': 'normal', 'value': 1.0}
]

# Real processing begins here — hidden among noise
raw_signals = [3, 7, 15, 31, 63]  # Pattern: 2^n - 1
filtered_signals = [x for x in raw_signals if x > 10]  # Only keep >10

# Extract pattern-based feature: detect Mersenne-like numbers
feature_map = defaultdict(int)
for val in filtered_signals:
    if (val + 1) & val == 0:  # Power of two check (val+1 is power of two)
        feature_map['mersenne_candidate'] += 1
    if val % 3 == 0:
        feature_map['divisible_by_3'] += 1

# Construct summary using counter (relevant step)
data_summary = Counter({
    'total_inputs': len(raw_signals),
    'filtered_count': len(filtered_signals),
    'candidates': feature_map['mersenne_candidate'],
    'div3': feature_map['divisible_by_3']
})

# Activation threshold depends on mathematical condition (key logic)
binary_flags = 0
for sig in raw_signals:
    binary_flags ^= sig  # Accumulate XOR (bit manipulation red herring)

# Real threshold calculation buried in distraction
activation_threshold = 0
for k, v in data_summary.items():
    if 'count' in k:
        activation_threshold += v * 2
    elif k == 'candidates':
        activation_threshold += int(math.sqrt(v + 1))  # sqrt(1+1)=sqrt(2)~1.41 → 1
    else:
        activation_threshold -= v // 2

# Core processing function — only one that matters
def process_metrics(metrics, threshold):
    base = metrics['total_inputs']
    filter_ratio = metrics['filtered_count'] / base if base else 0
    candidate_boost = metrics['candidates'] * 10
    penalty = metrics['div3'] ** 2
    
    # Complex but deterministic formula
    intermediate = (base + threshold) * filter_ratio
    intermediate += candidate_boost - penalty
    
    # Final transformation via modular arithmetic and rounding
    result = int((intermediate % 17) * math.pi)  # pi ~ 3.141592
    return result

# Critical execution point
final_diagnostic = process_metrics(data_summary, activation_threshold)

# Misleading secondary calculation (unused)
consistency_check = sum(1 for e in event_log if e['type'] == 'normal') >= 1

# Output the target result
print(f"Result: {final_diagnostic}")
from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation (distractor: not directly used)
sensor_readings = [1024, 2048, 512, 768, 3072, 1536]
reading_frequencies = Counter(sensor_readings)
adjusted_readings = [r // 10 for r in sensor_readings if r > 500]

def legacy_normalization(x):
    """Outdated normalization (dead code path)"""
    return (x - min(sensor_readings)) / (max(sensor_readings) - min(sensor_readings))

def transform_sequence(seq):
    """Apply FFT-like transformation (red herring)"""
    transformed = []
    for i in range(len(seq)):
        val = 0
        for j in range(len(seq)):
            val += seq[j] * math.cos(2 * math.pi * i * j / len(seq))
        transformed.append(round(val, 3))
    return transformed

# Historical thresholds (irrelevant constants)
THRESHOLDS_V1 = {"low": 250, "medium": 750, "high": 1500}
THRESHOLDS_V2 = {"critical": 2048, "warning": 1024}

def compute_moving_average(data, window=3):
    """Unused utility function (decoy)"""
    avg = []
    for i in range(len(data) - window + 1):
        avg.append(sum(data[i:i+window]) / window)
    return avg

def analyze_trend(pattern):
    """Simulate trend analysis (misleading intermediate)"""
    trend_score = 0
    for i in range(1, len(pattern)):
        if pattern[i] > pattern[i-1]:
            trend_score += 1
        elif pattern[i] < pattern[i-1]:
            trend_score -= 0.5
    return round(trend_score, 2)

# Core evaluation logic (relevant)
baseline = [8, 12, 10, 15, 9, 11]
metric_data = {
    'throughput': [10, 14, 11, 16, 10, 13],
    'latency': [12, 8, 10, 7, 11, 9],
    'jitter': [3, 5, 4, 6, 5, 4]
}

# Bitmask simulation for status flags (mixed relevance)
STATUS_ACTIVE = 0b101
STATUS_STANDBY = 0b010
combined_status = STATUS_ACTIVE & 0b111 | 0b001
status_check = bin(combined_status).count('1')

# Distractor: complex but unused data structure
tree_map = defaultdict(lambda: defaultdict(int))
for i, val in enumerate(baseline):
    tree_map[f'level_{i % 3}'][f'node_{val % 5}'] += 1

# Auxiliary calculation with partial relevance
def calculate_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

entropy_value = calculate_entropy([len(baseline), len(metric_data['throughput']), 2])

# Real-time factor adjustment (distractor)
current_epoch = 1678886400
time_drift = (current_epoch % 1000) / 100
adjusted_factor = math.sin(time_drift) ** 2

# Main processing pipeline
scaling_factors = []
for key in ['throughput', 'latency', 'jitter']:
    series = metric_data[key]
    base = baseline[:len(series)]
    factor = 0
    for i in range(len(series)):
        if key == 'latency' or key == 'jitter':
            # Inverse relationship for negative metrics
            delta = base[i] - series[i]
            factor += (1 + delta / base[i]) if base[i] != 0 else 1
        else:
            factor += series[i] / base[i]
    scaling_factors.append(factor / len(series))

# Weighted combination with modular arithmetic
weights = [0.5, 0.3, 0.2]
composite_ratio = 0
for w, f in zip(weights, scaling_factors):
    composite_ratio += w * (f % 1.75)  # Nonlinear modulation

# Secondary adjustment using bitwise manipulation
ratio_int = int(composite_ratio * 1000)
masked_value = ratio_int ^ 0b1101  # XOR mask
shifted_back = (masked_value >> 2) + (masked_value & 0b11)

decay_constant = 0.94
smoothed_result = shifted_back * decay_constant

# Final performance evaluation
final_components = []
for k in metric_data:
    comp = sum(metric_data[k]) * 0.1
    final_components.append(comp)

sum_components = sum(final_components)

# Critical execution point
final_score = int(smoothed_result + sum_components - entropy_value * 10 + status_check)

Result: {final_score}
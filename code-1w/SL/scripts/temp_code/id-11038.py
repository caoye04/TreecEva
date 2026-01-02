import math

# Simulated system performance metrics with distractor fields
def generate_metrics():
    raw_data = {
        'latency_ms': 120,
        'throughput_ops': 850,
        'error_rate': 0.012,
        'memory_usage_mb': 450,
        'cpu_temp_c': 73,  # irrelevant distractor
        'disk_reads': 2048,  # red herring
        'network_latency_jitter': 8.2  # unused in final calc
    }

    processed = {k: v for k, v in raw_data.items() if 'jitter' not in k and 'temp' not in k}
    processed['latency_normalized'] = 1000 / (processed['latency_ms'] + 1)
    processed['reliability'] = (1 - processed['error_rate']) * 100
    processed['efficiency'] = processed['throughput_ops'] / (processed['memory_usage_mb'] + 1)
    return processed

# Weighting schema – some weights are decoys
weights = {
    'latency_normalized': 0.3,
    'reliability': 0.4,
    'efficiency': 0.3,
    'fake_metric_a': 0.0,  # dead weight
    'placeholder_b': 0.0   # red herring
}

# Irrelevant helper functions (distractors)
def calculate_heat_index(temp, humidity=50):
    # Unused function – misleading
    return temp + 0.5 * humidity

def validate_checksum(data_str):
    # Not used in main logic
    return sum(ord(c) for c in data_str) % 256

def analyze_disk_fragmentation(level):
    # Completely irrelevant
    return level * 0.7 + 10

# Core evaluation logic with nested conditions and lambda transforms
adjustment_factor = lambda x, mode: x * 1.1 if mode == 'aggressive' else x * 0.95

preprocess_fn = lambda d: {
    k: round(v, 3) for k, v in d.items() if isinstance(v, (int, float))
}

filter_valid_keys = lambda w: {k: v for k, v in w.items() if v > 0}

# Complex data transformation chain
metrics = generate_metrics()
metrics = preprocess_fn(metrics)

# Decoy dictionary operations
shadow_copy = dict(metrics)
shadow_copy['latency_ms'] = 999  # fake mutation
shadow_copy.pop('efficiency', None)

# Conditional mutation that looks important but doesn't affect outcome
if metrics['reliability'] > 90:
    temp_boost = metrics['latency_normalized'] * 0.05
    metrics['latency_normalized'] += temp_boost  # minor adjustment

# Use of string methods as per requirement (slightly relevant)
dynamic_key = ''.join(['latency', '_', 'normalized']).upper()
if dynamic_key.lower() in metrics:
    metrics['latency_normalized'] *= 1.02  # slight boost

# Another layer of irrelevant computation
snapshot_log = []
for key in ['cpu_temp_c', 'disk_reads', 'network_latency_jitter']:
    if key in raw_data := generate_metrics():
        snapshot_log.append(f"{key.upper()}: {raw_data[key]}")

# Log generation using string methods (distractor)
log_entry = " | ".join(snapshot_log)
log_hash = sum(map(ord, log_entry)) % 10000

# Real weighting process begins here
active_weights = filter_valid_keys(weights)
score_components = []

for metric_name, weight in active_weights.items():
    if metric_name in metrics:
        raw_value = metrics[metric_name]
        # Normalize score between 0-100 scale
        capped = min(raw_value, 100) if 'reliability' not in metric_name else raw_value
        normalized = capped / 100.0 * 100  # identity op for distraction
        weighted = normalized * weight
        score_components.append(weighted)

# Final aggregation
raw_sum = sum(score_components)

def apply_curve(value, curve_type='sigmoid'):
    if curve_type == 'sigmoid':
        return 50 + 50 * (1 / (1 + math.exp(-0.1 * (value - 50))))
    return value

adjusted_sum = adjustment_factor(raw_sum, 'aggressive')
final_score = round(apply_curve(adjusted_sum), 4)

# Critical print statement for result extraction
print(f"Result: {final_score}")
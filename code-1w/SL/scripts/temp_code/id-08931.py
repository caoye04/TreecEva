import math

# Simulated system metrics (some are red herrings)
def get_system_metrics():
    raw_data = {
        'cpu_load': 78.2,
        'memory_usage': 4321,
        'disk_read_ops': 1209,
        'network_latency_ms': 45.3,
        'packet_loss_rate': 0.002,
        'gpu_temp': 67.8,  # irrelevant
        'fan_speed_rpm': 2300,  # irrelevant
        'power_draw_watts': 180.5  # irrelevant
    }
    return raw_data

# Weight configuration for scoring (only some weights matter)
weights = {
    'latency_penalty': 0.4,
    'throughput_bonus': 0.3,
    'stability_factor': 0.3,
    'aesthetic_weight': 0.0  # decoy: never used
}

# Complex transformation pipeline
preprocess = lambda x: {
    'normalized_load': min(100, x['cpu_load']),
    'effective_memory_gb': x['memory_usage'] / 1024,
    'throughput_estimate': 1e6 / (x['disk_read_ops'] + 1),
    'latency_score': 100 - (x['network_latency_ms'] * 1.2),
    'reliability_index': math.log(1 / (x['packet_loss_rate'] + 1e-5)) if x['packet_loss_rate'] > 0 else 20
}

# Secondary validation check (partially dead code)
def validate_integrity(data):
    if data.get('checksum_valid', True):
        return True
    for _ in range(3):  # fake retry logic
        pass
    return False  # never reached

# Core evaluation logic with distractors
extra_weights = {'debug_scale': 1.0, 'legacy_mode': False}
def apply_weighting(vals, w):
    base = 0
    base += vals['latency_score'] * w['latency_penalty']
    base += vals['throughput_estimate'] * w['throughput_bonus'] * 0.001
    stability_component = vals['reliability_index'] * w['stability_factor']
    base += stability_component

    # Distractor block: looks important but doesn't affect result
    temp_debug = {}
    temp_debug['intermediate'] = base * 1.05
    if extra_weights['legacy_mode']:
        temp_debug['intermediate'] *= 0.95

    return base  # only base matters

# Higher-order function factory (red herring)
def make_scorer(calibration='standard'):
    factors = {'standard': 1.0, 'aggressive': 0.8, 'conservative': 1.2}
    adjustment = factors.get(calibration, 1.0)

    def scorer(x):
        return x * adjustment  # never actually used
    return scorer

# Unused recursive helper (dead code path)
def calculate_depth(n):
    if n <= 1:
        return 1
    return n + calculate_depth(n - 2)  # unused

# Main processing chain
raw_metrics = get_system_metrics()
processed_metrics = preprocess(raw_metrics)

# Fake data structure manipulation
audit_log = []
audit_log.append({k: round(v, 2) for k, v in processed_metrics.items()})
audit_log.append({'validation_passed': validate_integrity({})})
audit_log.append({'timestamp': '2024-05-20'})

# Critical computation obscured by noise
final_score = apply_weighting(processed_metrics, weights)

# Additional misleading transformations
shadow_score = final_score * 1.1
if shadow_score > 100:
    shadow_score = 100

# Final output
Result: {final_score}
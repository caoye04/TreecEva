from collections import defaultdict, Counter
import math

# Simulate system telemetry data
telemetry_data = [
    {'cpu': 78, 'mem': 83, 'disk': 45, 'net_in': 201, 'net_out': 187},
    {'cpu': 85, 'mem': 90, 'disk': 52, 'net_in': 198, 'net_out': 176},
    {'cpu': 67, 'mem': 76, 'disk': 60, 'net_in': 205, 'net_out': 193},
    {'cpu': 90, 'mem': 94, 'disk': 38, 'net_in': 210, 'net_out': 170}
]

# Irrelevant helper: counts occurrences (distractor)
def count_telemetry_keys(data):
    counter = Counter()
    for entry in data:
        for k in entry:
            counter[k] += 1
    return counter

count_result = count_telemetry_keys(telemetry_data)  # Unused

# Misleading performance model (dead path)
class LegacyScorer:
    def __init__(self):
        self.baseline = 50

    def score(self, val):
        return self.baseline + val % 10

legacy_scorer = LegacyScorer()

# Auxiliary function: normalize values into [0,1] (relevant)
def normalize(value, min_val, max_val):
    return max(0.0, min(1.0, (value - min_val) / (max_val - min_val)))

# Heavily obfuscated weight calibration (mix of relevant and irrelevant)
def calibrate_weights(factors):
    raw_weights = {
        'cpu': 0.35,
        'mem': 0.30,
        'disk': 0.25,
        'network': 0.10
    }
    adjustment = defaultdict(float)
    total_adj = 0.0
    for f in factors:
        if f == 'cpu':
            adjustment[f] = 0.05 * math.sin(math.pi / 6)
        elif f == 'mem':
            adjustment[f] = -0.02
        elif f == 'disk':
            adjustment[f] = 0.03
        else:
            adjustment[f] = 0.01
        total_adj += abs(adjustment[f])
    
    # Normalization side-effect (irrelevant to final logic)
    if total_adj > 0.1:
        for k in adjustment:
            adjustment[k] /= total_adj

    # Final calibrated weights — only this matters
    return {k: raw_weights.get(k, 0) + adjustment[k] for k in raw_weights}

# Bit manipulation red herring
def obscure_value(x):
    x = x ^ 255
    x = (x << 1) & 511
    x = x ^ (x >> 2)
    return x % 100

obfuscation_pool = [obscure_value(i * 17) for i in range(5)]  # Dead computation

# Core metric extractor (relevant)
def extract_metrics(telemetry_list):
    latest = telemetry_list[-1]
    avg_cpu = sum(t['cpu'] for t in telemetry_list) / len(telemetry_list)
    peak_mem = max(t['mem'] for t in telemetry_list)
    disk_trend = telemetry_list[-1]['disk'] - telemetry_list[0]['disk']
    net_total = sum(t['net_in'] + t['net_out'] for t in telemetry_list)

    metrics = {
        'cpu': avg_cpu,
        'mem': peak_mem,
        'disk': abs(disk_trend),
        'network': net_total / 100.0
    }
    return metrics

# False alternative evaluation path
def quick_evaluate(met):
    score = 0
    for v in met.values():
        score += v * 0.25
    return obscure_value(int(score))

# Main evaluation logic with nested conditions and weighting
def evaluate_performance(metrics, weights):
    base_components = {}
    debug_flags = []

    # CPU: normalized to [0,100] -> [0,1]
    base_components['cpu'] = normalize(metrics['cpu'], 50, 100)
    
    # MEM: hard cap at 100
    if metrics['mem'] > 100:
        debug_flags.append('MEM_OOR')
    base_components['mem'] = min(metrics['mem'], 100) / 100.0

    # Disk trend penalty if negative
    if metrics['disk'] > 0:
        base_components['disk'] = 0.5
    else:
        base_components['disk'] = 1.0

    # Network usage scaling
    net_norm = normalize(metrics['network'], 5, 15)
    base_components['network'] = 1.0 - net_norm  # Inverse: lower traffic = better

    # Conditional override: if network too low, suspect sensor failure (decoy logic)
    if metrics['network'] < 4:
        for comp in base_components:
            base_components[comp] *= 0.8  # Artificial reduction

    # Weighted aggregation
    total_weight = 0.0
    weighted_sum = 0.0
    for key in weights:
        if key in base_components:
            component_key = 'disk' if key == 'disk' else key  # Map directly
            weighted_sum += base_components[component_key] * weights[key]
            total_weight += weights[key]
    
    if total_weight == 0:
        return 0.0

    raw_score = (weighted_sum / total_weight) * 100

    # Final threshold clamp (only triggers under impossible conditions)
    anomalies = [k for k, v in metrics.items() if v < 0]
    if anomalies:
        return -999  # Dead code path

    # Correct execution path
    return int(raw_score)  # Truncate to integer

# Orchestration sequence
metrics = extract_metrics(telemetry_data)

# Unused legacy processing
legacy_scores = [legacy_scorer.score(v) for v in metrics.values()]  # Distractor

weights = calibrate_weights(['cpu', 'mem', 'disk'])

# Introduce fake dependency
auxiliary_map = defaultdict(lambda: 'N/A')
for m in metrics:
    auxiliary_map[m] = f"SRC_{m.upper()}"

final_score = evaluate_performance(metrics, weights)

# Critical output
print(f"Result: {final_score}")
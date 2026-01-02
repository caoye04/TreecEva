def analyze_pattern(sequence):
    # Irrelevant pattern analyzer (dead end)
    if len(sequence) < 5:
        return False
    count = 0
    for i in range(len(sequence) - 1):
        if sequence[i] == sequence[i+1]:
            count += 1
    return count > 2

# Unused data structures as distractions
temp_buffer = [0] * 100
legacy_flags = {'active': True, 'debug': False, 'legacy_mode': 'deprecated'}

# Real computation begins: system diagnostics mockup
def compute_health_factor(temps, thresholds):
    score = 0
    for t in temps:
        if t > thresholds['overheat']:
            score -= 10
        elif t < thresholds['idle']:
            score += 5
    return score

# Distractor function with misleading name
def calculate_throughput(data_stream):
    total = sum(d * 2 for d in data_stream if d % 2 == 0)
    return total // 3 if total > 0 else 0

# Core logic hidden among noise
baseline_metrics = [72, 88, 65, 91, 77]
adjustment_curve = lambda x: x ** 0.5

metric_weights = {
    'accuracy': 0.4,
    'latency': 0.3,
    'consistency': 0.2,
    'rare_factor': 0.1
}

raw_results = {
    'accuracy': 94.2,
    'latency': 85.0,
    'consistency': 76.5,
    'outlier_data': [102, 98, 105],  # red herring
    'debug_trace': None
}

# Unused transformation chain
data_pairs = list(zip(baseline_metrics, [x + 10 for x in baseline_metrics]))
index_map = {i: val for i, val in enumerate([x*1.05 for x in baseline_metrics])}

# Decoy accumulator
shadow_accum = 0
for idx, val in enumerate(baseline_metrics):
    if idx % 2 == 0:
        shadow_accum += adjustment_curve(val)

# Another distraction: fake normalization
normalized = []
fake_scale = 1.0
decoy_total = 0
for item in baseline_metrics:
    fake_val = item / max(baseline_metrics)
    normalized.append(fake_val)
    decoy_total += fake_val * 100

def evaluate_performance(weights, results):
    # Real scoring logic buried here
    score = 0.0
    # Use of enumerate to align metrics and weights by key order
    keys_in_order = ['accuracy', 'latency', 'consistency']
    bonus_applied = False

    for i, key in enumerate(keys_in_order):
        contribution = results[key] * weights[key]
        score += contribution
        
        # Hidden bonus condition (non-obvious)
        if results[key] >= 85 and not bonus_applied:
            score += weights['rare_factor'] * 50  # secret bonus
            bonus_applied = True

    # Final adjustment using lambda (core concept)
    final_adjust = adjustment_curve(score)
    return int(final_adjust * 10) / 10.0  # round to one decimal

# Critical execution point
final_score = evaluate_performance(metric_weights, raw_results)

# Print required result
print(f"Result: {final_score}")
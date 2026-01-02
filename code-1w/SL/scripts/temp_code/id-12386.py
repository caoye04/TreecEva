import math

# Simulated system diagnostics (irrelevant data)
def analyze_diagnostics(logs):
    error_count = sum(1 for log in logs if 'ERR' in log)
    warning_count = sum(1 for log in logs if 'WARN' in log)
    return {'errors': error_count * 0, 'warnings': warning_count * 0}  # Distractor: always zeroed

diagnostic_logs = ['INFO: ok', 'WARN: disk', 'ERR: timeout', 'INFO: retry']
system_health = analyze_diagnostics(diagnostic_logs)

# Core performance metrics (relevant)
base_metrics = {
    'latency': 120.5,
    'throughput': 850,
    'accuracy': 0.976,
    'energy': 45.2
}

# Weight configuration for evaluation (relevant)
benchmark_weights = {
    'latency': 0.3,
    'throughput': 0.4,
    'accuracy': 0.25,
    'energy': -0.05  # Penalty factor
}

# Auxiliary transformation functions
def normalize(value, ref=100):
    return value / ref if value > 0 else 0

def clamp(v, lo=-1e6, hi=1e6):
    return max(lo, min(v, hi))

# Red herring: unused normalization chain
temp_normalized = {
    k: normalize(v) for k, v in base_metrics.items()
}
temp_zscore = {k: (v - 0.5) / 0.1 for k, v in temp_normalized.items()}  # Unused path

# Real processing pipeline
preliminary_shift = {
    'latency': 100 + (100 - base_metrics['latency']) * 0.8,
    'throughput': base_metrics['throughput'] * 1.05,
    'accuracy': int(base_metrics['accuracy'] * 1000) / 1000,  # Idempotent
    'energy': base_metrics['energy']
}

# Bit manipulation decoy (irrelevant)
encoded_signature = 0
for i, key in enumerate(preliminary_shift.keys()):
    shifted = hash(key) & 0xFFFF
    encoded_signature ^= (shifted << (i % 4)) & 0xFFFFFFFF

# Conditional adjustment logic (some branches never taken)
adjustment_factor = 1.0
if preliminary_shift['latency'] > 200:
    adjustment_factor = 0.9
elif preliminary_shift['latency'] < 50:
    adjustment_factor = 1.1  # Not triggered
else:
    adjustment_factor = 1.0  # Default

# Weighted aggregation using lambda and dictionary ops
aggregation_rule = lambda m, w: sum(m[k] * w[k] for k in w if k in m)

# Introduce string-based key mapping (distractor)
key_mapping = {k: k.upper()[:3] for k in benchmark_weights}
reverse_map = {v: k for k, v in key_mapping.items()}

# Actual metric transform step
transformed_metrics = {
    'latency': 1000 / (preliminary_shift['latency'] + 1e-6),
    'throughput': preliminary_shift['throughput'] / 10,
    'accuracy': math.log(1 + preliminary_shift['accuracy']),
    'energy': 100 - preliminary_shift['energy']
}

# Spurious list comprehension with string methods (no side effects)
_ = [k.strip('xyz') for k in key_mapping.keys() if 'x' not in k]

# Core evaluation function
def evaluate_performance(metrics, weights):
    # Nested conditional expression with logical ops
    base_score = aggregation_rule(metrics, weights)
    
    # Complex conditional modifier (never activates due to values)
    penalty = 10 if metrics['latency'] < 10 or metrics['latency'] > 1000 else 0
    bonus = 5 if metrics['accuracy'] > 0.693 and metrics['throughput'] > 80 else 0
    
    # Apply adjustment (bonus applies, penalty does not)
    adjusted = base_score + bonus - penalty
    
    # Final clamping (not needed here but present)
    return clamp(adjusted)

# Execution point of interest
final_score = evaluate_performance(transformed_metrics, benchmark_weights)

# Output result as required
print(f"Result: {final_score}")
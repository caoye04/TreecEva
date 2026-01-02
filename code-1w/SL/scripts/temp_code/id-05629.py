def analyze_component(reading, threshold=75):
    return reading > threshold

# Simulated diagnostic readings from system modules
diagnostic_readings = [88, 92, 67, 70, 95, 83, 74]

# Irrelevant auxiliary data (distractor)
baseline_logs = [(1, 'init'), (2, 'load'), (3, 'run')]
log_ids = [idx for idx, _ in baseline_logs]

# Weight mapping for performance aggregation (critical)
weights = {
    'latency': 0.3,
    'throughput': 0.25,
    'accuracy': 0.35,
    'power': 0.1
}

# Misleading transformation (dead path)
transformed = list(map(lambda x: x * 1.05 if x < 70 else x, diagnostic_readings))

# Conditional masking with enumerate (relevant + distractor mix)
mask = [idx for idx, val in enumerate(diagnostic_readings) if val >= 80]
masked_diagnostics = [diagnostic_readings[i] for i in mask]

# Auxiliary calculation (irrelevant)
avg_transformed = sum(transformed) / len(transformed) if transformed else 0

# Key metrics computation (mixed relevance)
metrics = {
    'latency': sum(1 for r in diagnostic_readings if r < 75),
    'throughput': len(masked_diagnostics) * 2,
    'accuracy': float(sum(masked_diagnostics)) / len(masked_diagnostics) if masked_diagnostics else 0,
    'power': len(diagnostic_readings) - len(mask)
}

# Decoy function (never called - red herring)
def calculate_efficiency(data):
    total = 0
    for i, x in enumerate(data):
        if i % 2 == 0:
            total += x * 0.1
    return total / len(data)

# Another decoy: complex but unused bitwise logic
flag_state = 0b101010
for reading in diagnostic_readings:
    flag_state ^= reading & 0b1111

# Conditional expression with zip and enumerate (core relevant logic)
adjusted_metrics = {
    key: (metrics[key] * weights[key]) if metrics[key] > 0 else 0
    for key, weight in weights.items()
}

# Core aggregation logic
performance_bonuses = []
for i, (key, value) in enumerate(adjusted_metrics.items()):
    bonus = 5.0 if value >= 20 else (2.5 if value >= 10 else 0)
    performance_bonuses.append(bonus)

# Final score depends on correct tracing through masks, weights, and bonuses
final_score = 0
for (k, v), bonus in zip(adjusted_metrics.items(), performance_bonuses):
    final_score += v + bonus

# Distractor: unused normalization
normalized = {k: v / max(adjusted_metrics.values()) for k, v in adjusted_metrics.items()} if adjusted_metrics else {}

# Target result output
Target result: {final_score}
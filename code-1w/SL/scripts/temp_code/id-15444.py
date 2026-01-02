def process_sensor_data(raw_data):
    # Irrelevant preprocessing - distractor
    cleaned = [x for x in raw_data if x > 0]
    normalized = [x / max(cleaned) for x in cleaned]
    fft_transform = [normalized[i] * 2 for i in range(len(normalized))]  # Unused
    return cleaned

# Misleading auxiliary function
def calculate_baseline(x):
    return (x ** 2 + 3 * x + 1) % 100

# Decoy metrics and unused logic paths
baseline_shift = 7
offset_map = {i: calculate_baseline(i) for i in range(10)}

# Real data structures with mixed relevance
metrics = {
    'latency': 42,
    'throughput': 88,
    'consistency': 67,
    'reliability': 91,
    'jitter': 23  # Not used in final calculation
}

weights = [
    lambda x: x * 0.2,      # latency weight
    lambda x: x * 0.35,     # throughput weight
    lambda x: x * 0.25,     # consistency weight
    lambda x: x * 0.2       # reliability weight
]

# Dead code path - never called
def deprecated_analysis(data):
    return sum(v**0.5 for v in data.values()) * 0.1

# Simulated sensor input - irrelevant to final result but looks important
sensor_input = [12, -5, 34, 0, 67, 23, 89]
sensor_processed = process_sensor_data(sensor_input)

# Core logic embedded in noise
scaling_factor = 1.05
adjustment_log = []

for key in ['latency', 'throughput', 'consistency', 'reliability']:
    val = metrics[key]
    if val >= 80:
        adjustment_log.append(f"High: {key}")
    elif val >= 60:
        adjustment_log.append(f"Medium: {key}")
    else:
        adjustment_log.append(f"Low: {key}")

# Key computation buried in distractions
composite = 0
for i, key in enumerate(['latency', 'throughput', 'consistency', 'reliability']):
    if key == 'jitter':  # Never true
        continue
    composite += weights[i](metrics[key])

# Secondary adjustment based on rule
if metrics['throughput'] > 85 and metrics['latency'] > 40:
    composite *= scaling_factor

# Final score computed from composite
final_score = int(composite + 0.5)  # Round to nearest integer

# Red herring: unrelated dictionary slicing
summary_slice = offset_map.copy()
del summary_slice[0:3]  # Invalid syntax ignored in execution context - actually does nothing

# Output the target result
Target result: {final_score}
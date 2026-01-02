import math

# Simulated sensor array diagnostics with embedded logic chain
def analyze_sensor_cluster(readings, thresholds):
    normalized = [r / max(readings) for r in readings if r > 0]
    weighted_sum = sum([n * (i+1) for i, n in enumerate(normalized)])
    
    # Irrelevant transformation - red herring
    inverted_map = {i: round(1/v, 3) for i, v in enumerate(normalized) if v != 0}
    dummy_aggregate = sum(inverted_map.values()) * 0.1
    
    # Core signal extraction
    valid_windows = []
    for i in range(len(normalized) - 2):
        window = normalized[i:i+3]
        if all(w > 0.2 for w in window):
            valid_windows.append(sum(window))
    
    # Decoy statistical analysis
    mean_valid = sum(valid_windows) / len(valid_windows) if valid_windows else 0.0
    variance_proxy = sum([(v - mean_valid)**2 for v in valid_windows]) / (len(valid_windows) if valid_windows else 1)
    stability_score = math.exp(-variance_proxy) if variance_proxy < 1e5 else 0.0
    
    # Unused fallback path - dead code
    def legacy_adjustment(x):
        return x * 0.85 if x > 0.5 else x * 1.2
    
    # Primary result computation
    activation_chain = [
        math.sin(math.pi * w / 2) for w in valid_windows
    ]
    efficiency_factor = math.prod([a for a in activation_chain if a > 0.5])
    
    # Critical intermediate - used later
    aggregate_score = int(weighted_sum * efficiency_factor * 100)
    
    return aggregate_score, stability_score, dummy_aggregate

# Anomaly detection subsystem
def anomaly_detector(metrics):
    if not metrics:
        return 0
    
    # Bit manipulation decoy
    bit_analysis = 0
    for m in metrics:
        shifted = int(m * 1000) & 0xFF
        bit_analysis ^= shifted << 1
    
    # Real logic buried in noise
    filtered_metrics = [m for m in metrics if 0.1 <= m <= 0.9]
    if len(filtered_metrics) < 3:
        return len(filtered_metrics) * 10
    
    # Sorting distraction
    sorted_pairs = list(zip(sorted(filtered_metrics), sorted(filtered_metrics, reverse=True)))
    correlation_proxy = sum([abs(a - b) for a, b in sorted_pairs]) / len(sorted_pairs)
    
    # Actual detection logic
    entropy = -sum([m * math.log(m) for m in filtered_metrics if m > 0])
    return int(entropy * 20)

# Main execution context
sensor_data = [102, 305, 188, 476, 223, 319, 88, 401]
config_thresholds = [0.15, 0.25, 0.35, 0.45]

# Generate derived data streams
base_diagnostics = analyze_sensor_cluster(sensor_data, config_thresholds)
aggregate_score = base_diagnostics[0]

# Multiple parallel computations - distraction
baseline_reference = sum([int(math.sqrt(x)) for x in sensor_data]) // len(sensor_data)
decay_sequence = [baseline_reference // (i+1) for i in range(5)]
reference_anchor = sum(decay_sequence) % 100

# Entropy source generation - relevant
raw_entropy = [round((x % 100) / 100.0, 3) for x in sensor_data]
filtered_entropy = [e for e in raw_entropy if e > 0.05]
sorted_indices = [i for i, _ in sorted(enumerate(raw_entropy), key=lambda x: x[1], reverse=True)]

# Secondary irrelevant structure
priority_map = dict(zip(config_thresholds, ['low', 'medium', 'high', 'critical']))
status_tracker = {level: 0 for level in priority_map.values()}

# Key computation with distractors
entropy_values = [e**1.5 for e in filtered_entropy]
temp_correction = sum([i*e for i,e in enumerate(entropy_values)]) / len(entropy_values)

# Final integration point
final_diagnostic = aggregate_score + anomaly_detector(entropy_values)

# Unused diagnostic branches - dead code paths
if final_diagnostic > 500:
    adjustment_cycle = [final_diagnostic >> i for i in range(3)]
    final_diagnostic -= adjustment_cycle[2]

for _ in range(2):  # Fake iterative refinement
    pass

# Output requirement
print(f"Result: {final_diagnostic}")
import math

# System health monitoring simulation with red herrings and complex data flow
def analyze_sensor_readings(readings, baseline):
    adjusted = [r - baseline for r in readings]
    squared_devs = [x ** 2 for x in adjusted]
    variance = sum(squared_devs) / len(squared_devs) if squared_devs else 0
    return math.sqrt(variance)

# Irrelevant auxiliary function - dead code path
def calculate_fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Core processing chain with distractors
def evaluate_component_stability(signal_trace, noise_floor):
    filtered = []
    for val in signal_trace:
        if abs(val) > noise_floor:
            filtered.append(abs(val))
    if not filtered:
        return 0.0
    
    # Distractor: complex but unused transformation
    normalized = [f / max(filtered) for f in filtered]
    weighted_sum = sum(f * (i + 1) for i, f in enumerate(filtered))
    
    # Actual relevant computation
    decay_weights = [0.9 ** i for i in range(len(filtered))]
    weighted_avg = sum(filtered[i] * decay_weights[i] for i in range(len(filtered))) / sum(decay_weights)
    
    return weighted_avg

# Decoy function using sets - never called
def detect_anomalies(data_stream):
    historical = set(data_stream[:len(data_stream)//2])
    recent = set(data_stream[len(data_stream)//2:])
    return recent - historical

# Main aggregation logic
thresholds = {
    'critical': 85.0,
    'warning': 60.0,
    'info': 30.0
}

sensor_data = [78, 82, 65, 91, 74, 88, 69, 93, 77]
baseline_offset = 60
noise_filter_level = 10

# Complex preprocessing chain with irrelevant steps
raw_diagnostics = []
dummy_registry = []
for i, datum in enumerate(sensor_data):
    temp_adj = datum - baseline_offset
    if temp_adj > 20:
        raw_diagnostics.append(temp_adj ** 0.5 * 1.5)
    elif temp_adj > 10:
        raw_diagnostics.append(temp_adj / 3)
    else:
        raw_diagnostics.append(temp_adj * 0.8)
    
    # Dead code - builds unused registry
    dummy_registry.append(f"entry_{i}_{datum % 7}")

# Real processing begins here
stability_metric = evaluate_component_stability(raw_diagnostics, noise_filter_level)
fluctuation_score = analyze_sensor_readings(sensor_data, baseline_offset + 5)

# Multiple assignment red herring
temp_a, temp_b, temp_c = 123, 456, 789
aux_data = [temp_b ^ temp_c, temp_a & 512, temp_c >> 3]

# Key data structure with cross-references
processing_chain = {
    'inputs': sensor_data,
    'adjusted': [x - baseline_offset for x in sensor_data],
    'diagnostics': raw_diagnostics,
    'stability': stability_metric,
    'fluctuation': fluctuation_score,
    'timestamp': 1678886400,
    'version': '2.1.5'
}

# Unused but plausible-looking transformation
if processing_chain['fluctuation'] > 15:
    processing_chain['adjusted'] = [x * 0.9 for x in processing_chain['adjusted']]

# Critical function with list comprehensions and conditional logic
def aggregate_metrics(chain, limits):
    base_vals = chain['diagnostics']
    
    # Irrelevant filtering
    significant = [v for v in base_vals if v > 5]
    if len(significant) < 3:
        return -1
    
    # Complex but unused bitwise combination
    magic_seed = 0
    for val in significant[:4]:
        magic_seed ^= int(val) & 255
    
    # Real calculation path
    capped = [min(x, limits['warning']) for x in base_vals]
    boosted = [x * 1.1 if x > limits['info'] else x * 0.9 for x in capped]
    
    primary_contributions = [x for x in boosted if x > 25]
    
    if len(primary_contributions) == 0:
        final_score = 0
    else:
        final_score = sum(primary_contributions) / len(primary_contributions)
    
    # Final adjustment based on secondary metric
    if chain['stability'] > 12.0:
        final_score *= 1.25
    else:
        final_score *= 0.85
    
    return round(final_score, 6)

# Execution point of interest
final_diagnostic = aggregate_metrics(processing_chain, thresholds)
print(f"Result: {final_diagnostic}")
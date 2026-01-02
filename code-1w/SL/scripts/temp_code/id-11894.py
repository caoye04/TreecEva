def process_subsystem_data(data, config):
    # Irrelevant preprocessing (distractor)
    normalized = [x * config['scale'] + config['offset'] for x in data]
    filtered = [x for x in normalized if x > 0]
    checksum = sum([x ^ 2 for x in filtered]) % 1000

    # Real logic hidden among noise
    stats = {}
    stats['peak'] = max(filtered) if filtered else 0
    stats['stability'] = len([x for x in zip(filtered, filtered[1:]) if abs(x[0]-x[1]) < 1.5])
    
    # Decoy computation
    entropy = 0
    for i in range(len(filtered)):
        if filtered[i] > 10:
            entropy += 1
    stats['entropy'] = entropy

    return stats


def evaluate_health(metrics, policy):
    # Misleading health indicators
    base_score = 0
    if metrics['peak'] > policy['max_peak_warn']:
        base_score += 3
    if metrics['stability'] < policy['min_stability']:
        base_score += 2
    if metrics.get('entropy', 0) > 5:  # Dead path - not used
        base_score += 1

    # Actual signal
    if metrics['stability'] > 7 and metrics['peak'] < 45:
        return True
    return False

# Simulated sensor inputs (red herring: temperature not directly used)
temperature_readings = [23.1, 22.9, 24.0, 23.5, 23.8, 24.1, 23.9, 23.4, 23.6, 23.7]
humidity_readings = [45, 47, 46, 48, 44, 45, 47, 46, 45, 46]

# Core system logs with real data
raw_signal = [12, 14, 13, 15, 16, 14, 13, 12, 15, 17, 16, 15, 14, 13, 12]

# Configuration with irrelevant fields
config_params = {
    'scale': 1.05,
    'offset': -2.1,
    'threshold_floor': 10,
    'debug_mode': False,
    'log_verbosity': 3
}

# Unused diagnostic function (dead code path)
def compute_fourier_components(signal):
    result = []
    for k in range(5):
        comp = sum(signal[n] * (1j)**(k*n) for n in range(len(signal)))
        result.append(abs(comp))
    return result

# Policy with misleading keys
safety_policy = {
    'max_peak_warn': 44,
    'min_stability': 6,
    'critical_entropy': 8,
    'grace_period': 5
}

# Thresholds that actually matter
operation_thresholds = {
    'activation': 13.5,
    'coherence': 0.77
}

# Main processing chain
processed_metrics = process_subsystem_data(raw_signal, config_params)

# Fake correlation analysis
fake_correlation = sum(1 for t, h in zip(temperature_readings, humidity_readings) if t > 23.5 and h > 45)

# Critical branching logic buried in noise
if processed_metrics['peak'] > 15:
    processed_metrics['coherence'] = processed_metrics['stability'] / len(raw_signal)
else:
    processed_metrics['coherence'] = 0.0

# Another decoy variable
audit_trail = []
for idx, val in enumerate(raw_signal):
    if val % 2 == 0:
        audit_trail.append(f"E{idx}-{val}")

# Hidden transformation
transformed = [x for x in raw_signal if x > operation_thresholds['activation']]
index_map = {i: val for i, val in enumerate(transformed)}

# Real decision logic
valid_entries = 0
for i, val in enumerate(transformed):
    if i in index_map and index_map[i] == val and val - i > 10:
        valid_entries += 1

# Final aggregation with distraction
summary_flag = False
if len(audit_trail) > 5 and fake_correlation > 3:
    summary_flag = True  # Misleading

# Core answer derivation
if processed_metrics['coherence'] > operation_thresholds['coherence']:
    final_diagnostic = valid_entries * 1000 + int(processed_metrics['peak'])
elif evaluate_health(processed_metrics, safety_policy):
    final_diagnostic = 500 + len(transformed)
else:
    final_diagnostic = -1 * len(raw_signal)

print(f"Result: {final_diagnostic}")
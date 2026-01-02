import math

# Simulated sensor fusion system for environmental monitoring
raw_signals = [32.4, 18.7, 95.2, 44.9, 12.3, 67.8, 88.1, 23.5]
noise_floor = 15.0
sample_weights = {i: math.exp(-i * 0.2) for i in range(8)}
calibration_offsets = {'temp': 2.1, 'humidity': -1.3, 'pressure': 0.8}

# Irrelevant signal processing chain (dead path)
def legacy_filter(data):
    return [x * 0.9 for x in data if x > 20]

legacy_output = legacy_filter(raw_signals)  # Unused

# Primary processing pipeline
def preprocess(signal_list, offset=0.0):
    filtered = []
    cumulative = 0.0
    for val in signal_list:
        adjusted = val + offset
        if adjusted > noise_floor:
            cumulative += adjusted * 0.3
        else:
            cumulative -= offset
        filtered.append(cumulative)
    return filtered

processed_signal = preprocess(raw_signals, calibration_offsets['temp'])

# Decoy transformation using sets and dictionaries (irrelevant)
decoys = set()
for i, v in enumerate(processed_signal):
    decoys.add(int(v) % 7)
symbol_map = {k: (k * k + 3) % 11 for k in decoys}

# Real data structure used later
threshold_map = {
    'critical': 40.0,
    'warning': 25.0,
    'info': 10.0
}

status_codes = []
code_lookup = {}
for idx, reading in enumerate(processed_signal):
    if reading > threshold_map['critical']:
        status_codes.append(3)
        code_lookup[idx] = 'CRIT'
    elif reading > threshold_map['warning']:
        status_codes.append(2)
        code_lookup[idx] = 'WARN'
    elif reading > threshold_map['info']:
        status_codes.append(1)
        code_lookup[idx] = 'INFO'
    else:
        status_codes.append(0)
        code_lookup[idx] = 'NONE'

# Dummy statistical analysis (misleading intermediate)
mean_status = sum(status_codes) / len(status_codes) if status_codes else 0
variance_proxy = sum((s - mean_status) ** 2 for s in status_codes) / len(status_codes)

# Another red herring: complex dictionary transformation
history_log = {}
for i in range(5):
    history_log[i] = {
        'readings': [processed_signal[j] for j in range(len(processed_signal)) if j % 5 == i],
        'flags': [code_lookup.get(j, 'N/A') for j in range(len(code_lookup)) if j % 5 == i]
    }

# Unused recursive function (distractor)
def trace_back(index, depth=0):
    if depth >= 3 or index < 0:
        return 0
    return index + trace_back(index - status_codes[index % len(status_codes)], depth + 1)

# Real logic begins here: data aggregation
aggregated_diagnostics = []
counter = 0
for key, code_str in code_lookup.items():
    if code_str == 'WARN' or code_str == 'CRIT':
        raw_val = raw_signals[key] if key < len(raw_signals) else 0
        weight = sample_weights.get(key, 0.1)
        score = raw_val * weight * (1.5 if code_str == 'CRIT' else 1.0)
        aggregated_diagnostics.append(score)
        counter += 1

# Key statement with actual answer computation
def analyze_readings(scores, limits):
    total = sum(scores)
    penalty = 0
    if total > limits['critical']:
        penalty = 150
    elif total > limits['warning']:
        penalty = 75
    else:
        penalty = 25
    
    # Additional logic involving set operations
    unique_contributions = set([round(s) for s in scores])
    adjustment_set = {x for x in unique_contributions if x % 2 == 1}
    adjustment = len(adjustment_set) * 3.5
    
    return total - penalty + adjustment

final_diagnostic = analyze_readings(aggregated_diagnostics, threshold_map)

# Final output
print(f"Result: {final_diagnostic}")
import itertools

# Simulated sensor data aggregation (irrelevant preprocessing)
def collect_sensor_readings():
    raw_streams = [range(10), range(5, 15), [x**2 for x in range(3, 8)]]
    flattened = list(itertools.chain.from_iterable(raw_streams))
    filtered = [x for x in flattened if x % 2 == 0]
    return {f'sensor_{i}': val for i, val in enumerate(filtered)}

# Misleading health scoring model (dead path)
def compute_health_score(data):
    score = 0
    for k, v in data.items():
        if 'sensor_3' in k:
            score += v * 0.3
        elif 'sensor_7' in k:
            score -= v * 0.1
    return round(score, 2)

# Data normalization (distractor function)
def normalize_readings(data_dict):
    values = list(data_dict.values())
    min_val, max_val = min(values), max(values)
    return {k: (v - min_val) / (max_val - min_val + 1e-8) for k, v in data_dict.items()}

# Core diagnostic logic (relevant)
def extract_critical_flags(readings):
    flags = []
    for key, value in readings.items():
        if 'sensor_' in key:
            idx = int(key.split('_')[1])
            # Critical flag condition
            if idx in [1, 4, 7] and value > 6:
                flags.append(value * 2)
    return flags

# Recursive filtering (relevant but obfuscated by nesting)
def filter_anomalies(flag_list, threshold=10):
    if not flag_list:
        return [0]
    if len(flag_list) == 1:
        return [flag_list[0]] if flag_list[0] > threshold else [threshold // 2]
    mid = len(flag_list) // 2
    left = filter_anomalies(flag_list[:mid], threshold)
    right = filter_anomalies(flag_list[mid:], threshold + 1)
    return left + right

# Main analysis with distractors
health_data = {
    'patient_id': 'P7890',
    'baseline': 23.5,
    'readings': [12, 8, 15, 4, 20, 6],
    'metadata': {'unit': 'mg/dL', 'site': 'neuro'}
}

# Irrelevant transformation chain
temp_log = []
for i in range(3):
    temp_log.append({
        'step': i,
        'value': health_data['baseline'] ** (i+1) // (i+1) if i != 0 else health_data['baseline']
    })

# Unused prediction model (red herring)
def predict_outcome(log_entries):
    total = 0
    for entry in log_entries:
        if entry['step'] % 2 == 0:
            total += entry['value'] * 0.7
    return total * 1.2

# Real processing begins here (buried among distractions)
raw_flags = extract_critical_flags(collect_sensor_readings())
filtered_diagnostics = filter_anomalies(raw_flags, threshold=9)

# Secondary data injection (misleading)
synthetic_offset = sum([len(key) for key in health_data.keys() if isinstance(health_data[key], str)])

# Actual core computation
aggregated = sum(filtered_diagnostics) + synthetic_offset

correction_factor = 1
if aggregated > 50:
    correction_factor = 0.9
elif aggregated < 10:
    correction_factor = 1.5
else:
    correction_factor = 1.1

adjusted_metric = aggregated * correction_factor

# Final decision logic
if adjusted_metric.is_integer():
    final_diagnostic = int(adjusted_metric) + 5
else:
    final_diagnostic = round(adjusted_metric)

Result: final_diagnostic
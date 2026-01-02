def analyze_signal_strength(signal, baseline):
    adjusted = [s - baseline for s in signal]
    return [a ** 2 for a in adjusted if a > 0]


def compute_entropy(data):
    from math import log2
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    entropy = -sum((count / total) * log2(count / total) for count in freq.values())
    return round(entropy, 4)

# Irrelevant helper function (decoy)
def predict_outcome(x):
    return (x * 11) % 7 + 2  # Unused in main logic

# Simulated sensor readings over time
sensor_readings = [
    [12, 15, 14, 18, 16],
    [10, 11, 10, 13, 12],
    [14, 17, 16, 15, 18],
    [9, 10, 11, 10, 9],
    [20, 22, 21, 24, 23]
]

# System thresholds and weights (some are red herrings)
system_thresholds = {
    'critical': 20,
    'warning': 15,
    'info': 10,
    'decay_rate': 0.85,
    'amplification': 3.2
}

# Historical logs with metadata (partially used)
log_data = [
    {'timestamp': 1680000000, 'level': 'ERROR', 'value': 23, 'source': 'A'},
    {'timestamp': 1680000060, 'level': 'WARN', 'value': 14, 'source': 'B'},
    {'timestamp': 1680000120, 'level': 'INFO', 'value': 8, 'source': 'A'},
    {'timestamp': 1680000180, 'level': 'ERROR', 'value': 25, 'source': 'C'},
    {'timestamp': 1680000240, 'level': 'WARN', 'value': 16, 'source': 'B'}
]

# Misleading intermediate calculations (distractors)
temp_analysis = []
for entry in log_data:
    if entry['level'] == 'WARN':
        temp_analysis.append(entry['value'] * 0.75)
    elif entry['level'] == 'INFO':
        temp_analysis.append(entry['value'] * 1.1)

# Unused transformation path (dead code)
legacy_buffer = []
for i, val in enumerate([entry['value'] for entry in log_data]):
    if i % 2 == 0:
        legacy_buffer.append(val << 1)
    else:
        legacy_buffer.append(val >> 1)

# Core processing function with relevant logic
def process_metrics(logs, thresholds):
    critical_count = 0
    warning_sum = 0
    source_map = {}
    
    # Extract source counts using enumerate and zip
    sources = [entry['source'] for entry in logs]
    for idx, src in enumerate(sources):
        if src not in source_map:
            source_map[src] = []
        source_map[src].append(idx)
    
    # Use zip to pair values and levels
    values_and_levels = [(e['value'], e['level']) for e in logs]
    for val, level in values_and_levels:
        if level == 'ERROR' and val > thresholds['critical']:
            critical_count += 1
        elif level == 'WARN' and val >= thresholds['warning']:
            warning_sum += val
    
    # Secondary analysis: gap between high-severity events
    error_indices = [i for i, e in enumerate(logs) if e['level'] == 'ERROR']
    max_gap = 0
    if len(error_indices) > 1:
        gaps = [error_indices[i+1] - error_indices[i] for i in range(len(error_indices)-1)]
        max_gap = max(gaps)
    
    # Compute derived metric: weighted diagnostic score
    base_score = critical_count * 17 + warning_sum // 2
    adjustment = 0
    if max_gap > 0:
        adjustment = len(source_map) * 3
    
    # Final computation (key point)
    final_diagnostic = base_score + adjustment
    
    # Dead branch with misleading comment (red herring)
    if final_diagnostic < 0:
        # This would indicate system instability — never reached
        final_diagnostic = -final_diagnostic * 2  
    
    return final_diagnostic

# Additional irrelevant signal analysis (distraction)
all_signals = [item for sublist in sensor_readings for item in sublist]
positive_power = analyze_signal_strength(all_signals, baseline=12)
entropy_value = compute_entropy(positive_power)

# Execution point of interest
final_diagnostic = process_metrics(log_data, system_thresholds)
print(f"Result: {final_diagnostic}")
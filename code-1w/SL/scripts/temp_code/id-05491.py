import itertools

# System health monitoring simulation with red herrings and complex data flow

def analyze_signal_strength(signal_data, threshold=0.75):
    strong_signals = [s for s in signal_data if abs(s) > threshold]
    return len(strong_signals) / len(signal_data) if signal_data else 0


def compute_entropy(values):
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = -sum((count / total) * log2(count / total) for count in freq.values())
    return round(entropy, 6)

# Irrelevant helper (decoy function)
def unused_data_transform(x):
    return [i ** 3 for i in x if i % 2 == 0]

# Misleading intermediate processing
temp_log = ['error', 'warning', 'info', 'debug']
log_count = {level: temp_log.count(level) for level in set(temp_log)}
shadow_metric = sum(len(level) for level in temp_log)  # Distractor

# Core sensor array simulation
sensor_ids = ['S1', 'S2', 'S3', 'S4']
sensor_readings = {
    'S1': [0.82, 0.76, 0.88, 0.64, 0.71],
    'S2': [0.91, 0.89, 0.92, 0.87, 0.90],
    'S3': [0.54, 0.61, 0.58, 0.63, 0.59],
    'S4': [0.77, 0.73, 0.75, 0.79, 0.70]
}

# Dead code path (never called)
def deprecated_calibration(seq):
    return [x * 1.05 for x in seq]

# Complex but partially irrelevant transformation chain
processing_artifacts = []
for sid in sensor_ids:
    readings = sensor_readings[sid]
    clipped = [r for r in readings if r >= 0.65]
    processed = list(map(lambda x: x ** 2, clipped))
    processing_artifacts.append(processed)

# Decoy accumulation
phantom_sum = 0
for group in processing_artifacts:
    for val in group:
        if val > 0.7:
            phantom_sum += val * 0.1  # Misleading metric

# Real signal analysis (critical path)
effective_strengths = []
for sid, readings in sensor_readings.items():
    ratio = analyze_signal_strength(readings, threshold=0.75)
    effective_strengths.append(ratio)

# Simulated timestamp drift (irrelevant)
timestamps = [1634567890 + i*30 for i in range(20)]
drift_correction = [(t % 1000) / 100 for t in timestamps[:5]]

# Bit manipulation red herring
config_flag = 0b101010
mask = 0b111100
obfuscated_key = config_flag ^ mask << 2

# Conditional decoy block (never executes due to logic)
if len(drift_correction) < 2:
    adjusted_flags = [obfuscated_key | 0b11]
else:
    adjusted_flags = []

# Real diagnostic computation begins here
baseline = [0.6, 0.8, 0.7, 0.9]
consistency_scores = []

for i, strength in enumerate(effective_strengths):
    deviation = abs(strength - baseline[i])
    score = 1 - (deviation / 1.0)
    consistency_scores.append(max(score, 0))

# Use of itertools (required feature)
combinations = list(itertools.combinations(consistency_scores, 2))
stability_index = sum(abs(a - b) for a, b in combinations)

# String method distraction
status_msg = "System nominal: all sensors online"
words = status_msg.split(':')
clean_status = words[1].strip().replace('online', 'active')
word_count = len(clean_status.split())

# Critical processing chain (mix of relevant and irrelevant)
processing_chain = [
    {'stage': 'preprocess', 'data': 1.0, 'valid': True},
    {'stage': 'filter', 'data': stability_index, 'valid': True},
    {'stage': 'encode', 'data': 0.0, 'valid': False},  # Invalid stage
    {'stage': 'diagnose', 'data': sum(consistency_scores), 'valid': True}
]

# Diagnostic metadata (partially used)
diagnostics = {
    'version': '2.1.0',
    'calibration': 'passed',
    'anomalies': 0,
    'last_updated': '2023-10-05',
    'entropy': compute_entropy([round(s, 2) for s in effective_strengths])
}

# Main aggregation function
def aggregate_metrics(chain, meta):
    valid_data = [step['data'] for step in chain if step['valid']]
    if not valid_data:
        return 0.0
    
    # Red herring: use string from earlier
    version_parts = meta['version'].split('.')
    version_factor = int(version_parts[0])
    
    # Real calculation
    base_metric = sum(valid_data) / len(valid_data)
    anomaly_penalty = meta['anomalies'] * 0.1
    entropy_bonus = meta['entropy'] * 0.05
    
    result = base_metric - anomaly_penalty + entropy_bonus
    return round(result, 6)

# Final computation - key execution point
final_diagnostic = aggregate_metrics(processing_chain, diagnostics)

# Print result as required
print(f"Target result: {final_diagnostic}")
import itertools

# Simulated system telemetry data (distraction)
telemetry_logs = [127, 255, 193, 104, 88, 201]
error_flags = {i: (v % 16 == 0) for i, v in enumerate(telemetry_logs)}
active_channels = list(itertools.compress(range(len(telemetry_logs)), [not f for f in error_flags.values()]))

# Legacy calibration constants (red herring)
CALIBRATION_MAP = {k: ((k * 17) % 19) for k in range(15)}
reference_checksum = sum(CALIBRATION_MAP.values()) % 1000

# Signal preprocessing pipeline
raw_signals = [0x1A, 0x2B, 0x3C, 0x4D]
filtered_signals = []
for s in raw_signals:
    processed = (s ^ 0xFF) & 0x7F
    if processed > 50:
        filtered_signals.append(processed)

# Data alignment routine (mostly irrelevant)
shift_register = [filtered_signals[i] >> i for i in range(len(filtered_signals))]
sync_marker = shift_register[0] | shift_register[-1]

# Core metric computation setup
baseline = {'alpha': 42, 'beta': 58, 'gamma': 64}
metrics = [
    {'type': 'latency', 'value': 120, 'weight': 0.25},
    {'type': 'throughput', 'value': 84, 'weight': 0.4},
    {'type': 'jitter', 'value': 16, 'weight': 0.35}
]

# Auxiliary transformation (distractor)
transformed_metrics = []
for m in metrics:
    temp_val = m['value']
    if m['type'] == 'latency':
        temp_val = max(0, 100 - m['value'] / 1.2)
    elif m['type'] == 'jitter':
        temp_val = (100 - m['value']) * 0.8
    transformed_metrics.append({**m, 'adjusted': temp_val})

# Bit manipulation layer (partial relevance)
def apply_mask(value, mask=0x1F):
    return (value & mask) ^ (mask >> 2)

# Weighted scoring engine
def compute_raw_score(data, base):
    score = 0.0
    for entry in data:
        contribution = 0
        if entry['type'] == 'latency':
            contribution = (base['alpha'] + entry['value']) * entry['weight']
        elif entry['type'] == 'throughput':
            contribution = (base['beta'] + entry['value']) * entry['weight']
        elif entry['type'] == 'jitter':
            contribution = (base['gamma'] - entry['value']) * entry['weight']
        score += contribution
    # Misleading adjustment
    adjustment_factor = apply_mask(int(score)) / 32.0
    return score - adjustment_factor

# Higher-order evaluation with red herrings
def enhance_with_context(signal_list, metric_set):
    # Unused context enrichment (dead path)
    combinations = list(itertools.combinations(signal_list, 2))
    avg_product = sum(a * b for a, b in combinations) / len(combinations) if combinations else 0
    
    # Decoy entropy calculation
    entropy_proxy = 0
    for x in signal_list:
        bits = bin(x).count('1')
        entropy_proxy += bits * 0.1
    
    # Actual relevant part: count high-frequency components
    hf_count = sum(1 for s in signal_list if s > 60)
    return hf_count * 1.5

# Final performance evaluator
def evaluate_performance(metrix, base_config):
    # Step 1: Compute base composite score
    raw = compute_raw_score(metrix, base_config)
    
    # Step 2: Extract signal enhancement factor (only one used element)
    sig_factor = enhance_with_context(filtered_signals, metrix)
    
    # Step 3: Apply enhancement multiplicatively
    enhanced = raw * (1 + sig_factor / 100)
    
    # Step 4: Apply final transformation using bitwise logic on integer part
    int_part = int(enhanced)
    decimal_noise = (apply_mask(int_part, 0x3F) / 1000)  # Small decimal perturbation
    final = int_part + decimal_noise
    
    # Irrelevant diagnostic print (distractor)
    # print(f'Diagnostic: noise={decimal_noise}, hf_signals={sig_factor}')
    
    return final

# Execution point of interest
metric_data = metrics  # alias to trigger reasoning
final_score = evaluate_performance(metric_data, baseline)
print(f'Target result: {final_score}')
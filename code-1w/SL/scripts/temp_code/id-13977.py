def analyze_system_health(health_data, weights):
    cumulative_score = 0
    for i, (metric, value) in enumerate(health_data.items()):
        if i % 2 == 0:
            cumulative_score += value * weights.get(metric, 1.0)
        else:
            cumulative_score -= value * 0.5
    return cumulative_score

# Irrelevant helper function (dead code path)
def encrypt_log(data):
    return ''.join(chr((ord(c) + 3) % 128) for c in data)

# Misleading diagnostic computation
temp_calibration = sum([i**2 for i in range(6)])  # Unused red herring

# Another decoy: bit manipulation with no effect
defect_flag = (0b1010 ^ 0b1100) >> 1  # Results in 3, never used

# Simulated log entries with sensor readings
log_entries = {
    'temp': 45,
    'pressure': 22,
    'vibration': 18,
    'humidity': 33,
    'voltage': 12
}

# System thresholds (some irrelevant keys included)
system_thresholds = {
    'temp': 50,
    'pressure': 25,
    'vibration': 20,
    'irrelevant_metric_1': 999,
    'irrelevant_metric_2': -1
}

# Weight map for health analysis (only partially used)
weight_map = {
    'temp': 1.2,
    'vibration': 0.8,
    'voltage': 1.5
}

# Auxiliary transformation using zip and enumerate (partially relevant)
adjusted_readings = []
for idx, (k, v) in enumerate(zip(log_entries.keys(), log_entries.values())):
    adjustment_factor = 1.1 if k in ['temp', 'humidity'] else 0.9
    adjusted_readings.append(v * adjustment_factor)

# Create lambda for dynamic filtering (used once)
above_threshold = lambda x, thresh: x > thresh

# Secondary processing: count how many metrics exceed their threshold
exceed_count = 0
for metric, value in log_entries.items():
    threshold = system_thresholds.get(metric, float('inf'))
    if above_threshold(value, threshold):
        exceed_count += 1

# Tertiary distraction: string-based status generation (unused)
current_status = "OK" if exceed_count < 3 else "ALERT"
status_code = hash(current_status) % 100  # Dead end

# Real logic begins: transform log entries into normalized scores
def process_metrics(entries, thresholds):
    score = 0
    base_keys = ['temp', 'pressure', 'vibration']
    
    # First pass: normalize each entry against threshold
    normalized = []
    for key, val in entries.items():
        if key in thresholds and thresholds[key] != float('inf') and thresholds[key] > 0:
            norm_val = round(val / thresholds[key], 4)
            normalized.append(norm_val)
    
    # Second pass: apply conditional boosts using enumerate
    boosted = []
    for i, val in enumerate(normalized):
        if i % 2 == 0 and val < 1.0:
            boosted.append(val * 1.1)
        elif i % 3 == 0 and val >= 1.0:
            boosted.append(val * 0.95)
        else:
            boosted.append(val)
    
    # Third pass: aggregate with weighted sum via lambda
    aggregator = lambda vals: sum(v ** 2 for v in vals)  # Emphasis on deviations
    raw_diagnostic = aggregator(boosted)
    
    # Final adjustment based on discrete conditions
    if len(boosted) > 3:
        raw_diagnostic *= 1.05
    elif exceed_count == 0:
        raw_diagnostic *= 0.98
    else:
        raw_diagnostic += 0.1
    
    # Critical assignment
    final_diagnostic = int(round(raw_diagnostic * 1000))
    
    # Dead return branch (never reached due to unconditional prior logic)
    if False:
        return sum([ord(c) for c in str(final_diagnostic)])  # Decoy
    
    return final_diagnostic

# Execute main logic
final_diagnostic = process_metrics(log_entries, system_thresholds)

# Print result as required
print(f"Result: {final_diagnostic}")
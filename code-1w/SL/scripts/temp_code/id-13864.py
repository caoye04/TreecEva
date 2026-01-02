from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timestamps = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008]
raw_readings = [23.5, 45.0, 12.8, 67.3, 29.1, 88.4, 34.7, 76.2]
status_flags = ['OK', 'WARN', 'OK', 'CRIT', 'OK', 'CRIT', 'OK', 'WARN']

# Irrelevant auxiliary mappings (distractor)
legacy_map = {'A': 1, 'B': 2, 'Z9': lambda x: x ** 2}
dummy_counter = Counter('irrelevantstring')

# System configuration parameters
system_thresholds = {
    'critical': 80.0,
    'warning': 50.0,
    'decay_rate': 0.9,
    'amplification_factor': 1.75
}

# Historical baseline (dead code path - not used in final computation)
def get_historical_baseline():
    return {ts: raw_readings[i] * 0.9 for i, ts in enumerate(timestamps)}

# Misleading diagnostic function that appears relevant but isn't used
def analyze_trend(data):
    trend_score = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_score += 1
    return trend_score / len(data)

# Core processing pipeline
log_entries = []
for i in range(len(timestamps)):
    entry = {
        'ts': timestamps[i],
        'value': raw_readings[i],
        'flag': status_flags[i],
        'category': 'CRIT' if raw_readings[i] > 60.0 else 'MONITOR'
    }
    log_entries.append(entry)

# Unused transformation (red herring)
scaled_logs = list(map(lambda x: {**x, 'scaled': x['value'] * 1.1}, log_entries))

# Auxiliary calculation with decoy intermediate results
event_risk_levels = defaultdict(int)
for entry in log_entries:
    level = 0
    if entry['value'] > system_thresholds['critical']:
        level = 3
    elif entry['value'] > system_thresholds['warning']:
        level = 2
    elif entry['flag'] == 'WARN':
        level = 1
    event_risk_levels[entry['ts']] = level

# Secondary metric tracker (partially used but mostly distraction)
flag_distribution = Counter(status_flags)

# Complex multi-step processor with nested logic
def compute_stability_index(entries, thresholds):
    critical_count = 0
    warning_count = 0
    total_deviation = 0.0
    
    for e in entries:
        val = e['value']
        if val > thresholds['critical']:
            critical_count += 1
        if val > thresholds['warning']:
            warning_count += 1
        base = thresholds['warning']
        deviation = max(0, val - base)
        adjusted = deviation * thresholds['amplification_factor']
        total_deviation += adjusted
    
    # Apply decay across cumulative deviation
    stabilized = total_deviation * (thresholds['decay_rate'] ** critical_count)
    
    # Incorporate risk distribution entropy (real usage)
    entropy = 0.0
    counts = [critical_count, warning_count, len(entries) - warning_count]
    total = sum(counts)
    if total > 0:
        probabilities = [c / total for c in counts if c > 0]
        entropy = -sum(p * math.log(p) for p in probabilities)
    
    return stabilized + (entropy * 10)

# Primary analysis engine
def process_metrics(entries, config):
    # Step 1: Filter high-risk entries
    crit_entries = [e for e in entries if e['category'] == 'CRIT']
    
    # Step 2: Compute aggregate statistics
    raw_sum = sum(e['value'] for e in entries)
    raw_avg = raw_sum / len(entries)
    
    # Step 3: Apply conditional amplification
    amplified_total = 0
    for e in entries:
        contribution = e['value']
        if e['flag'] == 'CRIT' or e['value'] > config['warning']:
            contribution *= config['amplification_factor']
        amplified_total += contribution
    
    # Step 4: Normalize by critical event count
    critical_events = len([e for e in entries if e['flag'] == 'CRIT'])
    normalization_factor = critical_events + 1  # avoid division by zero
    normalized_score = amplified_total / normalization_factor
    
    # Step 5: Adjust using stability index (actual dependency)
    stability = compute_stability_index(entries, config)
    
    # Step 6: Final diagnostic synthesis
    severity_bias = 0
    if critical_events >= 2:
        severity_bias = 25
    elif critical_events == 1:
        severity_bias = 10
    
    # Step 7: Apply bitwise mask based on timestamp parity (subtle but relevant)
    timestamp_xor = 0
    for ts in timestamps:
        if ts % 2 == 1:
            timestamp_xor ^= (ts % 100)
    
    # Step 8: Final composition
    raw_diagnostic = (normalized_score + stability + severity_bias)
    final_shift = timestamp_xor & 7  # Use only last 3 bits
    final_diagnostic = int(raw_diagnostic) >> final_shift
    
    return final_diagnostic

# Execute main processing
interim_result = compute_stability_index(log_entries, system_thresholds)
baseline_check = get_historical_baseline()  # Dead call (distractor)
dummy_usage = analyze_trend(raw_readings)  # Another red herring

final_diagnostic = process_metrics(log_entries, system_thresholds)

print(f"Result: {final_diagnostic}")
import math

# Simulated system telemetry and health monitoring with distractors
def analyze_signal_strength(signal):
    if signal < 0:
        return 0
    return int(math.log(signal + 1) * 10)

# Irrelevant helper - decoy function (never called in execution path)
def legacy_checksum(data):
    return sum([d % 256 for d in data]) ^ 0xFF

# Unused transformation map (red herring)
symbol_map = {i: chr(65 + (i % 26)) for i in range(50)}

# Core processing pipeline
log_entries = [
    {'timestamp': 1623456780, 'power': 230.5, 'load': 0.78, 'errors': 3},
    {'timestamp': 1623456781, 'power': 231.0, 'load': 0.82, 'errors': 2},
    {'timestamp': 1623456782, 'power': 229.8, 'load': 0.91, 'errors': 5},
    {'timestamp': 1623456783, 'power': 233.1, 'load': 0.67, 'errors': 1},
    {'timestamp': 1623456784, 'power': 230.9, 'load': 0.74, 'errors': 0}
]

# System thresholds (mixed relevant and irrelevant keys)
system_thresholds = {
    'critical_load': 0.9,
    'max_errors': 4,
    'min_power': 220.0,
    'overclock_limit': 350.0,  # unused
    'voltage_risk': 240.0       # unused
}

# Decoy statistical summary (never used)
basic_stats = {
    'avg_power': sum(e['power'] for e in log_entries) / len(log_entries),
    'total_errors': sum(e['errors'] for e in log_entries),
    'peak_load': max(e['load'] for e in log_entries)
}

# Higher-order function factory (partially used)
def make_filter(threshold_key):
    return lambda entry: entry['load'] > system_thresholds.get(threshold_key, 1.0)

# Create filter but don't immediately use it
load_filter = make_filter('critical_load')

# List of pending diagnostics (some never processed)
pending_diagnostics = set()
for entry in log_entries:
    if entry['errors'] > system_thresholds['max_errors']:
        pending_diagnostics.add(entry['timestamp'])

# Unused signal array (misleading intermediate)
signal_array = [analyze_signal_strength(e['power'] - 200) for e in log_entries]

# Real-time sorter (dead code path)
sorted_by_time = sorted(log_entries, key=lambda x: x['timestamp'], reverse=True)

# Main aggregation logic — this is where real computation happens
def count_high_load_periods(entries, threshold):
    count = 0
    consecutive = 0
    for e in entries:
        if e['load'] > threshold:
            consecutive += 1
        else:
            if consecutive >= 2:
                count += 1
            consecutive = 0
    if consecutive >= 2:  # Final sequence check
        count += 1
    return count

# Diagnostic scoring with lambda weighting
weight_function = lambda x: 1.5 if x > 0.8 else 1.0

# Secondary metric: weighted error density
weighted_error_score = 0
for entry in log_entries:
    weight = weight_function(entry['load'])
    weighted_error_score += entry['errors'] * weight

# Distractor: complex dictionary comprehension with no impact
summary_grid = {
    f"entry_{i}_{ts['timestamp'] % 1000}": {
        'risk': 'high' if ts['load'] > 0.85 else 'normal',
        'flagged': ts['errors'] > 2
    }
    for i, ts in enumerate(log_entries)
}

# Real processing function that combines multiple concepts
def process_metrics(entries, thresholds):
    # Step 1: Count sustained high-load periods (>=2 consecutive above threshold)
    high_load_bursts = count_high_load_periods(entries, thresholds['critical_load'])
    
    # Step 2: Check if any entry exceeded error threshold
    error_violations = sum(1 for e in entries if e['errors'] > thresholds['max_errors'])
    
    # Step 3: Calculate composite risk score
    base_score = high_load_bursts * 17
    penalty = error_violations * 23
    adjustment = int(weighted_error_score // 2)
    
    # Step 4: Apply conditional multiplier based on power stability
    power_stable = all(
        abs(entries[i]['power'] - entries[i-1]['power']) < 5.0
        for i in range(1, len(entries))
    )
    multiplier = 2 if not power_stable else 1
    
    # Step 5: Final diagnostic calculation
    result = (base_score + penalty + adjustment) * multiplier
    
    # Step 6: Additional check that doesn't alter result but looks important
    if result > 100:
        result -= 5  # Compensate for overestimation (actually makes it less accurate)
    
    return result

# Execute main logic
final_diagnostic = process_metrics(log_entries, system_thresholds)

# Print result as required
print(f"Target result: {final_diagnostic}")
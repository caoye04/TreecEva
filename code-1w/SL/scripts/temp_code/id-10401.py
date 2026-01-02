import math

def analyze_signal(data, threshold=0.75):
    # Irrelevant signal processing function (dead code path)
    return [x for x in data if abs(x) > threshold]

# Simulated sensor log entries with timestamped metrics
timestamps = list(range(1000, 2000, 10))
raw_values = [math.sin(t * 0.003) + 0.5 * math.cos(t * 0.007) for t in timestamps]
error_flags = [i % 97 == 0 for i in range(len(raw_values))]

log_entries = [
    {
        'ts': timestamps[i],
        'val': round(raw_values[i], 4),
        'err': error_flags[i],
        'meta': hex(timestamps[i] % 256)
    }
    for i in range(len(timestamps))
]

# System state with multiple health indicators
system_state = {
    'core_temp': 67.3,
    'fan_speed_rpm': 2400,
    'voltage_stable': True,
    'packet_loss': 0.002,
    'uptime_hours': 127,
    'maintenance_due': False
}

# Decoy diagnostic function that is never called
def assess_integrity(logs):
    critical_count = sum(1 for e in logs if e['val'] > 0.9 and e['err'])
    return critical_count > 5

# Auxiliary transformation: normalize values using lambda
group_key = lambda x: 'high' if x > 0.5 else 'low'
val_categories = {k: [] for k in ['high', 'low']}
for entry in log_entries:
    key = group_key(entry['val'])
    val_categories[key].append(entry['val'])

# Misleading statistical summary (unused later)
avg_high = sum(val_categories['high']) / len(val_categories['high']) if val_categories['high'] else 0
spurious_score = int(avg_high * 100) ^ 12345  # Bitwise red herring

# Conditional expression to compute filtered metric
base_reference = system_state['core_temp'] / 100.0
filter_threshold = base_reference if system_state['voltage_stable'] else 0.5

# Real processing begins here
filtered_vals = [
    entry['val'] for entry in log_entries 
    if not entry['err'] and entry['val'] >= filter_threshold
]

# Complex dictionary aggregation with conditional logic
stats_summary = {}
for v in filtered_vals:
    rounded = round(v, 2)
    stats_summary[rounded] = stats_summary.get(rounded, 0) + 1

# Secondary filtering based on frequency
frequent_readings = {k: v for k, v in stats_summary.items() if v > 2}

# Compute entropy-like measure from frequent readings
total_frequent = sum(frequent_readings.values())
entropy = 0.0
for count in frequent_readings.values():
    p = count / total_frequent
    entropy -= p * math.log(p)

# Dummy shift operation with no effect (bit manipulation distractor)
shifted_entropy = int(entropy * 1000) << 2 >> 2  # No change

# Main processing function used in final step
def process_metrics(logs, state):
    # Extract subset of non-error values above dynamic threshold
    dynamic_floor = 0.4 + (state['uptime_hours'] % 10) * 0.01
    valid_points = [e['val'] for e in logs if not e['err'] and e['val'] > dynamic_floor]
    
    # Unused intermediate calculation (misleading)
    peak_magnitude = max(valid_points) if valid_points else 0
    normalized_energy = sum(v**2 for v in valid_points) / len(valid_points) if valid_points else 0
    
    # Actual logic: count how many times consecutive pairs cross 0.65 upward
    crossings = 0
    for i in range(1, len(valid_points)):
        if valid_points[i-1] <= 0.65 < valid_points[i]:
            crossings += 1
    
    # Apply conditional multiplier based on system state
    multiplier = 3 if state['fan_speed_rpm'] > 2000 else 2
    adjustment = -5 if state['packet_loss'] > 0.001 else 0
    
    # Final diagnostic score computation
    raw_diagnostic = crossings * multiplier + adjustment
    
    # Additional obfuscation via dictionary mapping
    level_map = {'low': 10, 'med': 25, 'high': 40}
    load_level = 'high' if raw_diagnostic > 30 else 'med' if raw_diagnostic > 15 else 'low'
    final_component = level_map[load_level]
    
    return raw_diagnostic + final_component

# Dead code: unused analysis branch
if system_state['maintenance_due']:
    fallback_result = analyze_signal(raw_values)
    backup_diagnostic = len(fallback_result)

# Key execution point
final_diagnostic = process_metrics(log_entries, system_state)

# Output result
print(f"Result: {final_diagnostic}")
from collections import defaultdict
import math

# Simulated telemetry data from distributed sensors
telemetry_streams = {
    'node_01': [14, 17, 23, 15, 19],
    'node_02': [8,  11, 13, 16, 20],
    'node_03': [25, 31, 28, 24, 27],
    'node_04': [5,  9,  12, 14, 10]
}

# Irrelevant baseline reference (red herring)
baseline_norms = [10, 12, 15, 18, 20]

# System thresholds for anomaly detection (MUST use)
system_thresholds = {
    'warning': 16,
    'critical': 25
}

# Decoy function – looks important but unused in main logic
def calculate_baseline_stress(data):
    return sum(x ** 0.5 for x in data if x > 10) / len(data)

# Real processing pipeline
log_data = []
for node, readings in telemetry_streams.items():
    # Extract rolling window stats
    avg = sum(readings) / len(readings)
    peak = max(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    normalized_peak = math.log(peak) * 2.1 if peak > 0 else 0
    
    # Attach metadata flags
    flags = []
    if peak > system_thresholds['critical']:
        flags.append('CRIT')
    elif peak > system_thresholds['warning']:
        flags.append('WARN')
    
    # Append structured entry
    log_data.append({
        'id': node,
        'avg': round(avg, 2),
        'peak': peak,
        'variance': round(variance, 2),
        'norm_peak': round(normalized_peak, 2),
        'flags': flags
    })

# Distractor: unused transformation map (dead code path)
transformation_map = {i: (i * i) % 7 for i in range(1, 11)}

# Real processing function using lambda and list comprehension
def process_metrics(entries, thresholds):
    # Extract all normalized peaks above warning level
    high_activity = list(filter(lambda e: e['norm_peak'] > 6.0, entries))
    
    # Compute composite score from qualifying nodes
    scores = [e['avg'] * 1.5 + e['variance'] * 0.8 for e in high_activity]
    
    # Aggregate with conditional offset
    base_score = sum(scores)
    adjustment = len(high_activity) * 2.5 if any('CRIT' in e['flags'] for e in entries) else -3.7
    
    # Apply non-linear scaling
    if base_score > 50:
        adjusted = base_score * 0.9 + adjustment
    else:
        adjusted = base_score + adjustment * 1.2
    
    # Final diagnostic is integer-truncated result
    final_value = int(adjusted)
    
    # Distractor: irrelevant secondary metric
    phantom_metric = sum(1 for e in entries if e['avg'] > 15 and e['variance'] < 10)
    
    return final_value

# Key execution point
final_diagnostic = process_metrics(log_data, system_thresholds)

# Print result as required
print(f"Result: {final_diagnostic}")
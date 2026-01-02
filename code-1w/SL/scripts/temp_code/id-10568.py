from collections import defaultdict, Counter
import math

# Simulated system log analysis with diagnostic scoring

def preprocess_logs(raw_logs):
    processed = []
    for entry in raw_logs:
        timestamp, code, severity = entry
        if severity > 3:
            processed.append((timestamp % 86400, code))
    return processed

# Irrelevant helper - distractor function (dead path)
def deprecated_checksum(data):
    acc = 0
    for d in data:
        acc = (acc * 31 + d) % 10007
    return acc  # Never used in main logic

# Decoy statistical analyzer (misleading intermediate result)
def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Core pattern detection logic
def detect_anomaly_sequences(entries):
    sequences = defaultdict(list)
    for time, code in entries:
        sequences[code].append(time)
    
    anomalies = []
    for code, times in sequences.items():
        if len(times) >= 3:
            diffs = [times[i+1] - times[i] for i in range(len(times)-1)]
            if all(d < 300 for d in diffs):  # Frequent bursts under 5 min
                anomalies.append(code)
    return sorted(anomalies)

# Misdirection: Hardware health monitor (unused)
def evaluate_hardware_health(sensor_data):
    thermal_load = sum(s[1] for s in sensor_data if s[0] == 'CPU')
    fan_rpm = max(s[2] for s in sensor_data)
    return thermal_load > 200 and fan_rpm > 5000

# Real target function with multiple concepts
system_thresholds = defaultdict(lambda: 100)
system_thresholds.update({501: 80, 502: 120, 503: 95})

legacy_mappings = {101: 'A', 102: 'B', 103: 'C'}  # Unused mapping table

log_data = [
    (1200, 501, 4), (1230, 502, 5), (1245, 501, 4),
    (2400, 503, 5), (2415, 501, 5), (2430, 503, 4),
    (3600, 501, 5), (3610, 501, 5), (3615, 501, 5),  # Burst sequence
    (7200, 502, 4), (7230, 502, 4), (7260, 502, 4),  # Another burst
    (8000, 503, 3), (8050, 501, 4)
]

sensor_readings = [('CPU', 75, 4500), ('GPU', 68, 3200), ('CPU', 80, 4800)]  # Distractor dataset

# Flag dictionary with red herring keys
flags = {
    'debug_mode': False,
    'cache_enabled': True,
    'strict_validation': None,
    'anomaly_tracking': True,
    'experimental_parser': 'disabled'
}

# Main analysis pipeline
processed_logs = preprocess_logs(log_data)

# Compute entropy for distraction (no impact on final result)
entropy_value = compute_entropy([t for t, c in processed_logs])
decoy_score = deprecated_checksum([c for t, c in processed_logs])

# Actual critical logic path
anomalous_codes = detect_anomaly_sequences(processed_logs)

# Complex aggregation with dictionary operations
impact_scores = {}
for code in anomalous_codes:
    base_score = system_thresholds[code]
    occurrence_count = len([c for t, c in processed_logs if c == code])
    temporal_weight = 1.0 + (0.1 * (occurrence_count - 3))
    impact_scores[code] = round(base_score * temporal_weight)

# Secondary transformation
aggregated_impact = 0
for code, score in impact_scores.items():
    if code % 2 == 1:  # Only odd codes contribute
        aggregated_impact += score * 2
    else:
        aggregated_impact += score

# Final diagnostic computation (key statement)
def analyze_pattern(log_entries, system_flags):
    temp_cache = {}  # Local cache (distraction)
    for item in log_entries:
        key = item[1] % 10
        if key not in temp_cache:
            temp_cache[key] = 0
        temp_cache[key] += 1
    
    # Real calculation
    primary_codes = [c for t, c in log_entries]
    mode_code = Counter(primary_codes).most_common(1)[0][0]
    mode_frequency = Counter(primary_codes).most_common(1)[0][1]
    
    base_diagnostic = aggregated_impact  # Pulls from outer scope
    frequency_bonus = mode_frequency * 10 if mode_code in anomalous_codes else 0
    debug_adjustment = -5 if system_flags['debug_mode'] else 10
    
    return base_diagnostic + frequency_bonus + debug_adjustment

# Execution point of interest
final_diagnostic = analyze_pattern(log_entries=processed_logs, system_flags=flags)

print(f"Result: {final_diagnostic}")
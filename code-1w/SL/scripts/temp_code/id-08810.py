def analyze_system_load(performance_data, config_params):
    base_score = sum([x['cpu'] * 0.6 + x['mem'] * 0.4 for x in performance_data]) / len(performance_data)
    adjustment_factor = config_params.get('adaptive', False)
    if adjustment_factor:
        base_score *= 1.15
    return base_score

system_flags = {'debug': True, 'verbose': False, 'legacy_mode': False}

log_entries = [
    {'timestamp': '2023-05-01T10:00:00Z', 'cpu': 78, 'mem': 85, 'disk_io': 40},
    {'timestamp': '2023-05-01T10:01:00Z', 'cpu': 85, 'mem': 70, 'disk_io': 60},
    {'timestamp': '2023-05-01T10:02:00Z', 'cpu': 90, 'mem': 92, 'disk_io': 75},
    {'timestamp': '2023-05-01T10:03:00Z', 'cpu': 65, 'mem': 80, 'disk_io': 50}
]

# Irrelevant string processing (distractor)
def validate_logs(logs):
    valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789:-TZ')
    for entry in logs:
        ts = entry['timestamp']
        if not all(c in valid_chars for c in ts):
            return False
    return True

is_valid = validate_logs(log_entries)

# Unused helper function (dead code path)
def deprecated_normalization(data_list):
    mean_val = sum(data_list) / len(data_list)
    normalized = [(x - mean_val) / mean_val for x in data_list]
    return [round(x, 2) for x in normalized]

# Decoy metrics calculation (misleading intermediate result)
temp_analysis = [x['cpu'] * x['mem'] // 100 for x in log_entries]
avg_product_metric = sum(temp_analysis) // len(temp_analysis)

config_settings = {
    'thresholds': {'critical': 85, 'warning': 70},
    'adaptive': True,
    'sampling_interval': 60
}

# Real processing begins here
system_thresholds = config_settings['thresholds']

# Extract and filter high-load entries
critical_count = 0
for record in log_entries:
    if record['cpu'] > system_thresholds['critical'] or record['mem'] > system_thresholds['critical']:
        critical_count += 1

# Bit manipulation red herring (irrelevant)
status_word = 0b110101
masked_status = status_word & 0b1111
shifted_status = masked_status << 2

# Enumerate and zip usage (required Python feature)
timestamp_parts = [entry['timestamp'].split('T')[1].split(':')[0] for entry in log_entries]
hourly_counts = {}
for hour in timestamp_parts:
    hourly_counts[hour] = hourly_counts.get(hour, 0) + 1

hours = list(hourly_counts.keys())
indices = list(range(len(hours)))
indexed_hours = list(zip(indices, hours))

# Lambda-based transformation (required Python feature)
score_mapper = lambda x: round(0.7 * x['cpu'] + 0.3 * x['mem'], 1)
raw_scores = [score_mapper(entry) for entry in log_entries]

# Conditional expression with distractor logic
baseline_ref = 75 if system_flags['legacy_mode'] else 68
adjusted_scores = [s * 1.05 if s > baseline_ref else s for s in raw_scores]

# Accumulation with filtered conditions
high_risk_sum = 0
for score in adjusted_scores:
    if score > 80:
        high_risk_sum += score

# Destructuring assignment (relevant concept)
first_score, *remaining_scores = adjusted_scores

# Another decoy: min/max/average distraction
min_score = min(adjusted_scores)
max_score = max(adjusted_scores)
avg_score = sum(adjusted_scores) / len(adjusted_scores)
median_score = sorted(adjusted_scores)[len(adjusted_scores)//2]

# Core logic embedded within distractions
def process_metrics(entries, thresholds):
    load_profile = []
    for e in entries:
        severity = 0
        if e['cpu'] > thresholds['critical']:
            severity += 2
        elif e['cpu'] > thresholds['warning']:
            severity += 1
        if e['mem'] > thresholds['critical']:
            severity += 2
        elif e['mem'] > thresholds['warning']:
            severity += 1
        load_profile.append(severity)
    
    # Weighted accumulation over time
    weighted_risk = 0
    for i, risk in enumerate(load_profile):
        decay_factor = 0.9 ** i  # More recent entries weigh more
        weighted_risk += risk * decay_factor
    
    # Final transformation
    final_value = int(weighted_risk * 100) % 999
    
    # Additional conditional twist
    if critical_count > 2:
        final_value += 50
    
    return final_value

# Key execution point
final_diagnostic = process_metrics(log_entries, system_thresholds)

# Print result as required
print(f"Target result: {final_diagnostic}")
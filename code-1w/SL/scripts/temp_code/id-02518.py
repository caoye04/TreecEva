from collections import defaultdict, Counter

# Simulated system telemetry data
timestamps = [1623456780, 1623456789, 1623456795, 1623456801, 1623456810]
raw_logs = [
    'ERROR: disk_usage > 90%',
    'INFO: cpu_temp=75',
    'WARNING: disk_usage > 85%',
    'ERROR: network_latency > 200',
    'ERROR: disk_usage > 92%'
]

# Irrelevant auxiliary mapping (distractor)
status_codes = {'OK': 200, 'WARN': 400, 'ERR': 500, 'INFO': 201}
code_lookup = {v: k for k, v in status_codes.items()}

# System thresholds and weights (some values are decoys)
system_thresholds = {
    'disk_usage': 88,
    'cpu_temp': 80,
    'network_latency': 150,
    'memory_swap': 10,
    'power_draw': 250  # Unused in logic
}

# Misleading preprocessing (not used in final calculation)
normalized_codes = [len(x.split(':')) for x in raw_logs]
dummy_analysis = sum(normalized_codes) * 0.5

# Core log parser (relevant)
def parse_log_entry(entry):
    if 'ERROR' in entry:
        key = entry.split(':')[2].strip().split('=')[0].split('>')[-1].strip()
        try:
            return ('ERROR', float(key))
        except:
            return ('ERROR', key)
    elif 'WARNING' in entry:
        key = entry.split('>')[1].strip()
        return ('WARNING', float(key))
    return ('INFO', 0)

# Secondary function with red herring logic
def assess_stability(events):
    stability_score = 0
    for t in events:
        if t < 1623456800:
            stability_score += 10
        else:
            stability_score -= 5  # Distractor path
    return stability_score  # Never used

# Main processing with actual logic
def process_metrics(logs, thresholds):
    error_count = defaultdict(int)
    severity_weight = {'ERROR': 3, 'WARNING': 2, 'INFO': 0}
    metric_violations = []

    # Real parsing loop
    for log in logs:
        level, value = parse_log_entry(log)
        error_count[level] += 1

        # Determine which threshold was crossed
        if level == 'ERROR' and isinstance(value, str):
            if 'disk_usage' in log:
                metric_violations.append('disk_usage')
            elif 'network_latency' in log:
                metric_violations.append('network_latency')

    # Decoy statistical transform (unused)
    stats_snapshot = {
        'mean_error_level': sum(severity_weight[l] for l, _ in [parse_log_entry(log) for log in logs]) / len(logs),
        'peak_severity': max(severity_weight[l] for l, _ in [parse_log_entry(log) for log in logs])
    }

    # Actual diagnostic logic
    violation_counter = Counter(metric_violations)
    critical_failures = 0
    for metric, count in violation_counter.items():
        if thresholds.get(metric, 1000) > 0:  # All defined metrics pass
            baseline = thresholds[metric]
            # Only disk_usage above 90 triggers critical
            if metric == 'disk_usage' and count >= 2:
                critical_failures += count * 2

    # Hidden XOR-based obfuscation of final result
    temp_key = 0
    for i, ts in enumerate(timestamps):
        temp_key ^= (ts % 100) & i  # Bitwise red herring
    
    # Final computation (only this matters)
    base_score = error_count['ERROR'] * 100
    adjustment = violation_counter['disk_usage'] * 15
    final_diagnostic = base_score + adjustment - (critical_failures * 5)

    # Dead code branch (never reached)
    if final_diagnostic < 0:
        final_diagnostic = abs(final_diagnostic) ^ 999
    
    return final_diagnostic

# Orchestration block
log_entries = raw_logs  # Alias for semantic clarity

# Spurious enumeration usage (distractor)
enumerated_diagnostics = []
for idx, log in enumerate(log_entries):
    if 'disk' in log:
        enumerated_diagnostics.append((idx, len(log)))

# Actual execution point
final_diagnostic = process_metrics(log_entries, system_thresholds)

# Additional irrelevant transformation
zipped_data = list(zip(timestamps, normalized_codes, [x//100 for x in timestamps]))
lambda_filter = lambda x: x[0] > 1623456800
filtered_zipped = [x for x in zipped_data if lambda_filter(x)]

print(f"Result: {final_diagnostic}")
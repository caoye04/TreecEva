import math

# Simulated system telemetry data with mixed signal types
def generate_signals(duration):
    return [abs(math.sin(t * 0.1)) + (t % 7 == 0) * 0.5 for t in range(duration)]

# Irrelevant auxiliary function – dead code path (distractor)
def analyze_bandwidth(peaks):
    if len(peaks) > 10:
        return sum([p * 0.9 for p in peaks]) // len(peaks)
    return 0

# Signal filtering using lambda abstraction (relevant)
filter_noisy = lambda x: round(x * 100) / 100 if x > 0.1 else 0

# Simulate log entries with timestamped events and diagnostic codes
def build_logs(signals):
    logs = []
    for i, sig in enumerate(signals):
        code = 200 if sig > 0.5 else (404 if i % 11 == 0 else 500)
        logs.append({'time': i, 'value': sig, 'status': code})
    return logs

# Misleading transformation – appears useful but unused in final path (distractor)
def extract_errors(logs):
    errors = []
    for entry in logs:
        if entry['status'] != 200:
            errors.append(entry['time'])
    temp_result = [e ** 2 for e in errors if e % 3 != 0]
    return sorted(temp_result, reverse=True)

# Core metric processor with string-based tagging (relevant)
def tag_severity(val, thresh):
    return 'CRITICAL' if val >= thresh else 'STABLE'

# Main processing pipeline
system_threshold = 0.67
raw_signals = generate_signals(150)
filtered_values = [filter_noisy(v) for v in raw_signals]

# Construct diagnostic log entries
log_entries = build_logs(filtered_values)

# Dead-end computation – looks important but not used (distractor)
peak_moments = [i for i, v in enumerate(filtered_values) if v > 0.75]
system_baseline = sum(filtered_values) / len(filtered_values)
anomaly_report = analyze_bandwidth(peak_moments)  # Unused result

# String manipulation layer: encode state history (relevant)
state_sequence = ''.join([str(int(entry['status'] == 200)) for entry in log_entries])
segmented = state_sequence.split('0')
valid_segments = [seg for seg in segmented if len(seg) >= 3]

# Conditional branching with nested logic (relevant)
def process_metrics(logs, threshold):
    count_critical = 0
    total_diagnostic = 0.0
    
    # Secondary filter using string method (relevant)
    recent_tags = []
    for entry in logs:
        severity_label = tag_severity(entry['value'], threshold)
        recent_tags.append(severity_label.lower().replace('_', ''))
        
        if 'crit' in severity_label.lower():
            count_critical += 1
            total_diagnostic += entry['value'] * 1.5
        elif entry['status'] == 404:
            total_diagnostic -= 0.1  # Minor penalty
    
    # Nested conditional with decoy arithmetic
    adjustment_factor = 0.0
    if count_critical > 10:
        adjustment_factor = 1.2
    elif count_critical > 5:
        adjustment_factor = 0.8
    else:
        adjustment_factor = 0.5  # Distractor branch – not taken

    # Complex data transformation with tuple unpacking (relevant)
    summary_stats = (count_critical, len(logs), total_diagnostic)
    critical_count, total_count, raw_score = summary_stats
    
    # Final computation path
    stability_index = (total_count - critical_count) / total_count
    weighted_metric = raw_score * adjustment_factor
    
    # Key red herring: complex-looking but irrelevant bit manipulation
    decoy_key = 0b110101
    for x in peak_moments[:5]:
        decoy_key ^= (x << 2) & 0xFF
    final_decoy = decoy_key % 89  # Looks important, not used
    
    # Actual answer derivation
    if stability_index < 0.7:
        final_diagnostic = int(weighted_metric * 100) + 333
    else:
        final_diagnostic = int(weighted_metric * 85) + 111  # Not reached
    
    return final_diagnostic

# Execute main logic
final_diagnostic = process_metrics(log_entries, system_threshold)
print(f"Result: {final_diagnostic}")
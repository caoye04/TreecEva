import math

def analyze_response_time(rt):
    if rt < 0.1:
        return 'optimal'
    elif rt < 0.5:
        return 'acceptable'
    else:
        return 'critical'

# Simulated system timing log with timestamps in seconds
timing_log = [0.05, 0.12, 0.33, 0.08, 0.67, 0.44, 0.03, 0.51]

# Irrelevant auxiliary function for network prediction (dead code path)
def predict_bandwidth_usage(peaks):
    projected = 0
    for p in peaks:
        projected += math.log(p + 1) * 1.5
    return round(projected, 2)

# Historical failure codes from legacy modules (some are decoys)
failure_codes = {101, 205, 303, 404, 505, 606}
debug_mode = True
baseline_offset = 0.25

# Filter actual runtime failures based on timing and known codes
runtime_failures = [t for t in timing_log if t > 0.5]
failure_set = set()
for rt in runtime_failures:
    if rt > 0.5:
        failure_set.add(int(rt * 1000) % 999)  # generate artificial error codes

# Simulate partial health check (misleading intermediate computation)
current_load = sum(timing_log) / len(timing_log)
health_score = 100 - (current_load * 100)
system_status = 'stable' if health_score > 60 else 'unstable'

# Unused transformation - red herring list comprehension
efficiency_ratios = [round((0.5 - t) / 0.5, 3) for t in timing_log if t < 0.5]
warning_flags = [analyze_response_time(t) for t in timing_log]

# Decoy data structure - complex but unused
diagnostic_trace = {
    'version': '2.1',
    'nodes': [
        {'id': 'A1', 'load': 0.12, 'state': 'active'},
        {'id': 'B2', 'load': 0.67, 'state': 'throttled'},
        {'id': 'C3', 'load': 0.03, 'state': 'idle'}
    ],
    'checksum': 0,
    'flags': warning_flags
}

# Compute rolling average (distractor calculation)
window_size = 3
rolling_avg = []
for i in range(len(timing_log) - window_size + 1):
    window = timing_log[i:i+window_size]
    rolling_avg.append(sum(window) / window_size)

# Core diagnostic aggregation logic
system_health = {
    'response_classes': {},
    'peak_delay': max(timing_log),
    'fail_count': len(failure_set),
    'timestamp_count': len(timing_log)
}

# Categorize response times (relevant list comprehension)
for category in ['optimal', 'acceptable', 'critical']:
    system_health['response_classes'][category] = len([t for t in timing_log if analyze_response_time(t) == category])

# Spurious bit manipulation (red herring)
encoded_signature = 0
for code in failure_codes:
    encoded_signature ^= (code << 2) | (code >> 2)

# Auxiliary function to compute diagnostic metric
def aggregate_metrics(times, failures, health_map):
    base = len(times) * 10
    penalty = len(failures) * 100
    critical_load = health_map['response_classes']['critical'] * 50
    # Hidden adjustment: count characters in status word
    status_char_bonus = len(system_status) * 10
    # Secret modifier: sum of ASCII values of 'version' string
    version_ascii_sum = sum([ord(c) for c in diagnostic_trace['version']])
    # Final formula combines multiple concepts
    result = base - penalty + critical_load + status_char_bonus
    # Ignore version_ascii_sum — it's a decoy!
    return int(result)

# Execute main computation
final_diagnostic = aggregate_metrics(timing_log, failure_set, system_health)

# Output result
print(f"Result: {final_diagnostic}")
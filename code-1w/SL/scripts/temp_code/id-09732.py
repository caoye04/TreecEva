import math

def analyze_response_time(raw_samples, threshold):
    filtered = [x for x in raw_samples if x > 0]
    normalized = [math.log(x) if x >= 1 else 0 for x in filtered]
    above_threshold = sum(1 for x in normalized if x > threshold)
    return above_threshold

def update_cache_state(config_map, force_reset=False):
    cache_status = {}
    for k, v in config_map.items():
        if 'timeout' in k:
            cache_status[k] = v * 2 if not force_reset else 0
    # Irrelevant transformation
    temp_debug = {k: len(str(v)) for k, v in config_map.items()}
    return cache_status

def evaluate_consistency(pattern_trace, mode='strict'):
    if mode == 'strict':
        return sum(pattern_trace) // len(pattern_trace) if pattern_trace else 0
    else:
        return max(pattern_trace, default=0)

def aggregate_metrics(log_entries, flags):
    timing_data = []
    flag_weights = {'FATAL': 5, 'ERROR': 3, 'WARN': 1, 'INFO': 0}
    base_score = 0
    
    # Real processing path
    for entry in log_entries:
        timestamp, duration, tag = entry
        if tag == 'DIAGNOSTIC' and duration > 0:
            timing_data.append(math.sqrt(duration) * 100)
    
    # Distractor: unused data path
    debug_analysis = [e[1] * 0.1 for e in log_entries if 'DEBUG' in e[2]]
    
    for f in flags:
        base_score += flag_weights.get(f, 0)
    
    consistency_check = [int(f[-1]) for f in flags if f.startswith('FLAG_')]
    adjustment = evaluate_consistency(consistency_check, mode='strict')
    
    # Key calculation
    raw_metric = sum(timing_data) + base_score * 1000
    final_diagnostic = int(raw_metric - adjustment * 50)
    
    # Dead code branch (never executed due to logic)
    if len(flags) > 100:
        fallback = update_cache_state({'timeout_retry': 5}, force_reset=True)
        final_diagnostic = -9999
    
    return final_diagnostic

# Simulated system inputs
system_profile = {
    'version': 'v2.4.1',
    'max_retries': 3,
    'timeout_retry': 4,
    'buffer_size': 8192
}

# Generate synthetic timing log with mixed tags
raw_timings = [0.25, 0.49, 0.64, 0.81, 1.0]
timing_log = []
for i, t in enumerate(raw_timings):
    tag = 'DIAGNOSTIC' if i % 2 == 0 else 'DEBUG_TRACE'
    timing_log.append((1000 + i, t, tag))

# Add some decoy entries
timing_log.append((1005, 0.0, 'DIAGNOSTIC'))  # Zero duration, should be skipped
timing_log.append((1006, 1.44, 'DIAGNOSTIC'))

# System flags with red herring patterns
system_flags = ['ERROR', 'WARN', 'FATAL', 'FLAG_3', 'FLAG_7', 'FLAG_5']

# Misleading pre-analysis (unused in final result)
preliminary_score = analyze_response_time([0.1, 0.5, 1.5, 2.0], 0.4)
dummy_cache = update_cache_state(system_profile)

# Critical execution point
final_diagnostic = aggregate_metrics(timing_log, system_flags)

# Print final target result
print(f"Result: {final_diagnostic}")
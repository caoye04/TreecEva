def analyze_system_load(timestamps, thresholds):
    accumulated = 0
    peak_load = max(thresholds)
    baseline = sum(thresholds) / len(thresholds)
    temp_cache = {i: t * 1.2 for i, t in enumerate(thresholds)}  # Irrelevant transformation

    for ts in timestamps:
        if ts % 7 == 0:
            accumulated += 3
        elif ts % 5 == 0:
            accumulated += 2
        else:
            accumulated += 1

    # Dead code path — never executed due to logic above
    redundant_calc = [x ** 0.5 for x in temp_cache.values() if x > 100]
    scaling_factor = len(redundant_calc) if redundant_calc else 0.85

    return int((accumulated * scaling_factor) // 1)


def validate_integrity(checkpoints):
    status_flags = []
    for cp in checkpoints:
        if cp < 0:
            status_flags.append(1)
        elif cp == 0:
            status_flags.append(0)
        else:
            status_flags.append(-1)
    
    # Distractor: complex-looking but unused structure
    flag_summary = {idx: {'raw': f, 'adjusted': f * -1} for idx, f in enumerate(status_flags)}
    correction_offset = sum(f['adjusted'] for f in flag_summary.values())  # Unused

    return sum(status_flags)


def aggregate_metrics(log_entries, system_diagnostics):
    timing_log = [entry[1] for entry in log_entries]
    event_types = [entry[0] for entry in log_entries]
    
    # Real computation starts here
    load_score = analyze_system_load(timing_log, system_diagnostics)
    integrity_score = validate_integrity(system_diagnostics)
    
    # Complex distractor: elaborate but irrelevant dictionary
    diagnostic_profile = {
        'meta': {
            'version': '3.2.1',
            'schema': [hex(i + 40) for i in range(5)],
            'active': True
        },
        'metrics': {
            'latency_peaks': [t for t in timing_log if t > 50],
            'event_distribution': {etype: event_types.count(etype) for etype in set(event_types)},
            'baseline_shift': (min(timing_log) + max(timing_log)) / 2
        }
    }
    
    # Actual answer computation buried among distractions
    adjustment = len(diagnostic_profile['metrics']['latency_peaks']) if diagnostic_profile['metrics']['latency_peaks'] else 1
    intermediate = (load_score + abs(integrity_score)) * adjustment
    
    # Final red herring: bitwise decoy with no impact
    decoy_mask = 0b110101
    masked_intermediate = intermediate ^ decoy_mask | 8
    
    final_diagnostic = masked_intermediate + 5  # This is the real result
    
    # More irrelevant prints and operations
    debug_snapshot = list(zip(event_types, timing_log, [intermediate % 3 for _ in timing_log]))
    cleanup = [d for d in debug_snapshot if d[2] != 0]
    
    return final_diagnostic

# Input data
timestamps = [12, 15, 21, 25, 28, 30, 35, 42, 45, 49]
event_codes = ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'A', 'B', 'A']
threshold_readings = [45, 52, 60, 58, 70, 40, 65]

log_data = list(zip(event_codes, timestamps))
diagnostics = threshold_readings

# Execution point
final_diagnostic = aggregate_metrics(log_data, diagnostics)
print(f"Result: {final_diagnostic}")
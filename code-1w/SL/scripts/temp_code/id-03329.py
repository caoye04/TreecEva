import itertools

# Simulated sensor data with noise and redundant metrics
def generate_diagnostics():
    raw_readings = [102, 95, 110, 88, 76, 94, 105]
    timestamps = ['t0', 't1', 't2', 't3', 't4', 't5', 't6']
    status_flags = [True, False, True, True, False, True, True]
    
    # Irrelevant transformation: creates decoy data
    shifted = [x - 90 for x in raw_readings]
    normalized = [round((x - min(raw_readings)) / (max(raw_readings) - min(raw_readings)), 3) for x in raw_readings]
    
    # Distractor dictionary with unused fields
    diagnostics = {
        'readings': raw_readings,
        'norm': normalized,
        'flags': status_flags,
        'timestamps': timestamps,
        'aux_data': list(itertools.accumulate(shifted)),
        'outlier_indices': [i for i, x in enumerate(raw_readings) if abs(x - 95) > 15],
        'decoy_metric_1': sum(normalized) * 0.1,
        'phantom_sum': sum([x*x for x in shifted if x < 0])
    }
    
    return diagnostics

# Auxiliary function – appears important but used minimally
def apply_calibration(data, factor=1.05):
    return [round(x * factor, 2) for x in data]

# Core evaluation logic with embedded distractions
def evaluate_performance(metrics, baseline):
    # Extract relevant time-series subset
    all_data = generate_diagnostics()
    signal = all_data['readings']
    
    # Real computation begins: analyze trend around baseline
    window_center = len(signal) // 2
    focus_window = signal[window_center-2:window_center+2]  # slicing operation
    
    # Compute deviations
    deviations = [abs(x - baseline) for x in focus_window]
    avg_dev = sum(deviations) / len(deviations)
    
    # Bit manipulation red herring
    magic_offset = (baseline << 1) ^ 15 & 7  # bitwise decoy
    
    # Logical scoring with short-circuit distraction
    high_alert = any(x > 100 for x in focus_window) and not (avg_dev < 5 or True and False)  # short-circuit trap
    adjustment = -8 if high_alert else 0
    
    # Accumulate across permutations (itertools usage - partial relevance)
    perms = list(itertools.permutations(focus_window[:2]))  # only uses first two
    perm_count_bonus = len(perms) * 2 if len(perms) > 2 else 0  # always 2! = 2 → bonus=0
    
    # Decoy counters
    counter_a = 0
    counter_b = 0
    for val in signal:
        if val > 100:
            counter_a += 1
        elif val < 90:
            counter_b += 1
        else:
            continue  # dead branch

    # Actual score calculation (non-obvious due to context)
    base_score = 100 - avg_dev
    calibrated_score = base_score + adjustment + perm_count_bonus
    final_score = int(calibrated_score)  # key assignment
    
    # Dead code path - never reached
    if False:
        fallback = apply_calibration([base_score], 0.9)
        final_score = int(sum(fallback))

    # Debug print that could mislead
    # print(f'Debug: counter_a={counter_a}, counter_b={counter_b}, magic_offset={magic_offset}')

    return final_score

# Entry point
metric_data = generate_diagnostics()['readings']
final_score = evaluate_performance(metric_data, baseline=75)
print(f"Result: {final_score}")
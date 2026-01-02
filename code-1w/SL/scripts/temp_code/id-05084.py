def analyze_timing_sequence(events):
    base_offset = 17
    calibration_factor = 3
    timing_log = []
    temp_cache = {}
    debug_trace = []

    for event in events:
        raw_tick = event['tick']
        phase_flag = event['phase']
        checksum = (raw_tick + base_offset) % 19

        if phase_flag == 'INIT':
            adjusted = (raw_tick * calibration_factor) % 100
            timing_log.append(adjusted)
            temp_cache[raw_tick] = adjusted
        elif phase_flag == 'RUN':
            shifted = (raw_tick >> 2) ^ 7
            if shifted % 2 == 0:
                timing_log.append(shifted * 2)
            else:
                timing_log.append(shifted + 3)
            debug_trace.append(f"RUN:{shifted}")
        elif phase_flag == 'IDLE':
            masked = raw_tick & 15
            inverted = (~masked) & 15
            timing_log.append(inverted)

    # Irrelevant aggregation (dead logic path)
    cumulative = 0
    history_snapshot = []
    for val in timing_log:
        cumulative += val
        history_snapshot.append(cumulative)

    # Distractor transformation
    mirror_slice = timing_log[::-1][:5]
    padding = [0] * (5 - len(mirror_slice))
    padded_mirror = mirror_slice + padding  # Unused

    return timing_log


def validate_system_integrity(flags):
    critical_keys = ['F0', 'F3', 'F6']
    flag_states = {}
    for key in critical_keys:
        flag_states[key] = flags.get(key, False)
    
    # Complex but irrelevant validation chain
    score = 0
    if flag_states['F0']:
        score += 10
    if not flag_states['F3'] and flag_states['F0']:
        score -= 5
    if flag_states['F6']:
        score *= 2
    else:
        score += 2

    # Another decoy structure
    audit_trail = []
    for k, v in flag_states.items():
        audit_trail.append(f"{k}:{'OK' if v else 'FAIL'}")

    # Actual required output
    active_count = sum(1 for v in flags.values() if v)
    return active_count


def compute_diagnostic_weight(log_data):
    total = 0
    weights = [1, -1, 2, -2, 3]
    
    # Use slicing with step to extract every second element
    sampled = log_data[::2]
    extended_sample = sampled + sampled[:3]  # Artificial extension

    for i, val in enumerate(extended_sample):
        factor = weights[i % len(weights)]
        total += val * factor

    # Dead computation branch
    if total > 100:
        secondary_sum = 0
        for x in extended_sample:
            secondary_sum += x ^ i
        total -= secondary_sum % 10

    return abs(total)


def aggregate_metrics(log, flags):
    base_metric = compute_diagnostic_weight(log)
    flag_count = validate_system_integrity(flags)
    
    # Key manipulation involving bitwise and modular arithmetic
    combined_seed = (base_metric ^ flag_count) % 23
    adjustment = 0

    interim_stack = []
    for i in range(5):
        computed = (combined_seed * i + 3) % 17
        interim_stack.append(computed)
        if i % 2 == 0:
            adjustment += computed

    # Real contribution
    final_diagnostic = base_metric + adjustment

    # Numerous unused variables and red herrings below
    snapshot = {
        'raw': log.copy(),
        'flags_active': flag_count,
        'checksums': [x % 7 for x in log],
        'meta': {'version': '2.1', 'mode': 'DIAG'}
    }

    # Distractor: complex nested list comprehension with no effect
    _ = [[x for x in range(j) if x % 2 == 0] for j in (interim_stack[-3:] or [1, 2])]

    # Final irrelevant transformation
    if final_diagnostic % 4 == 0:
        final_diagnostic -= 1

    return final_diagnostic

# Main execution
if __name__ == '__main__':
    event_stream = [
        {'tick': 25, 'phase': 'INIT'},
        {'tick': 14, 'phase': 'RUN'},
        {'tick': 8,  'phase': 'IDLE'},
        {'tick': 31, 'phase': 'INIT'},
        {'tick': 18, 'phase': 'RUN'},
        {'tick': 5,  'phase': 'IDLE'},
        {'tick': 42, 'phase': 'INIT'},
    ]

    system_flags = {
        'F0': True,
        'F1': False,
        'F2': True,
        'F3': False,
        'F4': True,
        'F5': False,
        'F6': True,
        'F7': False,
    }

    timing_log = analyze_timing_sequence(event_stream)
    final_diagnostic = aggregate_metrics(timing_log, system_flags)
    print(f"Target result: {final_diagnostic}")
import itertools

# Simulated system telemetry data with mixed signal types
def generate_signals():
    base_values = [1.1, 2.3, 3.7, 4.0, 5.9]
    signals = []
    for i, val in enumerate(base_values):
        # Irrelevant transformation (red herring)
        noise_offset = (i ** 2) % 3 * 0.1
        signals.append(val + noise_offset if i % 2 else val - noise_offset)
    return signals

# Legacy function – unused but looks important (dead code path)
def legacy_calibrate(x):
    return sum([v ** 0.5 for v in x]) / len(x)

# Signal smoothing using moving average (distractor computation)
def smooth_signal(signal, window=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window + 1)
        smoothed.append(sum(signal[start:i+1]) / (i - start + 1))
    return smoothed

# Misleading health score calculator (decoy metric)
def compute_health_score(entries):
    score = 0
    for entry in entries:
        if entry['status'] == 'OK':
            score += entry['value'] * 0.8
        elif entry['status'] == 'WARNING':
            score -= 10
        else:
            score -= 50
    return max(0, min(100, score))  # Clamped result – irrelevant to final answer

# Core logic disguised among distractions
def analyze_trend(data, threshold=4.5):
    count_above = 0
    cumulative = 0.0
    for val in data:
        if val > threshold:
            count_above += 1
            cumulative += val
    return cumulative if count_above >= 2 else -1 * cumulative

# Real processing chain (obscured by decoys)
def encode_flags(values):
    flags = 0
    for v in values:
        flags <<= 1
        flags |= (v > 3.5)
    return flags

def decode_flag_sequence(flag_code, length=5):
    sequence = []
    for _ in range(length):
        sequence.append(flag_code & 1)
        flag_code >>= 1
    return list(reversed(sequence))

def filter_critical_entries(entries):
    # Uses dictionary operations and conditional expressions
    return [
        {**entry, 'priority': 'HIGH' if entry['value'] > 4.0 else 'LOW'}
        for entry in entries if entry['status'] != 'IGNORE'
    ]

def sort_by_impact(entries):
    # Sorting by computed impact factor
    return sorted(
        entries,
        key=lambda x: (x['value'] * 2 if x['priority'] == 'HIGH' else x['value']),
        reverse=True
    )

def aggregate_diagnostics(entries, mode='strict'):
    total = 0
    multiplier = 1
    for entry in entries:
        if mode == 'strict' and entry['priority'] == 'LOW':
            continue
        impact = entry['value'] * multiplier
        total += int(impact)  # Truncate to integer for diagnostic signature
        multiplier += 1
    return total

# Main processing function
def process_metrics(log_data, threshold_config):
    # Step 1: Extract raw values (relevant)
    raw_values = [entry['value'] for entry in log_data]
    
    # Distractor: Smoothing that isn't used later
    smoothed = smooth_signal(raw_values)
    
    # Distractor: Health score computed but not used
    health_score = compute_health_score(log_data)
    
    # Step 2: Analyze trend above threshold (key step)
    trend_result = analyze_trend(raw_values, threshold=threshold_config)
    
    # Step 3: Encode bit pattern of threshold crossings (key step)
    flag_code = encode_flags(raw_values)
    flag_sequence = decode_flag_sequence(flag_code)
    
    # Step 4: Filter and prioritize entries (key filtering)
    filtered = filter_critical_entries(log_data)
    sorted_entries = sort_by_impact(filtered)
    
    # Step 5: Aggregate final diagnostic signature (critical)
    diagnostic_sum = aggregate_diagnostics(sorted_entries, mode='strict')
    
    # Step 6: Combine trend and diagnostic (final formula)
    # Only the sign of trend_result matters; magnitude folded into logic
    adjustment = 100 if trend_result > 0 else -100
    
    # Final interference: Use of itertools on a static set (looks complex, deterministic)
    permutations = list(itertools.permutations([diagnostic_sum % 10, 7, 3]))
    perm_offset = permutations[0][0] - permutations[-1][-1]  # Always same due to fixed input
    
    final_diagnostic = int(abs(trend_result)) + diagnostic_sum + adjustment + perm_offset
    
    return final_diagnostic

# Simulate input data
if __name__ == '__main__':
    log_entries = [
        {'value': 1.1, 'status': 'OK'},
        {'value': 2.3, 'status': 'WARNING'},
        {'value': 3.7, 'status': 'OK'},
        {'value': 4.0, 'status': 'OK'},
        {'value': 5.9, 'status': 'CRITICAL'},
        {'value': 2.1, 'status': 'IGNORE'},  # Will be filtered out
    ]
    
    system_threshold = 4.5
    
    # Irrelevant preprocessing (red herring)
    calibrated_signals = generate_signals()
    recalibrated = [x * 1.01 for x in calibrated_signals]
    
    final_diagnostic = process_metrics(log_entries, system_threshold)
    print(f"Target result: {final_diagnostic}")
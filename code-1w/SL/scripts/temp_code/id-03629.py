import itertools

# Simulated system telemetry data with mixed signal types
def fetch_telemetry_snapshot():
    raw_signals = [2.1, -1.5, 0.8, 4.3, -2.2, 3.7, 0.0, -0.9]
    filtered = [x for x in raw_signals if abs(x) > 0.5]
    normalized = list(map(lambda v: round(v * 0.9 + 0.1, 2), filtered))
    return normalized

# Legacy function – irrelevant but looks important
def legacy_calibrate_buffers():
    buffers = [0] * 16
    for i in range(len(buffers)):
        buffers[i] = (i * 7 + 3) % 13
    return sum(buffers)  # Dead end

# Misleading diagnostic that computes a plausible-looking metric
def compute_ghost_score(data):
    if not data:
        return 0
    peak = max(data)
    avg = sum(data) / len(data)
    return (peak * 1.5) - (avg * 0.8) + 10  # Looks useful, never used

# Core transformation pipeline
def transform_logs(signals):
    segments = []
    for i, val in enumerate(signals):
        segment_key = i % 3
        encoded = {
            'id': f"SEG-{i}",
            'val': val,
            'class': 'CRITICAL' if val > 2.0 else 'NORMAL',
            'meta': (i + 1) * 0.5
        }
        segments.append(encoded)
    
    # Real work happens here: extract and scale values
    extracted = [s['val'] for s in segments]
    scaled = [round(x * x, 2) for x in extracted]  # Square each value
    return segments, scaled

# Flag processing with bit manipulation red herring
def analyze_system_flags(raw_flag_str):
    # Irrelevant bitwise expansion
    expanded = []
    for c in raw_flag_str:
        bit_rep = ord(c) << 2 | 0x3
        expanded.append(bit_rep)
    
    # Actual relevant logic
    critical_present = 'ERR' in raw_flag_str
    timeout_seen = 'TO' in raw_flag_str
    return {
        'critical': critical_present,
        'timeout': timeout_seen,
        'code': hash(raw_flag_str) % 1000  # Unused field
    }

# Real aggregation logic — depends only on specific inputs
def aggregate_metrics(entries, flags):
    # Only uses entries' squared values and flag status
    valid_entries = [e for e in entries if e['class'] == 'CRITICAL']
    base_scores = [e['val'] for e in valid_entries]
    
    # Real computation path
    if flags['critical']:
        multiplier = 3
    elif flags['timeout']:
        multiplier = 2
    else:
        multiplier = 1
    
    total_power = sum(base_scores)
    adjustment = len(valid_entries) * 0.5
    result = (total_power * multiplier) - adjustment
    return round(result, 2)

# === MAIN EXECUTION WITH DISTRACTORS ===
if __name__ == "__main__":
    # Irrelevant initialization block
    init_cycle = [i for i in range(5)]
    checksum = sum([i**2 for i in init_cycle])
    
    # Fetch real data
    signal_data = fetch_telemetry_snapshot()
    
    # Transform logs — produces side product
    log_segments, processed_values = transform_logs(signal_data)
    
    # Compute ghost score — looks important, never used
    phantom_diagnostic = compute_ghost_score(processed_values)
    
    # Analyze flags — only two boolean fields matter
    system_flags = analyze_system_flags("ERR_TO_2024")
    
    # Legacy calibration — dead code path
    buffer_state = legacy_calibrate_buffers()  # Value unused
    
    # Key statement
    final_diagnostic = aggregate_metrics(log_segments, system_flags)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")
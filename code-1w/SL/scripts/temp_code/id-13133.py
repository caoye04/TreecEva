def analyze_sensor_data(raw_stream):
    # Irrelevant preprocessing block (distractor)
    normalized = [x * 0.98 for x in raw_stream if x > 0]
    filtered = [y for y in normalized if y < 500]
    snapshot = sum(filtered) / len(filtered) if filtered else 0

    # Decoy statistical analysis (dead path)
    mean_val = sum(normalized) / len(normalized) if normalized else 0
    variance = sum((x - mean_val) ** 2 for x in normalized) / len(normalized) if normalized else 0
    z_scores = [abs(x - mean_val) / (variance ** 0.5) for x in normalized] if variance > 0 else []

    # Real computation begins: parse control string
    control_signal = 'CALIBRATE|OFFSET=73|MODE=DIAG'
    tokens = control_signal.split('|')
    offset_str = [t for t in tokens if t.startswith('OFFSET')][0]
    offset_value = int(offset_str.split('=')[1])

    # Extract status mode using string methods (actual use)
    mode_token = [t for t in tokens if 'MODE' in t][0]
    execution_mode = mode_token.split('=')[1].lower()

    # Bit manipulation for checksum (relevant but obscured)
    checksum = 0
    for c in execution_mode:
        checksum ^= ord(c)
    checksum = (checksum << 2) & 0xFF

    # Main data transformation chain
    processed = []
    for val in raw_stream:
        if val <= 0:
            continue
        adjusted = val ^ checksum  # bit flip based on mode
        scaled = adjusted * 1.05
        if scaled % 2 == 0:
            processed.append(scaled + 1)
        else:
            processed.append(scaled)

    # Aggregate measure computed via sorting and selection
    sorted_vals = sorted(processed, reverse=True)
    top_quartile = sorted_vals[:len(sorted_vals)//4]
    aggregate_measure = sum(top_quartile) / len(top_quartile) if top_quartile else 0

    # Correction factor derived from string analysis
    flag_chars = [c for c in execution_mode if c in 'dgai']
    unique_count = len(set(flag_chars))
    correction_factor = 1.0 + (unique_count * 0.1)

    # Red herring: unused recursive function
    def recursive_sum(n):
        return n + recursive_sum(n-1) if n > 0 else 0  # never called

    # Another decoy variable (misleading intermediate)
    baseline_reference = (aggregate_measure * 0.85) + 42.5

    # Key assignment statement
    final_diagnostic = aggregate_measure * correction_factor + offset_value

    # Unused complex structure (distractor)
    report_summary = {
        'version': '2.1',
        'entries': len(raw_stream),
        'valid': len(normalized),
        'anomalies': len([x for x in z_scores if x > 2.5]),
        'final': final_diagnostic
    }

    return final_diagnostic

# Simulated sensor input (deterministic)
sensor_input = [120, -5, 204, 301, 199, 0, 405, 256, 178, 330, 200, 250]

# Execution point
result = analyze_sensor_data(sensor_input)
print(f"Result: {result}")
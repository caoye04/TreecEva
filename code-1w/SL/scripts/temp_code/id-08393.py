def analyze_system_health():
    # Real-time telemetry data from distributed sensors
    sensor_ids = ['S101', 'S102', 'S103', 'S104']
    base_readings = [127, 255, 64, 192]
    calibration_offsets = {'S101': -12, 'S102': -25, 'S103': -6, 'S104': -19}

    # Irrelevant maintenance logs (red herring)
    last_maintenance = {
        'S101': '2023-10-05',
        'S102': '2023-09-12',
        'S103': '2023-11-03',
        'S104': '2023-08-17'
    }

    # Distractor: unused temperature conversion
    def celsius_to_fahrenheit(temp_c):
        return temp_c * 9/5 + 32

    # Sensor normalization using bitwise and arithmetic ops
    normalized = []
    for i, val in enumerate(base_readings):
        sid = sensor_ids[i]
        calibrated = val + calibration_offsets[sid]
        # Apply non-linear response curve (shift and scale)
        adjusted = (calibrated << 1) ^ 0xAA  # Bit manipulation red herring
        normalized.append(adjusted)

    # Log entry generation with metadata bloat
    log_entries = []
    for idx, norm_val in enumerate(normalized):
        entry = {
            'sensor': sensor_ids[idx],
            'raw': base_readings[idx],
            'norm': norm_val,
            'timestamp': f'2023-12-01T10:{idx}0:00Z',
            'location': f'Zone-{(idx % 2) + 1}',
            'version': 'v2.1'
        }
        log_entries.append(entry)

    # System thresholds with decoy fields
    system_thresholds = {
        'critical': 300,
        'warning': 200,
        'optimal': 150,
        'decay_rate': 0.95,  # Unused in final logic
        'max_spike_tolerance': 5  # Unused
    }

    # Legacy compatibility mapping (distractor)
    legacy_map = dict(zip(sensor_ids, ['L1', 'L2', 'L3', 'L4']))

    # Actual processing function with nested logic
    def process_metrics(entries, thresholds):
        cumulative_score = 0
        spike_count = 0
        penalty_factor = 1.0

        # Lambda-based filtering (required feature)
        is_anomalous = lambda x: x > thresholds['warning']

        for i, entry in enumerate(entries):
            norm_val = entry['norm']

            # Early return red herring (never triggered due to data)
            if entry['sensor'] == 'S999':
                return -999

            # Real logic begins: evaluate against thresholds
            if is_anomalous(norm_val):
                spike_count += 1
                if norm_val > thresholds['critical']:
                    cumulative_score += norm_val // 10
                else:
                    cumulative_score += norm_val // 15

            # Dead branch: location-based adjustment (no effect)
            if entry['location'] == 'Zone-X':
                cumulative_score -= 10

            # Meaningless string operation (distractor)
            code_name = f"DIAG-{entry['sensor']}"
            code_name.upper().replace('-', '_')

        # Secondary processing with enumerate (required feature)
        multipliers = [1, -1, 2, -2]
        for idx, entry in enumerate(entries):
            m = multipliers[idx] if idx < len(multipliers) else 1
            cumulative_score += (entry['raw'] & 0x3F) * m  # Bitwise masking

        # Final adjustment based on spike patterns
        if spike_count >= 2:
            cumulative_score -= 50
        elif spike_count == 1:
            cumulative_score -= 25

        # Core answer computation (obscured by noise)
        diagnostic_value = cumulative_score + 107
        return diagnostic_value

    # Trigger point: this assignment contains the target value
    final_diagnostic = process_metrics(log_entries, system_thresholds)
    
    # Irrelevant aggregation (dead code path)
    summary_stats = {
        'total_logs': len(log_entries),
        'average_norm': sum(e['norm'] for e in log_entries) / len(log_entries),
        'peak_raw': max(e['raw'] for e in log_entries)
    }

    # Output the target result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execute and capture result
analyze_system_health()
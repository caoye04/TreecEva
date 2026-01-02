def analyze_sensor_stream(raw_packets, config_profile):
    # Irrelevant preprocessing: checksum validation (never used)
    def validate_checksum(packet):
        return sum(packet) % 256 == packet[-1]

    # Dead function: formatting for display (not used in logic)
    def format_for_display(data_list):
        return [f'{x:.2f}' for x in data_list]

    # Unused transformation: converts to dB scale
    def to_decibel(x):
        return 10 * __import__('math').log10(abs(x)) if x != 0 else -float('inf')

    base_threshold = config_profile.get('base', 50)
    sensitivity_bias = config_profile.get('sensitivity', 1.2)
    calibration_sequence = [1.1, 0.9, 1.05, 0.95, 1.0]
    
    # Distractor: complex-looking but unused signal smoothing
    smoothed_packets = []
    for pkt in raw_packets:
        temp_smooth = []
        for i, val in enumerate(pkt[:-1]):  # Exclude checksum
            alpha = calibration_sequence[i % len(calibration_sequence)]
            temp_smooth.append(val * alpha)
        smoothed_packets.append(temp_smooth)

    # Real processing begins: extract payload and flatten
    flat_payload = []
    for packet in raw_packets:
        payload = packet[1:-2]  # Skip header, footer, checksum
        flat_payload.extend(payload)

    # Misleading intermediate: frequency analysis (unused)
    frequency_map = {}
    for val in flat_payload:
        freq_key = int(val / 10)
        frequency_map[freq_key] = frequency_map.get(freq_key, 0) + 1

    # Actual filtering based on dynamic thresholds
    dynamic_floor = base_threshold * (sensitivity_bias ** 2)
    filtered_data = [x for x in flat_payload if x > dynamic_floor and x % 3 != 1]

    # Decoy structure: FFT-like computation (completely irrelevant)
    fft_magnitude = []
    for i in range(8):
        re = sum(__import__('math').cos(2 * __import__('math').pi * i * k / 8) * flat_payload[k % len(flat_payload)] for k in range(8))
        im = sum(__import__('math').sin(2 * __import__('math').pi * i * k / 8) * flat_payload[k % len(flat_payload)] for k in range(8))
        fft_magnitude.append((re**2 + im**2)**0.5)

    # Key distraction: unused set operations with sensor ids
    active_sensors = {f'sensor_{i}' for i in range(len(raw_packets))}
    maintenance_needed = {f'sensor_{i}' for i in range(0, len(raw_packets), 3)}
    flagged_sensors = active_sensors & maintenance_needed
    sensor_log = {sid: 'OK' for sid in active_sensors}
    for sid in flagged_sensors:
        sensor_log[sid] = 'CALIBRATE'

    # Real work: prepare threshold map using enumerate and zip
    categories = ['critical', 'high', 'normal', 'low']
    base_levels = [200, 120, 70, 30]
    adjusted_levels = [lvl * sensitivity_bias for lvl in base_levels]
    
    # Use enumerate and zip as required
    threshold_map = {}
    for idx, (cat, level) in enumerate(zip(categories, adjusted_levels)):
        safety_margin = (idx + 1) * 5.5
        threshold_map[cat] = level + safety_margin
        if idx % 2 == 0:
            # Red herring: modifying unrelated dict entries
            threshold_map[f'dummy_{idx}'] = level * 0.1

    # Another decoy: string splitting/joining for log generation
    log_prefixes = ['ERR', 'WRN', 'INF']
    timestamp_parts = ['2023', '12', '07', '14', '22', '33']
    iso_timestamp = '-'.join(timestamp_parts[:3]) + ' ' + ':'.join(timestamp_parts[3:])
    event_log = []
    for code in log_prefixes:
        for val in frequency_map.keys():
            event_log.append(f'{iso_timestamp} | {code} | Frequency cluster {val}')

    # Actual diagnostic processor
    def process_readings(data_points, limits):
        stats = {
            'critical': 0,
            'high': 0,
            'normal': 0,
            'out_of_range': 0
        }
        
        # Use dictionary and set together
        unique_points = set()
        point_origin = {}
        
        for i, v in enumerate(data_points):
            unique_points.add(v)
            point_origin[v] = point_origin.get(v, []) + [i]
            
            if v > limits['critical']:
                stats['critical'] += 1
            elif v > limits['high']:
                stats['high'] += 1
            elif v > limits['normal']:
                stats['normal'] += 1
            else:
                stats['out_of_range'] += 1

        # Complex aggregation: weighted impact score
        impact_weights = {
            'critical': 8.5,
            'high': 4.2,
            'normal': 1.1,
            'out_of_range': -2.0
        }
        
        aggregate_score = 0.0
        for category, count in stats.items():
            modifier = 1.0
            if category == 'critical' and len(unique_points) < 10:
                modifier = 1.8  # extra weight if few unique high values
            aggregate_score += count * impact_weights[category] * modifier
        
        # Final transformation
        final_impact = aggregate_score * (1 + __import__('math').log1p(len(data_points)) / 10)
        return int(final_impact)  # deterministic integer result

    # Execute key statement
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")
    
    # Unused cleanup
    del smoothed_packets, fft_magnitude, event_log
    
    return final_diagnostic

# Simulate input data
__main_packet_data = [
    [0xAA, 65, 70, 205, 190, 220, 80, 0xFF, 0x3C],
    [0xAA, 75, 130, 210, 195, 225, 85, 0xFF, 0x4A],
    [0xAA, 80, 140, 230, 200, 240, 90, 0xFF, 0x5B],
    [0xAA, 85, 150, 245, 205, 250, 95, 0xFF, 0x6C],
    [0xAA, 90, 160, 255, 210, 260, 100, 0xFF, 0x7D]
]

__config = {
    'base': 68,
    'sensitivity': 1.3
}

# Run analysis
analyze_sensor_stream(__main_packet_data, __config)
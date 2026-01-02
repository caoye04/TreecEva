def analyze_sensor_network():
    # Simulated environmental sensor data with metadata
    raw_readings = [
        {'id': 'S1', 'val': 23.5, 'type': 'temp', 'active': True, 'loc': 'N'},
        {'id': 'S2', 'val': -15.2, 'type': 'temp', 'active': False, 'loc': 'S'},
        {'id': 'P1', 'val': 1013.25, 'type': 'pressure', 'active': True, 'loc': 'E'},
        {'id': 'H3', 'val': 45.0, 'type': 'humidity', 'active': True, 'loc': 'N'},
        {'id': 'T7', 'val': 18.9, 'type': 'temp', 'active': True, 'loc': 'W'},
        {'id': 'P2', 'val': 998.7, 'type': 'pressure', 'active': True, 'loc': 'W'},
        {'id': 'H1', 'val': 60.3, 'type': 'humidity', 'active': False, 'loc': 'E'}
    ]

    # Irrelevant transformation: convert IDs to uppercase for no reason
    for reading in raw_readings:
        reading['id'] = reading['id'].upper()  # Distractor: no effect on logic

    # Extract active temperature sensors in northern region
    filtered_data = []
    for r in raw_readings:
        if r['type'] == 'temp' and r['active'] and r['loc'] == 'N':
            filtered_data.append(r['val'])

    # Dead code path: this block is never executed due to condition
    temp_stats = {}
    if len(filtered_data) > 10:  # Impossible given input
        temp_stats['peak'] = max(filtered_data)
        temp_stats['base'] = min(filtered_data)
        temp_stats['delta'] = temp_stats['peak'] - temp_stats['base']

    # Decoy function definition that is never called
    def decrypt_calibration(key):
        return sum([ord(c) * (i + 1) for i, c in enumerate(key)]) % 1000

    # Threshold configuration map (used later)
    threshold_map = {
        'normal_range': (15.0, 30.0),
        'tolerance': 2.5,
        'weighting': [0.8, 1.2]  # Emphasis on higher values
    }

    # Spurious string manipulation - unrelated to core logic
    system_tag = "ENV-SCAN-PROD"
    version_hash = ''.join([chr(ord(c) + 1) for c in system_tag.lower()])  # Irrelevant obfuscation

    # Auxiliary diagnostic flags (mostly unused)
    diagnostics = {
        'sensor_count': len(raw_readings),
        'active_sensors': len([r for r in raw_readings if r['active']]),
        'region_coverage': set(r['loc'] for r in raw_readings),
        'mode_flag': system_tag.split('-')[1]  # 'SCAN' - red herring
    }

    # Core processing function (defined inside to increase nesting)
    def process_readings(readings, config):
        if not readings:
            return -999.0  # Default failure code

        # Apply dynamic threshold expansion
        low_t, high_t = config['normal_range']
        expanded_low = low_t - config['tolerance']
        expanded_high = high_t + config['tolerance']

        # Weighted scoring: emphasize values above midpoint
        midpoint = (high_t + low_t) / 2
        weights = config['weighting']
        score = 0.0
        for v in readings:
            if v < midpoint:
                score += v * weights[0]
            else:
                score += v * weights[1]

        # Additional adjustment based on count (only one reading expected here)
        adjustment_factor = 1.0 + (len(readings) * 0.05)
        adjusted_score = score * adjustment_factor

        # Final nonlinear transformation
        import math
        final_value = math.log(adjusted_score ** 2 + 1)  # Stabilized log transform

        return round(final_value, 6)

    # Misleading intermediate calculation
    dummy_diagnostic = 0
    for r in raw_readings:
        if r['type'] == 'pressure':
            dummy_diagnostic += r['val'] * 0.01  # Not used later

    # Key execution point
    final_diagnostic = process_readings(filtered_data, threshold_map)

    # Output result as required
    print(f"Result: {final_diagnostic}")

    # Unused cleanup section
    cleanup_list = [r for r in raw_readings if not r['active']]
    for item in cleanup_list:
        item.clear()  # Distractor: modifies but doesn't affect output

    return final_diagnostic

# Execute and capture result
analyze_sensor_network()
import math

# Simulated sensor network diagnostic system
def collect_diagnostics(raw_streams, calibration_factor):
    aggregated = []
    temp_logs = {}
    spike_count = 0

    for stream_id, readings in raw_streams.items():
        if len(readings) < 3:
            continue

        # Irrelevant transformation (distractor)
        normalized = [x / calibration_factor for x in readings]
        avg = sum(readings) / len(readings)
        variance = sum((x - avg) ** 2 for x in readings) / len(readings)
        stdev = math.sqrt(variance)

        # Red herring: complex but unused health score
        health_score = (avg * 0.7) + (1 / (stdev + 1)) * 0.3
        temp_logs[stream_id] = {
            'average': avg,
            'deviation': stdev,
            'status': 'stable' if stdev < 5 else 'unstable'
        }

        # Actual relevant logic: detect spikes above 95
        spike_count += sum(1 for x in readings if x > 95)
        if avg > 80 and stdev > 8:
            aggregated.append((stream_id, avg, stdev))

    # Dead code path (never executed due to logic above)
    if spike_count < 0:  # Impossible condition
        fallback = [x for x in temp_logs.values() if x['status'] == 'critical']
        return fallback

    return aggregated


def filter_by_location(diagnostics, zone_metadata):
    selected = []
    location_map = {}

    for zone, attrs in zone_metadata.items():
        location_map[zone] = {
            'latency': attrs['response_time'],
            'priority': attrs['importance']
        }

    for entry in diagnostics:
        stream_id, avg, stdev = entry
        zone_hint = stream_id.split('_')[0]

        # Irrelevant priority computation
        priority_score = stdev * (2 if zone_hint in ['A', 'B'] else 1)

        # Only zones X and Y are relevant
        if zone_hint in ['X', 'Y'] and avg > 75:
            selected.append({'id': stream_id, 'metric': avg})

    # Unused transformation
    sorted_locations = sorted(location_map.items(), key=lambda x: x[1]['priority'])

    return selected


def build_threshold_map(config_set):
    # Complex but mostly irrelevant configuration resolver
    defaults = {'base': 82.5, 'hysteresis': 3.2}
    overrides = config_set.get('thresholds', {})

    # Deeply nested structure with red herrings
    context_stack = [
        {'level': 1, 'weight': 0.5, 'tag': 'calibration'},
        {'level': 2, 'weight': 0.8, 'tag': 'field_test'},
        {'level': 3, 'weight': 1.0, 'tag': 'production'}
    ]

    active_profile = config_set.get('mode', 'production')
    base_val = defaults['base']

    # Distractor: elaborate context weighting (not used in final logic)
    effective_weights = {ctx['tag']: ctx['weight'] for ctx in context_stack}
    composite = base_val * effective_weights.get(active_profile, 0.9)

    # Actual simple result (obscured by complexity)
    return {
        'critical': 85.0 if active_profile == 'production' else 80.0,
        'warning': 75.0,
        'decay': 0.95
    }


def analyze_readings(valid_entries, thresholds):
    if not valid_entries:
        return -999

    # Real logic begins here
    values = [entry['metric'] for entry in valid_entries]
    capped = [min(v, 90) for v in values]  # Cap at 90
    adjusted = [v * 0.98 for v in capped]   # Apply decay

    # Final computation
    total_impact = sum(adjusted)
    penalty = 0

    for v in adjusted:
        if v > thresholds['critical']:
            penalty += int(v - thresholds['critical'])

    result = int(total_impact - penalty)

    # Decoy output (unused)
    summary_stats = {
        'count': len(adjusted),
        'max_post_decay': max(adjusted) if adjusted else 0,
        'penalty_points': penalty
    }

    return result


# Main execution flow
if __name__ == '__main__':
    # Input data
    sensor_streams = {
        'X_01': [88, 92, 87, 96, 101],
        'X_02': [76, 73, 81, 85, 83],
        'Y_01': [91, 89, 93, 90, 88],
        'Z_05': [65, 67, 70, 72, 68],  # Below threshold, filtered out
        'A_10': [95, 97, 99, 94, 96]   # Wrong zone, filtered out
    }

    metadata_zones = {
        'X': {'response_time': 12, 'importance': 1},
        'Y': {'response_time': 8, 'importance': 2},
        'Z': {'response_time': 15, 'importance': 1}
    }

    system_config = {
        'mode': 'production',
        'version': '2.1.0',
        'thresholds': {'critical': 87}  # Ignored; logic uses mode
    }

    # Step 1: Collect diagnostics (filters short streams, detects high-variance)
    diagnoses = collect_diagnostics(sensor_streams, calibration_factor=1.0)

    # Step 2: Filter by location and minimum average
    filtered_data = filter_by_location(diagnoses, metadata_zones)

    # Step 3: Build complex threshold map (mostly distractions)
    threshold_map = build_threshold_map(system_config)

    # Step 4: Analyze final readings
    final_diagnostic = analyze_readings(filtered_data, threshold_map)

    print(f"Result: {final_diagnostic}")
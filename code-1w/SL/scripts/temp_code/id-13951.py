def process_sensor_node(data, mode='primary'):
    # Irrelevant helper that simulates noise filtering (not used in final path)
    def apply_noise_filter(arr):
        return [x for x in arr if abs(x) > 0.1]

    # Misleading transformation chain
    scaled_data = [x * 1.7 for x in data]
    offset_data = [x + 2 for x in scaled_data]  # Dead end
    baseline_corrected = [x - 1.3 for x in scaled_data]

    # Real processing begins here
    filtered = [x for x in baseline_corrected if x > 0]
    squared = [x ** 2 for x in filtered]
    return sum(squared)


def evaluate_anomaly_score(series, limit=100):
    # Unused recursive red herring
    def recursive_sum(lst, idx=0):
        if idx >= len(lst):
            return 0
        return lst[idx] + recursive_sum(lst, idx + 1)

    # Another distraction: set operations with irrelevant outcome
    unique_values = set(int(x) for x in series if x > 0)
    outliers = {x for x in unique_values if x > 50}
    normal_set = {x for x in range(1, 50)}
    masked_set = outliers & normal_set  # Always empty, but looks meaningful

    # Actual relevant logic buried here
    clipped = [min(x, 45) for x in series]
    adjusted = [x - 10 for x in clipped if x > 10]
    return len(adjusted) > 0 and sum(adjusted) or 0


def aggregate_metrics(readings_map, threshold):
    # Critical variable - this is what we want
    accumulator = 0
    
    # Distractor: complex unused tuple unpacking
    for sensor_id, (raw, meta) in readings_map.items():
        if 'status' in meta and meta['status'] != 'active':
            continue
        temp_offset = meta.get('temp_comp', 0)
        humidity_factor = meta.get('humidity', 1.0)
        # Not actually influencing result

    # Real work happens here, with nesting and filtering
    for sensor_id, (data, metadata) in readings_map.items():
        if metadata.get('calibration') < 0.8:
            continue  # Skip poorly calibrated
        
        # Process primary signal
        signal_sum = 0
        for val in data:
            if val < 0:
                signal_sum += abs(val) * 0.5
            elif val > threshold:
                signal_sum += val * 1.2
            else:
                signal_sum += val * 0.8
        
        # Secondary logic with conditional increment
        if signal_sum > 150:
            if 'type' in metadata and metadata['type'] == 'auxiliary':
                signal_sum *= 0.9
            else:
                signal_sum *= 1.1

        # Accumulate only specific sensors
        if sensor_id.startswith('SNSR'):
            normalized = int(signal_sum / 10)
            accumulator += normalized % 100

    # Final computation involving set difference (actual use of set op)
    history = {1, 2, 3, 4, 5, accumulator % 5}
    expected = {1, 2, 3, 4, 5}
    deviation = history - expected  # Will be {accumulator % 5} if not in expected
    
    # Key line: final_diagnostic depends on accumulator and deviation
    final_diagnostic = accumulator + (sum(deviation) if deviation else -5)
    
    # Red herring: printing intermediate values that look important
    debug_snapshot = {
        'acc': accumulator,
        'dev': sum(deviation) if deviation else 0,
        'hist': history,
        'outlier_count': evaluate_anomaly_score([accumulator] * 5)
    }
    
    # This print is a distractor; the real answer is final_diagnostic
    print(f"Debug: {debug_snapshot}")
    
    return final_diagnostic

# Main execution
if __name__ == "__main__":
    # Simulated sensor network readings with metadata
    nested_readings = {
        'SNSR-A1': ([12.5, -3.2, 45.0, 67.8], {'calibration': 0.85, 'type': 'primary'}),
        'SNSR-B2': ([8.0, 14.2, 9.7], {'calibration': 0.92, 'type': 'auxiliary'}),
        'SNSR-C3': ([23.1, 78.9, -1.5, 34.2], {'calibration': 0.75, 'type': 'primary'}),  # Skipped due to calibration
        'MON-X9': ([5.5, 6.0], {'calibration': 0.98, 'status': 'inactive'}),  # Skipped due to status
        'SNSR-D4': ([40.0, 42.0, 41.5], {'calibration': 0.91, 'type': 'primary'})
    }

    base_threshold = 40.0

    # Decoy function calls with no side effects
    _ = process_sensor_node([1, 2, 3], mode='test')
    _ = evaluate_anomaly_score([100, 200, 300])

    # Critical execution point
    final_diagnostic = aggregate_metrics(nested_readings, base_threshold)
    
    # Correct output format
    print(f"Target result: {final_diagnostic}")
def sensor_calibration(raw_values, base_offset):
    calibrated = {}
    temp_store = []
    cumulative = 0
    
    for i, val in enumerate(raw_values):
        if i % 3 == 0:
            adjusted = val * 1.05 + base_offset
        elif i % 4 == 1:
            adjusted = val * 0.92 - base_offset
        else:
            adjusted = val * 1.01
        
        calibrated[f'sensor_{i}'] = round(adjusted, 3)
        temp_store.append(adjusted)
        cumulative += adjusted ** 0.5

    # Irrelevant aggregation
    outlier_count = 0
    for v in temp_store:
        if v > 150 or v < 5:
            outlier_count += 1

    # Dead path: never used
    if len(temp_store) > 100:
        normalized = [x / max(temp_store) for x in temp_store]
    else:
        dummy_flag = False

    return calibrated


def transform_keys(data_dict):
    new_dict = {}
    for k, v in data_dict.items():
        new_key = k.replace('sensor', 'node').upper()
        new_dict[new_key] = v * 0.98
    return new_dict


def filter_by_profile(configured_map, min_val=10.0, max_val=200.0):
    valid_entries = {}
    total_filtered = 0
    
    for key, threshold in configured_map.items():
        if min_val <= threshold <= max_val:
            valid_entries[key] = threshold * 1.1
        else:
            total_filtered += 1  # distractor count

    # Unused computation
    if total_filtered > 5:
        fallback_mode = True
    else:
        fallback_mode = False

    return valid_entries


def accumulate_diagnostics(log_entries):
    total_score = 0.0
    penalty = 0
    
    for entry in log_entries:
        if 'ERROR' in entry:
            penalty += 1
        elif 'WARNING' in entry:
            total_score -= 0.5
        else:
            total_score += 0.2
    
    # Red herring: complex string parsing with no effect
    summary = ''
    for entry in log_entries:
        words = entry.split(' ')
        if len(words) > 3:
            summary += words[0][0]
    
    return total_score


def analyze_readings(data, thresholds):
    result = 0
    debug_trace = []
    
    for k, v in data.items():
        prefix = k.split('_')[0]
        idx = int(k.split('_')[1])
        
        # Real logic branch
        if prefix == 'NODE':
            if idx % 2 == 0 and v > thresholds.get(k, 50):
                result += int(v // 10)
            elif idx % 5 == 0 and v < thresholds.get(k, 60):
                result -= int(v // 20)
        
        debug_trace.append(f'{k}:{v}')

    # Decoy transformation
    reversed_trace = [t[::-1] for t in debug_trace]
    trace_sum = sum(len(t) for t in reversed_trace)

    # Final adjustment based on actual conditions
    if result > 100:
        result = result // 2 + 7
    else:
        result = result * 2 - 3

    return result

# Main execution sequence
if __name__ == '__main__':
    raw_sensor_data = [120, 88, 95, 134, 76, 110, 145, 67, 103, 131, 89, 97]
    offset = 3.5
    
    # Step 1: Calibration
    calibrated_data = sensor_calibration(raw_sensor_data, offset)
    
    # Step 2: Transform keys (irrelevant modification)
    renamed_data = transform_keys(calibrated_data)
    
    # Step 3: Create threshold map with decoy entries
    threshold_config = {}
    for i, key in enumerate(renamed_data.keys()):
        if i % 2 == 0:
            threshold_config[key] = 95 + (i * 2)
        else:
            threshold_config[key] = 45 - (i % 10)  # Some go below min_val
    
    # Filter thresholds (some removed)
    filtered_thresholds = filter_by_profile(threshold_config)
    
    # Fake logging (distractor)
    logs = [
        'STATUS OK at 12:00',
        'WARNING: minor fluctuation',
        'STATUS NORMAL',
        'ERROR: timeout in sector 7',
        'STATUS RESUMED'
    ]
    diagnostic_score = accumulate_diagnostics(logs)
    
    # Critical statement
    final_diagnostic = analyze_readings(renamed_data, filtered_thresholds)
    
    print(f'Result: {final_diagnostic}')
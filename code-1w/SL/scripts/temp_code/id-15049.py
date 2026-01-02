import math

# Simulated sensor array data with noise and redundant metrics
def collect_sensor_array():
    raw_readings = [127, 255, 192, 64, 31, 88, 142, 201]
    timestamps = [1623456780 + i for i in range(8)]
    statuses = ['OK', 'OK', 'ERROR', 'OK', 'WARNING', 'OK', 'OK', 'ERROR']
    
    # Irrelevant derived stats (distractors)
    avg_temp = sum([r % 40 for r in raw_readings]) / len(raw_readings)
    peak_noise = max([r & 15 for r in raw_readings])
    entropy_proxy = len(set([r >> 2 for r in raw_readings]))

    # Actual relevant packaging
    sensor_data = []
    for i in range(len(raw_readings)):
        sensor_data.append({
            'id': i,
            'value': raw_readings[i],
            'ts': timestamps[i],
            'status': statuses[i]
        })
    
    return sensor_data

# Extraneous function: looks useful but unused in critical path
def analyze_trend(data_seq):
    if not data_seq:
        return 0
    diffs = [data_seq[i+1] - data_seq[i] for i in range(len(data_seq)-1)]
    trend_score = sum([1 for d in diffs if d > 0]) - sum([1 for d in diffs if d < 0])
    return abs(trend_score) * 0.5

# Another red herring: processes metadata but not used in final calculation
def compute_health_index(sensor_list):
    valid_count = sum([1 for s in sensor_list if s['status'] == 'OK'])
    error_count = sum([1 for s in sensor_list if s['status'] == 'ERROR'])
    warning_count = sum([1 for s in sensor_list if s['status'] == 'WARNING'])
    
    # Complex but irrelevant formula
    if valid_count == 0:
        return 0.0
    health = (valid_count * 1.0 + warning_count * 0.5) / (valid_count + error_count * 2)
    return round(health * 100, 2)

# Real processing begins here — filtering by status and bit condition
def filter_by_criteria(sensor_list):
    filtered = []
    for entry in sensor_list:
        # Key condition: only 'OK' status AND value has odd number of set bits
        if entry['status'] != 'OK':
            continue
        popcount = bin(entry['value']).count('1')
        if popcount % 2 == 1:  # Only odd parity values
            filtered.append(entry['value'])
    
    # Distractor: sort by something irrelevant
    sorted_filtered = sorted(filtered, key=lambda x: x ^ 17)  # meaningless sort
    return sorted_filtered

# Core transformation logic — combines arithmetic and bit manipulation
def apply_calibration(readings, factor):
    calibrated = []
    base_shift = int(math.log(factor + 1, 2)) if factor > 0 else 0
    
    for val in readings:
        # Multi-step transformation
        shifted = val >> base_shift
        adjusted = shifted * factor
        # Apply modulo mask to simulate register overflow
        masked = adjusted & 0xFF  # byte truncation
        calibrated.append(masked)
    
    # Dead code path: never executed due to design
    if len(calibrated) > 100:
        backup = [c ^ 0xAA for c in calibrated]
        return backup
        
    return calibrated

# Final diagnostic computation — uses list comprehension and string-based tagging
def process_readings(data_list, calib):
    if not data_list:
        return -1
    
    # Apply real transformation
    processed = apply_calibration(data_list, calib)
    
    # Generate diagnostic tags (string operations — distractor)
    tag_pool = ['SYS_OK', 'CALIBRATED', 'SENSOR_STABLE']
    tags = [t.lower() for t in tag_pool if len(t) % 2 == 1]  # filters to ['SYS_OK', 'SENSOR_STABLE']
    tag_hash = sum([len(t) for t in tags]) * 10
    
    # Core result: sum of squares modulated by calibration
    aggregate = sum([x * x for x in processed])
    modulation = calib % 7 if calib > 0 else 1
    if modulation == 0:
        modulation = 1
    
    # Final computation chain
    intermediate = aggregate // modulation
    final_value = intermediate - tag_hash  # subtract distractor-derived constant
    
    # Additional decoy logic
    if final_value < 0:
        binary_rep = bin(final_value & 0xFFFF)
        parity_check = binary_rep.count('1') % 2
        final_value += 50 * parity_check
    
    return final_value

# Main execution flow
if __name__ == '__main__':
    # Initialization block with multiple side computations
    sensor_grid = collect_sensor_array()
    
    # Unused statistical summaries (distractors)
    all_values = [s['value'] for s in sensor_grid]
    mean_val = sum(all_values) / len(all_values)
    variance_proxy = sum([(v - mean_val)**2 for v in all_values])
    std_dev_hint = math.sqrt(variance_proxy)
    
    # Health index computed but not used (red herring)
    system_health = compute_health_index(sensor_grid)
    
    # Trend analysis on timestamps — looks meaningful but unused
    time_series = [s['ts'] for s in sensor_grid]
    trend_metric = analyze_trend(time_series)
    
    # Critical path begins here
    filtered_data = filter_by_criteria(sensor_grid)
    calibration_factor = 6
    
    # Final processing step
    final_diagnostic = process_readings(filtered_data, calibration_factor)
    
    # Output the target result
    print(f"Target result: {final_diagnostic}")
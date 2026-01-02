import itertools

def analyze_sequence(data, threshold):
    count = 0
    temp_sum = 0
    for val in data:
        if val > threshold:
            count += 1
            temp_sum += val
    return temp_sum if count > 3 else 0

def generate_pairs(values):
    # Irrelevant helper function - dead code path
    return list(itertools.combinations(values, 2))

def compute_hash_chain(seed, length):
    # Distractor computation with no impact on final result
    result = seed
    for i in range(length * 2):
        result = (result ^ i) % 97
    return result

def extract_critical_flags(events):
    # Processes event flags but only some are used
    flags = {}
    for e in events:
        code = e['code']
        status = e['status']
        flags[code] = status == 'ACTIVE'
    
    # Decoy logic - looks important but unused
    if flags.get('ERR', False) and not flags.get('IOK', True):
        compute_hash_chain(42, 10)
    
    # Only this subset matters
    return flags.get('SNSR', False) and flags.get('PWR', True)

def integrate_readings(sensor_data, mode):
    base = 0
    offset = 10
    for entry in sensor_data:
        if mode == 'calibrated':
            base += int(entry['value'] // 2)
        else:
            base += int(entry['value'] * 1.5)
    return base - offset

def process_metrics(entries, config):
    # Core logic embedded in noise
    total_weight = 0
    active_segments = 0
    diagnostic_score = 0
    
    # Real processing begins
    for entry in entries:
        timestamp = entry['ts']
        readings = entry['readings']
        category = entry['type']
        
        # Meaningful condition
        if category == 'PRIMARY':
            segment_value = integrate_readings(readings, 'calibrated')
            total_weight += segment_value
            
            # Another layer of filtering
            valid_points = [r['value'] for r in readings if r['quality'] > 0.7]
            if len(valid_points) >= 4:
                active_segments += 1
                
    # This part uses external config
    limit = config['segment_limit']
    penalty_rate = config['penalty']
    
    # Real score calculation
    if active_segments >= limit:
        diagnostic_score = total_weight * 2
    else:
        diagnostic_score = total_weight - (active_segments * penalty_rate)
    
    # Red herring: complex bit manipulation that does nothing
    masked = diagnostic_score ^ 0xFF
    shifted = (masked << 2) >> 1
    compute_hash_chain(shifted, 5)  # Unused call
    
    # Final adjustment based on flag system (only SNSR and PWR matter)
    all_events = [
        {'code': 'BOOT', 'status': 'ACTIVE'},
        {'code': 'SNSR', 'status': 'ACTIVE'},
        {'code': 'PWR', 'status': 'ACTIVE'},
        {'code': 'NET', 'status': 'INACTIVE'},
        {'code': 'IOK', 'status': 'ACTIVE'}
    ]
    
    if extract_critical_flags(all_events):
        diagnostic_score += 25
    
    return int(diagnostic_score)

# Main execution flow
if __name__ == '__main__':
    # Simulated log entries - realistic structure
    log_entries = [
        {
            'ts': 1678886400,
            'type': 'PRIMARY',
            'readings': [
                {'value': 12.0, 'quality': 0.85},
                {'value': 15.0, 'quality': 0.90},
                {'value': 8.0, 'quality': 0.75},
                {'value': 20.0, 'quality': 0.80},
                {'value': 10.0, 'quality': 0.60}
            ]
        },
        {
            'ts': 1678886460,
            'type': 'PRIMARY',
            'readings': [
                {'value': 18.0, 'quality': 0.92},
                {'value': 14.0, 'quality': 0.77},
                {'value': 9.0, 'quality': 0.81},
                {'value': 22.0, 'quality': 0.88},
                {'value': 11.0, 'quality': 0.50}
            ]
        },
        {
            'ts': 1678886520,
            'type': 'SECONDARY',  # Will be ignored due to type
            'readings': [
                {'value': 30.0, 'quality': 0.95}
            ]
        }
    ]
    
    # System configuration
    system_thresholds = {
        'segment_limit': 2,
        'penalty': 12
    }
    
    # Irrelevant pre-computations
    dummy_data = [3, 7, 2, 8, 5, 9, 1]
    analyze_sequence(dummy_data, 4)
    generate_pairs(dummy_data)
    
    # Critical execution point
    final_diagnostic = process_metrics(log_entries, system_thresholds)
    
    # Output result
    print(f"Target result: {final_diagnostic}")
import math

def analyze_metrics(entries):
    total = 0
    count = 0
    temp_buffer = []
    for entry in entries:
        if 'error' in entry and entry['error']:
            continue
        if entry['type'] == 'A':
            total += entry['value'] * 0.8
        elif entry['type'] == 'B':
            total += entry['value'] * 0.6
        else:
            temp_buffer.append(entry['value'])
        count += 1
    adjustment = sum(temp_buffer) * 0.1 if temp_buffer else 0
    return total + adjustment

def validate_sequence(seq):
    if not seq:
        return False
    sorted_seq = sorted(seq)
    return all(sorted_seq[i] <= sorted_seq[i+1] for i in range(len(sorted_seq)-1))

def transform_key(value, key):
    shifted = (value << 2) & 0xFF
    return shifted ^ key

def build_lookup(keys):
    lookup = {}
    for k in keys:
        lookup[k] = transform_key(k, len(str(k)))
    return lookup

def simulate_calibration(data):
    calibrated = []
    base_shift = 10
    for d in data:
        if d % 3 == 0:
            calibrated.append(d + base_shift)
        elif d % 5 == 0:
            calibrated.append(d * 2)
        else:
            calibrated.append(d - 1)
    return [x for x in calibrated if x > 0]

def process_results(log, cfg):
    # Core logic path
    filtered_data = [e for e in log if e['active'] and e['version'] >= cfg['min_version']]
    raw_total = sum(e['size'] for e in filtered_data)
    
    # Irrelevant distraction: complex dictionary manipulation
    stats_map = {i: {'raw': val['size'], 'tier': 'high' if val['size'] > 100 else 'low'} 
                for i, val in enumerate(filtered_data)}
    tier_counts = {'high': 0, 'low': 0}
    for s in stats_map.values():
        tier_counts[s['tier']] += 1
    
    # Another red herring: sorting and validation on unrelated field
    metadata_seq = [len(str(e['meta_id'])) for e in filtered_data if 'meta_id' in e]
    is_valid_sequence = validate_sequence(metadata_seq)
    
    # Distractor: unused calibration simulation
    simulated = simulate_calibration([50, 15, 25, 33])
    fake_lookup = build_lookup([12, 24, 48, 96])
    
    # Actual computation path
    adjusted_total = raw_total
    if cfg['enable_enhancement']:
        bonus_factor = 1.2
        penalty_factor = 0.9
        enhancement = math.floor(adjusted_total * bonus_factor)
        if tier_counts['low'] > tier_counts['high']:
            enhancement = int(enhancement * penalty_factor)
        adjusted_total = enhancement
    
    # Final decision based on config mode
    if cfg['mode'] == 'strict':
        final_value = adjusted_total // 2
    elif cfg['mode'] == 'relaxed':
        final_value = int(adjusted_total * 1.1)
    else:
        final_value = adjusted_total  # default mode
    
    # Key assignment
    final_score = final_value + 17
    
    # Dead code branch - never reached due to prior logic
    if len(simulated) > 100:
        fallback = build_lookup(range(10))
        final_score -= sum(fallback.values())
    
    return final_score

# Main execution
if __name__ == '__main__':
    data_log = [
        {'active': True, 'version': 2.1, 'size': 120, 'meta_id': 1001, 'type': 'A', 'value': 50},
        {'active': True, 'version': 2.5, 'size': 85, 'meta_id': 1002, 'type': 'B', 'value': 30},
        {'active': False, 'version': 1.8, 'size': 200, 'meta_id': 1003, 'type': 'A', 'value': 70},
        {'active': True, 'version': 3.0, 'size': 95, 'meta_id': 1004, 'type': 'C', 'value': 40},
        {'active': True, 'version': 2.2, 'size': 150, 'meta_id': 1005, 'type': 'A', 'value': 60}
    ]
    
    config = {
        'min_version': 2.0,
        'enable_enhancement': True,
        'mode': 'default',
        'timeout': 30,
        'retries': 3
    }
    
    # Unused variables - distractions
    debug_trace = [transform_key(x['size'], 7) for x in data_log if x['active']]
    audit_checksum = sum(len(str(item)) for item in config.keys()) * 13
    
    final_score = process_results(data_log, config)
    print(f"Target result: {final_score}")
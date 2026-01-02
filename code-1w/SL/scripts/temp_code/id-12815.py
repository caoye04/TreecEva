def analyze_component_health(reading, threshold_map, mode='strict'):
    if mode == 'strict':
        return reading > threshold_map.get('critical', 75) and (reading % 11 != 0)
    elif mode == 'relaxed':
        return reading > threshold_map.get('warning', 50)
    return False

# Irrelevant helper (dead path)
def legacy_calibrate(x):
    return (x * 37) % 101

def transform_sequence(seq, key_offset):
    # Complex but partially irrelevant transformation
    shifted = [(v + key_offset) % 100 for v in seq]
    processed = []
    for i, val in enumerate(shifted):
        if i % 3 == 0:
            processed.append(val ^ 17)
        elif i % 4 == 0:
            processed.append(val | 5)
        else:
            processed.append(val)
    return [p for p in processed if p % 2 == 1]  # Keep only odds

# Unused data structure (distractor)
system_templates = {
    'A1': {'base': 42, 'limit': 90, 'mode': 'strict'},
    'B2': {'base': 35, 'limit': 85, 'mode': 'relaxed'}
}

def compute_entropy(vector):
    # Misleading scientific-looking function
    total = sum(vector)
    if total == 0:
        return 0.0
    entropy = 0.0
    for x in vector:
        if x > 0:
            prob = x / total
            entropy -= prob * __import__('math').log(prob)
    return round(entropy, 6)

# Real processing chain starts heredef extract_timestamps(entries):
    # Extract and hash timestamps (partially relevant)
    hashes = []    for entry in entries:
        if 'ts' in entry:
            hashed = (entry['ts'] * 7) % 97
            if hashed % 3 == 0:
                hashes.append(hashed)
    return hashes

def validate_checksum(data_list):
    # Bitwise checksum (red herring)
    chk = 0
    for d in data_list:
        chk ^= (d * 13) & 0xFF
    return chk

def process_metrics(log_entries, system_flags):
    # Core logic buried in noise
    
    # Step 1: Filter valid logs
    critical_logs = [e for e in log_entries if e.get('level') == 'CRITICAL']
    
    # Distractor: unused transformation
    dummy_seq = [8, 16, 24, 32, 40]
    transformed = transform_sequence(dummy_seq, 10)
    
    # Step 2: Extract numeric diagnostics
    raw_readings = [e['value'] for e in critical_logs if 'value' in e]
    
    # Step 3: Threshold map based on flags
    thresholds = {        'critical': 80 if system_flags.get('overclock') else 75,
        'warning': 55    }
    
    # Step 4: Analyze health status using actual logic
    health_status = []
    for r in raw_readings:
        is_unstable = analyze_component_health(r, thresholds)
        health_status.append(1 if is_unstable else 0)
    
    # Step 5: Count unstable readings
    instability_count = sum(health_status)
    
    # Step 6: Use dictionary operations meaningfully
    stats_summary = {
        'total_critical': len(raw_readings),
        'unstable_count': instability_count,
        'ratio': instability_count / len(raw_readings) if raw_readings else 0
    }
    
    # Step 7: Conditional logic with ternary
    base_score = 100 if stats_summary['ratio'] < 0.5 else 50
    
    # Step 8: Final diagnostic calculation (key result)
    adjustment = 15 if system_flags.get('debug_mode') and instability_count > 0 else 0
    final_diagnostic = base_score - adjustment
    
    # Irrelevant entropy side-calculation (distraction)
    if raw_readings:
        _ = compute_entropy([x for x in raw_readings if x > 0])
    
    # Unused zip + enumerate (meets language feature requirement)
    labels = ['A', 'B', 'C', 'D']
    for idx, (lbl, val) in enumerate(zip(labels, raw_readings)):
        _ = f'{idx}:{lbl}={val % 10}'  # Dead computation
    
    return final_diagnostic

# Main execution
if __name__ == '__main__':
    # Simulated input data
    log_entries = [
        {'level': 'INFO', 'ts': 1000, 'value': 60},
        {'level': 'CRITICAL', 'ts': 1001, 'value': 82},
        {'level': 'WARNING', 'ts': 1002, 'value': 70},
        {'level': 'CRITICAL', 'ts': 1003, 'value': 45},
        {'level': 'CRITICAL', 'ts': 1004, 'value': 88},
        {'level': 'CRITICAL', 'ts': 1005, 'value': 91},
        {'level': 'CRITICAL', 'ts': 1006, 'value': 67}
    ]
    
    system_flags = {
        'overclock': True,
        'debug_mode': True,
        'legacy_support': False
    }
    
    # Key execution point
    final_diagnostic = process_metrics(log_entries, system_flags)
    
    # Output result
    print(f"Target result: {final_diagnostic}")
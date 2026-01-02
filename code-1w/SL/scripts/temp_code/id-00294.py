import itertools

# Simulated sensor array data from environmental monitoring system
def process_sensor_readings(raw_readings, calibration_factor):
    calibrated = [r * calibration_factor for r in raw_readings]
    filtered = [r for r in calibrated if r > 0.5]
    
    # Irrelevant transformation chain (distractor)
    normalized = [r / max(filtered) for r in filtered] if filtered else [0]
    weighted = [n * 1.3 for n in normalized]
    bucketed = {i: [] for i in range(5)}
    for w in weighted:
        bucketed[min(4, int(w // 0.2))].append(w)
    
    # Relevant computation hidden among distractors
    bit_flags = 0
    for val in filtered:
        shifted = int(val * 10) & 7
        bit_flags ^= shifted  # XOR accumulation of low-order bits
    
    return filtered, bit_flags

# Data integrity verification (mostly dead code path)
def verify_checksum(data, key):
    if len(data) == 0:
        return 0
    checksum = 0
    for i, d in enumerate(data):
        checksum += d * (i + 1) ^ key
    return checksum % 97

# Core metric aggregator - the actual relevant function
def aggregate_metrics(chain, vkey):
    base_score = 0
    
    # Process multiple stages (some irrelevant)
    for stage in chain:
        if 'type' not in stage:
            continue
        
        # Real logic intermixed with noise
        if stage['type'] == 'filtered_signal':
            values = stage['data']
            if len(values) >= 3:
                # Real contribution to answer
                base_score += values[0] * 10
                base_score -= values[1]  
                base_score += len([v for v in values if v % 2 == 1])  # count odds
        
        # Distractor: complex but unused calculation
        if stage['type'] == 'auxiliary_trace':
            pairs = list(itertools.combinations(stage['data'], 2))
            distances = [abs(a - b) for a, b in pairs]
            avg_dist = sum(distances) / len(distances) if distances else 0
            transformed = ''.join([chr(int(65 + d % 26)) for d in distances[:10]])
            case_swapped = transformed.swapcase()  # string method used
            entropy = len(set(case_swapped)) / len(case_swapped) if case_swapped else 0
            # This entire block has no effect on final result
    
    # Critical operation using validation key (bitwise mix)
    base_score ^= vkey  # XOR with external key
    base_score += (vkey & 15)  # add lower nibble
    
    return base_score

# --- Main execution ---
if __name__ == '__main__':
    # Initial sensor inputs (simulated)
    readings = [0.1, 0.8, 1.2, 0.4, 1.6, 0.9]
    key = 13
    
    # Dead variables - red herrings
    audit_log = []
    system_status = 'OK'
    last_updated = '2023-11-05'
    config_override = False
    buffer_pool = [0] * 128
    temp_cache = set()
    
    # First processing step (produces real and fake outputs)
    processed_data, flag_value = process_sensor_readings(readings, 1.25)
    
    # Build processing chain - only one element matters
    processing_chain = [
        {
            'type': 'diagnostic_snapshot',
            'data': [1, 1, 0, 1],
            'timestamp': 1698979200
        },
        {
            'type': 'filtered_signal',
            'data': [8, 3, 7, 2, 9],  # This is the only relevant entry
            'source': 'sensor_7A'
        },
        {
            'type': 'auxiliary_trace',
            'data': [5.5, 3.1, 8.7],
            'active': True
        }
    ]
    
    # Secondary check with no impact (distractor)
    integrity = verify_checksum([8, 3, 7], key)
    if integrity < 50:
        temp_cache.add('flagged')
    else:
        temp_cache.add('normal')
    
    # Key state variable (misleading intermediate)
    diagnostic_weight = len(processed_data) * flag_value
    scaling_factor = diagnostic_weight / (key + 1) if key != -1 else 0
    
    # Actual target computation
    validation_key = (key ^ 7) + 2  # transforms 13 -> 10
    final_diagnostic = aggregate_metrics(processing_chain, validation_key)
    
    # Output the required result
    print(f"Result: {final_diagnostic}")
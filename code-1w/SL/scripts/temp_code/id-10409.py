import math

def analyze_efficiency(log_data):
    # Irrelevant function: processes string logs but not used in final calculation
    entries = log_data.split('\n')
    valid_count = 0
    for entry in entries:
        if 'ERROR' not in entry and len(entry.strip()) > 5:
            valid_count += 1
    return valid_count

def decode_sequence(encoded_seq):
    # Distractor: performs bit manipulation but result is unused
    decoded = 0
    shift = 0
    for b in encoded_seq:
        decoded |= (b % 2) << shift
        shift += 1
    return bin(decoded)

def filter_stages(stage_list, threshold=3):
    # Dead code path: not called in main flow
    filtered = []
    for stage in stage_list:
        if stage['level'] >= threshold:
            filtered.append(stage)
    return filtered

def calculate_thermal_output(sequence):
    base_factor = 7.3
    adjustment = 0.0
    temp_result = 0
    
    # Complex nested logic with relevant and irrelevant branches
    for step in sequence:
        if step['type'] == 'heat':
            if step['mode'] == 'pulse':
                temp_result += base_factor * math.sqrt(step['energy'])
            elif step['mode'] == 'hold':
                temp_result += base_factor * (step['duration'] / 2.5)
        elif step['type'] == 'cool' and step['active']:
            temp_result -= base_factor * 0.8
    
    # Apply nonlinear correction using string-derived key (subtle red herring)
    key_tag = "CALIBRATION_X9"
    if 'X9' in key_tag:
        exponent = len(key_tag.replace('_', '')) % 4  # This affects result
        adjustment = pow(1.1, exponent)
    
    # Final adjustment — only this matters
    final_value = temp_result * adjustment
    
    # Decoy assignment
    efficiency_ratio = final_value / (temp_result + 1e-9)
    
    return final_value

def main():
    # Simulated process sequence (relevant data)
    process_sequence = [
        {'type': 'heat', 'mode': 'pulse', 'energy': 16.0, 'duration': 10},
        {'type': 'heat', 'mode': 'hold', 'energy': 5.0, 'duration': 7},
        {'type': 'cool', 'active': True, 'energy': 3.0, 'duration': 5},
        {'type': 'heat', 'mode': 'pulse', 'energy': 25.0, 'duration': 12},
        {'type': 'heat', 'mode': 'hold', 'energy': 8.0, 'duration': 4},
        {'type': 'cool', 'active': True, 'energy': 2.0, 'duration': 3}
    ]
    
    # Irrelevant variables and computations
    system_log = 'INIT_OK\nLOADING_3\nPROCESS_START\nHEAT_PHASE_A\nCOOL_CHECK_PASS'
    log_integrity = analyze_efficiency(system_log)
    
    encoded_pattern = [1, 0, 1, 1, 0, 1]
    binary_repr = decode_sequence(encoded_pattern)
    
    dummy_matrix = [[i*j for j in range(4)] for i in range(4)]
    trace_sum = sum(dummy_matrix[i][i] for i in range(4))
    
    # Key execution point
    thermal_capacity = calculate_thermal_output(process_sequence)
    
    # Output the target result
    print(f"Result: {thermal_capacity}")

if __name__ == '__main__':
    main()
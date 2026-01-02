def analyze_frequency(seq, base):
    count = 0
    for c in seq:
        if c.lower() in 'aeiou':
            count += 1
    return count % base

# Irrelevant helper (distractor)
def validate_checksum(data):
    total = 0
    for i, val in enumerate(data):
        total += val * (i + 1)
    return total % 17

# Unused transformation (dead code path)
def transform_legacy(arr):
    return [x << 2 for x in arr if x % 3 != 0]

# Core logic disguised among noise
def filter_noisy_reads(raw_reads, min_val, max_val, mode_flag):
    cleaned = []
    for idx, reading in enumerate(raw_reads):
        adjusted = reading - (idx % 4)
        if min_val < adjusted < max_val:
            if mode_flag and idx % 2 == 0:
                cleaned.append(adjusted * 2)
            else:
                cleaned.append(adjusted)
    return [x for x in cleaned if x > 0]

# Another red herring: checksum-based pruning (not actually used in main flow)
def prune_anomalies(dataset):
    if len(dataset) < 5:
        return dataset[::-1]
    return [x for x in dataset if x % 2 == 1]

# Signal processor with key logic hidden in multiple conditions
def process_signals(data_list, config_map):
    temp_result = 0
    multiplier = config_map['gain']
    offset = config_map.get('offset', 0)
    
    for i, val in enumerate(data_list):
        # Simulate phase shift
        if i % 3 == 0:
            temp_result += val * multiplier
        elif i % 5 == 0:
            temp_result -= val // 2
        else:
            temp_result += (val + (i % 7)) % 10
    
    # Decoy operation (looks important but unused in final step)
    backup_state = temp_result ^ 0xFF
    scaling_factor = 1.5  # Never used
    
    return abs(temp_result - offset)

# Distractor: unrelated string processing
def encode_sequence(text):
    encoded = '''
    for char in text:
        if char.isalpha():
            shift = 3 if char.lower() in 'aeiou' else -1
            new_char = chr((ord(char.lower()) - 97 + shift) % 26 + 97)
            encoded += new_char.upper()
        else:
            encoded += char
    return encoded

# Main execution block
if __name__ == '__main__':
    # Input data (real signal stream)
    sensor_reads = [84, 12, 67, 91, 23, 44, 58, 19, 88, 33]
    
    # Irrelevant configuration (distractor)
    system_params = {
        'version': '2.1.5',
        'mode': 'diagnostic',
        'timeout': 1200,
        'gain': 7,  # Used later
        'offset': 14  # Used later
    }
    
    # Fake data transformation chain
    checksummed = validate_checksum(sensor_reads)  # Computed but not used
    legacy_processed = transform_legacy(sensor_reads)  # Dead code
    
    # Real filtering with subtle logic
    filtered_data = filter_noisy_reads(sensor_reads, 10, 90, True)
    
    # More distractions
    anomaly_test = prune_anomalies(filtered_data)  # Not used
    dummy_string = "SignalFrame_2024"
    processed_str = encode_sequence(dummy_string)  # Meaningless side computation
    
    # Critical configuration subset
    threshold_map = {
        'gain': system_params['gain'],
        'offset': system_params['offset']
    }
    
    # Key analysis using filtered data and config
    frequency_metric = analyze_frequency(processed_str, 13)
    auxiliary_score = frequency_metric * 5  # Looks important, never used
    
    # CORE COMPUTATION — answer derived here
    final_output = process_signals(filtered_data, threshold_map)
    
    # Output result as required
    print(f"Result: {final_output}")
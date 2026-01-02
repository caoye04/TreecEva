import itertools

# Simulated sensor data preprocessing with red herrings
def fetch_raw_sensor_data():
    return [127, 85, 193, 44, 201, 67, 142, 91]

# Irrelevant transformation - decoy function
def decrypt_signal(data):
    return [d ^ 0xFF for d in data[::-1]]  # Reversed and inverted - unused later

# Core transformation chain
def apply_noise_filter(data):
    filtered = []
    for i in range(len(data)):
        if i == 0:
            filtered.append(data[i])
        else:
            # Weighted moving average with window 2
            filtered.append((data[i-1] + 2 * data[i]) // 3)
    return filtered

# Bit manipulation misdirection
def analyze_signal_entropy(data):
    entropy_values = []
    for val in data:
        bit_count = bin(val).count('1')
        entropy_values.append(bit_count * val % 17)  # Complex but unused result
    return entropy_values  # Dead end

def extract_frequency_peaks(data):
    peaks = []
    for i in range(1, len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append(data[i])
    return peaks or [0]

# Data enhancement with tuple unpacking distraction
def augment_data_segments(raw_segments):
    enhanced = []
    metadata_log = []
    for idx, val in enumerate(raw_segments):
        # Real processing
        normalized = (val - 64) % 100
        category_flag = 'high' if normalized > 50 else 'low'
        
        # Distractor: complex unpacking that doesn't affect output
        info_tuple = (idx, val, normalized, category_flag, 0xDEADBEEF)
        _, _, clean_val, _, _ = info_tuple
        
        enhanced.append(clean_val)
        metadata_log.append(f"Sample {idx}: {category_flag}")  # Logged but not used
    
    return enhanced

# Conditional data routing - one path is dead
def route_data_stream(data, mode='primary'):
    if mode == 'diagnostic':
        checksum = sum(data) % 256
        debug_dump = {'data': data, 'checksum': checksum}
        return [], debug_dump  # Dead path
    else:
        return data, None

# Main transformation pipeline
def transform_sensor_stream(raw_data, threshold=75):
    step1 = apply_noise_filter(raw_data)
    
    # Red herring call
    _ = analyze_signal_entropy(step1)
    
    step2 = [x for x in step1 if x > threshold]
    step3 = extract_frequency_peaks(step2 + [max(step2)+1])  # Artificial peak
    
    if len(step3) < 3:
        step3.extend([threshold] * (3 - len(step3)))
    
    # Use itertools to create combinations - meaningful only in size
    combo_pool = list(itertools.combinations(step3[:3], 2))
    combination_weight = sum(a * b for a, b in combo_pool) % 1000
    
    return step3, combination_weight

# Final processing with configuration interaction
def process_transformed_data(data_list, config):
    base_value = config['base']
    multiplier = config['mult']
    offset = config.get('offset', 0)
    
    temp_result = base_value
    for val in data_list:
        if val > 0:
            temp_result = (temp_result + val) * 0.9
        else:
            temp_result -= val
    
    return int(temp_result * multiplier + offset)

# Unused diagnostic routine - full decoy
def run_system_diagnostics():
    diagnostics = {
        'status': 'OK',
        'version': '2.1.7',
        'last_calibrated': '2023-11-05',
        'sensor_health': [98, 95, 100, 89]
    }
    return diagnostics

# Orchestration with misleading calls
if __name__ == '__main__':
    raw_data = fetch_raw_sensor_data()
    
    # Decoy decryption (unused)
    _ = decrypt_signal(raw_data)
    
    # Real filtering
    filtered_data = apply_noise_filter(raw_data)
    
    # Augmentation with distractor unpacking
    processed_segments = augment_data_segments(filtered_data)
    
    # Routing through active path
    routed_data, _ = route_data_stream(processed_segments, mode='primary')
    
    # Key transformation
    transformed_data, weight_metric = transform_sensor_stream(routed_data)
    
    # Configuration with plausible parameters
    config = {
        'base': 42.5,
        'mult': 3,
        'offset': -15,
        'debug_mode': False,
        'buffer_size': 1024
    }
    
    # Critical execution point
    final_output = process_transformed_data(transformed_data, config)
    
    # Irrelevant post-processing
    audit_trace = f"Final integrity: {sum(transformed_data) % 100}"
    
    print(f"Result: {final_output}")
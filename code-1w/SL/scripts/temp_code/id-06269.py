import itertools

# Simulate sensor data preprocessing with red herrings
def fetch_raw_sensor_data():
    return [18, 23, 14, 57, 29, 33, 41, 12]

def calculate_checksum(seq):
    # Irrelevant checksum function (dead-end)
    return sum(seq) % 101

def generate_frequency_map(data):
    # Misleading frequency analysis (not used in final path)
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    return freq

def apply_filtering_noise_reduction(signal):
    # Real but partially obfuscated transformation
    filtered = []
    for i, val in enumerate(signal):
        if i == 0 or i == len(signal) - 1:
            filtered.append(val // 2)
        else:
            neighbor_avg = (signal[i-1] + signal[i+1]) // 2
            filtered.append((val + neighbor_avg) // 2)
    return filtered

def extract_peaks_and_valleys(series):
    # Distractor: identifies peaks but not used in main logic
    peaks = []
    for i in range(1, len(series) - 1):
        if series[i-1] < series[i] > series[i+1]:
            peaks.append(series[i])
    return peaks or [0]

def compose_transformation_chain(raw_stream, mode='optimized'):
    # Core relevant transformation chain
    stage1 = [x * 2 for x in raw_stream]
    stage2 = [x for x in stage1 if x % 3 != 0]  # Filter non-multiples of 3
    stage3 = [x + 5 for i, x in enumerate(stage2) if i % 2 == 0]  # Only even indices + offset
    return stage3

def integrate_with_metadata(transformed, meta_config):
    # Mix in some config-based adjustment
    factor = meta_config.get('amplification', 1)
    offset = meta_config.get('base_offset', 0)
    return [(x + offset) * factor for x in transformed]

def evaluate_stability_metric(stream):
    # Decoy stability calculation
    if len(stream) < 2:
        return 0.0
    diffs = [abs(stream[i] - stream[i-1]) for i in range(1, len(stream))]
    return round(sum(diffs) / len(diffs), 4)

def finalize_secure_encoding(result_seq):
    # Another decoy encoding layer (unused)
    encoded = ''
    for num in result_seq:
        encoded += hex(num ^ 255)[-2:]
    return encoded

def process_transformations(pipeline_steps, settings):
    # Main execution path with embedded distractions
    raw_data = fetch_raw_sensor_data()
    
    # Irrelevant checksum call (red herring)
    _ = calculate_checksum(raw_data)
    
    # Real processing begins
    cleaned = apply_filtering_noise_reduction(raw_data)
    
    # Generate unused peak data (misdirection)
    _peaks = extract_peaks_and_valleys(cleaned)
    
    # Key transformation pipeline
    intermediate = compose_transformation_chain(cleaned, mode=settings['mode'])
    
    # Use of enumerate and zip (required Python feature)
    indexed = list(enumerate(intermediate))
    shifted = [x - 3 for x in intermediate[1:]] + [intermediate[0]]
    paired = list(zip(intermediate, shifted))
    
    # Actual contribution to final result
    combined_sum = sum(a * b for a, b in paired) // 4
    
    # Integration with config (relevant)
    integrated = integrate_with_metadata([combined_sum], settings)
    
    # Final accumulation using slicing (required feature)
    windowed_sums = [sum(integrated[i:i+2]) for i in range(len(integrated))]
    total_acc = sum(windowed_sums)
    
    # Dead code path: entropy calculation never used
    def calculate_entropy(arr):
        from math import log
        total = sum(arr)
        probs = [x / total for x in arr if x > 0]
        return -sum(p * log(p) for p in probs if p > 0)
    
    # Another distraction: unused itertools.product
    _grid = list(itertools.product([1, 2], ['a', 'b']))  # No effect
    
    # Final output derived from accumulated value
    final_output = total_acc * settings['scaling']
    
    # Print required output format
    print(f"Result: {final_output}")
    return final_output

# Configuration with meaningful parameters
config = {
    'mode': 'optimized',
    'scaling': 3,
    'amplification': 2,
    'base_offset': 7
}

data_pipeline = {
    'source': 'sensor_array_7',
    'version': '3.1.4',
    'calibration_needed': True
}

# Execute main function
final_output = process_transformations(data_pipeline, config)

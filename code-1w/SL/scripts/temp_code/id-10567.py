import math

# Simulated sensor data processing with embedded logic chain
def collect_samples(base_signal, noise_factor):
    samples = []
    for i in range(16):
        noise = (math.sin(i * 0.5) + math.cos(i * 0.3)) * noise_factor
        sample = base_signal[i % 8] + noise
        samples.append(round(sample, 3))
    return samples

# Irrelevant transformation - distractor
def apply_filter(data, kernel_size=3):
    filtered = data[:]
    for i in range(len(data)):
        window = []
        for j in range(-kernel_size//2, kernel_size//2 + 1):
            idx = (i + j) % len(data)
            window.append(data[idx])
        filtered[i] = round(sum(window) / len(window), 3)
    return filtered

# Data reshaping with bit manipulation red herring
def reshape_buffer(raw, chunk_size=4):
    buffer = []
    temp_chunk = []
    mask = 0b1111  # Unused bitmask - misleading
    shift_reg = 2  # Dead variable
    
    for val in raw:
        temp_chunk.append(abs(val) % 100)
        if len(temp_chunk) == chunk_size:
            buffer.append(temp_chunk)
            temp_chunk = []
    
    # Decoy bitwise operation
    decoy_checksum = 0
    for row in buffer:
        for item in row:
            decoy_checksum ^= int(item) & 0b1111
    
    return buffer

# Conditional mapping - partially relevant
config_map = {
    'mode': 'diagnostic',
    'thresholds': [0.5, 1.2, 2.8],
    'flags': {k: (k % 3 == 0) for k in range(10)},  # Dictionary distraction
    'weights': [1.0, 0.8, 0.6, 0.4]
}

# Core transformation function with hidden logic
def transform_signal(samples, mode='refined'):
    exponent_tracker = []
    transformed = []
    
    for x in samples:
        if x < 0:
            adjusted = abs(x) ** 0.7
        elif x == 0:
            adjusted = 0.1
        else:
            adjusted = x ** (1 + (x % 0.71))
        
        exponent_tracker.append(round(math.log(adjusted + 1e-5), 4) if adjusted > 0 else -10)
        transformed.append(round(adjusted, 3))
    
    # Dead computation path - looks important but unused
    outlier_score = sum(1 for e in exponent_tracker if e > 2.0)
    normalization_factor = max(transformed) or 1
    
    return transformed

# Main analysis with conditional branching and set operations
def analyze_pattern(grid, settings):
    flat_data = []
    for row in grid:
        flat_data.extend(row)
    
    # Set-based filtering - relevant
    unique_values = set(round(v, 1) for v in flat_data)
    threshold_set = {v for v in unique_values if v > 1.5}
    
    # Misleading statistical summary
    mean_val = sum(flat_data) / len(flat_data)
    variance = sum((x - mean_val) ** 2 for x in flat_data) / len(flat_data)
    entropy_proxy = -sum((v / 100) * math.log(v / 100 + 1e-6) for v in unique_values)  # Red herring
    
    # Critical logic chain
    control_flags = []
    for i, val in enumerate(flat_data):
        case_a = (val > 2.0) and (i % 2 == 0)
        case_b = (val < 0.5) and (math.isclose(val, round(val, 1), abs_tol=0.01))
        case_c = (val in threshold_set) and (val * 100) % 4 == 0
        
        if case_a:
            control_flags.append(3)
        elif case_b:
            control_flags.append(-1)
        elif case_c:
            control_flags.append(2)
        else:
            control_flags.append(1)
    
    # Integration step - key to answer
    accumulator = 0
    weight_sequence = settings['weights']
    for idx, flag in enumerate(control_flags):
        cycle_weight = weight_sequence[idx % len(weight_sequence)]
        accumulator += flag * cycle_weight * (idx % 4 + 1)
    
    # Final adjustment - deterministic
    final_score = int(round(accumulator * 1.75))
    
    # Secondary red herring: complex dictionary traversal with no effect
    nested_meta = {'level1': {'level2': {'level3': {'checksum': 0}}}}
    temp_key = 'level1'
    while temp_key in nested_meta:
        if 'level3' in nested_meta[temp_key]:
            nested_meta[temp_key]['level2']['level3']['checksum'] ^= 15
        temp_key = None
    
    return final_score

# Orchestration with irrelevant setup
base_waveform = [0.8, 1.1, 2.3, 0.4, 3.2, 1.9, 0.7, 2.8]
sensor_noise = 0.35

raw_readings = collect_samples(base_waveform, sensor_noise)
filtered_readings = apply_filter(raw_readings)  # Unused
structured_buffer = reshape_buffer(filtered_readings)
transformed_data = transform_signal(raw_readings)
reshaped_for_analysis = reshape_buffer(transformed_data, 4)

# Key execution point
final_diagnostic = analyze_pattern(reshaped_for_analysis, config_map)
print(f"Result: {final_diagnostic}")
import itertools

# Simulated sensor fusion module for environmental monitoring system
def collect_sensor_data():
    raw_timestamps = list(range(100, 200, 3))
    raw_values = [t * 0.7 + ((t % 13) ** 1.5) for t in raw_timestamps]
    return list(zip(raw_timestamps, raw_values))

# Irrelevant auxiliary function - dead code path
def deprecated_normalization(data):
    mean_val = sum([v for _, v in data]) / len(data)
    return [(t, (v - mean_val) / mean_val) for t, v in data]

# Data filtering with red herring logic
def filter_outliers(data, limit=50):
    filtered = []
    temp_buffer = []
    spike_count = 0

    for t, v in data:
        if v > 95:  # Rare condition never met in actual data
            spike_count += 1
            continue
        if t % 7 == 0:  # Decoy condition - looks meaningful but doesn't affect outcome
            temp_buffer.append(v)
        filtered.append((t, v))
    
    # Misleading post-processing that does nothing to final result
    if len(temp_buffer) > 10:
        avg_temp = sum(temp_buffer) / len(temp_buffer)
        adjusted = [v * 0.95 if v > avg_temp else v for v in temp_buffer]
    
    return filtered[:12]  # Truncate to fixed size - critical for downstream

# Bit manipulation decoy
def generate_checksum(n):
    chk = 0
    for i in range(n):
        chk ^= (i * 241) % 256
    return chk

# Unused transformation chain
def transform_sequence(seq):
    doubled = [x * 2 for x in seq]
    shifted = [(x >> 1) for x in doubled]
    return [x for x in shifted if x % 3 != 0]

# Core processing with hidden logic
def compute_adaptive_weight(length):
    weight = 1.0
    for i in range(2, length + 1):
        weight *= (i % 5) + 0.1
    return round(weight, 4)

# Main processing function with distractors
def process_readings(data, config_map):
    base_sum = 0
    square_trace = 0
    count = 0
    
    # Irrelevant intermediate structure
    history_log = {'first': data[0], 'last': data[-1], 'size': len(data)}
    
    # Redundant unpacking and re-packing
    timestamps, values = zip(*data)
    
    # Decoy statistical measures
    mean_value = sum(values) / len(values)
    variance_proxy = sum((v - mean_value) ** 2 for v in values) / len(values)
    
    # Actual relevant computation buried in noise
    for idx, (t, v) in enumerate(data):
        if idx % 2 == 0:
            base_sum += v * config_map['scale_factor']
        else:
            base_sum -= v * 0.1
        
        # Meaningless trace accumulation
        square_trace += v ** 2
        
        # Hidden modulo-dependent accumulator
        if (t + int(v)) % 4 == 0:
            count += 1
    
    # Critical calculation using combined metrics
    adjustment = compute_adaptive_weight(len(data))
    raw_diagnostic = base_sum * adjustment
    
    # Final transformation with misleading offset
    final_diagnostic = int(raw_diagnostic + 0.5) - (count * 2)
    
    # Dead return branch
    if square_trace < 0:
        return -1
    
    return final_diagnostic

# Auxiliary map generation with irrelevant complexity
def build_threshold_map(seed=777):
    config = {}
    running_key = seed
    
    for key in ['scale_factor', 'noise_floor', 'decay_rate', 'buffer_size']:
        running_key = (running_key * 17 + 257) % 1000
        if key == 'scale_factor':
            config[key] = round(running_key / 1000.0, 3)
        elif key == 'noise_floor':
            config[key] = running_key % 23
        else:
            config[key] = running_key % 10
    
    # Unused derived values
    magic_seq = [seed]
    for _ in range(5):
        magic_seq.append((magic_seq[-1] * 7 + 13) % 101)
    
    return config

# Entry point with distraction
if __name__ == '__main__':
    # Generate raw input
    all_readings = collect_sensor_data()
    
    # Unused alternate processing path
    if len(all_readings) > 50:
        sampled = all_readings[::2]
    else:
        sampled = all_readings
    
    # Apply filtering (critical step)
    filtered_data = filter_outliers(sampled)
    
    # Build configuration (only scale_factor is used)
    threshold_map = build_threshold_map(777)
    
    # Compute diagnostic checksum for log (irrelevant)
    log_checksum = generate_checksum(len(filtered_data))
    
    # Real work happens here
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Additional decoy computation
    compressed = list(itertools.accumulate([len(filtered_data), 3, 2], lambda x, y: (x + y) % 7))
    
    # Output required result
    print(f"Result: {final_diagnostic}")
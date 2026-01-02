import math

# Simulated sensor data stream with metadata
def generate_sensor_stream():
    raw_values = [18, 22, 15, 30, 12, 25, 19, 24, 17]
    timestamps = [1623456000 + i * 60 for i in range(len(raw_values))]
    return list(zip(timestamps, raw_values))

# Irrelevant helper: converts timestamp to readable format (unused)
def ts_to_readable(ts):
    hours = (ts // 3600) % 24
    minutes = (ts // 60) % 60
    return f'{hours:02d}:{minutes:02d}'

# Decoy function: appears useful but not used
def calculate_moving_avg(data, window=3):
    averages = []
    for i in range(len(data) - window + 1):
        avg = sum(data[i:i+window]) / window
        averages.append(round(avg, 2))
    return averages

# Unused statistical outlier detection
def is_outlier(value, mean, std_dev):
    return abs(value - mean) > 2 * std_dev

# Core processing function with multiple concepts
def process_data(data_stream, config):
    # Extract values from timestamped data
    values = [item[1] for item in data_stream]
    
    # Distractor variables
    temp_log = []
    cumulative_sum = 0
    peak_count = 0
    normalized_vals = []
    
    # Real computation begins
    threshold = config['threshold']
    scale_factor = config['scale']
    
    # Bit manipulation red herring
    magic_mask = 0b101010
    masked_values = [v ^ magic_mask for v in values]  # unused
    
    # Dictionary-based state tracking
    state_tracker = {
        'high': 0,
        'medium': 0,
        'low': 0
    }
    
    processed = []
    for val in values:
        # Update distractor
        cumulative_sum += val
        
        # Actual logic: categorize and transform
        if val > threshold:
            state_tracker['high'] += 1
            processed.append(int(val * scale_factor))
        elif val == threshold:
            state_tracker['medium'] += 1
            processed.append(val)
        else:
            state_tracker['low'] += 1
            processed.append(int(val // scale_factor) if scale_factor != 0 else val)
        
        # Distractor: log transformation that's never used
        if val > 0:
            temp_log.append(math.log(val))
    
    # Early return decoy (never triggers)
    if len(processed) > 100:
        return -1
    
    # Real path continues
    filtered = [p for p in processed if p % 2 == 1]  # keep only odd
    
    # Linear search for first large value
    limit = config['limit']
    first_large_index = -1
    for i, p in enumerate(filtered):
        if p > limit:
            first_large_index = i
            break  # early break
    
    # Final transformation
    result = 0
    for i, v in enumerate(filtered):
        if i % 2 == 0:  # even indices
            result += v * (i + 1)
        else:
            result -= v
    
    return result

# Configuration map (dictionary usage)
config_map = {
    'threshold': 18,
    'scale': 1.5,
    'limit': 20,
    'mode': 'aggressive',
    'version': '2.1'
}

# Dead code path: unused alternative config
alt_config = {
    'threshold': 20,
    'scale': 2.0,
    'limit': 25
}

# Generate stream
stream_buffer = generate_sensor_stream()

# Unused grouping operation
value_groups = {}
for ts, val in stream_buffer:
    bucket = val // 10
    if bucket not in value_groups:
        value_groups[bucket] = []
    value_groups[bucket].append(val)

# Key execution point
final_output = process_data(stream_buffer, config_map)

# Print result
print(f"Result: {final_output}")
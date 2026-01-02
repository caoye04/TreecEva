import math

# Simulated sensor data stream with metadata
def generate_sensor_stream():
    raw_values = [127, 255, 64, 192, 32]
    timestamps = [1638420000, 1638420001, 1638420002, 1638420003, 1638420004]
    return list(zip(raw_values, timestamps))

# Irrelevant helper: checksum validation (not used in final result)
def validate_checksum(data):
    total = 0
    for val in data:
        total ^= val[0]
    return total == 127

# Misleading transformation chain
def transform_signal(signal):
    amplified = [s << 2 for s in signal]  # Amplify by bit shift
    filtered = [a for a in amplified if a > 200]
    normalized = [f / 255.0 for f in filtered]
    return sum(normalized)  # Dead-end computation

def decode_frame(frame):
    value, ts = frame
    phase = ts % 8
    if phase < 4:
        return value & 0x7F
    else:
        return (value >> 4) ^ 0x0A

# Core processing with distractors
def analyze_pattern(sequence):
    count_map = {}
    for item in sequence:
        count_map[item] = count_map.get(item, 0) + 1
    
    # Distractor: unused statistical analysis
    avg = sum(count_map.values()) / len(count_map) if count_map else 0
    variance_proxy = sum((v - avg) ** 2 for v in count_map.values())
    
    # Relevant logic: find dominant pattern
    if count_map:
        return max(count_map.keys())
    return 0

# Conditional expression and dictionary usage (required features)
def build_lookup(base_keys):
    lookup = {k: {'level': k >> 4, 'class': 'A' if k % 2 == 0 else 'B'} for k in base_keys}
    return lookup if len(lookup) > 3 else {'default': {'level': 0, 'class': 'Z'}}

def extract_features(values):
    feature_set = []
    for v in values:
        sign_bit = (v >> 7) & 1
        magnitude = v & 0x7F
        category = 'high' if magnitude >= 64 else 'low'
        feature_set.append({
            'raw': v,
            'sign': sign_bit,
            'mag': magnitude,
            'cat': category,
            'squared': magnitude * magnitude  # Distractor field
        })
    return feature_set

# Main processing pipeline
def process_data(data_stream, config):
    decoded = []
    for packet in data_stream:
        decoded_val = decode_frame(packet)
        decoded.append(decoded_val)
    
    # Extract magnitudes only
    magnitudes = [d & 0x7F for d in decoded]
    
    # Apply dynamic threshold based on config
    threshold = config.get('threshold', 50)
    filtered = [m for m in magnitudes if m > threshold]
    
    # Accumulate with modular arithmetic
    accumulator = 0
    for val in filtered:
        accumulator = (accumulator + val * 3) % 997
    
    # Conditional expression integration
    scaling_factor = 2.5 if config['mode'] == 'turbo' else 1.0
    adjusted = accumulator * scaling_factor
    
    # Dictionary-based state tracking
    state_log = build_lookup(magnitudes)
    state_size = len(state_log)  # Irrelevant metric
    
    # Secondary processing chain (mostly dead code)
    features = extract_features(decoded)
    total_squared = sum(f['squared'] for f in features)  # Red herring
    signal_strength = transform_signal([f['raw'] for f in features])  # Unused
    
    # Final decision logic
    if len(filtered) >= 2:
        trend = (filtered[-1] - filtered[0]) // len(filtered)
        adjusted += trend * 10
    
    # Key output calculation
    raw_result = int(adjusted) % 10000
    final_output = raw_result if raw_result != 0 else 999
    
    # Print required output
    print(f"Result: {final_output}")
    return final_output

# Entry point
if __name__ == '__main__':
    stream_buffer = generate_sensor_stream()
    
    # Distractor configuration set
    decoy_config = {
        'threshold': 1000,  # Never reached
        'debug': True,
        'mode': 'normal',
        'timeout': 30
    }
    
    # Actual active config
    config = {
        'threshold': 40,
        'mode': 'turbo',
        'version': '2.1'
    }
    
    # Spurious function calls (dead code paths)
    _ = validate_checksum(stream_buffer)
    _ = analyze_pattern([x[0] for x in stream_buffer])
    
    final_output = process_data(stream_buffer, config)
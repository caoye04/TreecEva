import math

# Simulated sensor data processing with red herrings
def preprocess_chunk(data_slice):
    magnitude = sum(x ** 2 for x in data_slice) ** 0.5
    normalized = [x / (magnitude + 1e-9) for x in data_slice]
    return [round(x * 100) for x in normalized]

# Irrelevant transformation - decoy function
def frequency_shift(signal, factor=1.5):
    return [int(x * factor) % 256 for x in signal]

# Unused helper - dead code path
def legacy_encode(data):
    encoded = 0
    for i, val in enumerate(data):
        encoded += val << (i % 8)
    return encoded

# Core analysis function with key logic interwoven with distractions
def analyze_signal(buffer, config_map):
    # Distractor variables
    temp_snapshot = buffer[::2]  # unused slicing
    debug_trace = []
    accumulator = 0
    
    # Real logic begins: detect pulse sequences
    pulse_count = 0
    for i in range(1, len(buffer) - 1):
        if buffer[i] > config_map['high'] and buffer[i-1] <= config_map['high']:
            pulse_count += 1
            debug_trace.append(i)  # logged but not used
    
    # Secondary condition chain with misleading intermediate
    baseline = sum(buffer[:len(buffer)//4]) / (len(buffer)//4)
    adjusted_baseline = baseline * 1.15  # distractor calculation
    deviation_score = 0
    for val in buffer:
        if val > baseline * 1.2:
            deviation_score += 1
    
    # Critical decision path
    if pulse_count >= 3:
        candidate_region = buffer[5:15]  # slice of interest
        smoothed = [sum(candidate_region[i:i+3])/3 for i in range(len(candidate_region)-2)]
        peak = max(smoothed)
        category_index = 2 if peak > 45 else 1
    else:
        category_index = 0
    
    # Tertiary computation with red herring control flow
    metadata_flag = False
    for k, v in config_map.items():
        if k.startswith('debug') and v == True:
            metadata_flag = True
            break

    # Actual answer derivation - depends only on pulse_count and baseline
    stability_factor = math.cos(math.radians(deviation_score))
    raw_diagnostic = (pulse_count * 1000) + int(baseline)
    
    # Final mapping - this is where the real answer is formed
    final_diagnostic = raw_diagnostic - int(stability_factor * 100)
    
    # Extraneous post-processing
    checksum = sum(final_diagnostic.to_bytes(3, 'little'))
    encrypted_result = (final_diagnostic ^ 0xAA) + checksum  # decoy output
    
    return final_diagnostic  # Only this matters

# Main execution block
if __name__ == '__main__':
    # Initialize sensor-like input
    pattern_buffer = [
        12, 15, 23, 35, 41, 48, 55, 60, 52, 45,
        30, 38, 47, 58, 62, 50, 40, 28, 20, 18
    ]
    
    # Configuration map with irrelevant fields
    threshold_map = {
        'high': 45,
        'low': 20,
        'window': 5,
        'debug_mode': False,
        'version': '2.1',
        'calibration_needed': True,
        'sample_rate': 1000
    }
    
    # Decoy data transformations
    processed_chunk = preprocess_chunk(pattern_buffer[:8])
    shifted_signal = frequency_shift(processed_chunk, 1.7)
    legacy_hash = legacy_encode(shifted_signal[:6])
    
    # Key statement
    final_diagnostic = analyze_signal(pattern_buffer, threshold_map)
    
    # Output the target result
    print(f"Result: {final_diagnostic}")
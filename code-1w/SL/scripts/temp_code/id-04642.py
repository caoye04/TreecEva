import math

# Simulated sensor data processing with red herrings
def analyze_readings(raw_data):
    temp_buffer = [x for x in raw_data if x > 0]
    filtered = list(map(lambda x: x * 1.05, temp_buffer))
    shifted = [filtered[i] << 1 for i in range(len(filtered)) if i % 2 == 0]  # Bit manipulation red herring
    return shifted[:len(filtered)//2]

# Irrelevant audio processing decoy function
def process_audio(signal):
    if len(signal) == 0:
        return [0]
    fft_peaks = [abs(x) ** 2 for x in signal]
    return sorted(fft_peaks, reverse=True)[:3]

# Core diagnostic logic buried in distractions
def compute_diagnostic(sensor_log, threshold=150):
    # Distractor variables
    baseline_offset = 789
    calibration_sequence = [i**2 for i in range(5)]
    checksum = sum(calibration_sequence) % 100

    # Real computation begins
    valid_entries = [x for x in sensor_log if isinstance(x, int) and x >= 0]
    capped_values = [min(val, 255) for val in valid_entries]
    
    # Conditional expression with slicing distraction
    processed = capped_values[::2] if len(capped_values) > 10 else capped_values[::-1]
    
    # Decoy statistical operations
    mean_val = sum(processed) / len(processed) if processed else 0
    variance_proxy = sum([(x - mean_val)**2 for x in processed]) / len(processed) if processed else 0
    entropy_approx = -math.log(variance_proxy) if variance_proxy > 0 else 0

    # Actual critical path
    trigger_points = [x for x in processed if x > threshold]
    activation_count = len(trigger_points)
    
    # Logical operation chain with short-circuiting (distraction)
    flag = (activation_count > 3) and (variance_proxy < 1000) or (entropy_approx > 1.5)
    
    # Key calculation buried in noise
    aggregate_score = sum(trigger_points) >> 1  # Right shift as subtle op
    
    # More irrelevant code
    metadata_tags = ['sensor_v2', 'diag_mode', 'encrypt_off']
    tag_hash = sum([len(tag) for tag in metadata_tags])
    audit_trail = {f'entry_{i}': i*2 for i in range(8)}

    # Correction based on bit count (actual dependency)
    bit_population = bin(activation_count).count('1')
    correction_factor = bit_population * 17
    
    # Dead code path - never executed due to fixed input
    if __debug__ and False:
        debug_dump = {'raw': sensor_log, 'offset': baseline_offset}
        return -1

    final_diagnostic = aggregate_score + correction_factor
    return final_diagnostic

# Unused helper functions to increase interference
def serialize_packet(data):
    return ''.join([format(x, '02x') for x in data])

def validate_checksum(stream):
    return len(stream) % 2 == 0

# Simulated input with mixed types and noise
input_stream = [120, -5, 180, 'corrupted', 210, 95, 260, 130, 170, 88, 240, 110, 190]

# Execution with decoy calls
_ = process_audio([1+2j, -3-4j, 5+6j])
_ = analyze_readings([10, 20, 30, 40])

# Critical execution point
result = compute_diagnostic(input_stream)
print(f"Result: {result}")
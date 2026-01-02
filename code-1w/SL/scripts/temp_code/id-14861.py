from collections import defaultdict, Counter

# System calibration constants (irrelevant to final result)
CALIBRATION_OFFSET = 0.00314
REFERENCE_VOLTAGE = 3.3
MAX_BUFFER_SIZE = 1024

# Simulated sensor input data (some values are decoys)
sensor_a = [1, 0, 1, 1]
sensor_b = [0, 1, 1, 0]
sensor_c = [1, 1, 0, 0]  # Unused sensor
timestamp_log = [1623456789, 1623456790, 1623456791, 1623456792]

# Signal encoding configuration (only some mappings are used)
encoding_map = defaultdict(int)
encoding_map.update({
    (1, 0): 3,
    (0, 1): 5,
    (1, 1): 9,  # This value is never accessed
    (0, 0): 0   # Dead code path
})

# Noise filter mask (distractor computation)
noise_profile = [x ^ 0b10 for x in sensor_a]
filtered_noise = [n & 0b01 for n in noise_profile]
smoothed_data = sum(filtered_noise) * CALIBRATION_OFFSET  # Irrelevant result

# Construct signal stack from active sensors (core logic begins)
signal_stack = []
for i in range(len(sensor_a)):
    if sensor_a[i] == 1 and sensor_b[i] == 1:
        signal_stack.append(2)  # Special case overlap
    elif sensor_a[i] == 1 or sensor_b[i] == 1:
        # Determine pair encoding
        key_pair = (sensor_a[i], sensor_b[i])
        encoded_val = encoding_map[key_pair]
        signal_stack.append(encoded_val)
    else:
        signal_stack.append(-1)  # Silence marker

# Decoy transformation (never invoked)
def transform_legacy(data):
    return [d * 2 + 1 for d in data if d > 0]

# Redundant validation check (no side effects)
validation_counter = Counter(signal_stack)
invalid_count = validation_counter[-1]
dropped_pairs = len(timestamp_log) - len(signal_stack)

# Core processing function
def process_transmission(signals, encoding):
    aggregate = 0
    shift_factor = 1
    
    # Accumulate weighted signal values
    for val in reversed(signals):
        if val > 0:
            aggregate += val * shift_factor
            shift_factor <<= 1  # Exponential growth via bit shift
        elif val == 2:
            aggregate += 7  # Override rule for overlapping signals
        else:
            aggregate -= 1  # Penalty for silence
    
    # Spurious internal calculation (distraction)
    temp_ratio = aggregate / (len(signals) + 0.1)
    normalized = int(temp_ratio * REFERENCE_VOLTAGE)
    
    # Final adjustment based on pattern frequency (only uses aggregate)
    freq_stats = Counter(signals)
    mode_value = max(freq_stats, key=freq_stats.get)
    
    # Actual final computation
    if mode_value == 5:
        result = aggregate * 3
    elif mode_value == 3:
        result = aggregate * 2
    else:
        result = aggregate + 10
    
    return result

# Execute main logic
temp_buffer = [x for x in signal_stack if x != -1]  # Unused buffer
scaling_factor = MAX_BUFFER_SIZE >> 10  # Equals 1, irrelevant

final_signal = process_transmission(signal_stack, encoding_map)

# Output result
print(f"Result: {final_signal}")
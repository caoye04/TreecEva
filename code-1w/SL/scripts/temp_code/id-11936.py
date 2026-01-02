import math

# Irrelevant helper function (dead code path)
def unused_signal_transform(data):
    return [math.sin(x) * math.cos(x) for x in data]

# Decoy function that looks relevant but is never called
def analyze_pattern(seq):
    magnitude = sum([abs(x) for x in seq]) / len(seq)
    return magnitude > 5

# Function with slicing and modular arithmetic
def extract_features(signal, stride=3):
    features = []
    for i in range(0, len(signal) - 4, stride):
        segment = signal[i:i+5]
        # Bitwise distraction
        magic_key = (segment[0] ^ segment[2]) & 7
        if magic_key == 3:
            features.append(sum(segment) % 11)
    return features

# Another red herring: complex transformation not used in main flow
temp_log = []
for t in range(6):
    temp_log.append(int(math.exp(t) % 100))

# Real processing chain starts here
def preprocess_stream(raw_input):
    cleaned = []
    for val in raw_input:
        if val < 0:
            continue
        if val % 2 == 0:
            cleaned.append(val // 2)
        else:
            cleaned.append(val * 3 + 1)
    return cleaned[1:-1]  # Slicing: remove first and last

# Data corruption simulation (unused)
corrupted_copy = [x ^ 0xF for x in [10, 20, 30, 40]]

# Core logic buried among distractions
def validate_frame(frame):
    checksum = 0
    for i, v in enumerate(frame):
        checksum += v * (i + 1)
    return checksum % 13 == 0

# Main processing with early return and conditional branching
def process_segment(buffer, size):
    if len(buffer) < size:
        return -1
    
    # Multiple distractor variables
    shadow_accum = 0
    temp_offset = 0
    for j in range(len(buffer)):
        shadow_accum += buffer[j] * (j % 4)
        
    # Real computation hidden here
    active_window = buffer[:size]
    window_sum = sum(active_window)
    
    # Conditional branch with short-circuit evaluation
    if size > 4 and (window_sum % 5 == 0 or True):
        window_sum -= 5
    
    # More decoy operations
    dummy_shift = (window_sum << 2) >> 1
    
    # Key manipulation using modular arithmetic and bit flip
    result = (window_sum ^ 0xAA) % 1000
    
    # Early return to mislead control flow analysis
    if result < 0:
        return 0
        
    return result

# Simulated sensor data (real input)
sensor_readings = [18, 7, 14, 3, 22, 9, 4]

# Apply preprocessing (this modifies the data meaningfully)
filtered_data = preprocess_stream(sensor_readings)  # becomes [3, 14, 3, 22] -> then [14, 3]

# Dead assignment - misleading
baseline_ref = sum(filtered_data) // len(filtered_data)

# Setup for actual computation
config_flags = [True, False, True]
window_size = len(filtered_data)  # evaluates to 2

# Use slicing to extract middle part
temp_buffer = filtered_data[::window_size]  # [14, 3] with step 2 -> [14]

# Fill with decoy values?
if len(temp_buffer) < 2:
    temp_buffer.extend([1] * (2 - len(temp_buffer)))  # Now [14, 1]

# This is the key execution point
final_output = process_segment(temp_buffer, window_size)

# Print required output
print(f"Target result: {final_output}")
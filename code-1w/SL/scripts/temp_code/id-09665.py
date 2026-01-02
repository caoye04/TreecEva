import math

# Simulated sensor data processing system
# Complex logic with extensive distractors and irrelevant computations

def preprocess_chunk(data_slice, config):
    temp_norm = 0
    for val in data_slice:
        temp_norm += val ** 2
    magnitude = math.sqrt(temp_norm)
    normalized = [x / magnitude for x in data_slice]
    return normalized

# Irrelevant helper - decoy function (never used in critical path)
def compute_entropy(vector):
    entropy = 0.0
    total = sum(vector)
    if total == 0:
        return 0
    for x in vector:
        prob = x / total
        if prob > 0:
            entropy -= prob * math.log(prob)
    return entropy

# Unused transformation matrix (red herring)
transform_kernel = [
    [0.25, 0.5, 0.25],
    [0.5,  1.0, 0.5],
    [0.25, 0.5, 0.25]
]

# Fake calibration routine (dead code path)
def calibrate_sensor(signal, level=2):
    if level == 1:
        return [x * 0.98 for x in signal]
    elif level == 2:
        return [x * 1.02 for x in signal]
    else:
        return signal

# Misleading intermediate diagnostic flags (distractors)
anomaly_flag_1 = False
anomaly_flag_2 = True
warning_level = 'GREEN'
checksum_pass = 1

# Real processing begins here
raw_samples = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Apply slicing to extract working segment (key python feature)
pattern_buffer = raw_samples[2:9]  # Extracts [4, 1, 5, 9, 2, 6, 5]

# Multiple irrelevant transformations on unused variables
shifted_view = raw_samples[1::2]  # [1, 1, 9, 6, 3] - not used later
decimated_data = raw_samples[::3]  # [3, 1, 2, 3] - dead end

# Threshold mapping with dummy entries (only specific keys matter)
threshold_map = {
    'low': 1.5,
    'medium': 4.0,  # This is used
    'high': 7.5,
    'critical': 10.0,
    'baseline': 0.0,
    'gain': 1.2,
    'offset': -0.5
}

# Secondary buffer with redundant computation
filtered_stream = []
for x in pattern_buffer:
    if x > threshold_map['low']:
        filtered_stream.append(x * 0.85)

# Another decoy accumulator (looks important but isn't)
energy_accumulator = 0
for val in raw_samples:
    energy_accumulator += abs(val) * math.sin(val % 3)

# Real analysis function buried among distractions
def analyze_signal(seq, thresholds):
    medium_threshold = thresholds['medium']
    count_above = 0
    sum_enhanced = 0.0
    
    # First real logic step: count elements above medium threshold
    for num in seq:
        if num > medium_threshold:
            count_above += 1
    
    # Second: apply transform and accumulate
    for i, num in enumerate(seq):
        if i % 2 == 0:  # Only even indices
            adjusted = num * 1.1
        else:
            adjusted = num * 0.9
        sum_enhanced += adjusted
    
    # Third: use slicing again to isolate center region
    center_portion = seq[1:-1]  # Exclude first and last
    center_avg = sum(center_portion) / len(center_portion)
    
    # Fourth: combine metrics into final score
    # Formula: (count_above * 100) + floor(sum_enhanced) - round(center_avg * 10)
    part_a = count_above * 100
    part_b = int(sum_enhanced)  # Floor via int truncation
    part_c = round(center_avg * 10)
    
    # Final diagnostic calculation
    result = part_a + part_b - part_c
    
    # Dead code branch inside function (misleading)
    if result < 0:
        return 0  # Never reached
    
    return result

# Global state distraction
system_uptime = 1274
last_calibration = '2023-11-05'

# Key execution point
final_diagnostic = analyze_signal(pattern_buffer, threshold_map)

# Additional red herring computation
spectral_index = 0
for i in range(len(pattern_buffer)):
    spectral_index += pattern_buffer[i] * (i + 1) ** 0.5

# What matters is printed at the end
print(f"Result: {final_diagnostic}")
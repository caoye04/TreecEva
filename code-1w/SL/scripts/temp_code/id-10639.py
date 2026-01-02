def preprocess_signal(raw_input, offset):
    adjusted = [x + offset for x in raw_input]
    filtered = []
    for val in adjusted:
        if val > 0:
            filtered.append(val ** 0.5)
    return filtered

# Irrelevant helper (dead function - red herring)
def compute_entropy(data):
    import math
    total = sum(data)
    entropy = 0
    for x in data:
        p = x / total
        entropy -= p * math.log2(p)
    return entropy

# Unused transformation chain
def obsolete_transform(seq):
    return [seq[i] ^ seq[(i+1)%len(seq)] for i in range(len(seq))]

# Core analysis function
def analyze_pattern(data, threshold):
    temp_result = 0
    history = []
    
    # Complex nested logic with distractors
    for i in range(len(data)):
        shifted_val = data[i] * (i + 1)
        if i % 2 == 0:
            shifted_val -= len(history)  # minor adjustment
        else:
            shifted_val += 1.5
            
        # Distractor: complex-looking but unused calculation
        decoy_accum = 0
        for j in range(1, min(i+2, 5)):
            decoy_accum += (shifted_val / j) % 3
        
        # Real logic branch
        if shifted_val > threshold:
            temp_result += int(shifted_val)
            history.append(shifted_val)
        elif shifted_val > 5:
            temp_result += 2  # small bonus
    
    # Secondary processing on history (relevant)
    if len(history) > 2:
        sorted_hist = sorted(history, reverse=True)
        mid_val = sorted_hist[len(sorted_hist)//2]
        temp_result -= int(mid_val // 2)
    
    return int(temp_result)

# Decoy data structure (unused)
system_config = {
    'version': '2.1.9',
    'mode': 'diagnostic',
    'flags': [0, 1, 1, 0],
    'checksum': 0xDEADBEEF
}

# Multiple irrelevant variables
buffer_size = 4096
retry_limit = 3
timeout_ms = 1500
padding_char = '*'  # never used

# Input data with misleading comment
raw_sensor_data = [2, 3, 1, 4, 2, 5]  # Simulated IoT sensor array (primes are noise)

# Unused transformation path
decimated = raw_sensor_data[::2]

# Key threshold - looks arbitrary but is critical
calibration_factor = sum([x*x for x in raw_sensor_data]) // 8
key_threshold = calibration_factor - 3

# Signal preprocessing (relevant)
offset_correction = -1
transformed_data = preprocess_signal(raw_sensor_data, offset_correction)

# Dummy statistical check (never executed)
defensive_mode = False
if sum(transformed_data) > 20 and defensive_mode:
    transformed_data = [x * 0.9 for x in transformed_data]

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, key_threshold)

# Print result as required
print(f"Result: {final_diagnostic}")
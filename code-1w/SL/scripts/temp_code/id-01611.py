import math

# Simulated sensor array data processing with diagnostic logic
def preprocess_sensor_readings(raw_readings):
    processed = []
    noise_floor = 0.041
    scaling_factor = 1.87
    for val in raw_readings:
        if abs(val) > noise_floor:
            processed.append(abs(val) ** 0.5 * scaling_factor)
    return [round(p, 3) for p in processed]


def generate_frequency_bands(signal):
    # Irrelevant frequency analysis (distractor)
    bands = {'low': 0, 'mid': 0, 'high': 0}
    for s in signal:
        if s < 1.0:
            bands['low'] += 1
        elif s < 2.0:
            bands['mid'] += 1
        else:
            bands['high'] += 1
    return bands

# Dead function - never called but looks important
def legacy_compatibility_layer(data):
    return [x | 2 for x in data if x % 3 == 0]

# Decoy transformation chain
def encrypt_sequence(seq):
    encrypted = []
    for i, v in enumerate(seq):
        encrypted.append(v ^ (i + 1) * 3)
    return encrypted

# Core bit manipulation and filtering
def extract_significant_bits(values):
    result = 0
    bit_weights = [1, 2, 4, 8, 16]
    temp_accum = 0
    for i, v in enumerate(values):
        truncated = int(v * 100) % 64
        if truncated & 8:  # Check if 4th bit is set
            temp_accum += bit_weights[i % 5]
    # Complex conditional bit setting
    if temp_accum > 10:
        result |= 32
    if temp_accum % 3 == 0:
        result |= 64
    result |= (temp_accum & 7)  # Add lower 3 bits
    return result

# Higher-order function with lambda (required feature)
def create_filter(threshold):
    return lambda x: x > threshold

# Main signal analyzer combining multiple concepts
def analyze_signal(data, config_map):
    # Nested conditionals and data transformations
    filtered = []
    t1 = config_map['t1']
    t2 = config_map['t2']
    filter_func = create_filter(t1)
    
    for d in data:
        if filter_func(d):
            filtered.append(d * 1.1)
    
    secondary_check = [f for f in filtered if f < t2]
    
    if len(secondary_check) == 0:
        base_score = 13
    else:
        base_score = int(sum(secondary_check) / len(secondary_check))
    
    # String-based switch (required string method usage)
    mode = "dynamic_enhanced_v2".split('_')[1].upper()
    enhancement = 0
    
    if 'DYN' in mode:
        enhancement = 5
    elif 'STAT' in mode:
        enhancement = 2
    
    # Red herring: complex-looking but unused calculation
    decoy_entropy = 0
    for i in range(len(data)):
        decoy_entropy += (data[i] * 7.3) % 3.1
        decoy_entropy = round(decoy_entropy, 2)
    
    # Critical path: bit manipulation determines final outcome
    bit_analysis = extract_significant_bits(data)
    
    # Final computation with multiple dependencies
    raw_component = base_score * 100
    bit_component = (bit_analysis & 96) >> 5  # Extract bits 5-6
    final_component = raw_component + bit_component * 10 + enhancement
    
    # Misleading intermediate that seems important
    diagnostic_checksum = sum(data) + bit_analysis - base_score
    
    return final_component

# Global constants and dummy data
REFERENCE_VOLTAGES = [0.12, 0.35, 0.88, 1.05, 0.09, 0.73, 1.21, 0.67]
CALIBRATION_OFFSETS = [0.01, -0.02, 0.005, 0.03, -0.01]

# Unused transformation pipeline (distractor)
transform_chain = [
    lambda x: x + 0.05,
    lambda x: x * 1.2 if x > 0.5 else x * 0.8,
    lambda x: round(x, 2)
]

# Simulate raw input
raw_sensor_data = [0.11, 0.33, 0.91, 1.02, 0.08, 0.75, 1.19, 0.69]
processed_signal = preprocess_sensor_readings(raw_sensor_data)

# Frequency analysis - irrelevant to final result
frequency_profile = generate_frequency_bands(processed_signal)

# Compression that affects final outcome
compressed_data = [round(math.log(p + 1) * 2.3, 3) for p in processed_signal]

# Threshold configuration used in analysis
threshold_map = {
    't1': 0.65,
    't2': 1.85,
    't3': 2.1
}

# Unused encrypted version (red herring)
encrypted_features = encrypt_sequence([int(c * 100) for c in compressed_data])

# Key statement
final_diagnostic = analyze_signal(compressed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")
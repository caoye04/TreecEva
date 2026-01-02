import math

# Simulated sensor array data from a distributed monitoring system
def fetch_sensor_data():
    raw_values = [248, 173, 94, 56, 201, 137, 88, 42, 195, 152]
    return [x * 1.07 for x in raw_values]  # Apply calibration factor

# Legacy normalization (unused but looks relevant)
def legacy_normalize(data):
    mean_val = sum(data) / len(data)
    return [(x - mean_val) / mean_val for x in data]

# Signal conditioning with multiple red herrings
def preprocess_signal(raw_readings):
    threshold = 100.0
    adjusted = []
    outliers = []
    temp_log = []  # Distractor: collected but unused

    for val in raw_readings:
        if val > threshold:
            adjusted.append(int(val // 1.5))  # Reduce high values
        else:
            adjusted.append(int(val * 1.1))

        # Bit manipulation decoy
        bit_shifted = (int(val) & 255) ^ 170
        temp_log.append(hex(bit_shifted))

        # Unused outlier tracking
        if abs(val - 150) > 75:
            outliers.append(val)

    return adjusted

# Complex transformation with list comprehension and filtering
def transform_frame(signal_chunk):
    # Apply sine-based correction (simulates frequency alignment)
    corrected = [round(math.sin(x / 100) * x, 2) for x in signal_chunk]
    
    # Filter using modular condition (only every 3rd passes?)
    filtered = []
    for i, val in enumerate(corrected):
        if i % 3 == 0:
            filtered.append(abs(val))
    
    # Dummy string operation to add distraction
    status_flag = "PASS" if len(filtered) > 3 else "FAIL"
    flag_bits = ''.join([bin(ord(c))[2:] for c in status_flag])  # Unused encoding
    
    return filtered

# Hash-based consistency check (distractor function - never called)
def verify_integrity(data_list):
    checksum = 0
    for item in data_list:
        checksum = (checksum * 31 + int(item)) % 10007
    return format(checksum, 'x')

# Main analysis pipeline
processed_cache = {}

def analyze_readings(validated_input):
    cumulative_score = 0.0
    
    # Unrelated sorting (looks important but not used in result)
    sorted_inputs = sorted(validated_input, reverse=True)
    ranked_deltas = [sorted_inputs[i] - sorted_inputs[i+1] for i in range(len(sorted_inputs)-1)]
    median_gap = ranked_deltas[len(ranked_deltas)//2] if ranked_deltas else 0
    
    # Real computation path
    for reading in validated_input:
        if reading < 50:
            contribution = reading ** 1.5
        elif reading < 120:
            contribution = reading * 1.8
        else:
            # Dominant path: uses bitwise masking and set logic
            masked = int(reading) & 0xFF  # Keep lower byte
            shift_key = (masked >> 4) ^ 0xA  # Nibble shift + XOR key
            base_factor = (shift_key * 3.7) % 25.0
            
            # Use of set operations (intersection decoy)
            ref_set = {1, 3, 5, 7, 9, 11}
            key_set = {shift_key % 12} | {base_factor % 10}
            bonus = 7.5 if len(ref_set & key_set) > 0 else 0
            
            contribution = base_factor + bonus
            
        cumulative_score += contribution
    
    # Secondary adjustment using string-derived key (distraction)
    control_key = "DYNAMIC_TUNE"
    adjustment_factor = sum([ord(c) % 7 for c in control_key]) / len(control_key)
    
    # Final nonlinear scaling
    final_value = math.log(cumulative_score + 10) * 4.2
    
    # Dead code: formatted report never used
    report_lines = [
        f"Reading: {validated_input[i]}, Norm: {round(math.log(v+1),2)}"
        for i, v in enumerate(validated_input)
    ]
    
    return round(final_value, 6)

# Execution flow
if __name__ == '__main__':
    raw_sensor_stream = fetch_sensor_data()
    processed_signals = preprocess_signal(raw_sensor_stream)
    refined_frame = transform_frame(processed_signals)
    
    # Critical assignment point
    final_diagnostic = analyze_readings(processed_signals)
    
    # Print target result
    print(f"Target result: {final_diagnostic}")
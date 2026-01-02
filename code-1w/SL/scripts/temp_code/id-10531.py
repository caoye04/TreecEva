def preprocess_signal(raw_input):
    # Irrelevant transformation (distractor)
    temp_adjusted = [x * 1.05 for x in raw_input]
    offset_compensated = [x - 0.5 for x in temp_adjusted]
    filtered_noise = [x for x in offset_compensated if abs(x) > 0.1]
    
    # Key computation path
    magnitude_series = [abs(x) for x in raw_input]
    squared_envelope = [x**2 for x in magnitude_series]
    energy_integral = sum(squared_envelope)

    # Dead code path - never used (red herring)
    def deprecated_normalizer(val):
        return val / (max(val, 1))
    
    # Unused variables (distractors)
    peak_amplitude = max(magnitude_series)
    avg_power = energy_integral / len(raw_input)
    
    return energy_integral


def encode_sequence(seq):
    # String manipulation - required Python feature
    seq_str = ''.join(map(str, seq))
    rotated = seq_str[2:] + seq_str[:2]  # slicing operation
    inverted = rotated[::-1]  # reverse string
    checksum = sum(int(d) for d in inverted[::2])
    
    # Decoy logic with no impact
    if len(inverted) > 10:
        padding = '0' * (len(inverted) % 4)
        inverted += padding
    
    # Actual useful result
    encoded_value = int(inverted[:6]) if len(inverted) >= 6 else int(inverted + '0'*(6-len(inverted)))
    return encoded_value


def transform_dataset(data):
    # Apply bit manipulation (paradigm mix)
    bitwise_shifted = [(x << 1) ^ 0b101 for x in data]
    masked_values = [x & 0xFF for x in bitwise_shifted]  # keep lower 8 bits
    
    # Conditional filtering (control flow)
    processed = []
    for val in masked_values:
        if val % 3 == 0:
            processed.append(val + 1)
        elif val % 5 == 0:
            processed.append(val * 2)
        else:
            processed.append(val)
    
    # More irrelevant operations
    baseline_reference = sum(processed) // len(processed)
    deviation_map = [abs(x - baseline_reference) for x in processed]
    
    # Only this line matters for downstream
    final_state = sum(processed[i] * (i+1) for i in range(len(processed)))
    
    return final_state


def analyze_pattern(diagnostic_input):
    # Complex condition chain
    if isinstance(diagnostic_input, int):
        hex_trace = hex(diagnostic_input)[2:]
        char_count = {c: hex_trace.count(c) for c in set(hex_trace)}
        
        # String slicing and method usage
        segment_a = hex_trace[:len(hex_trace)//2]
        segment_b = hex_trace[len(hex_trace)//2:]
        
        # Logical comparison with decoy expressions
        xor_sum = 0
        for i, c in enumerate(segment_a):
            if c in 'abcdef':
                xor_sum ^= int(c, 16) + i
        
        # Critical decision point
        if sum(char_count.values()) > 5 and 'a' in char_count:
            result_flag = 1
        else:
            result_flag = 0
        
        # Final computation - depends only on original input structure
        base_factor = diagnostic_input >> 4
        adjustment = len(segment_b) * result_flag
        outcome = base_factor - adjustment
        
        # Distractor: unused complex expression
        entropy_metric = -sum((count/len(hex_trace)) * __import__('math').log(count/len(hex_trace)) 
                             for count in char_count.values()) if len(char_count) > 1 else 0.0
        
        return outcome
    
    return -999

# Main execution flow
if __name__ == '__main__':
    # Initial dataset
    sensor_readings = [3, 7, 8, 12, 15, 16, 20, 23]
    
    # Irrelevant preprocessing (distractor)
    calibrated = [x + 2 for x in sensor_readings]
    normalized = [x / max(calibrated) for x in calibrated]
    discretized = [int(x * 10) for x in normalized]
    
    # Key signal processing path
    signal_energy = preprocess_signal(sensor_readings)
    
    # Encoding side-path (dead end)
    token_code = encode_sequence(discretized)
    verification_key = token_code ^ 0xFFFF
    
    # Core transformation
    transformed_data = transform_dataset([signal_energy % 1000])  # inject key value
    
    # Final analysis
    final_diagnostic = analyze_pattern(transformed_data)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")
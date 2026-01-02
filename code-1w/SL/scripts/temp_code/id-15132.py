def process_telemetry_data(raw_data):
    # Irrelevant signal normalization (dead path)
    normalized = [x * 0.95 for x in raw_data if x > 0]
    offset_correction = sum(normalized) // len(normalized) if normalized else 0

    # Core logic disguised among distractions
    filtered = [x for x in raw_data if x % 4 == 2]
    shifted = [(x >> 2) for x in filtered]
    
    # Decoy transformation chain
    inverted = [~x & 0xFF for x in raw_data]  # Bit manipulation red herring
    encoded = ''.join(chr(x % 95 + 32) for x in inverted[:10])  # Unused encoding

    # Distractor: complex but unused set operation
    unique_inverted = set(inverted)
    overlap_check = unique_inverted.intersection({x + 10 for x in unique_inverted if x < 200})

    # Actual critical path begins here
    truncated = shifted[:8]
    processed = []
    for val in truncated:
        if val > 10:
            processed.append(val // 3)
        elif val > 0:
            processed.append(val ** 2)
        else:
            processed.append(5)

    # Multi-step aggregation with rounding
    base_score = sum(processed)
    adjustment = len(truncated) * 2
    adjusted = base_score - adjustment
    
    # Conditional inversion based on parity pattern
    even_count = sum(1 for x in processed if x % 2 == 0)
    if even_count >= 3:
        adjusted = abs(adjusted - 17)
    
    # Final obfuscation layer
    checksum = 0
    for i, v in enumerate(processed):
        checksum ^= (v + i) & 0xF
    
    result = (adjusted ^ checksum) + 5
    return result


def encrypt_sequence(seq):
    # Unused encryption function (decoy)
    return [((x << 1) | (x >> 7)) & 0xFF for x in seq]


def analyze_fault_pattern(signals):
    # High-interference analysis with multiple red herrings
    
    # Irrelevant linguistic analysis (distractor)
    signal_text = ''.join(chr((x % 26) + 97) for x in signals[-5:])
    vowel_count = sum(1 for c in signal_text if c in 'aeiou')
    
    # Fake machine learning simulation
    weights = [0.1, 0.3, 0.6]
    prediction = sum(w * (sum(signals) % 10) for w in weights)
    confidence = int(prediction * 10) % 100
    
    # Real logic buried under noise
    relevant_subset = [x for x in signals if x > 0 and x % 3 != 0]
    transformed = []
    for val in relevant_subset:
        temp = val
        if temp < 20:
            temp = (temp + 4) * 2
        elif temp < 50:
            temp = temp * 1.5  # Becomes float
        else:
            temp = temp - (temp % 7)
        transformed.append(int(temp))
    
    # Set-based filtering (required Python feature)
    valid_range = set(range(15, 65))
    within_bounds = [x for x in transformed if x in valid_range]
    
    # Secondary filtering distraction
    outliers = set(transformed) - valid_range
    correction_factor = len(outliers) * 3
    
    # Final computation chain
    base = sum(within_bounds)
    modifier = len(within_bounds) ** 2
    intermediate = base - modifier
    
    # Case conversion decoy (unused)
    flag_str = "Error_" + str(correction_factor)
    upper_flag = flag_str.upper().replace('_', '-')
    
    # Key calculation step
    if intermediate > 100:
        final_value = intermediate // 4
    else:
        final_value = intermediate * 2 + 13
    
    # Last-minute adjustment
    final_value = (final_value + (correction_factor // 2)) & 0xFFFF  # Mask to 16 bits
    
    return final_value

# Main execution with misleading setup
raw_sensor_data = [18, -5, 42, 26, 30, 11, 8, 64, 14, 21, 9, 3]

# Dead code path: signal encryption
encrypted_signals = encrypt_sequence([x & 0x3F for x in raw_sensor_data])

# Primary processing (irrelevant for final answer)
diagnostic_code = process_telemetry_data(raw_sensor_data)

# Critical statement containing actual answer source
final_diagnostic = analyze_fault_pattern(encrypted_signals)

print(f"Target result: {final_diagnostic}")
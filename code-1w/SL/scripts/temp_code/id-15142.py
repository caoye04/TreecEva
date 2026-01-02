def analyze_data_packet(packet):
    raw_checksum = sum([ord(c) for c in packet])
    temp_offset = len(packet) * 2 if raw_checksum > 100 else len(packet)
    adjusted_value = raw_checksum + temp_offset
    
    # Irrelevant signal processing simulation (distractor)
    signal_strength = len(packet) ** 0.5
    noise_floor = signal_strength * 0.1
    filtered_signal = signal_strength - noise_floor  # Unused

    return adjusted_value


def validate_sequence(seq):
    base_score = 0
    for char in seq:
        if char.isupper():
            base_score += ord(char) % 17
        elif char.isdigit():
            base_score -= int(char) % 5
    
    # Red herring: unused transformation
    mirror_value = base_score ^ 255
    inverted_sum = 0
    for i in range(3):
        inverted_sum += (base_score >> i) & 1  # Slight distraction
    
    return base_score


def calculate_performance_rating():
    data_stream = "X9KLMN3PQ7"
    
    # Primary computation chain
    checksum_result = analyze_data_packet(data_stream)
    validation_score = validate_sequence(data_stream)
    
    # Secondary, semi-relevant transformation (not fully used)
    normalized_val = validation_score / 7.0
    rounded_norm = round(normalized_val)

    # Core logic with conditional expression
    penalty_factor = 4 if len(data_stream) > 8 else 2
    adjustment = -penalty_factor if '9' in data_stream else 0
    
    # Final score calculation
    intermediate = checksum_result // 3
    final_score = intermediate + validation_score + adjustment
    
    # Dead code path - never executed, adds interference
    if False:
        fallback = (intermediate * 2) - validation_score
        final_score = fallback if final_score < 0 else final_score + 1
    
    return final_score

# Execution entry point
final_score = calculate_performance_rating()
print(f"Result: {final_score}")
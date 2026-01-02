def analyze_sensor_data(raw_input: str, threshold: int) -> int:
    # Simulate multi-stage sensor data processing with distractions

    # Core data used in computation
    ascii_values = [ord(c) for c in raw_input]
    base_sum = sum(ascii_values)
    
    # Irrelevant transformation 1: character frequency map (not used later)
    char_freq = {}
    for c in raw_input:
        char_freq[c] = char_freq.get(c, 0) + 1
    frequency_boost = sum(char_freq.values()) % 7 if char_freq else 0

    # Distractor: unused signal normalization function
    def normalize_signal(x):
        return (x - min(ascii_values)) / (max(ascii_values) - min(ascii_values) + 1e-9)

    # Apply threshold filtering on ASCII values
    filtered_ascii = [val for val in ascii_values if val > threshold]

    # Simulated packet reconstruction (some parts irrelevant)
    packets = []
    temp_packet = []
    for v in filtered_ascii:
        temp_packet.append(v)
        if sum(temp_packet) > 200:
            packets.append(temp_packet[:])
            temp_packet.clear()
    # Leftover data ignored — red herring about packet integrity
    packet_integrity = len(temp_packet) == 0

    # Real processing path begins: reconstruct string from filtered ASCII
    filtered_data = ''.join(chr(val) for val in filtered_ascii if 32 <= val <= 126)

    # Decoy statistical analysis (never used)
    avg_val = sum(filtered_ascii) / len(filtered_ascii) if filtered_ascii else 0
    variance_proxy = sum((x - avg_val) ** 2 for x in filtered_ascii) / len(filtered_ascii) if filtered_ascii else 0

    # String slicing distraction: reverse every third word (unused)
    words = filtered_data.split()
    processed_words = []
    for i, word in enumerate(words):
        if i % 3 == 0 and len(word) > 1:
            processed_words.append(word[::-1])
        else:
            processed_words.append(word)
    obfuscated_text = ' '.join(processed_words)

    # Set operation distractor: unique characters in filtered_data
    unique_chars = set(filtered_data)
    special_count = len([c for c in unique_chars if c in "!@#$%^&*"])

    # Actual critical logic
    shift_key = base_sum % 9 + 1
    correction_factor = 0
    for i in range(len(filtered_data)):
        if filtered_data[i].isalpha():
            shifted = ord(filtered_data[i]) + shift_key
            if filtered_data[i].islower():
                shifted = ((shifted - ord('a')) % 26) + ord('a')
            else:
                shifted = ((shifted - ord('A')) % 26) + ord('A')
            if chr(shifted).lower() in 'aeiou':
                correction_factor += 1

    # Key assignment statement
    filtration_score = len(filtered_data) * correction_factor

    # Dead code path: error simulation never triggered
    if len(packets) > 100:
        raise RuntimeError("Simulated overflow")

    # Unused final checksum
    final_checksum = sum(ord(c) ^ (i % 5) for i, c in enumerate(filtered_data)) % 97

    return filtration_score

# Main execution
sensor_trace = "ThermalFlux_δ_Overload@95"
activation_threshold = 75
result = analyze_sensor_data(sensor_trace, activation_threshold)
print(f"Result: {result}")
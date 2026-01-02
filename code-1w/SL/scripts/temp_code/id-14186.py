import itertools

def analyze_frequency_band(data_stream, band_limit):
    frequency_map = {}
    temp_buffer = []
    for index, char in enumerate(data_stream):
        if char.isalpha():
            lower_char = char.lower()
            frequency_map[lower_char] = frequency_map.get(lower_char, 0) + 1
            temp_buffer.append(ord(lower_char) - ord('a'))
    
    # Distractor: irrelevant transformation
    transformed = [x ** 2 for x in temp_buffer if x % 2 == 0]
    excess_energy = sum(transformed) % 17

    # Actual relevant computation
    total_power = sum(frequency_map.values())
    dominant_band = max(frequency_map.values(), default=0)
    return total_power - dominant_band + excess_energy


def detect_modulation_patterns(seq):
    patterns = {'am': 0, 'fm': 0, 'pm': 0}
    for a, b in zip(seq, seq[1:]):
        diff = abs(ord(b) - ord(a))
        if diff > 10:
            patterns['fm'] += 1
        elif diff == 0:
            patterns['am'] += 1
        else:
            patterns['pm'] += 1
    
    # Dead code path (distractor)
    if len(seq) > 100:
        scaling_factor = len(seq) / 100
        for k in patterns:
            patterns[k] *= scaling_factor
    
    # Irrelevant set operation
    unique_chars = set(itertools.chain.from_iterable([[c] for c in seq if c.isupper()]))
    
    return sum(patterns.values())


def process_transmission(signal_sequence, noise_threshold):
    base_strength = analyze_frequency_band(signal_sequence, 5)
    modulation_score = detect_modulation_patterns(signal_sequence)
    
    # Intermediate distractor variables
    normalized_seq = ''.join(s for s in signal_sequence if s.isalnum()).upper()
    redundancy_check = len(normalized_seq) - len(set(normalized_seq))
    
    # Key logic with conditional override
    if redundancy_check > noise_threshold:
        adjustment = -3
    else:
        adjustment = 2
    
    interim_result = base_strength + modulation_score + adjustment
    
    # Additional misleading calculation
    entropy_proxy = 0
    for i, (x, y) in enumerate(zip(normalized_seq, reversed(normalized_seq))):
        if x == y and i % 2 == 0:
            entropy_proxy += 1
    
    # Final signal depends only on specific chain, not entropy
    final_signal = interim_result * 3 - noise_threshold
    
    # Print required output format
    print(f"Target result: {final_signal}")
    return final_signal

# Main execution
signal_data = "XyZzYxAbCcbaXMmXKtt"
threshold = 4
final_signal = process_transmission(signal_data, threshold)
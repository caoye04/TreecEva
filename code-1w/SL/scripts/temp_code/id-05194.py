def preprocess_signal(raw_data):
    filtered = [x for x in raw_data if x > 0]
    normalized = [round(x / sum(filtered), 6) for x in filtered]
    return normalized


def generate_lookup(keys):
    lookup = {k: idx ** 2 for idx, k in enumerate(keys)}
    inverse_map = {v: k for k, v in lookup.items()}
    return lookup  # Dead code path: inverse_map unused


def compute_entropy(values):
    from math import log2
    entropy = 0.0
    for v in values:
        if v > 0:
            entropy -= v * log2(v)
    return round(entropy, 6)


def shift_sequence(seq, offset):
    """Irrelevant transformation used as distractor"""
    return seq[-offset:] + seq[:-offset]


def decode_segments(packed_data):
    segments = []
    for item in packed_data:
        if isinstance(item, str):
            cleaned = item.strip().lower().replace("_", "")
            segments.append(len(cleaned))  # Only length matters
        else:
            segments.append(item * 2)
    return segments


def analyze_pattern(signal, config):
    # Core logic begins
    base_values = [x for x in signal if x < 0.5]
    
    # Bit manipulation red herring
    magic_flag = 0b1010 ^ 0b1100 & 0b0011
    temp_state = (magic_flag << 3) % 7  # Distractor

    # Real computation
    averaged = sum(base_values) / len(base_values) if base_values else 0
    
    # Conditional expression with string method decoy
    status_tag = "valid" if averaged > 0.1 else "low_amp"
    tag_length = len(status_tag.upper().strip())  # Irrelevant

    # Set operations that appear important but are not
    unique_marks = {len(x) for x in ['error', 'warn', 'info'] if 'e' in x}  # {5, 4}
    adjustment = len(unique_marks)  # = 2, misleading

    # Critical path: uses config[1] and averaged
    threshold_primary = config[1]
    scaled_score = averaged * 1000
    
    # Decoy conditional
    if scaled_score > 500:
        scaled_score = abs(scaled_score - 100)  # Not triggered

    # Key calculation
    final_weight = scaled_score if scaled_score < threshold_primary else threshold_primary
    
    # Another decoy: tuple unpacking with irrelevant vars
    _, _, meta_offset = (10, 20, len("diagnostic_log".split('_')))

    # Final result
    final_diagnostic = int(final_weight + temp_state - adjustment)
    
    return final_diagnostic

# Main execution block
if __name__ == '__main__':
    raw_sensor_data = [0.1, -0.5, 0.3, 0.4, 0.0, 0.2, 0.6, 0.7]
    processed = preprocess_signal(raw_sensor_data)
    
    keys_for_mapping = ['alpha', 'beta', 'gamma', 'delta']
    mapping_table = generate_lookup(keys_for_mapping)
    
    entropy_value = compute_entropy(processed)
    
    shifted = shift_sequence(processed, 2)
    
    packed_input = ["err_msg", "warning_alert", 5, "info"]
    decoded_lengths = decode_segments(packed_input)
    
    encoded_sequence = [round(x * 0.98, 6) for x in processed]
    
    thresholds = [0.15, 285, 0.4, 0.9]
    
    final_diagnostic = analyze_pattern(encoded_sequence, thresholds)
    
    print(f"Result: {final_diagnostic}")
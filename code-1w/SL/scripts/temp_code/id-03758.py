def normalize_sequence(seq):
    return [x % 7 for x in seq if x > 0]


def analyze_pattern(data):
    temp_result = 0
    shift_factor = len(data) // 2
    for i in range(len(data)):
        if i % 2 == 0:
            temp_result += data[i] << 1
        else:
            temp_result -= data[i] >> 1
    return temp_result + shift_factor


def extract_segments(text_block):
    segments = text_block.split(',')
    clean_parts = [seg.strip().upper() for seg in segments]
    filtered = [part for part in clean_parts if 'X' not in part]
    return ''.join(filtered)


def validate_purity(elements):
    base_value = 100
    adjustment = 0
    
    # Irrelevant string processing (distractor)
    metadata_tag = "PRC-789"
    tag_length = len(metadata_tag)
    suffix_value = sum(ord(c) for c in metadata_tag[:3])
    
    for elem in elements:
        if elem < 5:
            adjustment += elem * 2
        elif elem >= 5:
            adjustment -= elem // 3
    
    # Secondary distractor: bitwise manipulation with no effect on final logic
    masked_adjustment = adjustment ^ 0xFF
    inverted = ~masked_adjustment
    dummy_checksum = (inverted & 0xFFFF) + tag_length
    
    # Actual contribution to result
    base_value += adjustment
    
    # Dead code path (never executed due to fixed input)
    if len(elements) > 100:
        fallback = sum(elements) / len(elements)
        base_value = int(fallback)
    
    return base_value

# Main execution flow
raw_data = [12, -3, 7, 4, 9, 0, 5]
normalized_data = normalize_sequence(raw_data)

# Simulated intermediate analysis (semi-relevant)
pattern_metric = analyze_pattern(normalized_data)
info_chunk = "alpha, beta, gammaX, delta"
semantic_key = extract_segments(info_chunk)

# Core computation step
processed_elements = [x for x in normalized_data if x != 0]
filtration_score = validate_purity(processed_elements)

# Final output
print(f"Result: {filtration_score}")
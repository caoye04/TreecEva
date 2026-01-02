def analyze_pattern(sequence):
    count_upper = sum(1 for c in sequence if c.isupper())
    count_lower = sum(1 for c in sequence if c.islower())
    total_chars = len(sequence)
    ratio = count_upper / total_chars if total_chars else 0
    
    # Distractor: irrelevant transformation
    reversed_seq = sequence[::-1]
    mirrored = sequence + reversed_seq
    placeholder_value = len(mirrored) * 0.5
    
    return count_lower, ratio


def extract_features(data_string):
    segments = data_string.split('|')
    lengths = [len(s) for s in segments]
    avg_length = sum(lengths) / len(lengths) if lengths else 0
    
    # Distractor: unused statistical computation
    variance = sum((x - avg_length) ** 2 for x in lengths) / len(lengths) if lengths else 0
    
    normalized = [round(l / avg_length, 3) if avg_length else 0 for l in lengths]
    return segments, normalized


def validate_bounds(bounds, limit):
    adjusted = []
    for b in bounds:
        if b < 0:
            adjusted.append(0)
        elif b > limit:
            adjusted.append(limit)
        else:
            adjusted.append(b)
    return adjusted


def process_segments(segments, indices):
    subset = segments[indices[0]:indices[2]]
    
    # Real logic: count characters in selected segment slice
    char_count = sum(len(s) for s in subset)
    
    # Distractor: extra processing on case conversion
    case_flipped = ''.join(s.swapcase() for s in subset)
    dummy_sum = sum(ord(c) % 10 for c in case_flipped)
    
    # Semi-relevant: use of slicing and length
    mid_segment = subset[len(subset)//2] if subset else ''
    mid_length = len(mid_segment)
    
    result = char_count + mid_length
    return result

# Main execution flow
raw_input = "Alpha|betaTEST|gamma|deltaINNER|epsilonZ"
feature_data, norm_vals = extract_features(raw_input)

# Analyze first segment's pattern (distractor call)
analyze_pattern(feature_data[0])

# Define boundary indices with potential overflow
boundaries = [1, 3, 10]
validated_bounds = validate_bounds(boundaries, len(feature_data))

# Core computation
final_score = process_segments(feature_data, validated_bounds)

# Output result
print(f"Result: {final_score}")
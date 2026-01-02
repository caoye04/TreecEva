def analyze_pattern(sequence):
    char_freq = {}
    for char in sequence:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    # Distractor: counting vowels (not used later)
    vowel_count = sum(1 for c in sequence if c.lower() in 'aeiou')
    total_pairs = 0
    for i in range(len(sequence) - 1):
        if sequence[i] == sequence[i+1]:
            total_pairs += 1

    # Irrelevant transformation
    reversed_chunks = [sequence[i:i+3][::-1] for i in range(0, len(sequence), 3)]
    return char_freq, total_pairs, vowel_count


def filter_boundaries(indices, threshold=2):
    filtered = []
    temp_sum = 0
    for idx, val in enumerate(indices):
        temp_sum += val
        if temp_sum > threshold:
            filtered.append(idx)
            temp_sum = 0  # reset
    return filtered if filtered else [0]


def process_segments(data, bounds):
    segment_stats = []
    start = 0
    
    # Use of enumerate and zip: key Python features
    for i, end in enumerate(bounds):
        segment = data[start:end+1]
        if not segment:
            continue
        
        # Character case conversion and analysis
        upper_version = ''.join([c.upper() for c in segment])
        lower_version = upper_version.lower()
        
        # Count specific pattern: consecutive same characters
        repeat_count = 0
        for j in range(len(lower_version) - 1):
            if lower_version[j] == lower_version[j+1]:
                repeat_count += 1
        
        # Track length and repeat density
        length = len(segment)
        density = repeat_count / length if length else 0
        segment_stats.append((length, repeat_count, density))
        
        start = end + 1
    
    # Final aggregation
    total_length = sum(st[0] for st in segment_stats)
    total_repeats = sum(st[1] for st in segment_stats)
    avg_density = sum(st[2] for st in segment_stats) / len(segment_stats) if segment_stats else 0
    
    # Secondary distractor calculation (unused)
    max_segment_repeats = max(st[1] for st in segment_stats) if segment_stats else 0
    smoothness_score = (total_length - total_repeats) / (total_length + 1e-5)
    
    # The actual answer computation
    final_count = total_length + total_repeats - len(segment_stats)
    
    # Print result as required
    print(f"Result: {final_count}")
    return final_count

# Main execution
raw_sequence = "aabbcccddeeffgghh"
boundaries = [4, 8, 12, 16]

# Initial analysis (some outputs unused)
freq_map, pair_total, vowel_total = analyze_pattern(raw_sequence)

# Process boundary filtering with distractor
filtered_limits = filter_boundaries(boundaries, threshold=5)

# Introduce string method distraction
modified_seq = raw_sequence.replace('a', 'x').strip('x').title()

# Reuse original for correctness
segment_data = raw_sequence  # Ensure we use correct data

# Key statement
final_count = process_segments(segment_data, filtered_limits)

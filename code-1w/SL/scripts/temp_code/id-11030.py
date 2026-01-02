def process_segment(data, offset=0):
    segment = data[offset:offset + 5]
    base_value = sum(ord(c) for c in segment if c.isupper())
    shift = len(segment) % 4
    
    # Irrelevant transformation (distractor)
    temp_encoded = ''.join(chr((ord(c) - 65 + shift) % 26 + 65) if c.isalpha() else c for c in segment)
    
    # Semi-relevant intermediate
    mirrored = segment[::-1]
    mirror_score = sum(ord(mirrored[i]) * (i + 1) for i in range(len(mirrored)))
    
    return (base_value + mirror_score) % 97


def analyze_phases(input_str):
    phase_results = []
    working_data = input_str.upper()
    
    # Dummy counters (distractors)
    total_iterations = 0
    placeholder_sum = 0
    
    for i in range(0, len(working_data) - 4, 3):
        total_iterations += 1
        chunk_value = process_segment(working_data, i)
        phase_results.append(chunk_value)
        
        # Dead computation path (misleading)
        if chunk_value > 50:
            adjusted = (chunk_value * 2) % 101
            placeholder_sum += adjusted  # never used later
    
    # Extra logic that doesn't affect final result
    if len(phase_results) < 3:
        phase_results.extend([0] * (3 - len(phase_results)))
    
    # Real computation begins here
    trimmed = phase_results[1:-1] if len(phase_results) > 2 else phase_results
    
    # More distractions
    stats = {
        'avg': sum(phase_results) / len(phase_results),
        'peak': max(phase_results),
        'entropy': sum(-v/97 * (v/97) for v in phase_results[:2])  # partial use
    }
    
    return trimmed

# Finalization logic
def finalize(values):
    acc = 0
    for v in values:
        acc ^= v  # XOR accumulation
        acc = (acc + 13) % 10007
    return acc * 2

# Main execution
if __name__ == '__main__':
    raw_input = "aBcDeFgHiJkLmNoPqRsTuVwXyZ"
    
    # Preprocessing with slicing distraction
    cleaned = ''.join(c for c in raw_input if c.isalpha())
    processed = cleaned[::2].lower() + cleaned[1::2].upper()  # mixed case rearrangement
    
    # Unused statistical variables (distractors)
    char_count = {c: processed.count(c) for c in set(processed)}
    vowel_ratio = sum(1 for c in processed if c.lower() in 'aeiou') / len(processed)
    
    # Actual important call
    results = analyze_phases(processed)
    
    # Key statement
    checksum = finalize(sum(results))
    
    # Print target result
    print(f"Target result: {checksum}")
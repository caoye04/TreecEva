def analyze_signal_quality(signal_sequence):
    segments = signal_sequence.split('|')
    valid_segments = []
    invalid_count = 0
    for seg in segments:
        stripped_seg = seg.strip()
        if len(stripped_seg) >= 3 and stripped_seg.isalpha():
            valid_segments.append(stripped_seg.lower())
        else:
            invalid_count += 1
    
    unique_passing = list(set(valid_segments))
    passing_segments = [s for s in unique_passing if 'z' not in s]
    base_multiplier = 7
    penalty_count = invalid_count * 2
    final_score = len(passing_segments) * base_multiplier - penalty_count
    return final_score

result = analyze_signal_quality('Cat|Dog|ZZZ| |Elephant|cat|   |Bat')
print(f"Result: {result}")
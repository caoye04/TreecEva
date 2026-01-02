def evaluate_performance(sequence, criteria):
    # Preprocess: normalize case and extract key patterns
    normalized = ''.join([c.lower() for c in sequence if c.isalpha()])
    segments = [normalized[i:i+3] for i in range(0, len(normalized), 3)]
    
    # Irrelevant transformation (distractor)
    mirrored = [s[::-1] for s in segments]
    encoded_values = [sum(ord(ch) for ch in seg) for seg in segments]
    
    # Set operations on character inventory (relevant)
    unique_chars = set(normalized)
    criterion_set = set(criteria.lower())
    overlap_count = len(unique_chars & criterion_set)
    
    # Scoring logic with slicing distraction
    sliced_weights = encoded_values[1::2]  # every second value - not actually used
    base_score = sum(encoded_values) // len(encoded_values) if encoded_values else 0
    
    # Secondary distractor: dead-end loop with no impact
    temp_result = 0
    for i in range(len(mirrored)):
        if len(mirrored[i]) == 3:
            temp_result += ord(mirrored[i][0])  # never used
    
    # Actual score refinement using overlap and base
    adjustment = 0
    if overlap_count > 4:
        adjustment = 15
    elif overlap_count > 2:
        adjustment = 8
    else:
        adjustment = -5
    
    # Final computation
    stability_check = len(normalized) % 4
    if stability_check == 0:
        final_score = base_score + adjustment
    else:
        final_score = base_score + adjustment - (stability_check * 2)
    
    return final_score

# Main execution
assessment_sequence = "AbC1xYzPqRtLmNuOpEeAaBbCcDdXxYyZz!@#"
criteria_string = "ABCDEexyz"

# Dead variable assignments (distraction)
diagnostic_trace = [len(part) for part in assessment_sequence.split('1')]
placeholder_data = {f'key_{i}': i*2 for i in range(5)}
metadata_cache = []
for char in assessment_sequence:
    if char.isdigit():
        metadata_cache.append(char)

# Key call
final_score = evaluate_performance(assessment_sequence, criteria_string)
print(f"Target result: {final_score}")
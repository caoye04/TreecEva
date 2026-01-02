def analyze_pattern(sequence):
    count_vowels = 0
    temp_sum = 0
    for idx, char in enumerate(sequence):
        if char in 'aeiou':
            count_vowels += 1
            temp_sum += idx
    return count_vowels, temp_sum


def validate_sequence(seq_list):
    valid_count = 0
    total_length = 0
    dummy_result = 0
    for s in seq_list:
        total_length += len(s)
        vowel_cnt, _ = analyze_pattern(s)
        if vowel_cnt > 1:
            valid_count += 1
        else:
            dummy_result += len(s)  # Distractor: not used later
    avg_len = total_length / len(seq_list) if seq_list else 0
    return valid_count, avg_len


def compute_weights(values):
    weighted_vals = []
    for i, v in enumerate(values):
        weight = 1 + (i * 0.1)
        weighted_vals.append(v * weight)
    return weighted_vals


def calculate_final_score(raw_data):
    # Step 1: Extract and process text patterns
    sequences = [item['text'] for item in raw_data]
    scores = [item['base_score'] for item in raw_data]
    
    # Intermediate analysis with distractors
    vowel_info = [analyze_pattern(s) for s in sequences]
    pattern_scores = [v[0] * 2 + v[1] for v in vowel_info]  # Uses vowel count and index sum
    
    # Distractor computations
    _, average_length = validate_sequence(sequences)
    adjustment_factor = average_length * 0.5 if average_length > 3 else 1.0
    
    # Real computation path
    weighted_bases = compute_weights(scores)
    base_aggregate = sum(weighted_bases) * adjustment_factor
    
    # Additional distraction: unused loop over zipped data
    cumulative_noise = 0
    for txt, score in zip(sequences, scores):
        noise = len(txt) - score
        if noise > 5:
            cumulative_noise += 1  # Not used in final result

    # Final logic step: combine pattern and base contributions
    pattern_contribution = sum(pattern_scores) // len(pattern_scores) if pattern_scores else 0
    final_value = int(base_aggregate + pattern_contribution - 15)  # Key deterministic result
    
    return final_value

# Input data
input_data = [
    {'text': 'algorithm', 'base_score': 8},
    {'text': 'function', 'base_score': 6},
    {'text': 'code', 'base_score': 5},
    {'text': 'variable', 'base_score': 7}
]

# Execution point
final_score = calculate_final_score(input_data)
print(f"Result: {final_score}")
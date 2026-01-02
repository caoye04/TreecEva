def analyze_text_patterns(input_str):
    char_count = {}
    for c in input_str:
        char_count[c] = char_count.get(c, 0) + 1
    
    # Irrelevant computation: counting vowels (not used later)
    vowel_count = sum(1 for v in input_str if v.lower() in 'aeiou')
    
    # Semi-relevant transformation: normalize frequencies
    total_chars = len(input_str)
    freq_map = {k: v / total_chars for k, v in char_count.items()}
    
    # Extract specific pattern: repeated characters
    repeats = [k for k, v in char_count.items() if v > 1]
    repeat_string = ''.join(repeats)
    
    # Distractor: unused string manipulation
    reversed_unique = ''.join(sorted(set(input_str), reverse=True))
    palindrome_check = repeat_string == repeat_string[::-1]
    
    return freq_map, repeat_string, total_chars


def transform_sequence(seq, multiplier):
    # Apply modular arithmetic with distraction
    transformed = []
    temp_sum = 0
    for i, val in enumerate(seq):
        new_val = (val * multiplier + i) % 19
        transformed.append(new_val)
        temp_sum += new_val
    
    # Dead code: this list is never used
    squared_chain = [x**2 for x in transformed if x % 2 == 0]
    
    # Return only relevant result
    return transformed


def calculate_adjusted_score(data_tuple):
    raw_freq, rep_str, length = data_tuple
    base_score = sum(raw_freq.values()) * 100
    
    # String-based adjustment
    adjustment = 0
    if len(rep_str) > 0:
        # Use string method to count specific patterns
        adjustment = rep_str.count('a') * 5 + len(rep_str) * 2
    
    # Additional irrelevant check
    ascii_sum = sum(ord(c) for c in rep_str)
    is_stable = all(c.islower() for c in rep_str)
    
    # Final scoring logic
    score = base_score + adjustment - length // 4
    return int(score)

# Main execution flow
raw_input = "abracadabra"
sequence_seed = [3, 7, 2, 8, 5]

# Step 1: Analyze text patterns
analysis_result = analyze_text_patterns(raw_input)

# Step 2: Transform numerical sequence (distractor with partial relevance)
transformed_seq = transform_sequence(sequence_seed, 3)
intermediate_total = sum(transformed_seq) // len(transformed_seq)

# Step 3: Prepare data for scoring
processed_data = analysis_result  # Pass through full analysis tuple

# Step 4: Calculate final score
final_score = calculate_adjusted_score(processed_data)

# Output result
print(f"Result: {final_score}")
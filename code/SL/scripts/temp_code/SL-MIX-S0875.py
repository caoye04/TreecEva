import itertools

def process_data(text_input):
    # Distractor variables and computations
    temp_analysis = len(text_input) * 3.14159
    char_freq = {char: text_input.count(char) for char in set(text_input)}
    vowel_check = sum(1 for c in text_input if c in 'aeiouAEIOU')
    
    # Misleading intermediate processing
    shifted_values = [ord(c) << 2 for c in text_input[:5]]
    pattern_tracker = sum(shifted_values) // len(shifted_values) if shifted_values else 0
    
    # Main logic with nested operations
    words = text_input.split()
    word_combinations = list(itertools.combinations(words, 2))
    
    # Dead code path - never executed due to condition
    if len(words) > 10:
        unused_calc = sum(len(w) for w in words) ** 2
    
    # Core computation with conditional expressions
    valid_pairs = [(w1, w2) for w1, w2 in word_combinations 
                   if len(w1) > 3 and len(w2) > 3]
    
    pair_scores = [(len(p[0]) + len(p[1])) if p[0][0] == p[1][0] 
                  else (len(p[0]) * len(p[1])) // 2 
                  for p in valid_pairs]
    
    # Red herring calculation
    redundant_sum = sum(ord(c) for c in text_input) % 100
    
    # Final result computation
    final_count = sum(pair_scores) - redundant_sum if pair_scores else 0
    
    return final_count

# Main execution
input_string = "python programming benchmark evaluation complex reasoning"
result = process_data(input_string)
print(f"Result: {result}")
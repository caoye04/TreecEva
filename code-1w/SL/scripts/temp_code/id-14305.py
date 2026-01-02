def analyze_text_pattern(text):
    char_count = {}
    for char in text:
        if char.isalpha():
            char_count[char.lower()] = char_count.get(char.lower(), 0) + 1
    
    # Distractor: Count vowels separately (not used later)
    vowel_list = 'aeiou'
    vowel_count = sum(1 for c in char_count if c in vowel_list)
    consonant_count = len(char_count) - vowel_count

    # Semi-relevant transformation
    frequency_ranks = sorted(char_count.values(), reverse=True)
    rank_weight = 0
    for i, freq in enumerate(frequency_ranks):
        rank_weight += freq * (i + 1)

    return rank_weight


def compute_total(values, factors):
    total = 0
    temp_results = []
    
    # Real computation with slicing and enumerate
    for idx, val in enumerate(values[::2]):  # Only even indices
        modified_val = val * factors[idx % len(factors)]
        temp_results.append(modified_val)
        total += modified_val
    
    # Dead code path - never executed due to condition
    if len(temp_results) > 100:
        backup = [x * 0.5 for x in temp_results]
        total -= sum(backup)

    # Additional irrelevant accumulation
    cumulative = 0
    for v in values:
        cumulative += v ** 0.5
    
    return int(total)

# Main execution
input_string = "DynamicAnalysisOfCodePatterns"
dummy_data = [3, 7, 2, 9, 4, 8, 1, 6]
modifier_weights = [1.5, 0.8, 2.1]

# Trigger distractor function
noise_metric = analyze_text_pattern(input_string)

# Prepare actual inputs
base_values = [x + (i*2) for i, x in enumerate(dummy_data)]
modifiers = [m + 0.1 for m in modifier_weights]  # Adjusted weights

# Key operation
final_score = compute_total(base_values, modifiers)

# Print result as required
print(f"Result: {final_score}")
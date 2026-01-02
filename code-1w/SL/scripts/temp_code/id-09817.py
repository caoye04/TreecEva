def analyze_text_patterns(input_str):
    char_freq = {}
    for ch in input_str:
        if ch.isalpha():
            lower_ch = ch.lower()
            char_freq[lower_ch] = char_freq.get(lower_ch, 0) + 1
    
    # Irrelevant vowel tracking (distractor)
    vowels = 'aeiou'
    total_vowels = sum(char_freq.get(v, 0) for v in vowels)
    total_consonants = sum(char_freq.values()) - total_vowels

    # Misleading transformation chain (semi-relevant but not used directly)
    normalized = {k: round(v / sum(char_freq.values()), 3) for k, v in char_freq.items()}
    sorted_chars = sorted(normalized.items(), key=lambda x: x[1], reverse=True)

    # Actual relevant computation begins
    weighted_sum = 0
    for i, (char, freq) in enumerate(sorted_chars):
        weight = 1 / (i + 1)  # Higher rank gets more weight
        weighted_sum += ord(char) * weight * freq
    
    return weighted_sum


def transform_case_magnitude(data_list):
    case_scores = []
    magnitude_total = 0
    
    for item in data_list:
        upper_count = sum(1 for c in item if c.isupper())
        lower_count = sum(1 for c in item if c.islower())
        net_case_bias = upper_count - lower_count
        
        # Dead code path (distractor)
        if net_case_bias == 0:
            adjustment_factor = 1.0
        else:
            adjustment_factor = abs(net_case_bias) ** 0.5  # unused
        
        magnitude_total += len(item) * net_case_bias
        case_scores.append(abs(net_case_bias))
    
    # Another distractor: zipping unrelated sequences
    indices = list(range(len(case_scores)))
    paired = list(zip(indices, case_scores))
    shuffled_value = sum(i * s for i, s in paired if s % 2 == 1)

    return magnitude_total


def calculate_adjusted_score(raw_components):
    base_value = raw_components['text_metric']
    bias_penalty = raw_components['case_magnitude']
    
    # Simulate multi-step dependency with intermediate adjustments
    adjustment_steps = []
    temp = base_value
    for _ in range(3):
        temp = (temp + bias_penalty) / 2
        adjustment_steps.append(temp)
    
    # Use only the last step
    final_step = adjustment_steps[-1]
    
    # Red herring calculation
    hypothetical = sum(adjustment_steps) * 0.1  # unused
    
    return int(round(final_step))

# Main execution flow
raw_text = "DynamicAnalysisWithMixedCASEPatterns"
data_stream = ["Data", "PIPELINE", "Test", "CASEflow"]

# Step 1: Analyze character patterns (core component)
metric_a = analyze_text_patterns(raw_text)

# Step 2: Compute case magnitude across stream (core component)
magnitude_b = transform_case_magnitude(data_stream)

# Step 3: Prepare structured input
processed_data = {
    'text_metric': metric_a,
    'case_magnitude': magnitude_b,
    'metadata_flag': len(raw_text) > 20  # distractor
}

# Key statement
final_score = calculate_adjusted_score(processed_data)

print(f"Result: {final_score}")
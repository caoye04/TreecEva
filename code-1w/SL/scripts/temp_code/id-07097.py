def analyze_text_patterns(text_data):
    char_count = {}
    for char in text_data:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Irrelevant vowel tracking (distractor)
    vowels = 'aeiou'
    vowel_count = sum(1 for c in text_data if c.lower() in vowels)
    
    # Semi-relevant: compute entropy-like measure (not used directly)
    import math
    total_chars = len(text_data)
    entropy = 0
    for count in char_count.values():
        prob = count / total_chars
        entropy -= prob * math.log2(prob) if prob > 0 else 0
    
    # Extract positions of special characters
    special_positions = [i for i, c in enumerate(text_data) if not c.isalnum()]
    
    # Use slicing to get every second character from the middle third
    mid_start = total_chars // 3
    mid_end = 2 * total_chars // 3
    mid_segment = text_data[mid_start:mid_end]
    sampled = mid_segment[::2]
    
    # Count alphanumeric and symbol chars (only alphanumeric used later)
    alpha_count = sum(1 for c in text_data if c.isalpha())
    digit_count = sum(1 for c in text_data if c.isdigit())
    symbol_count = total_chars - alpha_count - digit_count

    return alpha_count, digit_count, symbol_count, entropy, special_positions, sampled


def evaluate_performance(metrics, weights):
    # metrics: (alpha, digit, symbol, entropy, _, _)
    base_score = 0
    adjustment = 0
    
    # Core logic: weighted sum of relevant counts
    for i, weight in enumerate(weights):
        if i < 3:  # Only first three metrics are meaningful
            base_score += metrics[i] * weight
        else:
            # Higher-indexed metrics have diminishing impact
            adjustment += metrics[i] * 0.1 * weight
    
    # Bitwise interference (misleading)
    temp_flag = (metrics[0] & 1) ^ (metrics[1] & 1)
    if temp_flag:
        adjustment += 0.5
    
    final_raw = base_score + adjustment
    
    # Normalize by length proxy
    proxy_length = metrics[0] + metrics[1]*2 + metrics[2]*3
    if proxy_length > 0:
        final_raw /= (proxy_length / 10.0)
    
    return int(final_raw)

# Main execution
raw_input = "DataAnalysis_2023@SyntaxHighlight#ParseTree$")

# Extract features with helper function
features = analyze_text_patterns(raw_input)

# Weights: alpha=3, digit=2, symbol=4, entropy=1, others irrelevant
weights = [3, 2, 4, 1, 0, 0]

# Critical statement
final_score = evaluate_performance(features, weights)

print(f"Result: {final_score}")
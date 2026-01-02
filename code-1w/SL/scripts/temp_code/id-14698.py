def analyze_pattern(sequence):
    count_vowels = sum(1 for c in sequence if c.lower() in 'aeiou')
    count_consonants = sum(1 for c in sequence if c.isalpha() and c.lower() not in 'aeiou')
    total_chars = len(sequence)
    ratio = count_vowels / total_chars if total_chars else 0
    
    # Distractor: irrelevant transformation
    transformed = ''.join(chr(ord(c) ^ 3) for c in sequence[:10])
    dummy_sum = sum(ord(c) for c in transformed)

    return count_vowels, count_consonants, ratio


def validate_threshold(value, min_val=5, max_val=50):
    # Semi-relevant logic with conditional expression
    status = 'valid' if min_val <= value <= max_val else 'invalid'
    penalty = 10 if status == 'invalid' else 0
    return penalty


def calculate_final_score(data, weights):
    raw_scores = []
    penalties = 0
    
    for item in data:
        # Extract meaningful features
        length = len(item)
        unique_chars = len(set(item))
        char_diversity = unique_chars / length if length else 0
        
        # Call helper function (partially relevant)
        vowels, consonants, vowel_ratio = analyze_pattern(item)
        
        # Core computation
        score_component = (vowel_ratio * 100) + (char_diversity * 50)
        raw_scores.append(score_component)
        
        # Apply penalty based on length threshold
        penalties += validate_threshold(length)
    
    # Weighted aggregation using conditional expression
    base_score = sum(raw_scores[i] * weights[i] for i in range(len(raw_scores))) if raw_scores else 0
    adjustment = -penalties if penalties > 0 else 0
    
    # Final computation
    final_score = base_score + adjustment
    
    # Red herring: unused complex structure
    summary_report = {
        'items_processed': len(data),
        'average_raw': sum(raw_scores)/len(raw_scores) if raw_scores else 0,
        'total_penalty': penalties,
        'bitwise_fingerprint': hash(''.join(data)) & 0xFFFF
    }
    
    return int(final_score)

# Main execution
if __name__ == '__main__':
    input_data = ['algorithm', 'function', 'variable', 'lambda', 'recursion']
    weights = [0.2, 0.3, 0.1, 0.15, 0.25]
    
    # Irrelevant pre-processing
    processed = [s[::-1].title() for s in input_data]
    temp_values = [len(s) * 2 + 3 for s in processed]
    
    final_score = calculate_final_score(input_data, weights)
    print(f"Result: {final_score}")
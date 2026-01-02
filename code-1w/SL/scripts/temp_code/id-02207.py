from itertools import combinations

def analyze_text_patterns(text):
    words = text.lower().split()
    word_pairs = list(combinations(words, 2))
    pair_freq = {}
    for pair in word_pairs:
        normalized = tuple(sorted(pair))
        pair_freq[normalized] = pair_freq.get(normalized, 0) + 1
    
    # Distractor: complex frequency analysis not used later
    rare_pairs = [p for p, cnt in pair_freq.items() if cnt == 1]
    diversity_index = len(rare_pairs) / len(pair_freq) if pair_freq else 0
    
    char_count = sum(len(word) for word in words)
    avg_word_length = char_count / len(words) if words else 0
    
    return avg_word_length, diversity_index

def calculate_redundancy(sequence):
    seen = set()
    redundant = 0
    for item in sequence:
        if item in seen:
            redundant += 1
        seen.add(item)
    return redundant

def evaluate_performance(metrics, base):
    adjustment_factor = 1.0
    if metrics['length'] > base['max_length']:
        adjustment_factor *= 0.9
    if metrics['complexity'] < base['min_complexity']:
        adjustment_factor *= 0.85
    
    raw_score = metrics['accuracy'] * metrics['efficiency']
    adjusted_score = raw_score * adjustment_factor
    
    # Misleading intermediate calculation
    hypothetical_gain = (base['ideal_score'] - adjusted_score) * 0.1
    
    noise = calculate_redundancy([int(adjusted_score), int(raw_score), int(hypothetical_gain)])
    final_score = adjusted_score - noise * 0.05
    
    return final_score

def main():
    input_text = "The quick brown fox jumps over the lazy dog repeatedly in the morning"
    
    # Extract linguistic features
    avg_len, diversity = analyze_text_patterns(input_text)
    
    # Generate synthetic metrics (some are distractions)
    token_count = len(input_text.split())
    vowel_chars = sum(c in 'aeiou' for c in input_text.lower())
    case_ratio = sum(c.isupper() for c in input_text) / len(input_text)
    
    # Core metrics used in evaluation
    metrics = {
        'accuracy': 0.94,
        'efficiency': 87.5,
        'length': token_count,
        'complexity': avg_len,
    }
    
    # Baseline configuration
    baseline = {
        'max_length': 12,
        'min_complexity': 4.2,
        'ideal_score': 100.0
    }
    
    # Irrelevant pre-computations
    entropy_approx = 0
    for i in range(1, min(6, len(input_text))):
        entropy_approx += (vowel_chars / len(input_text)) ** i
    
    temp_result = [x for x in range(token_count) if x % 3 == 0]
    dummy_agg = sum(temp_result) / len(temp_result) if temp_result else 0
    
    # Key statement
    final_score = evaluate_performance(metrics, baseline)
    
    # Print result as required
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()
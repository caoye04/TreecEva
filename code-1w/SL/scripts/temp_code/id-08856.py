from itertools import combinations

def analyze_frequencies(text):
    char_count = {}
    for char in text:
        if char.isalpha():
            char_count[char.lower()] = char_count.get(char.lower(), 0) + 1
    return char_count

def filter_relevant_keys(freq_dict, threshold=2):
    return {k: v for k, v in freq_dict.items() if v >= threshold}

def generate_pairs(keys):
    return list(combinations(sorted(keys), 2))

def compute_pair_stability(pairs, text_window):
    stability_scores = {}
    for a, b in pairs:
        count = 0
        for i in range(len(text_window) - 1):
            if text_window[i] == a and text_window[i+1] == b:
                count += 1
        stability_scores[(a, b)] = count * 1.5
    return stability_scores

def calculate_entropy(values):
    total = sum(values)
    entropy = 0
    for v in values:
        if v > 0:
            p = v / total
            entropy -= p * (p ** 0.5)  # simplified pseudo-entropy
    return round(entropy, 4)

def evaluate_performance(metrics, base):
    score = 0
    if 'density' in metrics:
        score += metrics['density'] * 1.2
    if 'entropy' in metrics:
        score += metrics['entropy'] * 2.1
    if 'pair_count' in metrics:
        score += metrics['pair_count'] // 2
    adjustment = abs(base - metrics.get('density', 0))
    if adjustment > 3:
        score -= 5
    else:
        score -= 2
    return int(score)

def main():
    raw_text = "Dynamic programming solves complex problems by breaking them into simpler subproblems."
    window_text = raw_text[:40].lower()
    
    # Step 1: Character frequency analysis
    frequencies = analyze_frequencies(raw_text)
    
    # Irrelevant intermediate: character set operations
    unique_chars = set(frequencies.keys())
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = unique_chars - vowels
    vowel_count = len([c for c in raw_text.lower() if c in vowels])
    
    # Filter frequent characters
    relevant = filter_relevant_keys(frequencies, threshold=3)
    
    # Generate all possible letter pairs from frequent chars
    key_pairs = generate_pairs(relevant.keys())
    
    # Compute stability of these pairs in sliding window
    stability_map = compute_pair_stability(key_pairs, window_text)
    
    # Dummy computation: unused stability stats
    avg_stability = sum(stability_map.values()) / len(stability_map) if stability_map else 0
    high_stability = {pair: s for pair, s in stability_map.items() if s > 1.0}
    
    # Build performance metrics
    metrics = {
        'density': len(relevant) * 1.5,
        'entropy': calculate_entropy(list(relevant.values())),
        'pair_count': len(key_pairs),
        'redundant_metric': avg_stability * 0.7  # not used
    }
    
    # Baseline from an arbitrary calculation
    baseline = len(consonants) + 2
    
    # Critical execution point
    final_score = evaluate_performance(metrics, baseline)
    
    # Print result for evaluation
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()
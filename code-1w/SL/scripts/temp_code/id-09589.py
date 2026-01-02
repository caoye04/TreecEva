from collections import defaultdict

def analyze_pattern(sequence):
    freq = defaultdict(int)
    for item in sequence:
        freq[item] += 1
    return freq

def validate_stability(readings):
    variance = sum((x - sum(readings)/len(readings))**2 for x in readings) / len(readings)
    return variance < 5.0

def calculate_performance(results, importance_weights):
    base_scores = {}
    adjustment_factor = 0.0
    
    # Irrelevant intermediate computation (distractor)
    temp_analysis = [x * 1.5 for x in results if x > 10]
    ignored_total = sum(temp_analysis) / (len(temp_analysis) + 1e-8)
    
    for i, score in enumerate(results):
        weight = importance_weights.get(i, 0.5)
        if score >= 20:
            adjustment_factor += 0.1
        base_scores[i] = score * weight
    
    composite = sum(base_scores.values())
    
    # Additional logic with conditional expression
    penalty = 5.0 if any(s < 5 for s in results) else 0.0
    normalized = composite / (len(results) or 1)
    
    # Final calculation using multiple concepts
    final_score = int(normalized + adjustment_factor * 10 - penalty)
    
    return final_score

def main():
    # Simulated benchmark data
    raw_data = [23, 18, 25, 12, 30]
    categories = ['compute', 'memory', 'io', 'network', 'startup']
    
    # Unrelated character counting (distractor)
    char_count = sum(len(cat) for cat in categories)
    metadata_hash = char_count * 17
    
    # Data transformation
    processed = [x + 2 if x < 20 else x for x in raw_data]
    
    # Another irrelevant structure
    status_flags = {cat: (val > 20) for cat, val in zip(categories, processed)}
    
    # Frequency analysis (semi-relevant but not used in final score)
    distribution = analyze_pattern([p // 10 for p in processed])
    
    # Weight mapping with default fallbacks
    weights = defaultdict(lambda: 0.5)
    for idx, w in enumerate([1.2, 0.8, 1.5, 0.7, 1.3]):
        weights[idx] = w
    
    # Validate data stability (not actually used in final path)
    stable = validate_stability(raw_data)
    consistency_report = 'Stable' if stable else 'Unstable'
    
    # Key execution point
    final_score = calculate_performance(processed, weights)
    
    # Print result as required
    print(f"Result: {final_score}")

if __name__ == '__main__':
    main()
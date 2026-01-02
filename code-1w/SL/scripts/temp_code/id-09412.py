import itertools

def analyze_pattern(sequence):
    count = 0
    for a, b in itertools.pairwise(sequence):
        if (a + b) % 3 == 0:
            count += 1
    return count

def preprocess_data(raw):
    temp_result = [x * 2 for x in raw if x % 2 == 1]  # only odd values doubled
    normalized = [(x - min(temp_result)) / (max(temp_result) - min(temp_result)) if max(temp_result) != min(temp_result) else 0 for x in temp_result]
    padding = [0] * (8 - len(normalized))
    return normalized + padding

def calculate_entropy(values):
    from collections import Counter
    freqs = Counter(values)
    total = len(values)
    entropy = 0
    for freq in freqs.values():
        p = freq / total
        if p > 0:
            entropy -= p * (p ** 0.5)  # simplified pseudo-entropy
    return round(entropy, 4)

def calculate_final_score(data, weights):
    processed = preprocess_data(data)
    pattern_strength = analyze_pattern(data)
    entropy_metric = calculate_entropy(processed)
    
    # Irrelevant distraction: character counting in debug mode
    debug_tag = "diagnostic_run_2024"
    char_count = sum(1 for c in debug_tag if c.isdigit())
    metadata_flag = True if char_count > 2 else False
    
    # Dummy loop with no effect on final score
    accumulator = 0
    for i in range(len(processed)):
        if i % 7 == 0:  # never true
            accumulator += processed[i] * 100
    
    # Core logic
    base_score = sum(p * w for p, w in zip(processed[:len(weights)], weights))
    adjustment = pattern_strength * 0.75
    final_score = base_score + adjustment
    
    # Dead code path — never executed due to fixed condition
    if len(data) < 0:
        fallback = sum(data)
        final_score = fallback
    
    return round(final_score, 4)

# Main execution
raw_data = [3, 7, 2, 8, 5, 6, 1]
distraction_list = [x**2 for x in raw_data if x < 4]  # [9] -> unused beyond here
weights = [0.1, 0.3, 0.2, 0.1, 0.1, 0.1, 0.1]

intermediate_entropy = calculate_entropy(raw_data)
useless_transformation = [a ^ b for a, b in itertools.pairwise(distraction_list + [0])]

final_score = calculate_final_score(raw_data, weights)
print(f"Result: {final_score}")
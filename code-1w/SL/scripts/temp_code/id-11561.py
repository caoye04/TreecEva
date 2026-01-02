from itertools import combinations

def analyze_patterns(sequence):
    counts = {}
    for item in sequence:
        counts[item] = counts.get(item, 0) + 1
    return counts

def filter_elite_elements(data, threshold=3):
    frequency = analyze_patterns(data)
    return {k for k, v in frequency.items() if v >= threshold}

def generate_pairs(elements):
    return list(combinations(elements, 2))

def compute_pair_weights(pairs, base_values):
    weights = []
    temp_log_data = []
    for x, y in pairs:
        weight = (base_values.get(x, 1) + base_values.get(y, 1)) * 0.5
        weights.append(weight)
        temp_log_data.append(f"Pair({x},{y}):{weight}")
    return weights

def rank_elements(freq_dict):
    sorted_items = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    return {item[0]: idx + 1 for idx, item in enumerate(sorted_items)}

def process_rankings(rank_map, elite_set):
    score = 0
    adjustment_factor = len(elite_set) * 0.1
    for element, rank in rank_map.items():
        if element in elite_set:
            score += (1 / rank) * 10
    score += adjustment_factor * 5
    return int(score)

def main():
    raw_input = [1, 3, 3, 7, 7, 7, 4, 4, 4, 4, 2, 8, 8, 8]
    
    # Irrelevant distraction: analyzing patterns not fully used
    pattern_analysis = analyze_patterns(raw_input)
    
    # Key intermediate step: identify frequent elements
    elite_set = filter_elite_elements(raw_input, threshold=3)
    
    # Distractor: generating pairs and computing weights (not used later)
    candidate_pairs = generate_pairs(elite_set)
    pair_scores = compute_pair_weights(candidate_pairs, pattern_analysis)
    
    # Another distraction: modifying a copy of data
    modified_input = [x * 2 for x in raw_input if x in elite_set]
    modified_freq = analyze_patterns(modified_input)
    
    # Core logic begins: ranking elements by frequency
    rank_map = rank_elements(pattern_analysis)
    
    # Critical statement
    final_score = process_rankings(rank_map, elite_set)
    
    # Dead code path - never executed
    if False:
        fallback = sum(modified_freq.values())
        final_score -= fallback
    
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()
def analyze_trends(data_stream):
    raw_magnitude = sum([x ** 2 for x in data_stream if x > 0])
    normalized_flow = raw_magnitude / len(data_stream)
    
    # Distractor: irrelevant signal processing
    dummy_weights = [0.1 * i for i in range(len(data_stream))]
    weighted_sum = sum(w * d for w, d in zip(dummy_weights, data_stream))
    adjusted_bias = weighted_sum * 0.05 if weighted_sum > 10 else 0
    
    return normalized_flow + adjusted_bias


def detect_cycles(sequence):
    cycle_count = 0
    seen_pairs = set()
    for i in range(len(sequence) - 1):
        pair = (sequence[i], sequence[i+1])
        if pair in seen_pairs:
            cycle_count += 1
        else:
            seen_pairs.add(pair)
    
    # Distractor: unused statistical measure
    mean_val = sum(sequence) / len(sequence)
    variance_proxy = sum((x - mean_val) ** 2 for x in sequence) / len(sequence)
    
    return len(seen_pairs)


def evaluate_performance(patterns, loops):
    base = sum(patterns)
    penalty = 0
    
    # Relevant logic: combinatorics of overlapping elements
    common_elements = set(patterns) & set(loops)
    if len(common_elements) >= 2:
        from math import comb
        penalty = comb(len(common_elements), 2)
    
    # Distractor: complex-looking but unused calculation
    theoretical_max = 2 ** len(patterns) - 1
    entropy_approx = len(patterns) * 0.693 if theoretical_max > 100 else 0
    
    # Actual answer computation
    adjustment_factor = len(loops) // 2
    result = base - penalty + adjustment_factor
    
    # Key variable assignment point
    final_score = result * 3
    return final_score

# Main execution block
if __name__ == "__main__":
    input_sequence = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    
    # Irrelevant preprocessing chain
    filtered_data = [x for x in input_sequence if x % 2 == 1]
    extended_data = filtered_data + [x + 10 for x in filtered_data]
    processed_magnitude = analyze_trends(extended_data)
    
    # Generate semi-relevant structures
    trend_strength = int(processed_magnitude)
    feedback_loops = [trend_strength + i for i in range(5)]
    
    # Real data source for answer
    cycle_signature = detect_cycles(input_sequence)
    dominant_patterns = [cycle_signature + i for i in range(4)]
    
    # Critical statement
    final_score = evaluate_performance(dominant_patterns, feedback_loops)
    
    print(f"Result: {final_score}")
import itertools

def analyze_feedback(responses):
    # Irrelevant helper function analyzing user feedback (distractor)
    sentiment_score = 0
    for r in responses:
        if 'good' in r:
            sentiment_score += 1
        elif 'bad' in r:
            sentiment_score -= 1
    return sentiment_score

def preprocess_data(raw):
    # Misleading preprocessing that isn't used in final calculation
    processed = [x * 1.5 for x in raw if x > 0]
    offset = sum(processed) % 7
    return [int(y - offset) for y in processed]

def calculate_baseline(measures):
    # Dead code path — never actually called
    base = 0
    for i, val in enumerate(measures):
        base += val * (i % 4 + 1)
    return base

def evaluate_performance(weights, outcomes):
    # Core logic: dot product of weights and transformed outcomes
    adjusted = [round(o ** 0.5, 2) for o in outcomes]  # Square root of each outcome
    
    # Distractor: complex but unused list comprehension with itertools
    all_pairs = list(itertools.combinations_with_replacement(adjusted, 2))
    pair_sum = sum(a + b for a, b in all_pairs if a != b)
    temp_factor = int(pair_sum % 100)
    
    # Actual computation
    weighted_total = 0
    for i in range(len(weights)):
        weighted_total += weights[i] * adjusted[i]
    
    # Additional red herring: conditional that looks important but doesn't affect result
    penalty = 0
    if weighted_total > 50:
        penalty = temp_factor // 10  # Unused in final score
    
    # Final score depends only on weighted_total
    result = int(weighted_total)
    
    # Another misleading dictionary operation (not influencing final answer)
    diagnostics = {
        'count': len(outcomes),
        'peak': max(outcomes),
        'flagged': [x for x in outcomes if x < 10],
        'noise': temp_factor - penalty
    }
    
    return result

# Main execution flow
if __name__ == "__main__":
    # Input data
    metric_weights = [0.8, 1.2, 0.9, 1.5, 1.1]
    raw_outcomes = [64, 144, 81, 225, 121]  # Perfect squares for clean sqrt
    
    # Irrelevant variables and dead computations (distractors)
    user_feedback = ["good response", "bad experience", "good"]
    sentiment_analysis = analyze_feedback(user_feedback)
    scaled_data = preprocess_data([-5, 10, 15])
    
    # Unused dictionary operations
    metadata_map = {k: v for k, v in enumerate(['A', 'B', 'C'])}
    reverse_lookup = {v: k * 2 for k, v in metadata_map.items()}
    
    # Key statement
    final_score = evaluate_performance(metric_weights, raw_outcomes)
    
    # Output result as required
    print(f"Result: {final_score}")
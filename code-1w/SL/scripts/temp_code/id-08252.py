from itertools import combinations

def preprocess_data(raw):
    # Irrelevant preprocessing (distractor)
    cleaned = [x for x in raw if x > 0]
    outliers = [x for x in cleaned if x > 100]
    return [min(x, 100) for x in cleaned]  # Capped at 100

def evaluate_condition(a, b, c):
    # Semi-relevant logic with red herring conditions
    if a > b and b <= c:
        return a * 0.5
    elif a == b or c < 0:
        return c
    else:
        return b * 0.1

def calculate_final_score(data, weights):
    # Core logic begins
    base_values = [x * 0.1 for x in data]  # Normalize

    # Generate all pairs — actual relevant use of itertools
    paired_sums = [sum(pair) for pair in combinations(base_values, 2)]
    
    # Tracking intermediate state (some used, some not)
    sum_of_pairs = sum(paired_sums)
    count_of_pairs = len(paired_sums)
    average_pair_value = sum_of_pairs / count_of_pairs if count_of_pairs else 0

    # Weighted adjustment — only first two weights are used
    adjustment_factor = weights[0] * 0.3 + weights[1] * 0.7  # weights[2] ignored

    # Apply conditional evaluation using helper function
    temp_adjust = evaluate_condition(int(average_pair_value), len(data), int(sum_of_pairs))

    # Key computation chain
    score_component_1 = average_pair_value * adjustment_factor
    score_component_2 = temp_adjust * len([x for x in data if x > 10])  # List comprehension
    
    # Final aggregation
    final_score = score_component_1 + score_component_2
    
    # Dead code path (distractor)
    if final_score < 0:
        final_score *= -1  # Never reached due to data constraints
    
    return final_score

# Main execution block
if __name__ == "__main__":
    raw_input_data = [20, 50, 30, 80, 120, -5]  # Includes outlier and negative
    filtered_data = preprocess_data(raw_input_data)
    
    # Additional irrelevant tracking
    total_entries = len(raw_input_data)
    valid_count = len(filtered_data)
    
    # Weight vector — third element is misleading
    tuning_weights = [2.0, 4.0, 999.0]  # 999.0 is never used
    
    # Enumerate over filtered data for no real purpose (distractor)
    indexed = list(enumerate(filtered_data))
    shifted = [v * (i + 1) for i, v in indexed]  # Unused transformation
    
    # Zip two unrelated sequences (distractor)
    aux_data = [1, 2, 3, 4]
    zipped = list(zip(shifted, aux_data))  # Not used beyond here
    
    # Critical statement
    final_score = calculate_final_score(filtered_data, tuning_weights)
    
    # Print result as required
    print(f"Result: {final_score}")
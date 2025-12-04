import itertools

def calculate_bonus(base_value, multiplier):
    # Irrelevant helper function that's never called
    return (base_value * multiplier) // 2 + 7

def filter_valid_scores(scores, threshold=50):
    # This function is called but its result is partially ignored
    valid_scores = [score for score in scores if score >= threshold]
    fake_result = sum(valid_scores) * 3 - 15  # Misleading computation
    return valid_scores, fake_result

def process_sequence(values, weights):
    # Main processing with multiple logical steps
    processed = []
    temp_sum = 0
    
    # Step 1: Filter and process initial values
    filtered_vals, distraction = filter_valid_scores(values)
    
    # Step 2: Generate combinations (distractor)
    combos = list(itertools.combinations(filtered_vals, 2))
    combo_sum = sum(sum(pair) for pair in combos[:3])  # Partial use
    
    # Step 3: Apply weights with conditional logic
    for i, val in enumerate(filtered_vals):
        if i < len(weights):
            weighted_val = val * weights[i]
            if weighted_val > 100:
                processed.append(weighted_val // 2)
            else:
                processed.append(weighted_val + 10)
        else:
            processed.append(val * 2)  # Different path
    
    # Step 4: Final computation with early exit condition
    if len(processed) == 0:
        return -999  # Dead code path
    
    # Step 5: Core logic chain
    result = sum(processed) - combo_sum + len(filtered_vals) * 5
    
    # More distractions
    unused_var = distraction // 2  # Never used
    misleading_result = result * 2 - 25  # Misleading intermediate
    
    return result

# Initial data setup
initial_values = [45, 78, 92, 34, 67, 81, 56]
score_weights = [2, 3, 1, 4, 2]

# Irrelevant computations
distraction_values = [x * 2 for x in initial_values if x > 60]
fake_total = sum(distraction_values) + 100

# Main execution
final_score = process_sequence(initial_values, score_weights)

# Print the target result
print(f"Target result: {final_score}")
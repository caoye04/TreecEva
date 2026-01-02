def preprocess_data(raw):
    cleaned = []
    for item in raw:
        if isinstance(item, str):
            cleaned.append(len(item.strip()))
        elif isinstance(item, int):
            cleaned.append(abs(item) % 10)
        else:
            cleaned.append(0)
    normalization_factor = sum(cleaned) / len(cleaned) if cleaned else 1
    return [val / max(normalization_factor, 1) for val in cleaned]


def validate_entry(entry):
    return isinstance(entry, (int, float)) and entry >= 0


def calculate_final_score(raw_data, importance_weights):
    processed = preprocess_data(raw_data)
    
    # Irrelevant tracking variables (distractors)
    total_iterations = 0
    debug_log = []
    temp_aggregate = 0
    
    score_components = {}
    weighted_sum = 0
    weight_sum = 0
    
    for i, (val, w) in enumerate(zip(processed, importance_weights)):
        total_iterations += 1
        if w <= 0:
            continue
            
        # Real computation branch
        adjusted_val = val * 1.5 if i % 2 == 0 else val * 0.8
        contribution = adjusted_val * w
        weighted_sum += contribution
        weight_sum += w
        
        # Semi-relevant but non-critical logging
        temp_aggregate += val
        debug_log.append(f'Step {i}: {contribution:.3f}')
        
        if i > 0 and temp_aggregate > 5:
            temp_aggregate -= 1  # Artificial damping (not used in final result)

    # Final aggregation
    average_contribution = weighted_sum / weight_sum if weight_sum > 0 else 0
    
    # Secondary scoring mechanism (never actually affects output)
    secondary_metric = 0
    for idx, v in enumerate(processed):
        if idx % 3 == 0:
            secondary_metric += v ** 2
    
    # Key result calculation
    bonus = 10 if len(processed) >= 5 else 5
    penalty = 2 if sum(1 for x in processed if x < 1) > 2 else 0
    
    final_score = average_contribution * 10 + bonus - penalty
    
    # Unused diagnostic data
    diagnostics = {
        'entries': len(processed),
        'bonus_applied': bonus,
        'penalty_applied': penalty,
        'raw_weighted_avg': average_contribution
    }
    
    return final_score

# Input data
input_sequence = [' apple ', 123, 'banana', '', 456, None, 789]
weights = [1.0, 2.0, 1.5, 0.5, 2.5, 1.0, 0.0]

# Execution
final_score = calculate_final_score(input_sequence, weights)
print(f"Target result: {final_score}")
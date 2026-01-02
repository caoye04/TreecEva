def calculate_final_score(items, importance_weights):
    base_scores = [0] * len(items)
    temp_buffer = [0] * len(items)
    adjustment_factor = 0.85
    
    # Compute base scores with conditional logic and slicing
    for i in range(len(items)):
        if items[i]['type'] == 'critical':
            base_scores[i] = items[i]['value'] * 3
        elif items[i]['type'] == 'normal':
            base_scores[i] = items[i]['value'] * 2
        else:
            base_scores[i] = items[i]['value']

    # Irrelevant computation: simulate debug trace (distractor)
    debug_trace = list(map(lambda x: x * 0.1 + 2.5, base_scores))
    avg_debug = sum(debug_trace) / len(debug_trace)

    # Apply sliding window average to temp_buffer (semi-relevant preprocessing)
    for i in range(1, len(base_scores)-1):
        temp_buffer[i] = (base_scores[i-1] + base_scores[i] + base_scores[i+1]) / 3
    temp_buffer[0] = base_scores[0]
    temp_buffer[-1] = base_scores[-1]

    # Use slicing to extract mid-section for secondary analysis (not used in final result)
    mid_section = temp_buffer[1:-1]
    midpoint_avg = sum(mid_section) / len(mid_section) if mid_section else 0

    # Weighted aggregation using importance weights
    weighted_sum = 0
    total_weight = 0
    for j in range(len(importance_weights)):
        weight = importance_weights[j]
        score = temp_buffer[j]
        weighted_sum += score * weight
        total_weight += weight

    normalized_score = weighted_sum / total_weight if total_weight != 0 else 0

    # Final nonlinear transformation
    final_score = int(normalized_score * adjustment_factor + 0.5)

    # Dead code path: edge case that doesn't trigger (distractor)
    if len(items) > 100:
        fallback = sum(base_scores) // len(items)
        final_score = max(final_score, fallback)

    return final_score

# Main execution context
config_flags = {'enable_logging': False, 'debug_mode': False}
data = [
    {'type': 'normal', 'value': 12},
    {'type': 'critical', 'value': 8},
    {'type': 'low', 'value': 5},
    {'type': 'critical', 'value': 10},
    {'type': 'normal', 'value': 7}
]
weights = [1.0, 2.5, 0.5, 3.0, 1.5]

# Preprocessing: reverse data order for alignment (slicing)
data_reversed = data[::-1]
weights_reversed = weights[::-1]  # mismatched intentionally

# Correct alignment: use original order
effective_data = data[:]
effective_weights = weights

# Key statement
final_score = calculate_final_score(effective_data, effective_weights)

# Output result
print(f"Result: {final_score}")
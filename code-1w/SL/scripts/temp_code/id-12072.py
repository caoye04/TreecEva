def analyze_sequence(data, threshold=5):
    # Track positions and values above threshold
    high_vals = []
    temp_sum = 0
    index_map = {}
    
    for i, val in enumerate(data):
        if val > threshold:
            high_vals.append(val)
            index_map[i] = val * 2  # Distractor: not directly used
        temp_sum += val % 3  # Irrelevant accumulation

    # Compute frequency distribution (semi-relevant)
    freq_count = {}
    for val in data:
        freq_count[val] = freq_count.get(val, 0) + 1
    
    # Extract unique counts using set operations
    unique_freqs = set(freq_count.values())
    adjustment_factor = sum(unique_freqs) if unique_freqs else 1
    
    # Secondary processing with zip
    shifted_data = data[1:] + [0]
    paired_changes = []
    for curr, next_val in zip(data, shifted_data):
        paired_changes.append(abs(curr - next_val))
    
    # Calculate volatility score (distractor metric)
    volatility = sum(p for p in paired_changes if p > 2) // 2
    
    # Core logic: weighted contribution of high values
    weight_sequence = [i+1 for i in range(len(high_vals))]
    weighted_total = 0
    for idx, hv in enumerate(high_vals):
        weighted_total += hv * weight_sequence[idx]
    
    # Dead code path - never executed under normal input
    if len(data) > 1000:
        return -1  # Unreachable with small inputs

    # Final computation depends only on weighted_total and adjustment_factor
    final_score = (weighted_total // adjustment_factor) + len(index_map)
    
    # Additional noise variables
    dummy_avg = temp_sum / len(data) if data else 0
    outlier_flags = [v for v in data if v == max(data)]
    
    return final_score

# Main execution
sequence = [4, 7, 2, 8, 6, 3, 9, 1]
baseline = 5
interim_result = analyze_sequence(sequence, threshold=baseline)
final_score = interim_result

print(f"Result: {final_score}")
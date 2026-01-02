def process_metrics(entries, importance):
    total = 0
    base_offset = len(entries) * 2
    temp_result = []
    
    # Tracking auxiliary stats (semi-relevant)
    magnitude_sum = 0
    adjustment_factor = 0.0
    
    for i, entry in enumerate(entries):
        # Misleading computation with no impact
        redundant_calc = (i ** 2 + 5) % 3
        
        if i % 2 == 0:
            adjusted_val = entry * importance[i % len(importance)]
            temp_result.append(adjusted_val)
            magnitude_sum += abs(adjusted_val)
        else:
            shifted = entry << 1
            temp_result.append(shifted)
    
    # Secondary loop with enumerate and zip — actual logic here
    status_flags = [x > 0 for x in temp_result]
    cumulative = 0
    
    for idx, (val, flag) in enumerate(zip(temp_result, status_flags)):
        if not flag:
            continue
        # Real contribution to result
        cumulative += val * (idx + 1)

    # Distractor: complex-looking but unused calculation
    outlier_detect = sum(x for x in temp_result if x > 50)
    normalization_shift = magnitude_sum / (len(temp_result) or 1)
    adjustment_factor = round(normalization_shift * 0.1, 3)

    # Final score depends only on cumulative and base_offset
    final_score = cumulative - base_offset

    # Irrelevant state tracking
    debug_snapshot = {"entries_processed": len(entries), "peak_value": max(temp_result, default=0)}
    
    return final_score

# Input data
raw_data = [12, -5, 8, 15, 3]
weights = [1.5, 0.8, 2.0]

# Execution point
result = process_metrics(raw_data, weights)
print(f"Result: {result}")
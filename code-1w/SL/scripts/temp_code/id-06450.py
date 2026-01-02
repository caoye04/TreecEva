def process_metrics(entries, importance):
    base_values = [abs(x) for x in entries if x != 0]
    filtered = [val for val in base_values if val > 1]
    
    # Irrelevant transformation (distractor)
    inverted = list(map(lambda v: round(1 / v, 3), base_values))
    sum_inverted = sum(inverted)

    # Semi-relevant normalization
    normalized = [round(b / sum(base_values), 4) for b in base_values]
    
    # Weight application
    weighted = [b * importance[i % len(importance)] for i, b in enumerate(base_values)]
    
    # Conditional amplification
    amplified = []
    for w in weighted:
        if w < 5:
            amplified.append(w * 1.2)
        elif w < 10:
            amplified.append(w * 1.1)
        else:
            amplified.append(w * 0.95)
    
    # Redundant slicing check (distractor)
    mid_slice = amplified[1:-1]
    slice_avg = sum(mid_slice) / len(mid_slice) if len(mid_slice) > 0 else 0
    
    # Final computation chain
    raw_total = sum(amplified)
    penalty = 0
    for val in entries:
        if val < 0:
            penalty += 0.5
    adjusted_total = raw_total - penalty
    
    # Key assignment
    final_score = int(round(adjusted_total))
    
    # Dead code path (distractor)
    if False:
        debug_log = {"entries": entries, "inverted": inverted}
        print(debug_log)
    
    return final_score

# Input data
metrics = [4, -3, 0, 7, -8, 12, 5]
weights = [0.8, 1.1, 0.9]

# Execution point
final_score = process_metrics(metrics, weights)
print(f"Result: {final_score}")
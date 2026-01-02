def evaluate_performance(weights, outcomes):
    # Initialize tracking variables
    total_contributions = 0.0
    temp_buffer = []
    adjustment_factor = 1.2  # Used for scaling final impact
    
    # Irrelevant pre-processing: simulates data cleaning but doesn't affect core logic
    cleaned_outcomes = [x if x >= 0 else 0 for x in outcomes]
    outlier_count = sum(1 for x in outcomes if x > 100)
    
    # Core evaluation logic with nested conditions and dictionary mapping
    performance_map = {i: outcomes[i] * weights[i] for i in range(len(outcomes))}
    
    magnitude_indicator = 0
    for key, value in performance_map.items():
        if value > 50:
            magnitude_indicator += 1
        elif value > 20:
            # Semi-relevant branch: modifies buffer not used in final score
            temp_buffer.append(value * 0.1)

    # Bitwise interference: computes a mask that isn't actually needed
    bitmask = 0
    for i in range(len(outcomes)):
        bitmask ^= i & 3  # Distractor computation
    
    # Conditional expression chain with red herring variables
    base_score = sum(performance_map[k] for k in performance_map)  \
        if len(performance_map) > 3 else sum(performance_map.values()) * 0.9
    
    # Dead code path: never executed due to fixed condition
    emergency_override = False
    if outlier_count > 100:
        base_score *= 0.5
        emergency_override = True  # This is never triggered

    # String-based state tracker (irrelevant to math)
    status_log = "Processed_" + "_".join([str(int(x)) for x in cleaned_outcomes[:3]])
    status_log += "_OK" if '1' in str(bitmask) else "_WARN"

    # Final aggregation with unused intermediate values
    volatility_proxy = sum(abs(performance_map[i] - performance_map.get(i-1, 0)) 
                           for i in range(1, len(performance_map)))
    
    # Key assignment: this is where the answer is determined
    final_score = base_score * adjustment_factor

    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Input data
metric_weights = [0.8, 1.1, 0.9, 1.3, 1.0]
raw_outcomes = [45, 60, 30, 70, 25]

# Execution point of interest
final_score = evaluate_performance(metric_weights, raw_outcomes)
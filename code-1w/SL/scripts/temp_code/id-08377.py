def evaluate_performance(codes, log):
    base_score = 0
    penalty_adjustment = 0
    temp_result = []
    
    # Irrelevant string transformation (distractor)
    transformed = [c.lower().replace('-', '_') for c in codes]
    filtered_codes = [c for c in codes if c.startswith('P')]
    
    # Misleading set operation with unused result
    code_set = set(transformed)
    shadow_copy = code_set.copy()  # Dead code path
    
    # Core logic: analyze logs and compute score
    valid_entries = 0
    total_latency = 0.0
    high_priority_count = 0
    
    for entry in log:
        parts = entry.split('|')
        status = parts[0].strip()
        latency_str = parts[1].strip()
        priority = parts[2].strip()
        
        try:
            latency = float(latency_str)
        except ValueError:
            continue
        
        if status == "SUCCESS":
            valid_entries += 1
            total_latency += latency
            
            if priority == "HIGH":
                high_priority_count += 1
                penalty_adjustment -= 0.5  # Reward for high-priority completion
        else:
            penalty_adjustment += 1

    # Auxiliary computation with partial relevance
    average_latency = total_latency / valid_entries if valid_entries > 0 else 0.0
    
    # Build derived metric (semi-relevant)
    performance_ratio = (valid_entries / len(log)) * 100 if log else 0
    
    # Distractor: complex but unused combinatorics
    combinations = 0
    for i in range(len(filtered_codes)):
        for j in range(i + 1, len(filtered_codes)):
            if filtered_codes[i][1:] == filtered_codes[j][1:]:
                combinations += 1
    
    # Final scoring logic (depends only on specific variables)
    base_score = valid_entries * 10
    time_bonus = 50 if average_latency < 100 else 20
    priority_bonus = high_priority_count * 7
    
    final_score = int(base_score + time_bonus + priority_bonus + penalty_adjustment)
    
    return final_score

# Input data
product_codes = ['P101', 'P102', 'X205', 'P103', 'P104']
metrics_log = [
    "SUCCESS|95.3|HIGH",
    "FAILURE|120.1|MEDIUM",
    "SUCCESS|87.6|HIGH",
    "SUCCESS|200.0|LOW",
    "SUCCESS|45.2|MEDIUM",
    "FAILURE|300.5|HIGH"
]

# Execution point of interest
final_score = evaluate_performance(product_codes, metrics_log)
print(f"Result: {final_score}")
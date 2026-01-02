def analyze_efficiency(metrics, thresholds):
    efficiency_list = []
    for i, (val, thresh) in enumerate(zip(metrics, thresholds)):
        if val >= thresh:
            efficiency_list.append(1)
        else:
            efficiency_list.append(0)
    
    # Distractor: unused computation
    total_pairs = 0
    for x in metrics:
        for y in thresholds:
            if x + y > 15:
                total_pairs += 1

    return sum(efficiency_list)


def compute_stability_index(data):
    base_index = 0
    adjustment = 0
    for i, x in enumerate(data):
        if i % 2 == 0 and x > 5:
            base_index += x * 0.5
        elif x <= 3:
            adjustment -= 1
    # Semi-relevant transformation
    return int(base_index) + abs(adjustment)


def evaluate_performance(productivity, risk_factor):
    score = 0
    penalty = 0
    
    # Core logic with distractors
    temp_results = []
    for idx, p in enumerate(productivity):
        if idx < len(risk_factor):
            adjusted_p = p - risk_factor[idx]
            temp_results.append(adjusted_p)
            
            # Relevant branching
            if adjusted_p > 7:
                score += 3
            elif adjusted_p > 4:
                score += 2
            else:
                penalty += 1
    
    # Dead code path (distractor)
    if len(temp_results) > 100:
        fallback = sum(temp_results) // len(temp_results)
        score = max(score, fallback)

    # Key computation
    final_score = score * 5 - penalty * 2
    
    # Irrelevant tracking variables
    cumulative_shift = 0
    for j in range(len(temp_results)):
        cumulative_shift += j * temp_results[j] % 3
    
    return final_score

# Main execution
productivity = [8, 9, 6, 7, 5, 10, 4]
risk_factor = [2, 1, 3, 2, 0, 4, 1]

# Unused but plausible data structures
baseline_metrics = [7, 8, 6, 6, 4, 9, 5]
safety_thresholds = [6, 7, 5, 6, 3, 8, 4]

# Intermediate calls with side results
efficiency_rating = analyze_efficiency(baseline_metrics, safety_thresholds)
stability = compute_stability_index([5, 6, 7, 2, 8])

# Critical statement
final_score = evaluate_performance(productivity, risk_factor)

print(f"Result: {final_score}")
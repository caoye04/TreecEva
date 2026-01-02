from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [120, 105, 98, 130, 112, 108, 115]
    metrics = defaultdict(float)
    
    # Irrelevant transformation (distractor)
    temp_offsets = [x % 13 for x in raw_data]
    offset_avg = sum(temp_offsets) / len(temp_offsets)
    
    # Relevant aggregations
    metrics['avg_response'] = sum(raw_data) / len(raw_data)
    metrics['peak_usage'] = max(raw_data)
    metrics['stability'] = len([x for x in raw_data if x > 100])
    metrics['consistency'] = sum([abs(raw_data[i] - raw_data[i-1]) for i in range(1, len(raw_data))])
    
    # Dead code path (misleading)
    if len(raw_data) < 5:
        metrics['dummy_flag'] = True
    else:
        dummy_list = [i for i in range(len(raw_data)) if i % 7 == 0]
        
    return metrics

# Weighting schema for evaluation
def define_weights():
    weights = {}
    weights['avg_response'] = 0.3
    weights['peak_usage'] = 0.1
    weights['stability'] = 0.4  # Most important factor
    weights['consistency'] = 0.2
    
    # Unused weight (red herring)
    weights['dummy_factor'] = 0.0  # Has no effect
    
    # Extra computation with no impact
    scaling_factor = 1.0 / sum(weights.values())
    normalized = {k: v * scaling_factor for k, v in weights.items()}
    
    return weights  # Return unnormalized for actual use

# Main evaluation logic
def evaluate_performance(metrics, weights):
    score = 0.0
    
    # Apply weighted scoring
    for key in weights:
        if key in metrics:
            score += metrics[key] * weights[key]
    
    # Secondary adjustment based on thresholds (partially relevant)
    if metrics['avg_response'] > 110:
        score -= 5.0  # Penalty for high average
    if metrics['peak_usage'] > 125:
        score += 3.0  # Bonus for handling peak
    
    # Distractor calculation (never used)
    phantom_score = 0.0
    for m in metrics:
        if 'u' in m:  # matches 'peak_usage', 'consistency'
            phantom_score += len(m) * 0.1
    
    # Final nonlinear transformation
    score = round(score * 1.25, 2)
    
    return score

# Auxiliary function not directly related
def generate_report_stub():
    report_sections = ['intro', 'data', 'summary']
    page_counts = {section: len(section) + 2 for section in report_sections}
    total_pages = sum(page_counts.values())
    return total_pages  # Unused return

# Orchestration
def main():
    # Collect observed system behavior
    metrics = collect_metrics()
    
    # Define importance weights
    weights = define_weights()
    
    # Compute final performance score
    final_score = evaluate_performance(metrics, weights)
    
    # Print result as required
    print(f"Target result: {final_score}")
    
    return final_score

# Execute
main()
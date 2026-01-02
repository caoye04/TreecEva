def analyze_performance(metrics):
    total = 0
    count = 0
    bonus_tracker = []
    for i, (name, value) in enumerate(metrics.items()):
        if value < 50:
            continue
        adjusted = value * (i + 1)
        if adjusted > 100:
            bonus_tracker.append(adjusted / 2)
        total += adjusted
        count += 1
    avg_adjusted = total / count if count else 0
    extra = sum(bonus_tracker) // len(bonus_tracker) if bonus_tracker else 0
    return avg_adjusted + extra // 2


def validate_inputs(data_list):
    # Redundant validation function that doesn't affect final result
    valid_count = 0
    for item in data_list:
        if isinstance(item, dict):
            valid_count += 1
    return valid_count >= 3


def calculate_rating(entries, factors):
    temp_results = []
    offset = len(entries) % 3
    scaling_factor = 1.0
    
    for idx, (entry, weight) in enumerate(zip(entries, factors)):
        base_score = 0
        for metric_val in entry.values():
            base_score += metric_val
        
        # Irrelevant intermediate transformation
        transformed = (base_score ** 0.5) * (idx + 1)
        if idx % 2 == 0:
            transformed -= offset
        
        weighted = transformed * weight
        temp_results.append(weighted)
        
        # Dead code path: never used again
        if weighted > 200:
            scaling_factor *= 0.95
    
    # Core logic buried among distractions
    raw_total = sum(temp_results)
    penalty = 0
    for val in temp_results:
        if val > 150:
            penalty += val * 0.05
    
    net_score = raw_total - penalty
    
    # Final adjustment using integer math
    final_adjustment = int(net_score // 10) % 7
    return int(net_score + final_adjustment)

# Main execution block
if __name__ == "__main__":
    # Input datasets
    assessments = [
        {'accuracy': 85, 'speed': 76, 'consistency': 92},
        {'accuracy': 90, 'speed': 88, 'consistency': 70},
        {'accuracy': 78, 'speed': 95, 'consistency': 83}
    ]
    
    weights = [0.4, 0.35, 0.25]
    
    # Unrelated preprocessing (distractor)
    flat_data = []
    for a in assessments:
        for k, v in a.items():
            flat_data.append((k, v))
    
    index_map = {i: key for i, (key, _) in enumerate(flat_data)}
    
    # Call to irrelevant function (distractor)
    is_valid = validate_inputs(assessments)
    
    # Key computation with moderate nesting and mixed operations
    intermediate_metric = analyze_performance(assessments[0])
    
    # Critical statement
    final_score = calculate_rating(assessments, weights)
    
    print(f"Result: {final_score}")
def evaluate_performance(metrics, thresholds):
    # Irrelevant transformation (distractor)
    adjusted_metrics = [m * 1.05 for m in metrics]
    
    # Semi-relevant preprocessing
    normalized = [min(max(m, 0), 100) for m in adjusted_metrics]
    
    # Key slicing operation: only use middle three values
    segment = normalized[1:4]
    
    # Initialize tracking variables (some irrelevant)
    total_points = 0
    penalty_count = 0  # unused later but looks important
    bonus_applied = False
    
    # Threshold-based scoring with dictionary lookup
    level_map = {'low': 1, 'medium': 2, 'high': 3}
    threshold_map = {'A': 60, 'B': 70, 'C': 80}  # used in logic
    
    # Dummy loop (misleading)
    temp_sum = 0
    for i in range(len(segment)):
        temp_sum += segment[i] % 10  # minor side computation
    
    # Actual scoring logic (core)
    for idx, val in enumerate(segment):
        if idx == 0 and val >= threshold_map['A']:
            total_points += level_map['medium']
        elif idx == 1 and val >= threshold_map['B']:
            total_points += level_map['high']
            if val > 90:
                bonus_applied = True
        elif idx == 2 and val >= threshold_map['C']:
            total_points += level_map['high']
            total_points += 1  # extra point for high achievers

    # Another distraction: complex but unused calculation
    efficiency_ratio = sum(segment) / (max(segment) + 1)
    derived_metric = round(efficiency_ratio * 100, 2)
    
    # Final score computed from controlled logic chain
    base = total_points * 10
    final_score = base + (5 if bonus_applied else 0)
    
    return final_score

# Main execution context
raw_data = [85, 76, 92, 68, 54]
config_thresholds = {'A': 60, 'B': 70, 'C': 80}

# Preprocessing that seems important but only slice matters
processed = [x + 2 for x in raw_data]
processed[-1] = processed[-1] * 0.5  # tweak last element (not used)

# Key statement
final_score = evaluate_performance(processed, config_thresholds)

print(f"Result: {final_score}")
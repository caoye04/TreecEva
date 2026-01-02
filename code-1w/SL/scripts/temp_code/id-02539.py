from itertools import compress, count

def analyze_performance(values, weights):
    weighted_sum = sum(v * w for v, w in zip(values, weights))
    avg = weighted_sum / len(weights) if weights else 0
    adjusted = [v * 0.9 + 0.1 for v in values]  # minor adjustment, not used later
    return weighted_sum

def validate_input(data):
    if not data or len(data) == 0:
        return False
    return all(isinstance(x, (int, float)) and x >= 0 for x in data)

def calculate_final_score(data, thresholds):
    # Irrelevant pre-processing
    filtered = [x for x in data if x > thresholds.get('min', 0)]
    capped = list(map(lambda x: min(x, thresholds.get('cap', 100)), filtered))
    
    # Distractor variables
    temp_stats = {"sum": sum(capped), "count": len(capped)}
    normalization_factor = temp_stats["count"] if temp_stats["count"] > 0 else 1
    normalized = [x / normalization_factor for x in capped]
    
    # Real computation begins
    base_score = sum(capped)
    
    # Apply bonus logic based on threshold hits
    bonus_tracker = []
    for val in capped:
        if val >= thresholds.get('bonus', 80):
            bonus_tracker.append(10)
        elif val >= thresholds.get('partial_bonus', 60):
            bonus_tracker.append(5)
    bonus_score = sum(bonus_tracker)
    
    # Additional distraction: unused string processing
    status_labels = ['pass' if x >= 70 else 'fail' for x in capped]
    pass_count = len(list(compress(status_labels, (s == 'pass' for s in status_labels))))
    
    # Final score calculation (only base_score and bonus_score matter)
    final_score = base_score + bonus_score
    
    # Dead code branch (never executed due to prior filtering)
    if any(x < 0 for x in data):
        final_score -= 100
    
    return final_score

# Main execution
raw_data = [85, 72, 90, 45, 68, 82, 93]
config = {"min": 50, "cap": 95, "bonus": 80, "partial_bonus": 60}

# Pre-validation (distractor)
is_valid = validate_input(raw_data)
dummy_counter = count(1)
next(dummy_counter)  # unused

# Key processing steps
processed_data = [min(x, 95) for x in raw_data if x >= config['min']]
score_components = {"data_sum": sum(processed_data)}

# This function call contains the critical statement
final_score = calculate_final_score(raw_data, config)

print(f"Result: {final_score}")
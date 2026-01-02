from collections import defaultdict

# Simulate user feedback analysis in a learning system
def analyze_feedback_patterns(feedback_log):
    pattern_count = defaultdict(int)
    temporal_trend = 0
    peak_moment = -1
    
    for i, entry in enumerate(feedback_log):
        if entry > 3:
            pattern_count['positive'] += 1
            temporal_trend += i * entry
        elif entry == 3:
            pattern_count['neutral'] += 1
        else:
            pattern_count['negative'] += 1
            
        if entry > peak_moment:
            peak_moment = entry
    
    # Irrelevant aggregation
    avg_position = temporal_trend / max(len(feedback_log), 1)
    return pattern_count, avg_position

# Assess module complexity based on interaction depth
def calculate_module_weight(interactions):
    base_weight = len(interactions)
    adjustment_factor = 0.0
    
    for level in interactions:
        if level >= 4:
            adjustment_factor += 0.2
        elif level <= 2:
            adjustment_factor -= 0.1
    
    # Dummy tracking variable
    complexity_flag = base_weight > 5 and adjustment_factor > 0
    
    return base_weight * (1 + adjustment_factor)

# Main evaluation logic
def evaluate_performance(feedback_sequence, reference_level):
    stats, position_metric = analyze_feedback_patterns(feedback_sequence)
    weight = calculate_module_weight(feedback_sequence)
    
    # Secondary derived metrics (some not used)
    total_entries = sum(stats.values())
    positive_ratio = stats['positive'] / total_entries if total_entries else 0
    negative_ratio = stats['negative'] / total_entries if total_entries else 0
    
    # Core computation
    performance_base = (stats['positive'] - stats['negative']) * 10
    penalty = 5 if negative_ratio > 0.3 else 0
    
    # Distractor calculation: unused trend score
    trend_score = position_metric * weight
    
    # Final scoring logic
    adjusted_performance = performance_base - penalty
    final_score = int(adjusted_performance + 5)  # Offset for minimum engagement
    
    return final_score

# Execution setup
feedback_levels = [5, 2, 4, 3, 5, 1, 4, 4, 2]
baseline = 3

# Key execution point
final_score = evaluate_performance(feedback_levels, baseline)
print(f"Result: {final_score}")
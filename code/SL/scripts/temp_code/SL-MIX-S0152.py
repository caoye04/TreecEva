from collections import Counter

def analyze_inventory(items):
    # Irrelevant inventory analysis (distractor)
    item_counts = Counter(items)
    max_count = max(item_counts.values()) if item_counts else 0
    min_count = min(item_counts.values()) if item_counts else 0
    
    # Dead code path - never executed
    if max_count > 100:
        bonus_points = 50
    else:
        bonus_points = 25
    
    return max_count - min_count

def calculate_quality_scores(base_metrics):
    # Misleading intermediate calculations
    raw_total = sum(base_metrics)
    average_score = raw_total / len(base_metrics) if base_metrics else 0
    
    # Irrelevant quality threshold check
    quality_threshold = 75.0
    if average_score > quality_threshold:
        quality_bonus = 15
    else:
        quality_bonus = 5
    
    # Unused variable (distractor)
    unused_calibration = quality_bonus * 2
    
    return average_score, quality_bonus

# Main execution with multiple distractor variables
inventory_data = ['widget', 'gadget', 'widget', 'tool', 'gadget', 'widget']
metrics_data = [82, 76, 91, 68, 85]

# Distractor function call
inventory_range = analyze_inventory(inventory_data)

# Relevant calculations mixed with distractors
base_score, bonus = calculate_quality_scores(metrics_data)

# Misleading intermediate variable
intermediate_value = base_score * 1.1

# Dead code - condition never met
if intermediate_value > 100:
    adjustment_factor = 12
else:
    adjustment_factor = 8

# Another distractor calculation
quality_variance = max(metrics_data) - min(metrics_data)

# Core logic chain
primary_score = int(base_score + bonus)
correction_offset = quality_variance // 10

# Final answer calculation
final_metric = primary_score - adjustment_factor + correction_offset

print(f"Result: {final_metric}")
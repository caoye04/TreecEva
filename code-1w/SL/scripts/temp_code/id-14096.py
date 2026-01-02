def analyze_metrics(data_points):
    total = 0
    count = 0
    outlier_threshold = 75
    adjustment_factor = 0.85
    
    for val in data_points:
        if val > outlier_threshold:
            total += val * adjustment_factor
        else:
            total += val
        count += 1
    
    average = total / count if count else 0
    return average


def evaluate_streak(records):
    max_streak = 0
    current_streak = 0
    
    for record in records:
        if record.get('status') == 'success':
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0
    
    penalty = 2 if max_streak < 3 else 0
    return max_streak - penalty


def calculate_performance(logs):
    base_score = 0
    bonus_multiplier = 1.2
    tier_modifiers = {'A': 10, 'B': 5, 'C': 2}
    temp_result = 0
    
    for log in logs:
        category = log['category']
        points = log['points']
        
        if category in tier_modifiers:
            base_score += points + tier_modifiers[category]
        
        # Irrelevant computation (distractor)
        temp_result += points ** 0.5
    
    # Misleading scaling operation (not actually impactful due to override below)
    scaled_score = base_score * bonus_multiplier
    
    # Override with alternate logic path
    final_score = base_score + 5  # Final effective assignment
    
    return final_score

# Main execution
raw_data = [10, 20, 30, 90, 40, 95]
processed_avg = analyze_metrics(raw_data)

activity_logs = [
    {'status': 'success', 'duration': 10},
    {'status': 'success', 'duration': 15},
    {'status': 'fail', 'duration': 5},
    {'status': 'success', 'duration': 12},
    {'status': 'success', 'duration': 8},
    {'status': 'success', 'duration': 20}
]
streak_score = evaluate_streak(activity_logs)

bonus_tracker = [
    {'category': 'A', 'points': 50},
    {'category': 'B', 'points': 30},
    {'category': 'A', 'points': 20},
    {'category': 'C', 'points': 40}
]

intermediate_value = processed_avg * streak_score

# Key statement
final_score = calculate_performance(bonus_tracker)

# Dead code branch (distractor)
if False:
    final_score *= 0.9

# Noise variable
debug_info = {
    'timestamp': 1678886400,
    'source': 'simulated',
    'version': '2.1'
}

print(f"Result: {final_score}")
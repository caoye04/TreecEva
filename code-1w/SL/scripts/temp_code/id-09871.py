def analyze_trends(data):
    trend_values = [x * 1.05 for x in data if x > 50]
    adjusted = [val + 10 for val in trend_values if val < 200]
    return sum(adjusted) // len(adjusted) if adjusted else 0


def validate_integrity(checkpoints):
    base_sum = sum([c * c for c in checkpoints])
    threshold = 1000
    penalty = 0
    if base_sum > threshold:
        penalty = (base_sum - threshold) // 50
    return penalty  # Unused in final logic, distraction


def preprocess_input(raw):
    cleaned = [max(0, x - 5) for x in raw]
    smoothed = []
    for i in range(len(cleaned)):
        window = cleaned[max(0, i-1):i+1]
        smoothed.append(sum(window) / len(window))
    return smoothed


def calculate_performance(raw_data):
    # Step 1: Preprocess
    processed = preprocess_input(raw_data)
    
    # Step 2: Extract key metrics
    high_performers = [x for x in processed if x >= 45]
    performance_base = sum(high_performers)
    
    # Step 3: Apply conditional multipliers
    multiplier = 1.0
    if len(high_performers) > 3:
        multiplier = 1.2
    elif len(high_performers) == 0:
        multiplier = 0.5
    else:
        multiplier = 1.1
    
    # Step 4: Secondary adjustment based on trends
    trend_effect = analyze_trends(processed)
    adjustment_factor = 0.1 if trend_effect > 60 else 0.05
    
    # Step 5: Compute final score
    base_score = performance_base * multiplier
    final_score = int(base_score + (trend_effect * adjustment_factor))
    
    # Irrelevant tracking variables (distractors)
    avg_raw = sum(raw_data) / len(raw_data) if raw_data else 0
    outlier_count = len([x for x in raw_data if x > 100])
    temp_result = [x**0.5 for x in raw_data]  # Dead computation
    
    return final_score

# Main execution
raw_input = [40, 60, 55, 70, 30, 80, 25]
consistency_check = [80, 90, 100, 110]

# Call validation (result unused)
integrity_penalty = validate_integrity(consistency_check)

# Core computation
final_score = calculate_performance(raw_input)
print(f"Result: {final_score}")
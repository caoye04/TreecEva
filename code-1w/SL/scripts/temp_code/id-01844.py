def calculate_performance(base, data):
    adjustment_factor = 1.2
    bonus = lambda x: x * 0.1 if x > 75 else 0
    
    # Compute weighted metrics using list comprehension
    weighted_metrics = [val * (idx + 1) for idx, val in enumerate(data)]
    raw_total = sum(weighted_metrics)
    
    adjusted_total = raw_total * adjustment_factor
    
    performance_bonus = bonus(adjusted_total)
    return int(adjusted_total + performance_bonus)

# Irrelevant distraction variable (minimal interference)
dummy_threshold = 95

baseline = 100
metrics = [80, 70, 85]

final_score = calculate_performance(baseline, metrics)
print(f"Result: {final_score}")
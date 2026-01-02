def calculate_performance(base, attrs):
    adjustment = (lambda x: x ** 0.5 if x > 20 else x / 2)(base)
    
    # Irrelevant distraction: string processing with no impact on result
    status_msg = "System operational"
    clean_msg = status_msg.replace(" ", "_").lower()
    
    # Core logic
    weights = {'precision': 0.4, 'recall': 0.6}
    weighted_sum = sum(attrs[key] * weights[key] for key in attrs)
    
    # Conditional expression affecting final score
    bonus = 10 if 'recall' in attrs and attrs['recall'] > 0.75 else 5
    
    return int(adjustment + weighted_sum * 10 + bonus)

# Setup data
baseline = 36
metrics = {'precision': 0.85, 'recall': 0.8}

# Execution point of interest
final_score = calculate_performance(baseline, metrics)
print(f"Result: {final_score}")
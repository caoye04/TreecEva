def calculate_performance(bonus_enabled, metrics):
    base_score = sum([m * (i + 1) for i, m in enumerate(metrics)])
    adjustment = 1.5 if bonus_enabled else 0.5
    
    # Irrelevant distraction: logging setup (minimal interference)
    log_level = 'INFO'
    debug_mode = False
    
    weighted_avg = base_score / len(metrics)
    bonus = 10 if all(m > 2 for m in metrics) else 0
    
    # Conditional expression using case conversion (suggested paradigm)
    multiplier = 2 if 'HIGH'.lower() == 'high' else 1
    
    final_score = (weighted_avg + bonus) * adjustment * multiplier
    return final_score

# Main execution
metrics_data = [3, 4, 5, 3]
bonus_enabled = True

# Spurious variable (minor distractor, intervention=5)
placeholder_result = None
temp_factor = 7  # unused in final calculation

final_score = calculate_performance(bonus_enabled, metrics_data)
print(f"Result: {final_score}")
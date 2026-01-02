def calculate_performance(base, data):
    adjusted = base * 0.85
    penalty = 0
    for val in data:
        if not isinstance(val, str) or len(val.strip()) == 0:
            penalty += 10
        elif val.lower().startswith('err'):
            penalty += 5
        else:
            adjusted += len(val.strip())
    
    # Irrelevant distraction: tracking unused stats
    stats_summary = {'total': len(data), 'penalties_applied': penalty // 5}
    
    return adjusted - penalty

# Main execution
baseline = 100
inputs = ['OK', 'error_1', '', 'valid_input', 123]
dummy_var = [x for x in range(3)]  # Distractor: unused list comprehension

final_score = calculate_performance(baseline, inputs)
print(f"Result: {final_score}")
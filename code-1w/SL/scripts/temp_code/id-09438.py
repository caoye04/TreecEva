def calculate_performance(base, data):
    adjusted_values = []
    offset = len(data) - base
    
    for val in data:
        if val <= 0:
            continue
        normalized = val / base
        adjusted_values.append(round(normalized, 2))
    
    sorted_vals = sorted(adjusted_values, reverse=True)
    
    # Only use top 3 values
    top_three = sorted_vals[:3]
    
    total = sum(top_three)
    penalty = 0.1 * len([x for x in data if str(x).isdigit() and int(x) > base])
    final_score = total - penalty
    
    return final_score

# Irrelevant auxiliary variable (mild distraction)
ignore_threshold = 0.5

baseline = 8
readings = [10, -5, 16, 24, 0, 7]

final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")
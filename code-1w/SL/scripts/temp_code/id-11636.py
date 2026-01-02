def calculate_performance(base, data):
    adjusted_values = []
    offset = len(data) - base
    
    for val in data:
        if val > base:
            adjusted_values.append(val + offset)
        else:
            adjusted_values.append(val - offset)
    
    processed = ''.join([str(abs(x)) for x in adjusted_values if x != 0])
    sum_digits = sum(int(d) for d in processed if d.isdigit())
    
    penalty = processed.count('5') * 2
    raw_score = sum_digits - penalty
    
    scaling_factor = base / 10.0
    final_score = int(raw_score * scaling_factor)
    
    temp_debug = [x for x in data if x % 2 == 0]  # irrelevant tracking
    extra_count = len(temp_debug)  # minor distraction
    
    return final_score

# Main execution
dataset = [12, 15, 9, 10, 8]
baseline = 10

result = calculate_performance(baseline, dataset)
final_score = result
print(f"Result: {final_score}")
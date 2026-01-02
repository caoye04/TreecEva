def calculate_performance(base, data):
    adjusted = set()
    for val in data:
        if val > base:
            adjusted.add(val - base)
        else:
            adjusted.add(base - val)
    
    total = sum(adjusted)
    count = len(adjusted)
    average_deviation = total / count
    
    threshold = 15
    if average_deviation > threshold:
        multiplier = 0.8
    else:
        multiplier = 1.2
    
    raw_score = total * count
    final_score = raw_score * multiplier
    return final_score

# Irrelevant auxiliary variable (minimal distraction)
dummy_list = [1, 2, 3]

baseline = 10
readings = [12, 15, 8, 20, 7]
final_score = calculate_performance(baseline, readings)
print(f"Target result: {final_score}")
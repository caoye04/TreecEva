from collections import defaultdict

def calculate_performance(base, data):
    adjustments = defaultdict(float)
    total_offset = 0.0
    
    for i, reading in enumerate(data):
        if i % 2 == 0:
            adjustments['even'] += (reading - base) * 0.5
        else:
            adjustments['odd'] += (base - reading) * 0.3

    temp_result = adjustments['even'] - adjustments['odd']
    penalty = len([x for x in data if x < base]) * 0.2
    
    # Irrelevant distraction: unused variable
    theoretical_max = base * len(data)
    
    return round(temp_result - penalty, 3)

# Input data
baseline = 10
readings = [12, 8, 14, 7, 10]

# Computation entry point
final_score = calculate_performance(baseline, readings)

# Output result
print(f"Result: {final_score}")
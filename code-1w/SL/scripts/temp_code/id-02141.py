from collections import defaultdict

def calculate_performance(base, data):
    adjustments = defaultdict(float)
    for reading in data:
        if reading > base + 10:
            adjustments['positive'] += 0.5
        elif reading < base - 10:
            adjustments['negative'] -= 0.3
   
    total_adj = adjustments['positive'] + adjustments['negative']
    return round(base + total_adj, 2)

# Irrelevant auxiliary variable (minor distraction)
placeholder_value = "N/A"

baseline = 50
readings = [65, 40, 70, 25, 55]

final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")
from collections import defaultdict

def calculate_performance(base, data):
    stats = defaultdict(float)
    for val in data:
        if val > base:
            stats['above'] += 1
        elif val < base:
            stats['below'] += 1
    
    adjustment = 1.5 if stats['above'] >= stats['below'] else 0.8
    score = (stats['above'] * 2) - (stats['below'] * 0.5)
    return score * adjustment

baseline = 75.0
readings = [68, 72, 76, 80, 65, 90, 74]

# Additional variables for minimal interference
temp_log = [x for x in readings if x > 70]
ignored_flag = len(temp_log) % 2 == 0

final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")
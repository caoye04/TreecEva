from collections import defaultdict

def calculate_performance(base, data):
    stats = defaultdict(float)
    for value in data:
        if value > base:
            stats['above'] += 1
        elif value < base:
            stats['below'] += 1
        stats['total_count'] += 1
    
    # Compute performance ratio: (above - below) / total
    above = stats['above']
    below = stats['below']
    total = stats['total_count']
    
    if total == 0:
        return 0.0
    
    performance_ratio = (above - below) / total
    normalized = performance_ratio * 100
    
    # Apply damping factor for stability
    damping = 0.95
    adjusted_score = normalized * damping
    
    return round(adjusted_score, 3)

# Irrelevant auxiliary variable (minimal distraction)
temp_offset = 2.5

baseline = 74.0
readings = [70, 78, 80, 72, 73, 76, 75, 69, 81, 71]

final_score = calculate_performance(baseline, readings)
print(f"Target result: {final_score}")
from collections import defaultdict

def calculate_performance(base, data):
    stats = defaultdict(float)
    for val in data:
        if val > base:
            stats['above'] += (val - base) * 1.5
        elif val < base:
            stats['below'] -= (base - val) * 0.8
    
    bonus = 10 if stats['above'] > 20 else 0
    penalty = 5 if stats['below'] < -15 else 0
    
    return int(stats['above'] + stats['below'] + bonus - penalty)

# Irrelevant utility function (minor distraction)
def normalize(x):
    return x / max(1, sum([1 for _ in str(x)]))

baseline = 75
readings = [80, 60, 90, 70, 95]

# Key computation
final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")
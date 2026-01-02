from itertools import compress

def calculate_performance(base, data):
    adjusted = [abs(d - base) for d in data]
    weights = [0.8, 1.2, 1.0, 0.9, 1.1]
    weighted_deviation = sum(w * a for w, a in zip(weights, adjusted))
    reliability = len([d for d in data if d > base]) / len(data)
    final_score = (100 - weighted_deviation) * reliability
    return final_score

baseline = 75.0
readings = [70, 80, 78, 72, 85]

# Irrelevant auxiliary variable (minor distraction)
dummy_flag = True

final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")
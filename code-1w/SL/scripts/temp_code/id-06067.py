from collections import defaultdict

# Sensor data processing for environmental monitoring
def analyze_readings(readings):
    stats = defaultdict(int)
    for value in readings:
        if value > 30:
            stats['high'] += 1
        elif value > 20:
            stats['moderate'] += 1
        else:
            stats['low'] += 1
    return stats

# Performance evaluation using lambda-based scoring
baseline = 25
readings = [18, 22, 33, 27, 19, 35, 24]

scoring_rule = lambda x, base: 1.5 if x > base else 0.8

scores = [scoring_rule(val, baseline) for val in readings]

def calculate_performance(base, data):
    analysis = analyze_readings(data)
    total = sum(scores)
    adjustment = analysis['high'] * 0.5
    return int(total - adjustment)

final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")
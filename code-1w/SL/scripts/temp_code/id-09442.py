from collections import defaultdict

# Simulate sensor readings over time with some baseline correction
def analyze_readings(readings, baseline):
    stats = defaultdict(int)
    adjusted = [x - baseline for x in readings]
    
    for val in adjusted:
        if val > 0:
            stats['positive'] += 1
        elif val < 0:
            stats['negative'] += 1
        else:
            stats['neutral'] += 1

    return stats

def calculate_performance(base, data):
    results = analyze_readings(data, base)
    score = results['positive'] * 2
    score -= results['negative']
    score += results['neutral']
    return score

# Experimental sensor data
baseline = 5
readings = [4, 6, 5, 8, 3, 5, 7]

# Irrelevant auxiliary variable (minor distraction)
temp_log = {'run_id': 'XYZ', 'status': 'completed'}

final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")
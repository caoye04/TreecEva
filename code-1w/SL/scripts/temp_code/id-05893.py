from collections import defaultdict

# Sensor data calibration and performance calculation
def analyze_readings(data):
    stats = defaultdict(int)
    for value in data:
        if value > 0:
            stats['positive'] += 1
        elif value < 0:
            stats['negative'] += 1
        stats['total'] += 1
    return stats

def calculate_performance(base, samples):
    offset = base * 2
    adjusted = [x - offset for x in samples]
    
    # Analyze distribution of adjusted values
    results = analyze_readings(adjusted)
    
    # Performance metric based on balanced response
    balance_factor = abs(results['positive'] - results['negative'])
    efficiency = results['total'] - balance_factor
    
    # Final nonlinear transformation
    transform = lambda x: x ** 0.5 if x > 0 else 0
    return int(transform(efficiency * 5))

# Baseline calibration value
baseline = 7

# Raw sensor inputs (after noise filtering)
readings = [18, 12, -5, 23, -10, 4, 15]

# Key computation step
final_score = calculate_performance(baseline, readings)

print(f"Result: {final_score}")
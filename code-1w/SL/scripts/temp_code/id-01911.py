from collections import defaultdict

# Simulate sensor data processing with performance scoring
def analyze_readings(data_points):
    stats = defaultdict(int)
    anomalies = []
    total_power = 0
    
    for point in data_points:
        raw_value = point['value']
        sensor_id = point['sensor']
        
        # Irrelevant temperature tracking (distractor)
        if 'temp' in point:
            stats['total_temp'] += point['temp']
        
        # Core power accumulation
        if raw_value > 0:
            adjusted = raw_value ** 2 if raw_value < 50 else raw_value * 1.5
            total_power += adjusted
        
        # Anomaly detection (semi-relevant but not used later)
        if raw_value < 0 or raw_value > 100:
            anomalies.append(sensor_id)
    
    return total_power

def calculate_efficiency_factor(n):
    # Complex but partially irrelevant efficiency curve
    factor = 1.0
    for i in range(2, n + 1):
        if n % i == 0:
            factor *= (1 + (i % 4) * 0.1)
    return round(factor, 4)

def calculate_performance(flags, metric):
    base = 100
    penalty = 0
    
    # Multiple flag checks with some red herrings
    flag_values = [f for f in flags if isinstance(f, int)]
    extra_boost = sum([v for v in flag_values if v % 3 == 0])
    
    if len(flags) > 3:
        base += 20
    if 'override' in flags:
        base += 50  # This won't trigger
    
    # Real penalty logic
    for f in flags:
        if isinstance(f, str) and 'error' in f:
            penalty += 15
    
    # Efficiency scaling
    adjustment = calculate_efficiency_factor(int(metric))
    final = (base - penalty) * adjustment + extra_boost
    
    # Dead code branch (distractor)
    if False:
        final = max(final, 200)
    
    return int(final)

# Main execution
if __name__ == '__main__':
    readings = [
        {'sensor': 'A1', 'value': 30, 'temp': 22},
        {'sensor': 'B2', 'value': 60},
        {'sensor': 'C3', 'value': 25, 'temp': 18},
        {'sensor': 'D4', 'value': -5},  # anomaly
        {'sensor': 'E5', 'value': 75}
    ]
    
    # Intermediate computations with distractors
    processed_total = analyze_readings(readings)
    temp_cache = [x**2 for x in range(10)]  # unused cache
    
    efficiency = processed_total / 1000  # normalized metric
    
    # Bonus system with mixed types
    bonus_flags = [True, 12, 'error_init', 'debug_mode', 9, 18]
    
    # Key statement
    final_score = calculate_performance(bonus_flags, efficiency)
    
    print(f"Result: {final_score}")
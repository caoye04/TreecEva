def analyze_temperatures(temp_data):
    avg_temp = sum(temp_data) / len(temp_data)
    high_count = sum(1 for t in temp_data if t > 30)
    fluctuation = max(temp_data) - min(temp_data)
    return avg_temp, high_count, fluctuation


def calculate_humidity_score(humidity_list):
    score = 0
    for h in humidity_list:
        if h > 80:
            score += 2
        elif h > 60:
            score += 1
    # Distractor: unused computation
    normalized = [h / 100 for h in humidity_list]
    return score


def calculate_final_score(sensor_data, limits):
    temperatures = [entry['temp'] for entry in sensor_data]
    humidities = [entry['humidity'] for entry in sensor_data]
    
    # Extract metadata using enumerate (python idiom)
    invalid_count = 0
    for i, entry in enumerate(sensor_data):
        if not entry.get('valid', True):
            invalid_count += 1

    # Use zip to pair data (python idiom)
    paired = list(zip(temperatures, humidities))
    temp_sum = sum(t for t, h in paired if h > limits['humidity'])
    
    # Real logic starts here
    avg_temp, high_temp_days, swing = analyze_temperatures(temperatures)
    humidity_score = calculate_humidity_score(humidities)
    
    # Main scoring logic
    base_score = avg_temp * 2
    if high_temp_days > limits['max_hot_days']:
        base_score -= 10
    
    # Use dictionary operation (get with default)
    penalty_factor = limits.get('penalty', 1)
    adjusted_score = base_score - (swing * 0.5) * penalty_factor
    
    # Final composition
    final_score = int(adjusted_score + humidity_score)
    
    # Dead code path (distractor)
    if False:
        final_score = -999
    
    return final_score

# Simulated sensor readings over 7 days
data = [
    {'temp': 25, 'humidity': 65, 'valid': True},
    {'temp': 32, 'humidity': 85, 'valid': True},
    {'temp': 31, 'humidity': 90, 'valid': True},
    {'temp': 28, 'humidity': 70, 'valid': True},
    {'temp': 33, 'humidity': 88, 'valid': True},
    {'temp': 24, 'humidity': 50, 'valid': True},
    {'temp': 26, 'humidity': 55, 'valid': True}
]

# Threshold configuration
targets = {
    'humidity': 70,
    'max_hot_days': 3,
    'penalty': 1
}

# Execution point
final_score = calculate_final_score(data, targets)
print(f"Result: {final_score}")
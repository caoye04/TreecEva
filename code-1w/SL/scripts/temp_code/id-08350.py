from collections import defaultdict

# Simulate sensor readings with timestamps
def generate_sensor_data():
    data = [
        {'time': 1, 'temp': 22.1, 'pressure': 1013, 'humidity': 45},
        {'time': 2, 'temp': 23.5, 'pressure': 1012, 'humidity': 47},
        {'time': 3, 'temp': 24.0, 'pressure': 1010, 'humidity': 50},
        {'time': 4, 'temp': 23.8, 'pressure': 1008, 'humidity': 52},
        {'time': 5, 'temp': 24.1, 'pressure': 1009, 'humidity': 53}
    ]
    return data

# Analyze trends in sensor data
def analyze_trends(data):
    temp_changes = []
    for i in range(1, len(data)):
        delta = data[i]['temp'] - data[i-1]['temp']
        temp_changes.append(delta)
    avg_change = sum(temp_changes) / len(temp_changes)
    return avg_change

# Apply exponential smoothing (irrelevant to final score but adds distraction)
def smooth_data(data, alpha=0.3):
    smoothed = [data[0]['temp']]
    for i in range(1, len(data)):
        smoothed_val = alpha * data[i]['temp'] + (1 - alpha) * smoothed[-1]
        smoothed.append(smoothed_val)
    return smoothed

# Calculate composite index (distractor function)
def compute_composite_index(data):
    index = 0
    count = 0
    for entry in data:
        if entry['time'] % 2 == 0:
            index += entry['pressure'] * 0.01
        else:
            index += entry['humidity'] * 0.1
        count += 1
    return round(index / count, 3)

# Main scoring logic
def calculate_final_score(data, weights):
    base_score = 0
    adjustment = 0
    
    # Track per-sensor contribution
    contributions = defaultdict(float)
    
    for entry in data:
        time_weight = 1.0
        if entry['time'] > 3:
            time_weight = 1.2
        
        temp_score = entry['temp'] * weights['temp'] * time_weight
        pressure_score = (entry['pressure'] - 1000) * weights['pressure']
        humidity_score = (50 - abs(50 - entry['humidity'])) * weights['humidity']
        
        total_entry = temp_score + pressure_score + humidity_score
        
        # Record breakdown (some used later)
        contributions['temp'] += temp_score
        contributions['pressure'] += pressure_score
        contributions['humidity'] += humidity_score
        
        base_score += total_entry
    
    # Final adjustment based on trend (uses auxiliary analysis)
    trend = analyze_trends(data)
    if trend > 0.5:
        adjustment = 10
    elif trend > 0:
        adjustment = 5
    else:
        adjustment = 0
    
    # Irrelevant aggregation (distractor)
    flat_data = []
    for entry in data:
        flat_data.extend([entry['temp'], entry['pressure'], entry['humidity']])
    avg_flat = sum(flat_data) / len(flat_data)
    flat_correction = avg_flat * 0.01  # Not used
    
    # Final score computation
    final_raw = base_score + adjustment
    normalized = round(final_raw, 2)
    
    # Unused transformation
    max_contrib = max(contributions.values())
    scaled_max = max_contrib * 0.95  # Dead code
    
    return int(normalized)

# Main execution block
data = generate_sensor_data()
weights = {
    'temp': 2.5,
    'pressure': 0.15,
    'humidity': 1.2
}

# Smoothing not used in final calculation (distraction)
smoothed_temps = smooth_data(data)
composite_idx = compute_composite_index(data)

# Key statement
final_score = calculate_final_score(data, weights)

print(f"Result: {final_score}")
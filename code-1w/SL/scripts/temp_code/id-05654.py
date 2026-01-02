from collections import defaultdict

# Simulate sensor readings with timestamps and types
def collect_sensor_data():
    raw_data = [
        (100, 'temp', 23.5),
        (101, 'pressure', 1013.25),
        (102, 'temp', 24.1),
        (103, 'humidity', 45.0),
        (104, 'temp', 22.8),
        (105, 'pressure', 1012.9),
        (106, 'humidity', 47.3),
        (107, 'temp', 24.7),
        (108, 'pressure', 1014.1),
        (109, 'humidity', 44.8)
    ]
    
    grouped = defaultdict(list)
    for tid, s_type, value in raw_data:
        grouped[s_type].append(value)
    
    return dict(grouped)

# Apply moving average filter to smooth data
def smooth_data(values):
    if len(values) < 3:
        return values
    smoothed = []
    for i in range(len(values)):
        if i == 0 or i == len(values) - 1:
            smoothed.append(values[i])
        else:
            avg_val = (values[i-1] + values[i] + values[i+1]) / 3
            smoothed.append(round(avg_val, 2))
    return smoothed

# Normalize values to 0-1 scale based on min-max
def normalize_series(series):
    if not series:
        return []
    min_v, max_v = min(series), max(series)
    if min_v == max_v:
        return [0.5] * len(series)
    return [(x - min_v) / (max_v - min_v) for x in series]

# Compute weighted aggregate score
def compute_final_score(data, weights):
    processed = {}
    temp_raw = data.get('temp', [])
    pressure_raw = data.get('pressure', [])
    humidity_raw = data.get('humidity', [])
    
    # Irrelevant transformation: reverse pressure just for distraction
    pressure_reversed = [round(p * 0.01, 3) for p in reversed(pressure_raw)]
    _ = sum(pressure_reversed)  # Dead computation
    
    # Process temperature with smoothing
    temp_smooth = smooth_data(temp_raw)
    temp_norm = normalize_series(temp_smooth)
    
    # Process humidity directly
    humidity_norm = normalize_series(humidity_raw)
    
    # Weighted combination
    w_temp, w_pressure, w_humidity = weights['temp'], weights['pressure'], weights['humidity']
    
    # Use only first valid reading from each (after processing)
    base_temp = temp_norm[1] if len(temp_norm) > 1 else (temp_norm[0] if temp_norm else 0)
    base_pressure = sum(pressure_raw) / len(pressure_raw) * 0.001  # Arbitrary scaling
    base_humidity = humidity_norm[0] if humidity_norm else 0
    
    # Final score calculation - actual key logic
    final_score = (
        w_temp * base_temp + 
        w_pressure * base_pressure + 
        w_humidity * base_humidity
    )
    
    # Extra irrelevant variables
    outlier_count = 0
    for val in temp_raw:
        if abs(val - sum(temp_raw)/len(temp_raw)) > 1.0:
            outlier_count += 1
    
    return round(final_score, 4)

# Main execution
if __name__ == '__main__':
    sensor_data = collect_sensor_data()
    config_weights = {
        'temp': 0.4,
        'pressure': 0.3,
        'humidity': 0.3
    }
    final_score = compute_final_score(sensor_data, config_weights)
    print(f"Result: {final_score}")
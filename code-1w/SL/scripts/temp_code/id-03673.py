from collections import defaultdict

# Simulate sensor data with noise and valid readings
def preprocess_sensor_data(raw_readings):
    filtered_data = []
    noise_count = 0
    for reading in raw_readings:
        if reading < 0 or reading > 1000:  # Invalid range
            noise_count += 1
            continue
        if reading % 7 == 0:  # Mark multiples of 7 as unstable
            reading -= 5
        filtered_data.append(reading)
    
    # Irrelevant statistics (distractor)
    avg_noise = noise_count / len(raw_readings) if raw_readings else 0
    stability_ratio = sum(1 for x in filtered_data if x > 500) / len(filtered_data) if filtered_data else 0
    
    return filtered_data

# Group data by magnitude bands
def group_by_band(data):
    bands = defaultdict(list)
    temp_stats = []  # Dead storage, not used later
    for val in data:
        if val < 200:
            bands['low'].append(val)
        elif val < 600:
            bands['medium'].append(val)
        else:
            bands['high'].append(val)
        # Misleading computation
        temp_stats.append(val ** 0.5)
    
    # Extra unused aggregation
    summary = {k: sum(v) for k, v in bands.items()}
    return bands

# Compute final score based on weighted contributions
def compute_final_score(banded_data):
    weights = {'low': 0.2, 'medium': 0.5, 'high': 0.8}
    total_weighted = 0.0
    total_count = 0
    
    # Real logic: compute weighted average
    for band_name, values in banded_data.items():
        if values:
            band_avg = sum(values) / len(values)
            total_weighted += band_avg * weights[band_name] * len(values)
            total_count += len(values)
    
    # Distractor: irrelevant normalization attempt
    if total_count > 5:
        adjustment = total_weighted * 0.01
        total_weighted -= adjustment  # Minor distortion, still deterministic
    
    return int(total_weighted / total_count) if total_count else 0

# Main execution
if __name__ == '__main__':
    raw_sensor_data = [14, 21, 99, 105, 400, 525, 600, 707, 800, 950, -5, 1005, 350, 420]
    
    # Preprocessing step
    processed_data = preprocess_sensor_data(raw_sensor_data)
    
    # Band grouping (contains distractor computations)
    grouped_data = group_by_band(processed_data)
    
    # Critical statement
    final_score = compute_final_score(grouped_data)
    
    print(f"Result: {final_score}")
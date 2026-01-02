def analyze_temperatures(raw_readings):
    # Filter out invalid sensor readings (below -50 or above 130)
    valid_readings = [temp for temp in raw_readings if -50 <= temp <= 130]
    
    # Calculate moving average over 3-point window
    smoothed = []
    for i in range(1, len(valid_readings) - 1):
        avg_temp = (valid_readings[i-1] + valid_readings[i] + valid_readings[i+1]) / 3
        smoothed.append(round(avg_temp, 2))
    
    # Identify anomalous fluctuations (>10 degree change)
    fluctuation_flags = []
    for i in range(1, len(smoothed)):
        if abs(smoothed[i] - smoothed[i-1]) > 10:
            fluctuation_flags.append(i)
    
    # Compute baseline statistics (distractor: not used later)
    mean_temp = sum(smoothed) / len(smoothed) if smoothed else 0
    variance_proxy = sum((t - mean_temp) ** 2 for t in smoothed) / len(smoothed) if smoothed else 0
    peak_count = len([t for t in smoothed if t > 80])
    
    return smoothed


def calculate_humidity_weight(humidity_list):
    # Dummy function to add interference
    if not humidity_list:
        return 0.5
    total_weight = 0
    for h in humidity_list:
        if h < 20:
            total_weight += 0.1
        elif h > 80:
            total_weight += 0.3
        else:
            total_weight += 0.2
    return total_weight / len(humidity_list)


def process_sensor_data(data_stream):
    # Extract temperature and humidity from structured data
    temperatures = [entry['temp'] for entry in data_stream if 'temp' in entry]
    humidities = [entry['humidity'] for entry in data_stream if 'humidity' in entry]
    
    # Analyze temperature trends
    processed_temps = analyze_temperatures(temperatures)
    
    # Compute derived metrics (some are red herrings)
    temp_set = set(processed_temps)
    reference_set = {t for t in temp_set if t > 60}
    cold_set = {t for t in temp_set if t < 40}
    overlap_check = temp_set & reference_set  # Always equals reference_set
    
    # Simulate correction factor based on overlapping conditions (unused)
    correction_factor = len(overlap_check) * 0.05 if overlap_check else 0.0
    
    # Accumulate score based on high-temp occurrences
    high_temp_events = [t for t in processed_temps if t >= 75]
    event_bonus = sum(1.5 for _ in high_temp_events)
    
    # Use set difference to identify stable zones (distractor computation)
    stable_readings = temp_set - reference_set - cold_set
    stability_score = len(stable_readings) * 0.7
    
    # Final aggregation (only event_bonus matters)
    base_score = len(processed_temps) * 0.5
    penalty = len(cold_set) * 0.2
    final_component = base_score + event_bonus - penalty + stability_score
    
    return {
        'core_data': processed_temps,
        'score_breakdown': {
            'base': base_score,
            'bonus': event_bonus,
            'penalty': penalty,
            'stability': stability_score
        },
        'final_value': final_component
    }


def calculate_final_score(dataset):
    # Extract final_value from processed structure
    return int(dataset['final_value'])

# Main execution
sensor_input = [
    {'temp': 35, 'humidity': 45},
    {'temp': 150, 'note': 'outlier'},  # invalid temp
    {'temp': 45, 'humidity': 50},
    {'temp': 120, 'humidity': 85},
    {'temp': -60, 'status': 'error'},  # invalid temp
    {'temp': 95, 'humidity': 90},
    {'temp': 135, 'flag': 'bad'},      # invalid temp
    {'temp': 88, 'humidity': 70},
    {'temp': 30, 'humidity': 25},
    {'temp': 92, 'humidity': 80},
    {'temp': 140, 'skip': True},       # invalid temp
    {'temp': 78, 'humidity': 60}
]

processed_data = process_sensor_data(sensor_input)
intermediate_metric = calculate_humidity_weight([entry['humidity'] for entry in sensor_input if 'humidity' in entry])
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")